https://github.com/vogetihrsh/icopydav

```
./configure --disable-fortran  --with-device=ch4:ofi  --prefix=/home/Desktop/HPC/mpich-3.4.1/mpich-install 2>&1 | tee c.txt

export MPI_ROOT=/local_data1/MED/programs/CNVtools/icopydav/mpich-3.4.2install/ #这一步对应你自己的安装地址
export PATH=$MPI_ROOT/bin:$PATH
export MANPATH=$MPI_ROOT/man:$MANPATH
```
https://cdn.iiit.ac.in/cdn/bioinf.iiit.ac.in/icopydav/icopyDAV_Tutorial.pdf
