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


# CNVpytor
## 交互式命令
`https://github.com/abyzovlab/CNVpytor/blob/master/cnvpytor/viewer.py`
```
cnvpytor> help

help
    Print help for a topic, command or parameter.

USAGE
    help <topic>

    List of params: bin_size, panels, rd_raw, rd_corrected, rd_partition, rd_call, r
d_use_mask, rd_use_gc_corr, callers, Q0_range, pN_range, dG_range, size_range, p_ran
ge, annotate, rd_range, rd_manhattan_range, rd_manhattan_call, snp_use_mask, snp_use
_id, snp_use_phase, snp_call, markersize, lh_markersize, lh_marker, rd_colors, legen
d, title, snp_colors, snp_alpha_P, rd_circular_colors, snp_circular_colors, baf_colo
rs, lh_colors, plot_files, plot_file, plot, file_titles, chrom, style, grid, subgrid
, panel_size, xkcd, margins, dpi, output_filename, print_filename, contrast, min_seg
ment_size


    List of commands: set, unset, help, save, show, quit, exit, rd, likelihood, baf, snp, info, stat, rdstat, circular, manhattan, genotype, calls, print, ls, meta, compare

    List of topics: plotting, signals

EXAMPLE(s)
    help bin_size
    help plotting

cnvpytor> gc_info
cnvpytor> show
```
## 过滤
+ The regions of deletion and duplication were then genotyped and only the regions with a copy number of >1.75 and <2.25 in normal samples were considered. To further filter the CNAs, only the regions with copy number difference greater than 0.2 with respect to normal tissue were chosen.（doi: 10.18632/oncotarget.23687）