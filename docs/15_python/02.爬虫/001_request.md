https://www.cnblogs.com/wenwei-blog/p/10435602.html

```
>>> import requests                    #导入requests库
>>> r = requests.get(url="http://www.baidu.com",timeout=30)  #返回一个Python对象r
>>> r.status_code 
200                                    #状态码200 Ok
>>> r.encoding = r.apparent_encoding   #
>>> r.text
>>> type(r)                            #查看r类型，返回的是一个对象
<class 'requests.models.Response'>
```

Response对象的常用属性
```
r.status_code  http请求的返回状态，200是OK
r.text  http响应内容的字符串形式，即URL返回的页面内容
r.encoding   从http Header中猜测的响应内容的编码方式，若header没有charset字段，则默认为ISO-8859-1编码，<meta charset='utf-8'>
r.apparent_encoding  从内容分析出的响应内容编码方式（备选编码）这个更准确解析页面的编码
r.content  http响应内容的二进制形式（如图片是由二进制存储的，就可以通过r.content还原这图片）
r.headers  http响应的响应头
r.raise_for_status http请求状态码不是200则会引发HTTPError异常
```

模板
```
import requests
from lxml import etree
#r = requests.get(url = url,timeout=30)
#r.status_code
#html = r.content.decode()

session = requests.Session()
r = session.get(URL)
root = etree.HTML(r.content)
items = root.xpath('//*[@id="rankCont"]/div[1]/div[2]/table/tbody/tr')
```