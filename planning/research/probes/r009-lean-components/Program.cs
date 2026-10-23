// Disposable component fixtures. Not an algorithm, strategy, broker adapter or Trading OS implementation.
using System.Text.Json;
using NodaTime;
using QuantConnect;
using QuantConnect.Data;
using QuantConnect.Data.Market;
using QuantConnect.Interfaces;
using QuantConnect.Orders;
using QuantConnect.Orders.Fills;
using QuantConnect.Securities;
using QuantConnect.Securities.Equity;

class Configs : ISubscriptionDataConfigProvider {
    public SubscriptionDataConfig Config;
    public List<SubscriptionDataConfig> GetSubscriptionDataConfigs(Symbol symbol=null,bool includeInternalConfigs=false) => new(){Config};
}
class Program {
    static readonly DateTime T=new(2030,1,2,10,0,0,DateTimeKind.Utc);
    static readonly Symbol Sym=new(SecurityIdentifier.GenerateEquity("FICTION",Market.USA,mapSymbol:false),"FICTION");
    static readonly List<object> Rows=new();
    static string F(decimal value)=>value.ToString(System.Globalization.CultureInfo.InvariantCulture);
    static void Check(string id,Func<string> observed,string expected) {
        try {var v=observed();Rows.Add(new{id,observed=v,expected,status=v==expected?"PASS":"FAIL"});}
        catch(Exception e) {Rows.Add(new{id,status="ERROR",error_type=e.GetType().Name});}
    }
    static (Equity,TimeKeeper,Configs,SecurityManager) Fixture() {
        var clock=new TimeKeeper(T,DateTimeZone.Utc);
        var manager=new SecurityManager(clock);
        var config=new SubscriptionDataConfig(typeof(TradeBar),Sym,Resolution.Minute,DateTimeZone.Utc,DateTimeZone.Utc,false,false,false,dataNormalizationMode:DataNormalizationMode.Raw);
        var security=new Equity(SecurityExchangeHours.AlwaysOpen(DateTimeZone.Utc),config,new Cash("USD",0,1),SymbolProperties.GetDefault("USD"),new IdentityCurrencyConverter("USD"),RegisteredSecurityDataTypesProvider.Null);
        security.SetBuyingPowerModel(new CashBuyingPowerModel());
        manager.Add(Sym,security);
        return(security,clock,new Configs{Config=config},manager);
    }
    static void Bar(Equity s,TimeKeeper c,DateTime time,decimal o=90,decimal h=92,decimal l=89,decimal close=91,decimal volume=5) {
        c.SetUtcDateTime(time.AddMinutes(1));
        s.SetMarketPrice(new TradeBar(time,Sym,o,h,l,close,volume,TimeSpan.FromMinutes(1)));
    }
    static OrderEvent Fill(Equity s,Configs c,Order o) => s.FillModel.Fill(new FillModelParameters(s,o,c,TimeSpan.FromHours(1),new Dictionary<Order,Security>{{o,s}})).First();
    static void Main() {
        Check("GAP_STOP_MARKET_PRICE",()=>{var(s,c,p,_)=Fixture();Bar(s,c,T);return F(Fill(s,p,new StopMarketOrder(Sym,-2,95,T.AddMinutes(-1))).FillPrice);},"90");
        Check("GAP_STOP_LIMIT_NO_FILL",()=>{var(s,c,p,_)=Fixture();Bar(s,c,T);return F(Fill(s,p,new StopLimitOrder(Sym,-2,95,94,T.AddMinutes(-1))).FillQuantity);},"0");
        Check("STOP_LIMIT_RECOVERS_AFTER_TRIGGER",()=>{var(s,c,p,_)=Fixture();var o=new StopLimitOrder(Sym,-2,95,94,T.AddMinutes(-1));Bar(s,c,T);Fill(s,p,o);Bar(s,c,T.AddMinutes(1),96,97,95,96,5);var f=Fill(s,p,o);return (f.FillQuantity==-2&&f.FillPrice>=94).ToString();},"True");
        Check("NO_FILL_BAR_END_EQUAL_ORDER_TIME",()=>{var(s,c,p,_)=Fixture();Bar(s,c,T);return F(Fill(s,p,new StopMarketOrder(Sym,-2,95,T.AddMinutes(1))).FillQuantity);},"0");
        Check("DEFAULT_COMPONENT_FULL_QUANTITY_NOT_VOLUME_CAP",()=>{var(s,c,p,_)=Fixture();Bar(s,c,T,volume:5);return F(Fill(s,p,new StopMarketOrder(Sym,-10,95,T.AddMinutes(-1))).FillQuantity);},"-10");
        Check("RAW_DIVIDEND_CASH_IMMEDIATE",()=>{var(s,c,p,m)=Fixture();Bar(s,c,T,99,99,99,99);s.Holdings.SetHoldings(100,10);var b=new SecurityPortfolioManager(m,new SecurityTransactionManager(null,m),new AlgorithmSettings());b.SetCash(1000);b.ApplyDividend(new Dividend(Sym,T,1,100),false,DataNormalizationMode.Raw);return F(b.CashBook["USD"].Amount);},"1010");
        Check("DUPLICATE_COMPONENT_DIVIDEND_CALL_CREDITS_TWICE",()=>{var(s,c,p,m)=Fixture();Bar(s,c,T,99,99,99,99);s.Holdings.SetHoldings(100,10);var b=new SecurityPortfolioManager(m,new SecurityTransactionManager(null,m),new AlgorithmSettings());b.SetCash(1000);var d=new Dividend(Sym,T,1,100);b.ApplyDividend(d,false,DataNormalizationMode.Raw);b.ApplyDividend(d,false,DataNormalizationMode.Raw);return F(b.CashBook["USD"].Amount);},"1020");
        Check("ADJUSTED_MODE_NO_EXTRA_DIVIDEND_CASH",()=>{var(s,c,p,m)=Fixture();s.Holdings.SetHoldings(100,10);var b=new SecurityPortfolioManager(m,new SecurityTransactionManager(null,m),new AlgorithmSettings());b.SetCash(1000);b.ApplyDividend(new Dividend(Sym,T,1,100),false,DataNormalizationMode.Adjusted);return F(b.CashBook["USD"].Amount);},"1000");
        Check("RAW_SPLIT_QUANTITY_AND_AVERAGE",()=>{var(s,c,p,m)=Fixture();Bar(s,c,T,100,100,100,100);s.Holdings.SetHoldings(100,10);var b=new SecurityPortfolioManager(m,new SecurityTransactionManager(null,m),new AlgorithmSettings());b.ApplySplit(new Split(Sym,T,100,.5m,SplitType.SplitOccurred),s,false,DataNormalizationMode.Raw);return F(s.Holdings.Quantity)+":"+F(s.Holdings.AveragePrice);},"20:50.0");
        Console.WriteLine("QL2_RESULT="+JsonSerializer.Serialize(new{rows=Rows,scope="NATIVE_COMPONENT_FICTITIOUS_NOT_BACKTEST",strategy_trials=0,market_data_accessed=false}));
    }
}
