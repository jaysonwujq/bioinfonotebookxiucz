```
pip3 install jupyterlab  -i https://pypi.tuna.tsinghua.edu.cn/simple

```

## 通过SSH远程使用jupyter notebook
Step-1: 在远程服务器上，启动jupyter notebooks服务：
```
jupyter notebook --no-browser --port=8889
```
Step-2: 在本地机器的Terminal中启动SSH：
```
#ssh -N -f -L localhost:8888:localhost:8889 remote_user@remote_host
ssh -N -f -L localhost:8813:10.5.120.18:8811 fszb@10.5.120.18 #（使用这个最好）

```
其中： -N 告诉SSH没有命令要被远程执行； -f 告诉SSH在后台执行； -L 是指定port forwarding的配置，远端端口是8889，本地的端口号的8888。remote_user@remote_host 用实际的远程帐户和远程地址替换

>  端口如果被占用，就换一下

Step-3: 打开浏览器，输入地址：
```
http://localhost:8888/
```

## R
Jupyter notebook中使用R语言需打开R，安装R包"IRkernel"
```
install.packages('IRkernel')
```
然后在R的命令行里激活
```
IRkernel::installspec()
```
这时候会出现 

###
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)


### window查看端口
```
netstat -ano | findstr "8813"
taskkill -PID 23144 -F
tasklist
```
#### Ref_Info 
原文链接：https://blog.csdn.net/patrick75/article/details/51473884
https://www.cnblogs.com/yangxiaolan/p/5778305.html

https://blog.csdn.net/qq_40944311/article/details/121396856

# 使用内存过大导致浏览器崩溃

```
jupyter notebook --generate-config
```

Jupyter处理大量数据，会导致堆栈内存溢出，像我用chrome的话，就是导致网页崩溃。

其实，jupyter的单个模块限制的大小上限为100MB，所以基本上，你的代码大过这个数值，就会导致网页崩溃，解决办法是提高jupyter默认的处理文件上限。

通过路径`envs\fcLCA\Lib\site-packages\tornado\`
找到文件iostream.py
找到self.max_buffer_size一般在150行左右的样子（根据版本不同）

默认设置的是100 MB，我把它改为了1000MB，现在用起来基本没什么问题
/drives/d/anaconda/Lib/site-packages/tornado/iostream.py

https://blog.csdn.net/weixin_46305693/article/details/124049787?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1-124049787-blog-106454402.pc_relevant_aa2&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1-124049787-blog-106454402.pc_relevant_aa2&utm_relevant_index=1

https://github.com/jupyter/notebook/issues/650


## 