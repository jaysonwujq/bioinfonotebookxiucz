1) 在 Bash 中，可以按下 ctrl-w 删除你键入的最后一个单词，ctrl-u 可以删除行内光标所在位置之前的内容，alt-b 和 alt-f可以以单词为单位移动光标，ctrl-a 可以将光标移至行首，ctrl-e 可以将光标移至行尾，ctrl-k 可以删除光标至行尾的所有内容，ctrl-l 可以清屏。键入 man readline 可以查看 Bash 中的默认快捷键。内容有很多，例如 alt-. 循环地移向前一个参数，而 alt-* 可以展开通配符。

2) pstree -p 以一种优雅的方式展示进程树。

3) 使用 netstat -lntp 或 ss -plat 检查哪些进程在监听端口（默认是检查 TCP 端口; 添加参数 -u 则检查 UDP 端口）或者 lsof -iTCP -sTCP:LISTEN -P -n (这也可以在 OS X 上运行)。

https://silenwang.github.io

We have not implemented nanopore yet.

# cp 
## cp ignore unchanged files
```
rsync -av --progress /source /destination/
```

```
cp -u
```

```
scp  `find /data/*.gz -type f -mtime -7` USER@SERVER:/backup/
```