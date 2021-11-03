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
ssh -N -f -L localhost:8888:localhost:8889 remote_user@remote_host
```
其中： -N 告诉SSH没有命令要被远程执行； -f 告诉SSH在后台执行； -L 是指定port forwarding的配置，远端端口是8889，本地的端口号的8888。remote_user@remote_host 用实际的远程帐户和远程地址替换

Step-3: 打开浏览器，输入地址：
```
http://localhost:8888/
```

#### Ref_Info 
原文链接：https://blog.csdn.net/patrick75/article/details/51473884
https://www.cnblogs.com/yangxiaolan/p/5778305.html