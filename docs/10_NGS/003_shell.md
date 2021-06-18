## ack
## rsync
## tee

### 统计fastq中每个读长的counts数
```
直接用awk命令

awk '{if(NR%4==2) print length($1)}' read.fastq | sort -n | uniq -c > reads_length.txt
NR%4==2的意思是以每四行为一个组，统计每组的第二行（在fastq文件中就是碱基信息行）。

然后用R

library(ggplot2)

reads <- read.csv('reads_length.txt', sep=' ', header=FALSE)
ggplot(reads, aes(x=reads$V2, y=reads$V1)) + 
	geom_bar(stat='identity') + 
	xlab('read length') + 
	ylab('counts') + 
	ggtitle('Read Length Distribution')
```

### shell数组
```
https://www.cnblogs.com/qdhxhz/p/10902110.html

for i in `ls /local_data1/MED/projects/linzuopeng/shen/bam/*.sorted.bam`
do
sample=`basename $i`
#array=(`echo $str | tr '.' ' '`)
#array=(${string//,/ })

sample_tmp=
dir=`dirname $i`

oldIFS=$IFS
IFS=.
arr=($sample)
IFS=$oldIFS
#for s in ${arr[@]};do;echo "$s";done
#for i in "${!array[@]}"; do echo "$i：${array[i]}";done
sample_name=${arr[0]}

echo "/local_data1/work/zhangbo/software/samtools-1.9/samtools view -@ 4 -F 256 -ub $i > $i.tmp.bam \
&& mkdir -p $dir/$sample_name \
&& /local_data1/work/zhangbo/software/bamdst/bamdst -p \
/local_data1/MED/medicine_temp/S07604514_Covered_sorted_merged_hg19.bed \
-o $dir/$sample_name $i.tmp.bam \
&& rm -f $i.tmp.bam"

done
```

### 位置参数
```
$* 是把所有的参数当成为一个整体 
$@ 则是把每个参数独立看待。
$# 表示位置参数的个数, 也可以理解为最后一个参数的下标
``` 

```
# test.sh

echo "${@: 1:1}"
echo "${@: 2:1}"
echo "${@: 3:1}"
echo "${@: $#:1}"
echo "${@: $#-1:1}"
echo "${@: $#-2:1}"
echo "************"
echo "${@:1:1}"
echo "${@:2:1}"
echo "${@:3:1}"
echo "*************"
x=${@:2:1}
echo ${x}

#echo $1 +x
#echo $1 +y
#shift 2
#echo $@

echo ####
echo $@
echo "${@: 1:1}"
echo "${@: 2:1}"
echo "${@: 3:1}"

echo .....
echo $@
echo ${!#}
echo '${@:1:$#-1}' ${@:1:$#-1}
echo '${@:1:$#-1}' ${@:1:$#-1}
echo '${@:2:$#-1}' ${@:2:$#-1}
echo '${@:$#-1:1}' ${@:$#-1:1} #获取倒数数第二个参数
#echo (${@:1:#})
```
#### Ref_Info
https://www.jianshu.com/p/eaa3406b7cff
