<!-- TOC -->

- [g++ 和 gcc](#g-和-gcc)
- [编译](#编译)
  - [gcc编译器](#gcc编译器)
  - [make](#make)
  - [automake](#automake)
  - [CMake](#cmake)
    - [基本语法](#基本语法)
    - [构建](#构建)
      - [Ref_Info](#ref_info)
  - [glibc 安装问题](#glibc-安装问题)

<!-- /TOC -->
# g++ 和 gcc
gcc和g++的区别主要是在对cpp文件的编译和链接过程中，因为cpp和c文件中库文件的命名方式不同，那为什么g++既可以编译C又可以编译C++呢，这时因为g++在内部做了处理，默认编译C++程序，但如果遇到C程序，它会直接调用gcc去编译.

# 编译
+ 构建套件
+ 供构建套件需要的配置文件（如上面的 ./bootstrap 和 ./configure）
## gcc编译器
+ gcc是GNU Compiler Collection（就是GNU编译器套件），也可以简单认为是编译器，它可以编译很多种编程语言（括C、C++、Objective-C、Fortran、Java等等）。
+ 当你的程序只有一个源文件时，直接就可以用gcc命令编译它。
+ 但是当你的程序包含很多个源文件时，用gcc命令逐个去编译时，你就很容易混乱而且工作量大, 所以出现了**make**工具。

## make
+ make工具可以看成是一个智能的批处理工具，它本身并没有编译和链接的功能，而是用类似于批处理的方式—通过调用makefile文件中用户指定的命令来进行编译和链接的。
+ makefile是什么？简单的说就像一首歌的乐谱，make工具就像指挥家，指挥家根据乐谱指挥整个乐团怎么样演奏，make工具就根据makefile中的命令进行编译和链接的。
+ makefile命令中就包含了调用gcc（也可以是别的编译器）去编译某个源文件的命令。
+ .makefile在一些简单的工程完全可以人工手下，但是当工程非常大的时候，手写makefile也是非常麻烦的，如果换了个平台makefile又要重新修改。这时候就出现了**Cmake**这个工具。

## automake
## CMake 
+ CMake是一个跨平台的安装（编译）工具，可以用简单的语句来描述所有平台的安装(编译过程)。
+ CMake 是跨平台，可生成 native 编译配置文件，在 Linux/Unix平台，生成 Makefile，在苹果平台，生成 xcode，在 Windows 平台，可以生成 MSVC 工程文件。
+ CMake 指令是大小写不敏感的。
+ CMake比make更为高级，使用起来要方便得多。CMake主要是编写**CMakeLists.txt**（学名：组态档）文件，然后用cmake命令将CMakeLists.txt文件转化为make所需要的**makefile**（学名：建构档）文件，最后用make命令编译源码生成可执行程序或共享库（so(shared object)）。它的作用和qt的qmake是相似的。

### 基本语法
```
CMAKE_MINIMUM_REQUIRED 用于检查系统 CMake 版本是否满足最低要求，
PROJECT 指令通过名字定义工程，
SET 用于设置 CMake 变量，
${VAR_NAME} 的方式引用变量，
MESSAGE 用于向终端输出信息，
ADD_EXECUTABLE 则用于生成可执行二进制文件。
```

### 构建
所有的文件创建完成后，ex_01 目录中应该存在 **main.c** 和 **CMakeLists.txt** 两个文件，接下来我们来构建这个工程，在这个目录运行：

```
> cd 
> cmake .
> make
> ./hello
```
“cmake .”，. 表示当前目录，运行后将会自动生成 <table><tr><td bgcolor=#54FF9F>BCMakeFiles 文件夹，CMakeCache.txt，cmake_install.cmake 等文件，并且生成了 Makefile。</td></tr></table>下一步 “make” 则是去执行的 Makefile，生成我们的目标文件 hello。你可以通过 “make VERBOSE=1” 看到 make 构建的详细过程。最后通过 ./hello 即可运行目标二进制文件。完成构建后的工程源文件目录如下：

实际上，上面我们采用的是一种叫做 **in-source build(内部构建)**的构建方式，顾名思义，这种方式直接在源代码中进行构建，构建过程的中间产物以及最终的目标文件都会混在一起，我们没办法将项目文件与其分开，更没办法做到自动删除这些中间文件和目标文件。
　　另外一种比较合理的构建方式叫做 **out-of-source build(外部构建)** ，这种方式单独在与源代码工程独立的目录下执行构建，保证源代码的纯洁性，更能实现中间文件和目标文件的快速删除。
```
> cd ~/Workspace/cmake_ws/ex_01/
> mkdir build
> cd build/
> cmake ..
> make
> ./hello
> cd ..
> rm -rf build/
```
#### Ref_Info
https://durant35.github.io/2016/04/21/tool_CMake_%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8/


## glibc 安装问题 

https://blog.csdn.net/RyanFang/article/details/100984938
