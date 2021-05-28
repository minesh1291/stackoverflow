
- Problem

    For some years there are not data.
```
    2014-10-07    5036.883410
    2013-10-11    5007.515654
    2013-10-27    5020.184053
    2014-09-12    5082.379630
    2014-10-14    5032.669801
    2014-10-30    5033.276159
    2016-10-03    5046.921912
    2016-10-19    5141.861889
    2017-10-06    5266.138810
```
    Returns ValueError
```
    data.groupby(pd.TimeGrouper('A')).agg( lambda x : x.idxmax() )
```
- Solution
```
data.resample('A').agg(
    lambda x : np.nan if x.count() == 0 else x.idxmax()
)
```
