<!-- TOC -->

- [Latex 介绍](#latex-%E4%BB%8B%E7%BB%8D)
- [Latex 语法](#latex-%E8%AF%AD%E6%B3%95)
    - [表格](#%E8%A1%A8%E6%A0%BC)
        - [表格表题](#%E8%A1%A8%E6%A0%BC%E8%A1%A8%E9%A2%98)
        - [表格字体](#%E8%A1%A8%E6%A0%BC%E5%AD%97%E4%BD%93)
        - [表格内文字过长自动换行](#%E8%A1%A8%E6%A0%BC%E5%86%85%E6%96%87%E5%AD%97%E8%BF%87%E9%95%BF%E8%87%AA%E5%8A%A8%E6%8D%A2%E8%A1%8C)
        - [两个表格具有相同右对齐的列宽](#%E4%B8%A4%E4%B8%AA%E8%A1%A8%E6%A0%BC%E5%85%B7%E6%9C%89%E7%9B%B8%E5%90%8C%E5%8F%B3%E5%AF%B9%E9%BD%90%E7%9A%84%E5%88%97%E5%AE%BD)
        - [\usepackage{multirow}](#%5Cusepackagemultirow)
    - [latexmk 简介](#latexmk-%E7%AE%80%E4%BB%8B)
    - [PyLaTex环境配置](#pylatex%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE)
        - [strawberry-perl官网：https://strawberryperl.com/](#strawberry-perl%E5%AE%98%E7%BD%91httpsstrawberryperlcom)
        - [安装报错](#%E5%AE%89%E8%A3%85%E6%8A%A5%E9%94%99)
        - [Linux安装](#linux%E5%AE%89%E8%A3%85)

<!-- /TOC -->




# Latex 介绍
+ 常用的包
+ Latex文档结构
    + 命令
    + 文档类声明
        + 用来指明文档类型，常用的类型有三种，分别是article,report,book，命令的一种
            +   book 文类就为了适应书籍的装订，为奇数页和偶数页安排了不同的左右边距；
            + report 和 article 非常相似，但 report 中可以使用更多的章节等级
            + article 则是几乎最简单的一种。
    + 环境
+ 编译环境/编辑器
    + CTEX套装
        + 使用MikiTeX
    + TeX Live
    + Overleaf, Online LaTeX Editor 
        + 从源码可以看到，他是使用 latexmk -xelatex 命令编译的。
    + Sumatra PDF
        + 反向搜索



# Latex 语法
table
```
https://www.tablesgenerator.com/
https://www.latex-tables.com/
https://tableconvert.com/

```
## 表格
```
\RequirePackage{multirow}  % 列合并需要的宏包
\RequirePackage{array}	   % 对齐相关的宏包
\RequirePackage{booktabs}  % 三线表宏包
\RequirePackage{tabularx}  % 自动平均分配列宽的宏包
\RequirePackage{longtable} % 跨页表格需要的宏包
\RequirePackage{tabu}      % 大表格需要的宏包
\RequirePackage{threeparttable} % 三段式表格，主要用于表格内引用

\begin{table}[!htbp]
    \begin{center}
    \caption{Fitness of the three formations for the Huskies}
    \begin{tabular}{cccc}
        \toprule
        Formation  & Coordination & Flexibility & Pressing\\
        \midrule
        \textsf{4-3-3}	&5.1043	&32.42	&42.37\\
        \textsf{4-4-2}	&6.0104	&40.88	&43.58\\
        \textsf{5-3-2}	&7.5032	&23.50	&49.67\\
        \bottomrule
    \end{tabular}\label{tb:Fitness_formations}
    \end{center}
\end{table}


```
首先，开启table环境，并将浮动体结构进行一定的设定，我一边选择的都是！htbp随便表格怎么浮动，但是有时候为了固定位置可以会引用float宏包中的浮动体设置H强制放置。

接着，开启center环境，使表格居中。

利用\caption语句添加表头。\label语句可以加在\caption后面也可以跟在表格后面。

接着，使用最基础的tabular环境制表，具体tabular的用法可以看lshort，在此不表。tabular环境使用*⟨column-spec⟩* 参数指定表格的列数以及每列的格式。基本的列格式见下表。




### 表格表题
https://blog.csdn.net/weixin_43849277/article/details/115249293
https://blog.csdn.net/meowcyanimpostor/article/details/120810571?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_paycolumn_v3&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_paycolumn_v3&utm_relevant_index=1

```

\documentclass{article}

\begin{document}

\begin{table}[h!]
  \begin{center}
    \caption{Your first table.}
    \begin{tabular}{l|c|r} % <-- Alignments: 1st column left, 2nd middle and 3rd right, with vertical lines in between
      \textbf{Value 1} & \textbf{Value 2} & \textbf{Value 3}\\
      $\alpha$ & $\beta$ & $\gamma$ \\
      \hline
      1 & 1110.1 & a\\
      2 & 10.1 & b\\
      3 & 23.113231 & c\\
    \end{tabular}
  \end{center}
\end{table}

\end{document}
```

```
#table环境部分
\begin{center}让表格居中

#表格表题
第一种方法，使用\captionsetup命令。例如：
\captionsetup[table]{position=above}
##去掉表的序号
若在此基础上加星号改成\caption*{}则可以去掉序号“表1”，编译后可以看到这个subsection前面既不出现编号，在目录中也没有把它编进去。

#tabular环境部分
\begin{tabular}{l|c|r}这里面的{l|c|r}，包含了三个字母，代表了表格总共有三列，第一列靠左偏移，第二列居中，第三列靠右偏移。竖线代表列之间用线分隔开来，如果想要左右两边都用线包围起来，应该改成{|l|c|r|}。接下来就是正式的表格绘制部分。

latex里的表格是一行行来绘制的，每一行里面用&来分隔各个元素，用\\来结束当前这一行的绘制。代码中\textbf{Value 1} & \textbf{Value 2} & \textbf{Value 3}\\绘制表格的第一行，是三个加粗的字符串。第二行$\alpha$ & $\beta$ & $\gamma$ \\则是三个希腊字符。

接着是\hline，它的作用是画一整条横线，注意如果想画一条只经过部分列的横线，则可以用cline{a-b}，代表的是画一条从第a列到第b列的横线。

```

### 表格字体
调试Latex表格会遇见表格出界的问题，我们可以让其自动调整字体的大小。

```
\resizebox{\textwidth}{!}{}


\begin{table*}[!t]
\centering
\caption{***}
\label{***}
\resizebox{\textwidth}{!}{
\begin{tabular}{***}
\hline
***
\end{tabular}}
\end{table*}
```
### 表格内文字过长自动换行

### 两个表格具有相同(右对齐)的列宽
如果您使用 array包，你可以放\hfill在标题中，如下所示，因此您不必记住将它(或 \parbox)放在每一行中。

\cline{2-3}, 表示画出一条在第2栏位到第3栏位的横线段，其他栏位将不会有横线段

### \usepackage{multirow}
```
\multicolumn{参数1}{参数2}{参数3}
参数1 表示要将整个单元格分成多少列
参数2 表示对齐方式
参数3 表示这个单元格的内容
\multirow{参数1}{参数2}{参数3}
参数1 表示要将整个单元格分成多少行
参数2 表示对齐方式
参数3 表示这个单元格的内容
```
## latexmk 简介


## PyLaTex环境配置
```
pip install pylatex
```
### strawberry-perl官网：https://strawberryperl.com/

### 安装报错
2. CTEX缺少latexmk.pl文件
```
https://www.ctan.org/tex-archive/support/latexmk

```

### Linux安装

创建conda环境，使用pip安装
```
pip install pylatex
```
```
! LaTeX Error: File `lastpage.sty' not found.问题
```
原因是在tex文件中使用了lastpage包，但是我只安装的basic版本的tex中没有这个包（link），所以需要另行安装。
```
conda install -c conda-forge texlive-core
```
继续报错，`#mktexlsr.pl`

```
\documentclass{article}
\usepackage{array}
\newcolumntype{L}{>{\centering\arraybackslash}m{3cm}}

\begin{document}

\begin{table}
    \begin{tabular}{|c|L|L|}
        \hline
        Title 1 & Title 2 & Title 3 \\
        \hline 
        one-liner & multi-line and centered & \multicolumn{1}{m{3cm}|}{multi-line piece of text to show case a multi-line and justified cell}   \\
        \hline
        apple & orange & banana \\
        \hline
        apple & orange & banana \\
        \hline
    \end{tabular}
\end{table}
\end{document}
```


```
\documentclass[11pt, a4paper]{book}
\usepackage{tabulary}
\usepackage{array}

\begin{document}


...
\begin{tabulary}{\linewidth}{LCL}
    \hline
    Short sentences      & \#  & Long sentences                                                 \\
    \hline
    This is short.       & 173 & This is much loooooooonger, because there are many more words.  \\
    xxxxx This is still loooooooonger, because there are many more words. \\
    \hline
\end{tabulary} 


\newcolumntype{L}{>{\centering\arraybackslash}m{3cm}}

\begin{table}
    \begin{tabular}{|c|L|L|}
        \hline
        Title 1 & Title 2 & Title 3 \\
        \hline 
        one-liner & multi-line and centered & \multicolumn{1}{m{3cm}|}{multi-line piece of text to show case a multi-line and justified cell}   \\
        \hline
        apple & orange & banana \\
        \hline
        apple & orange & banana \\
        \hline
    \end{tabular}
\end{table}


\end{document}




```
```
An alternative solution with tabularray package:

\documentclass{article}
\usepackage{caption}
\usepackage{tabularray}
\begin{document}
    
\begin{table}
  \centering
  \caption{Multiprogram sets}
  \label{multiprogram}
  \begin{tblr}{
    hline{1,2} = {2-Z}{solid},
    hline{3,4} = {solid},
    vline{1} = {Z}{solid},
    vline{2-Z} = {solid},  % Z stands for the last
    cells = {c},
    cell{1}{2} = {c=8}{c}, % multicolumn
  }
          & Sets &   &   &   &   &   &   &   \\
          & 1    & 2 & 3 & 4 & 5 & 6 & 7 & 8 \\
    astar &      & * &   & * &   &   & * &   \\
  \end{tblr}
\end{table}

\end{document}
```