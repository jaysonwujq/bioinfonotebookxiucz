https://github.com/deweylab/RSEM

```
bowtie2 -q --phred33 --sensitive --dpad 0 --gbar 99999999 \
--mp 1,1 --np 1 --score-min L,0,-0.1 -I 1 -X 1000 --no-mixed \
--no-discordant -p 6 -k 200 -x /home/anlan/reference/index/RSEM/hg38/ \
-1 SRR6269049.clean_1.fastq -2 SRR6269049.clean_2.fastq | samtools view -S -b -o RSEM/SRR6269049.temp/SRR6269049.bam
```
+ 从上述--gbar可看出，RSEM是不支持有gap的比对；--no-mixed则表示RSEM不支持单个reads的比对；--no-discordant则告诉我们RSEM也不支持paired reads discordant的比对;-k 200表明RSEM希望bowtie2输出最佳的200个比对结果
+ 考虑了多重比对的reads

####  Ref_Info

https://www.bioinfo-scrounger.com/archives/482/
