<!-- TOC -->

- [fasta](#fasta)
- [建立索引](#建立索引)
- [比对](#比对)
- [输出](#输出)

<!-- /TOC -->

## fasta
> It is strongly recommended to include major chromosomes (e.g., for human chr1-22,chrX,chrY,chrM,) as well as un-placed and un-localized scaffolds.

> Generally, patches and alternative haplotypes should not be included in the genome. 

sjdbOverhang

## 建立索引
```
STAR \
--runMode genomeGenerate \
--runThreadN 6  \
--genomeDir index_dir \
--genomeFastaFiles genome.fasta \
--sjdbGTFfile genome.gtf \
--sjdbOverhang 149

--runThreadN：线程数。
--runMode genomeGenerate：构建基因组索引。
--genomeDir：索引目录。（index_dir一定要是存在的文件夹，需提前建好）
--genomeFastaFiles：基因组文件。
--sjdbGTFfile：基因组注释文件。
--sjdbOverhang：reads长度减1。
```

## 比对
```
STAR \
--twopassMode Basic \
--quantMode TranscriptomeSAM GeneCounts \
--runThreadN 6 \
--genomeDir index_dir \
--alignIntronMin 20 \
--alignIntronMax 50000 \
--outSAMtype BAM SortedByCoordinate\
--sjdbOverhang 149 \
--outSAMattrRGline ID:sample SM:sample PL:ILLUMINA \
--outFilterMismatchNmax 2 \
--outSJfilterReads Unique \
--outSAMmultNmax 1 \
--outFileNamePrefix out_prefix \
--outSAMmapqUnique 60 \
--readFilesCommand gunzip -c \
--readFilesIn seq1.fq.gz seq2.fq.gz

Aligned.out.bam        _starF_checkpoints
Chimeric.out.junction  star-fusion.fusion_predictions.abridged.coding_effect.tsv
FusionInspector.log    star-fusion.fusion_predictions.abridged.tsv
Log.final.out          star-fusion.fusion_predictions.tsv
Log.out                star-fusion.preliminary
Log.progress.out       _STARgenome
pipeliner.10541.cmds   _STARpass1
ReadsPerGene.out.tab   _STARtmp
SJ.out.tab

```


| **p** | default| 描述|**arriba** |STAR-Fusion|
|:---------|:---------------|:----|:------------|:----|
|--outStd | |BAM_Unsorted | | |
--outSAMtype|| BAM Unsorted|-|BAM SortedByCoordinate |
--outSAMunmapped|| Within|Within||
--outFilterMultimapNmax |10|-|50|-|
--peOverlapNbasesMin |0|minimum number of overlap bases to trigger mates merging and realignment|10|12|
--alignSplicedMateMapLminOverLmate| 0.66 | alignSplicedMateMapLmin normalized to mate length|0.5|0|
--alignSplicedMateMapLmin|0|minimum mapped length for a read mate that is spliced|-|30|
--alignSJstitchMismatchNmax|0 -1 0 0 | | 5 -1 5 5 | 5 -1 5 5 |
--chimSegmentMin |0| parameter controls the minimum mapped length of the two segments that is allowed.| 10 |12|
--chimOutType |Junctions|-|WithinBAM HardClip| - |
--chimJunctionOverhangMin| 20|minimum overhang for a chimeric junction|10|8|
--chimScoreDropMax |20|max drop (difference) of chimeric score (the sum of scores of all chimeric segments) from the read length|30| -|
--chimScoreJunctionNonGTAG |-1 | penalty for a non-GT/AG chimeric junction | 0| -4|
--chimScoreSeparation| 10 |minimum difference (separation) between the best chimeric score and the next one|-|1
--chimSegmentReadGapMax|0| maximum gap in the read sequence between chimeric segments | 3|-|
--chimMultimapNmax |0| maximum number of chimeric multi-alignments |50 |20|
--twopassMode |-|-|-|Basic
--outSAMstrandField |-|-|-|intronMotif|
--chimOutJunctionFormat|-|-|-|1(# **essential** includes required metadata in Chimeric.junction.out file.)|
--alignSJDBoverhangMin|3|is used at the mapping step to define the minimum allowed overhang over splice junctions. For example, the default value of 3 would prohibit overhangs of 1b or 2b.|-|10|
--alignMatesGapMax| 0 | maximum gap between two mates, if 0, max intron gap will be determined by (2ˆwinBinNbits)*winAnchorDistNbins| - | 100000(# avoid readthru fusions within 100k)|
--alignIntronMax|0 |maximum intron size, if 0, max intron size will be determined by (2ˆwinBinNbits)*winAnchorDistNbins | - | 100000 |
--chimMultimapScoreRange|1|-|-|3|
--chimNonchimScoreDropMin|20|-|-|10|
--peOverlapMMp|0.01|-|-|0.1|
--alignInsertionFlush|None|-|-|Right|
|--outFilterMatchNmin |20 |alignment will be output only if the number of matched bases is higher than or equal to this value.| -| -|
|----|----|----|----|----|
| --readFilesCommand  |  UncompressionCommand/zcat/gunzip -c|
| --sjdbGTFfile |specifies the path to the file with annotated transcripts in the standard GTF format. STAR will extract splice junctions from this file and use them to greatly improve accuracy of the mapping.  While this is optional, and STAR can be run without annotations, using annotations is highly recommended whenever they are available. Starting from 2.4.1a, the annotations can also be included on the fly at the mapping step.|
|--sjdbOverhang | 1. specifies the length of the genomic sequence around the annotated junction to be used in constructing the splice junctions database. Ideally, this length should be equal to the ReadLength-1, where ReadLength is the length of the reads. For instance, for Illumina 2x100b paired-end reads, the ideal value is 100-1=99. In case of reads of varying length, the ideal value is max(ReadLength)-1. In most cases, the default value of 100 will work as well as the ideal value. 2. The --sjdbOverhang is used only at the genome generation step, and tells STAR how many bases to concatenate from donor and acceptor sides of the junctions. If you have 100b reads, the ideal value of --sjdbOverhang is 99, which allows the 100b read to map 99b on one side, 1b on the other side. One can think of --sjdbOverhang as the maximum possible overhang for your reads. 仅仅用在建立剪接数据中步骤中。 如果设置为0，剪接位点数据框则不会被用到。|
|--sjdbOverhang|This also means that for every different read-length to be aligned a new genome SA needs to be generated. Otherwise a drop in aligned reads can be experienced.|
| --genomeLoad | LoadAndKeep NoSharedMemory Remove LoadAndRemove LoadAndExit|
|--outSAMunmapped  | Within KeepPairs/ Within|
|--sjdbOverhang| specifies the length of the genomic sequence around the annotated junction to be used in constructing the splice junctions database. Ideally, this length should be equal to the ReadLength-1, where ReadLength is the length of the reads. For instance, for Illumina 2x100b paired-end reads, the ideal value is 100-1=99. In case of reads of varying length, the ideal value is max(ReadLength)-1. In most cases, the default value of 100 will work as well as the ideal value.|
|--twopassMode Basic|使用two-pass模式进行reads比对。简单来说就是先按索引进行第一次比对，而后把第一次比对发现的新剪切位点信息加入到索引中进行第二次比对。|
|--quantMode TranscriptomeSAM GeneCounts|将reads比对至转录本序列。|
|--runThreadN|线程数。|
|--genomeDir|索引目录。|
|--alignIntronMin|最短的内含子长度。（根据GTF文件计算）|
|--alignIntronMax|最长的内含子长度。（根据GTF文件计算）|
|--outSAMtype BAM SortedByCoordinate| 输出BAM文件并进行排序。
|--sjdbOverhang|reads长度减1。|
|--outSAMattrRGline|ID代表样本ID，SM代表样本名称，PL为测序平台。在使用GATK进行SNP Calling时同一SM的样本可以合并在一起。
|--outFilterMismatchNmax|比对时允许的最大错配数。|
|--outSJfilterReads Unique|对于跨越剪切位点的reads（junction reads)，只考虑跨越唯一剪切位点的reads。
|--outSAMmultNmax|每条reads输出比对结果的数量。
|--outFileNamePrefix：|输出文件前缀。|
|--outSAMmapqUnique 60：|将uniquely mapping reads的MAPQ值调整为60，满足下游使用GATK进行分析的需要。|
|--readFilesCommand：|对FASTQ文件进行操作。
|--readFilesIn |输入FASTQ文件的路径。|
|--outStd| |
|--outBAMcompression|1|int: -1 to 10 BAM compression level, -1=default compression (6?), 0=no
compression, 10=maximum compression|||



## 输出
### Aligned.out.bam
```
A00988:45:H7HTMDSX2:3:1101:3495:1000	99	chr17	8280907	255	104M2103N46M=	8285503	5588	TNTTCCTTGTATTTGCCCTTTTCCTTTCCTACTTGGCGAGATTTGGCTTTCCGTTCGAGGATCTTTTTGCGGTCTTTGTCCAGTTTTAGCCTAGTGATAACCACCTTGCTGGGGTGAATGCCTACGTGGACAGTTGTGCCATTAGCCTTT	F#,,:FFF:FF::FFFFFFFFFFFFFFFFFF:FFFFFFFFFFFFF,F,FFF:FFFF:FFFFFFFF:FFFFFFFF:FFFFFFFFF,:FFFFFFFFFFFFFF:,F,F,FFFF:FFFFFFFFFFFFFF:FFFFFFFFFFFFFFF,FF:FFFFF	NH:i:1	HI:i:1	AS:i:285	nM:i:8	RG:Z:xx	NM:i:1
```
+ (column 5): The mapping quality MAPQ  is 255 for uniquely mapping reads, and int(-10*log10(1- 1/Nmap)) for multi-mapping reads. 
+ SAM attributes. STAR默认是输出NH HI AS nM attributes：
  + HI 其表示多重比对的reads的起始位置，默认是以1开始算的，但是如果下游分析需要用到Cufflinks or StringTie的话，需要用--outSAMattrIHstart设置为0
  + NH:i:1 Value of 1 corresponds to unique mappers, while values >1 corresponds to multi-mappers. 
  + uT:A:1 uT SAM tag indicates reason for not mapping:
    + 0 : no acceptable seed/windows, ”Unmapped other” in the Log.final.out
    + 1 : best alignment shorter than min allowed mapped length, ”Unmapped: too short” in the Log.final.out
    + 2 : best alignment has more mismatches than max allowed number of mismatches, ”Unmapped: too many mismatches” in the Log.final.out
    + 3 : read maps to more loci than the max number of multimappng loci, ”Multimapping: mapped to too many loci” in the Log.final.out
    + 4 : unmapped mate of a mapped paired-end read 


###
```
head DRB_TT_seq_SRR8112732SJ.out.tab
chr1    10078   10178   2       2       0       0       1       26
chr1    10084   10178   2       2       0       0       1       32
chr1    10090   10178   2       2       0       0       1       32
chr1    10102   10178   2       2       1       0       4       37
chr1    10113   10183   2       2       1       0       1       37
chr1    10137   10282   2       2       1       0       1       30
chr1    10137   10288   2       2       1       1       1       37
chr1    10137   10294   2       2       1       0       1       30
chr1    10162   10397   2       2       1       0       1       13
chr1    10179   10225   2       2       1       3       2       27
#第一列：染色体名称
#第二列：内含子起始位点
#第三列：内含子结束位点
#第四列：链。1是正链，2是负链。
#第五列：内含子的motif: 0: 非典型; 1: GT/AG, 2: CT/AC, 3: GC/AG, 4: CT/GC, 5:AT/AC, 6: GT/AT
#第六列：0: 未注释的； 1：注释的
#第七列：横跨这个junction上的唯一比对上的reads数
#第八列：横跨这个junction上的muoti-mapping的reads数
#第九列：maximum spliced alignment overhang
```

### Log files
Log.out: main log file with a lot of detailed information about the run. This file is most useful for troubleshooting and debugging.

**Log.progress.out: ** reports job progress statistics, such as the number of processed reads, % of mapped reads etc. It is updated in 1 minute intervals.

Log.final.out: summary mapping statistics after mapping job is complete, very useful for quality control. The statistics are calculated for each read (single- or paired-end) and then summed or averaged over all reads. Note that STAR counts a paired-end read as one read, (unlike the samtools flagstat/idxstats, which count each mate separately). Most of the informa- tion is collected about the UNIQUE mappers (unlike samtools flagstat/idxstats which does not separate unique or multi-mappers). Each splicing is counted in the numbers of splices, which would correspond to summing the counts in SJ.out.tab. The mismatch/indel error rates are calculated on a per base basis, i.e. as total number of mismatches/indels in all unique mappers divided by the total number of mapped bases.

```
```
### `to short`:
```
--seedSearchStartLmax 30  # increase overall mapping sensitivity
--outFilterScoreMinOverLread 0 --outFilterMatchNminOverLread 0  --outFilterMatchNmin 50 # allow output of short alignments
```

```
"too short" means that the best alignments STAR found were too short to pass the filters.

This is controlled by --outFilterScoreMinOverLread --outFilterMatchNminOverLread which by default are set to 0.66. which means that ~2/3 of the total read length (sum of mates) should be mapped.

So what your output means is that 12% of the reads aligned unniquely, 7.7% aligned but multimapped and then 80% of your reads couldn't align with the above parameters. You can try to reduce these parameters to see how many more reads will be mapped. However, it looks like your data might just be contaminated with that alignment score :((

Here is a link to the convo I had with Alex, the developer of STAR. LINK
```
https://www.biostars.org/p/243020/

```
Another option is to output unmapped read into the SAM/BAM files - then the "unmapped type" is marked with the uT:A: tag, with n=1.

```





####

