```
rmdup bam
tree
his
stat

partition
call
genotype

https://github.com/abyzovlab/CNVnator/issues/210
```

## 安装
```
wget -c https://github.com/abyzovlab/CNVnator/releases/download/v0.4.1/CNVnator_v0.4.1.zip
```
+ The results of calling is RD signal normalized to 1, while genotyping returns estimated number of copies, which is 2 for all germline chromosomes except for X and Y in males.)
+ By default CNVnator estimates CN (-genotype, last two number in each line) using bin size that you provided and bins of 1000 bp. If histogram for 1k bp bins don’t exist then the software prints the warning and print -1 (the last field).
+ Larger events are more reliable. Also, regions with less repeats and segments duplication are more reliable (but this is taken care of by q0 filtering).
+ First e-values is more conservative. You can ignore e-val3 and e-val4. By default CNVantor reports calls that are with <0.05 either for e-val1 or e-val2.
+ `q0=-1`, this could be homozygous region but could also be unassembled region in the reference genome.
+ estimated real copy number = round( normalized_RD *2 )
+ So, 0.522541 will correspond to 1.04 CN for diploid chromosomes, while  0.765529 will be 1.53 CN again for diploid chromosomes.
+ in principle yes. But CNVnator assumes that coverage is more or less the same across genome. For highly aneuploid cancer this may not be the case, which will affect RD signal normalization, and may bias results.
+ gender abnormalities
```
1- CNVnator calculate avg_coverage of all autosomes collectively on one side , then on X-Y (i.e. avg_cvg of X and Y considered together);
2- It assumes gender based on X-Y_avg_coverage: if X-Y_avg_coverage is half autosomes_avg_cvg, then it considers it male. Otherwise it considers it female.
3- It uses avg_coverage of all autosomes when calling CNVs on autosomes, while it uses avg_coverage of X-Y when calling CNVs on X or Y. Therefore:
3.a) It calls almost-whole-Y-homoz-deletion (RD=0, except for pseudo-autosomal regions) in all females;
3.b) copy number of the call would be: 2RD if autosome, 2RD if X in female, 1RD if Y in male, 1RD if X in male.
3.c) it CANNOT identify: XXX, nor X0. It CAN identify XYY.
```
+ e-values show how many regions with such RD one can find across whole genome by chance.First e-values is more conservative. You can ignore e-val3 and e-val4.

## CNV、genetic CNV、CNV gene定义
(all from doi/10.1101/gr.187187.114.)