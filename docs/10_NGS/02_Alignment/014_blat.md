对psl输出结果，需要注意一下几点：

1. blat的结果在subject上允许存在很大的gap（intron区域），所以同一个结果在query和subjects上覆盖的区域可能会相差很多，这一点与blast不同。
2. 在基因对基因组的比对中，block的个数不能等同于exon的个数。因为blat对block的定义是一个没有插入缺失的比对，任何插入或者缺失的碱基都会使一个block终止，所以一个exon很可能是有很多block构成的。因此exon和intron的个数要通过足够大的gap来判断。
3. psl结果里面碱基位置的计算是从0开始的而不是1.

```
#blat常见用法
#处理单个job
blat chr11.fa human/test.fa test.psl #输出不含序列
blat chr11.fa human/test.fa -out=pslx test.pslx #输出含序列
blat chr11.fa human/test.fa -out=blast test.blast #输出格式同NABI的blast格式
#并行处理多个jobs
time parallel blat chr{}.fa human/human.fa test_{}.psl ::: {1..22} X Y M
#
blat database query -out=blast8 output.psl
```

## 获取psl格式

```
1. Go to table Browser in UCSC
2. Select RefSeq Genes track from Genes Group
3. Select RefSeqAli Table
4. Select Fields from primary and related tables
5. Click Get Output
6. Select all fields from hg19.refSeqAli EXCEPT bin
7. Also select geneName from hg19.refFlat fields
8. Save as Hg19.file
9. grep -v '#' Hg19.file|perl -ane '@arr=join("\t",@F[0..20]);print "@arr\n"'|sort >Hg19.psl
10. grep -v '#' Hg19.file|awk '{print $22"\t"$10}' |sort > ID.list
RockChalkJayhawk is offline  	
```
> http://seqanswers.com/forums/showthread.php?t=5925

http://genome.ucsc.edu/FAQ/FAQformat#format9.2



