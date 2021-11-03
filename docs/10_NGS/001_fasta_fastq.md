https://jianzuoyi.github.io/post/2020-12-24-pyfastx/


统计fastq中reads条数
```
 /public/frasergen/MED/software/software/pigz/pigz-2.6/pigz -dc AW237-1_1.trim.fastq.gz | awk 'NR%4==2{c++} END{print c}' 
```