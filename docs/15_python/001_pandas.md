<!-- TOC -->

- [2. 行列选择](#2-行列选择)
    - [2.1 行选择](#21-行选择)
        - [2.1.1 根据包含的字符串选择行](#211-根据包含的字符串选择行)
        - [2.1.2 选择包含空格的行](#212-选择包含空格的行)
    - [2.2. 列选择](#22-列选择)
        - [2.2.1. 根据列值选择行](#221-根据列值选择行)
        - [2.2.2. 选择列值不等于some_value的行](#222-选择列值不等于some_value的行)
        - [2.2.3. 列名里是否包含字符串](#223-列名里是否包含字符串)
- [3 常见操作](#3-常见操作)
    - [3.1 去重复](#31-去重复)
    - [3.2 从python 中的列名称检索列索引](#32-从python-中的列名称检索列索引)
        - [3.2.1. get_loc()](#321-get_loc)
        - [3.2.2. searchsorted()](#322-searchsorted)
    - [3.3 检索某字母开头的行](#33-检索某字母开头的行)
    - [3.4 读写](#34-读写)
        - [DataFrame.to_excel多次写入不同Sheet](#dataframeto_excel多次写入不同sheet)
- [4. Pandas中的map(), apply()和applymap()的应用](#4-pandas中的map-apply和applymap的应用)
    - [Remap values in  column with a dict](#remap-values-in--column-with-a-dict)
            - [Ref_Info](#ref_info)
    - [Get top biggest values from each column of the .DataFrame](#get-top-biggest-values-from-each-column-of-the-dataframe)
    - [merge multiple dfs](#merge-multiple-dfs)
        - [](#)
    - [Collapse two rows into 1 in Pandas](#collapse-two-rows-into-1-in-pandas)
    - [把某列百分数转成浮点数](#把某列百分数转成浮点数)
    - [列字符型变成列浮点型](#列字符型变成列浮点型)

<!-- /TOC -->

# 2. 行列选择
## 2.1 行选择
```
df = pd.DataFrame(...) #任意初始化一个列数为3的DataFrame
df.columns=['a', 'b', 'c']

df['b']
df.b #这里b为列名称，但必须是连续字符串，不能有空格。如果列明有空格，则只能采取上种方法
data1[data1.columns[1:]]
data1[5:10] #这里取6到11行的所有数据，而不是列数据
```
```
data = DataFrame(np.arange(16).reshape(4,4),index=list('abcd'),columns=list('wxyz'))

data['w']  #选择表格中的'w'列，使用类字典属性,返回的是Series类型

data.w    #选择表格中的'w'列，使用点属性,返回的是Series类型

data[['w']]  #选择表格中的'w'列，返回的是DataFrame属性

data[['w','z']]  #选择表格中的'w'、'z'列

data[0:2]  #返回第1行到第2行的所有行，前闭后开，包括前不包括后

data[1:2]  #返回第2行，从0计，返回的是单行，通过有前后值的索引形式，#如果采用data[1]则报错

data.ix[1:2] #返回第2行的第三种方法，返回的是DataFrame，跟data[1:2]同

data['a':'b']  #利用index值进行切片，返回的是**前闭后闭**的DataFrame, #即末端是包含的  
data.irow(0)   #取data的第一行
data.icol(0)   #取data的第一列

data.head()  #返回data的前几行数据，默认为前五行，需要前十行则dta.head(10)
data.tail()  #返回data的后几行数据，默认为后五行，需要后十行则data.tail(10)

ser.iget_value(0)  #选取ser序列中的第一个
ser.iget_value(-1) #选取ser序列中的最后一个，这种轴索引包含索引器的series不能采用ser[-1]去获取最后一个，这回引起歧义。

data.iloc[-1]   #选取DataFrame最后一行，返回的是Series
data.iloc[-1:]   #选取DataFrame最后一行，返回的是DataFrame

data.loc['a',['w','x']]   #返回‘a’行'w'、'x'列，这种用于选取行索引列索引已知

data.iat[1,1]   #选取第二行第二列，用于已知行、列位置的选取。
```

.loc,.iloc,.ix,只加第一个参数如.loc([1,2]),.iloc([2:3]),.ix[2]…则进行的是行选择 
2. .loc,.at，选列是只能是列名，不能是position 
3. .iloc,.iat，选列是只能是position，不能是列名 
4. df[]只能进行行选择，或列选择，不能同时进行列选择，列选择只能是列名。

### 2.1.1 根据包含的字符串选择行
```
s.str.findall("[a-z]")
```

### 2.1.2 选择包含空格的行 
```
tmp.loc[tmp["Related Diseases"].str.contains("Leuk", na = False)]
```

## 2.2. 列选择
### 2.2.1. 根据列值选择行
```
df.loc[df['column_name'] == some_value]
```
选择列值在可迭代值some_values中的行，请使用isin：
```
df.loc[df['column_name'].isin(some_values)]
```

### 2.2.2. 选择列值不等于some_value的行
```
df.loc[df['column_name'] != some_value]
```
isin返回一个布尔系列，所以要选择值不在some_values的行，使用〜来否定布尔系列：
```
df.loc[~df['column_name'].isin(some_values)]
```
```
df.loc[(df['A'] == 'foo') & (df['B'] == 'one')]
```

### 2.2.3. 列名里是否包含字符串
```
short_way = [df.columns.get_loc(col) for col in query_cols if "xx" in col]
df.columns.str.contains("xxx")
df.columns.str.find("xxx")
df.columns.str.match("xxx")
```

```
df.loc[0:1,['A','B']] ##  取行index为0与1之间的,列标签为A,B的，返回DataFrame
```

# 3 常见操作
## 3.1 去重复
DataFrame的duplicated方法返回一个布尔型Series,表示各行是否重复行。

而 drop_duplicates方法，它用于返回一个移除了重复行的DataFrame


## 3.2 从python 中的列名称检索列索引
### 3.2.1. get_loc()
```
df = DataFrame({"pear": [1,2,3], "apple": [2,3,4], "orange": [3,4,5]})
In [46]: df.columns
Out[46]: Index([apple, orange, pear], dtype=object)
In [47]: df.columns.get_loc("pear")
Out[47]: 2
```
https://stackoverflow.com/questions/13021654/get-column-index-from-column-name-in-python-

### 3.2.2. searchsorted() 
1. You could use np.where, which returns a tuple of row and column indices where your value is present. 
2. Use np.searchsorted -
```
np.searchsorted(s.index.values,'D')
```
Or use the method, like so -
```
s.index.searchsorted('D')
```
https://stackoverflow.com/questions/48911071/more-effective-way-to-use--get-loc

https://stackoverflow.com/questions/13021654/get-column-index-from-column-name-in-python-

## 3.3 检索某字母开头的行
https://stackoverflow.com/questions/40249152/python-3--select-dataframe-using-startswith-or

https://stackoverflow.com/questions/15325182/how-to-filter-rows-in--by-regex

https://stackoverflow.com/questions/17071871/select-rows-from-a-dataframe-based-on-values-in-a-column-in-

## 3.4 读写
```
df.to_csv(r'Z:\temp\test.csv',quoting=1,mode='w',index=False,header=True,encoding= 'utf-8',columns=['TABNAME','TIME'])
```
## 3.5 DataFrame.to_excel多次写入不同Sheet
```
>>> writer = pd.ExcelWriter('output.xlsx')
>>> df1.to_excel(writer,'Sheet1')
>>> df2.to_excel(writer,'Sheet2')
>>> writer.save()
```
## 3.6 列计算
```
df.loc['total'] = df[['data1','data2']].apply(lambda x : x.sum(),axis=0 )
```


# 4. Pandas中的map(), apply()和applymap()的应用
map() 是一个Series的函数，DataFrame结构中没有map()。map()将一个自定义函数应用于Series结构中的每个元素(elements)。

apply()将一个函数作用于DataFrame中的每个行或者列

applymap()将函数做用于DataFrame中的所有元素(elements)

> #axis =1 ,apply function to each row. 

> #axis =0,apply function to each column,default 0


https://stackoverflow.com/questions/40083266/replace-comma-with-dot-

https://stackoverflow.com/questions/19377969/combine-two-columns-of-text-in-dataframe-in--python

查看数据类型
```
df.applymap(type)
```

## Remap values in  column with a dict
```
>>> df = pd.DataFrame({'col2': {0: 'a', 1: 2, 2: np.nan}, 'col1': {0: 'w', 1: 1, 2: 2}})
>>> di = {1: "A", 2: "B"}
>>> df
  col1 col2
0    w    a
1    1    2
2    2  NaN
>>> df.replace({"col1": di})
  col1 col2
0    w    a
1    A    2
2    B  NaN
```
or directly on the Series, i.e. df["col1"].replace(di, inplace=True).
#### Ref_Info
https://stackoverflow.com/questions/20250771/remap-values-in--column-with-a-dict

## Get top biggest values from each column of the .DataFrame
Here is my .DataFrame:
```
import  as pd
data = pd.DataFrame({
  'first': [40, 32, 56, 12, 89],
  'second': [13, 45, 76, 19, 45],
  'third': [98, 56, 87, 12, 67]
}, index = ['first', 'second', 'third', 'fourth', 'fifth'])
```
I want to create a new DataFrame that will contain top 3 values from each column of my data DataFrame.

Here is an expected output:
```
   first  second  third
0     89      76     98
1     56      45     87
2     40      45     67
```

```
#1
def sorted(s, num):
    tmp = s.sort_values(ascending=False)[:num]  # earlier s.order(..)
    tmp.index = range(num)
    return tmp
    
data.apply(lambda x: sorted(x, 3))

#2
pd.DataFrame({c: data[c].nlargest(3).values for c in data})
```


https://xlsxwriter.readthedocs.io/working_with_.html

https://xlsxwriter.readthedocs.io/_examples.html

## merge multiple dfs 
https://stackoverflow.com/questions/44327999/python--merge-multiple-dataframes/44338256
https://stackoverflow.com/questions/23668427/-three-way-joining-multiple-dataframes-on-columns


设置excel边框 https://mp.weixin.qq.com/s/6hBKbaV3Ygfddi_yvzW75Q

替换某列字符串
```
pd.DataFrame({'col1': ['$46.51', '$38.00', 40], 
              'col2': [1, 2, 3]}).to_csv('test_df.csv', index=False)

>>> pd.read_csv('test_df.csv', converters={'col1': lambda s: float(s.replace('$', ''))})
    col1  col2
0  46.51     1
1  38.00     2
2  40.00     3
```

### 
```
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)

```

## Collapse two rows into 1 in Pandas

```
>>> df1
                                   #Query_id  Query_length  Query_start  Query_end
0  m64033_201215_092254/132081/150862_170300         19438         5840      14430
1  m64033_201215_092254/132081/150862_170300         19438          128       5786
2  m64033_201215_092254/132081/150862_170300         19438        14477      19433
3  m64033_201215_092254/132081/150862_170300         19438            1        396
4  m64033_201215_092254/132081/150862_170300         19438         5840      14430

print df.groupby('value')['tempx'].apply(' '.join).reset_index()

>>> df1.groupby(["#Query_id"])['Query_start'].agg(list).reset_index()
```

## 把某列百分数转成浮点数
https://stackoverflow.com/questions/25669588/convert-percent-string-to-float-in-pandas-read-csv

## 列字符型变成列浮点型
```
df["A"] = pd.to_numeric(df["A"], downcast="float")
```
