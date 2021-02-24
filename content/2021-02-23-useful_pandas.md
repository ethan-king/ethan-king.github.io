Title: A Pandas Summary
Date: 2021-02-23 00:00
Category: Python
Tags: pandas, data
Slug: useful-pandas
Authors: Ethan King
Summary: Useful pandas transformations

This is a guide to using pandas for data transformations. One can't reasonably be expected to remember the pandas API, 
and I google them often enough to be annoyed with having to look at the same Stack Overflow responses or documentation 
pages.

## Display options
Display options make the Python REPL output easier to look at.
```python
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
```

## Time series grouping 
Working with time series data, it's useful to bucket time values into a unit of time that makes 
sense for the dataset. (minutes, hours, days, weeks, months, etc.)  
[Official Pandas Grouper docs](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Grouper.html)  
[Pbpython Grouper explanation](https://pbpython.com/pandas-grouper-agg.html)  
```python
pd.Grouper(key='date', freq='M')
```
## Dataframe aggregation
After grouping a dataset, we can generate some useful statistics about the group using 
aggregation functions. Agg takes a function name as a parameter, and below is a list of such named functions.  
[.agg](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.agg.html)
set axis = 1 to aggregate column-wise.
```python
DataFrame.agg(func=None, axis=0, *args, **kwargs)
```
### Aggregation Functions
[This blog post](https://pbpython.com/groupby-agg.html) goes into aggregation functions into more detail, including 
named functions from scipy and numpy as well as custom functions.
Basic math
```python
['sum', 'mean', 'median', 'min', 'max', 'std', 'var', 'mad', 'prod', 'describe']
```
Counting  
Count excludes NaN values, whereas size includes NaN's.    
nunique also excludes NaN's.  
sorting is important for first / last calculation.  
```python
['count', 'nunique', 'size', 'first', 'last', 'idxmax', 'idxmin']
df.sort_values(by=['col1'], ascending=False).groupby(['col2']).agg({'col2':'first'})
```

## iterating rows and transforming 
Sometimes, one will need to iterate through each row of a dataframe to generate a new feature. In order to transform the
original dataframe, call iloc with the new column name as a parameter on the orginal dataframe.
```python
df = pd.Dataframe()
for index, row in df.iterrows():
    if SOME_CONDITION:
        df.iloc[index, 'new column'] = some_function(row['col1'])
```

## Datetime
Dates are a funny data type to work with. Sometimes you'll have something stored as a string, sometimes its a 
datetime object. In any case, it's important to be able to work with both. 
[Working with strftime](https://www.programiz.com/python-programming/datetime/strftime)  
[strftime.org format reference](https://strftime.org/)  
```python
from datetime import datetime
now = datetime.now() # current date and time
print("date and time:", now.strftime("%m/%d/%Y, %H:%M:%S"))	
date and time: 02/24/2021, 04:59:31
```

That's all for now, but this post is a work in progress. Have any commonly googled pandas uses that are missing? 
Leave a comment below!