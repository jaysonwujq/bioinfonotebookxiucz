输入 Tmux 前缀和一个冒号呼出命令提示行

## session
```
# 列出所有会话：
tmux ls
# 新建一个无名称的会话
tmux
# 新建一个名称为demo的会话
tmux new -s demo
# 断开当前会话，会话在后台运行
tmux detach
# 默认进入第一个会话
tmux a 
# 进入到名称为demo的会话
tmux a -t demo
 # 关闭demo会话
tmux kill-session -t demo
# 关闭服务器，所有的会话都将关闭
tmux kill-server

## window
c  创建新窗口
w  列出所有窗口
n  后一个窗口
p  前一个窗口
f  查找窗口
,  重命名当前窗口
&  关闭当前窗口

%  垂直分割
"  水平分割
o  交换窗格
x  关闭窗格
⍽  左边这个符号代表空格键 - 切换布局
q 显示每个窗格是第几个，当数字出现的时候按数字几就选中第几个窗格
{ 与上一个窗格交换位置
} 与下一个窗格交换位置
z 切换窗格最大化/最小化


输入 Tmux 前缀和一个冒号呼出命令提示行

## session

# 列出所有会话：
tmux ls
# 新建一个无名称的会话
tmux
# 新建一个名称为demo的会话
tmux new -s demo
# 断开当前会话，会话在后台运行
tmux detach
# 默认进入第一个会话
tmux a 
# 进入到名称为demo的会话
tmux a -t demo
 # 关闭demo会话
tmux kill-session -t demo
# 关闭服务器，所有的会话都将关闭
tmux kill-server

## window
# 创建新窗口
prefix + c
# 列出所有窗口 
prefix + w
# 后一个窗口
n
#前一个窗口  
p  
#重命名当前窗口
, 
关闭当前窗口 
&  

%  垂直分割
"  水平分割
o  交换窗格
x  关闭窗格
⍽  左边这个符号代表空格键 - 切换布局
q 显示每个窗格是第几个，当数字出现的时候按数字几就选中第几个窗格
{ 与上一个窗格交换位置
} 与下一个窗格交换位置
z 切换窗格最大化/最小化
```

## 配置
```
set -g prefix C-b
set-option -g prefix2 ` # 设置一个不常用的`键作为指令前缀，按键更快些

#set -g mouse off
set -g base-index 1 ## 设置窗口的起始下标为1
set -g renumber-windows on
set -g pane-base-index    1 # 设置面板的起始下标为1
#set-window-option -g monitor-activity on
#set-window-option -g bell-action any

setw -g automatic-rename off
setw -g allow-rename off






run-shell ~/.tmux/plugins/tmux-resurrect/resurrect.tmux
run-shell ~/.tmux/plugins/tmux-continuum/continuum.tmux
set -g @continuum-save-interval '600'




##
# git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm , use prefix + I install plugins
# List of plugins
#set -g @plugin 'tmux-plugins/tpm'
#set -g @plugin 'tmux-plugins/tmux-sensible'

# plugins
# prefix + Ctrl-s - save;  prefix + Ctrl-r - restore.  https://github.com/tmux-plugins/tmux-resurrect
#set -g @plugin 'tmux-plugins/tmux-resurrect'
#set -g @plugin 'tmux-plugins/tmux-continuum'
# restore vim/neovim session
set -g @resurrect-strategy-vim 'session'
set -g @resurrect-strategy-nvim 'session'
set -g @continuum-restore 'on'
set -g @resurrect-capture-pane-contents 'on'

set -g @resurrect-save-shell-history 'on'

# Initialize TMUX plugin manager (keep this line at the very bottom of tmux.conf)
#run '~/.tmux/plugins/tpm/tpm'
```

## 
### tmp安装
但是使用过程中有一个问题，就是一旦机器重启或者 tmux 不幸挂掉了，之前的工作区会话就会全部丢失了。有一种快速启动 tmux 会话的方式就是用 tmuxp 启动一个 yaml 配置，不过笔者最近用的也非常少了。这次介绍两个 tmux 的插件，使用它们可以很方便 地自动保存和恢复 tmux 会话，即使你重启机器也不用怕了，打开的各种目录可以很快恢复了，甚至你之前的命令输出/vim会话也可以恢复。
https://zhuanlan.zhihu.com/p/259640277

### 手动安装


## 进阶操作
加载conf文件
```
[zhangbo@mu01 bin]$ tmux source-file ~/.tmux.conf
'~/.tmux/plugins/tpm/tpm' returned 1
```

## 意外崩溃恢复
```
tmux new -s C
prefix +S
```