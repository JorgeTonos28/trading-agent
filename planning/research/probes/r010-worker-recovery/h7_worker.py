"""Disposable Temporal worker. No LLM, broker, financial data or production code."""
import asyncio
import json
import os
from datetime import timedelta
from pathlib import Path

from temporalio import activity, workflow
from temporalio.client import Client
from temporalio.common import RetryPolicy
from temporalio.worker import Worker


@activity.defn(name="h7_activity")
async def synthetic_activity(payload: dict) -> dict:
    target = Path(os.environ["H7_SCRATCH"]).resolve()
    if target.parent != Path(os.environ["TEMP"]).resolve() or not target.name.startswith("r010_h7_"):
        raise ValueError("Synthetic scratch outside declared TEMP prefix")
    attempt = activity.info().attempt
    (target / f"entered-{attempt}.json").write_text(
        json.dumps({"attempt": attempt, "authority": "NONE"}), encoding="utf-8")
    if attempt == 1:
        await asyncio.sleep(12)  # Controller terminates this worker after the marker.
    return {"job_id": payload["job_id"], "attempt": attempt, "authority": "NONE"}


@workflow.defn
class SyntheticRecoveryWorkflow:
    @workflow.run
    async def run(self, payload: dict) -> dict:
        return await workflow.execute_activity(
            "h7_activity", payload,
            start_to_close_timeout=timedelta(seconds=5),
            schedule_to_close_timeout=timedelta(seconds=30),
            retry_policy=RetryPolicy(initial_interval=timedelta(seconds=1), maximum_attempts=2),
        )


async def main():
    address = os.environ["H7_ADDRESS"]
    if not address.startswith("127.0.0.1:"):
        raise ValueError("Loopback only")
    client = await Client.connect(address)
    async with Worker(client, task_queue="H7-SYNTHETIC",
                      workflows=[SyntheticRecoveryWorkflow], activities=[synthetic_activity]):
        await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
