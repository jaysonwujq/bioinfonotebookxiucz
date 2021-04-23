<!-- TOC -->

- [1. gcc下载](#1-gcc下载)
- [2. gcc解压和查看安装准备](#2-gcc解压和查看安装准备)
- [2. gcc依赖包下载](#2-gcc依赖包下载)
  - [2.1 安装gmp(>=4.3.2)](#21-安装gmp432)
    - [安装过程](#安装过程)
  - [2.2 安装mpfr(3.1.0)](#22-安装mpfr310)
  - [2.3 安装mpc（1.0.1）](#23-安装mpc101)
  - [2.4 安装gcc](#24-安装gcc)
- [4. 调用新版gcc来编译软件](#4-调用新版gcc来编译软件)
- [5. 注意](#5-注意)

<!-- /TOC -->
# 1. gcc下载

对于gcc的安装，建议使用源码安装，而不要使用conda进行安装。

以gcc 10.2.0版本为例：
```
https://ftp.gnu.org/gnu/gcc/gcc-10.2.0/gcc-10.2.0.tar.gz
```

# 2. gcc解压和查看安装准备


假设你的下载到`$GCCPATH`中，进入文件夹
```
cd $GCCPATH
tar -zxvf gcc-10.2.0.tar.gz
```
耗时有点久。。。。

在`INSTALL/prerequisites.html`中查看安装要求
```

GNU Multiple Precision Library (GMP) version 4.3.2 (or later)
Necessary to build GCC. If a GMP source distribution is found in a subdirectory of your GCC sources named gmp, it will be built together with GCC. Alternatively, if GMP is already installed but it is not in your library search path, you will have to configure with the --with-gmp configure option. See also --with-gmp-lib and --with-gmp-include. The in-tree build is only supported with the GMP version that download_prerequisites installs.

MPFR Library version 3.1.0 (or later)
Necessary to build GCC. It can be downloaded from https://www.mpfr.org. If an MPFR source distribution is found in a subdirectory of your GCC sources named mpfr, it will be built together with GCC. Alternatively, if MPFR is already installed but it is not in your default library search path, the --with-mpfr configure option should be used. See also --with-mpfr-lib and --with-mpfr-include. The in-tree build is only supported with the MPFR version that download_prerequisites installs.

MPC Library version 1.0.1 (or later)
Necessary to build GCC. It can be downloaded from http://www.multiprecision.org/mpc/. If an MPC source distribution is found in a subdirectory of your GCC sources named mpc, it will be built together with GCC. Alternatively, if MPC is already installed but it is not in your default library search path, the --with-mpc configure option should be used. See also --with-mpc-lib and --with-mpc-include. The in-tree build is only supported with the MPC version that download_prerequisites installs.

```
# 2. gcc依赖包下载
1. 自动下载
```
cd $GCCPATH/gcc-10.2.0/
./contrib/download_prerequisites
```

2. 手动下载安装
   
**安装gcc-10.2.0 gmp,mpfr,mpc，这三个组件的顺序不能乱，因为后面的依次依赖前面**
 
## 2.1 安装gmp(>=4.3.2)
```
# https://ftp.gnu.org/gnu/gmp/

cd $GCCPATH/gcc-10.2.0/
wget -c https://ftp.gnu.org/gnu/gmp/gmp-5.1.3.tar.gz
tar -zxvf gmp-5.1.3.tar.gz

cd gmp-5.1.3
./configure --prefix=$GCCPATH/gcc-10.2.0/gmp
make -j
make install
```
### 安装过程
`[guest191@cu-0036 gmp-6.1.0]$ ./configure --prefix=/local_data1/GUEST/guest191/software/gcc-7.2.0/gmp-6.1.0`过程中出现`checking for suitable m4... configure: error: No usable m4 in $PATH or /usr/5bin (see config.log for reasons).`报错。
```
[guest191@cu-0036 gmp-6.1.0]$ wget -c http://ftp.gnu.org/gnu/m4/m4-1.4.16.tar.bz2
tar -jxvf m4-1.4.16.tar.bz2
[guest191@cu-0036 m4-1.4.16]$ cd m4-1.4.16
make -j 20
make install
export PATH=/local_data1/GUEST/guest191/software/gcc-7.2.0/gmp-6.1.0/m4-1.4.16/bin:$PATH
```
重新安装m4后，解决问题。

```
export LD_LIBRARY_PATH=/local_data1/GUEST/guest191/software/gcc-7.2.0/gmp-6.1.0/lib:$LD_LIBRARY_PATH
```

## 2.2 安装mpfr(3.1.0)
```
#https://ftp.gnu.org/gnu/mpfr/
cd $GCCPATH/gcc-10.2.0/
wget -c https://ftp.gnu.org/gnu/mpfr/mpfr-4.1.0.tar.gz
tar -zxvf mpfr-4.1.0.tar.gz
cd mpfr-4.1.0
./configure --prefix=$GCCPATH/gcc-10.2.0/mpfr --with-gmp=$GCCPATH/gcc-10.2.0/gmp
make -j 20
make install
```

## 2.3 安装mpc（1.0.1）
```
#https://ftp.gnu.org/gnu/mpc/
cd $GCCPATH/gcc-10.2.0/
wget -c https://ftp.gnu.org/gnu/mpc/mpc-1.2.1.tar.gz
tar -zxvf mpc-1.2.1.tar.gz
./configure --prefix=$GCCPATH/gcc-10.2.0/mpc --with-gmp=$GCCPATH/gcc-10.2.0/gmp --with-mpfr=$GCCPATH/gcc-10.2.0/mpfr
make -j 20
make install
```

## 2.4 安装gcc
```
mkdir $GCCPATH/gcc-10.2.0/build
cd $GCCPATH/gcc-10.2.0/build
../configure --prefix=$GCCPATH/gcc-10.2.0/ --with-mpc=$GCCPATH/gcc-10.2.0/tmp/gcc-10.2.0/mpc --with-gmp=$GCCPATH/gcc-10.2.0/gmp --with-mpfr=$GCCPATH/gcc-10.2.0/mpfr --disable-multilib --disable-static --enable-shared --enable-threads=posix --disable-checking --enable--long-long --enable-languages=c,c++

```

# 4. 调用新版gcc来编译软件
也是本文的目的,碰到低版本的gcc无法编译你所需要安装的软件时。
```
export PATH="$GCCPATH/gcc-10.2.0/bin:$PATH"  # commented out by conda initialize
```
# 5. 注意
1. 本文比较实用于叫高版本的gcc安装，对于较低版本的gcc也有对应安装方法，不详述。
2. 对于新手，尽量不要将gcc的环境变量写进`~/.bashrc`中，每次需要用到的时候`export`一下就好。



