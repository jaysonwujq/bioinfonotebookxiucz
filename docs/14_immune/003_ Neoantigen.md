  配对样本的全外的.bam数据，第一步通过POLYSOLVER tool工具对每个样本4-digit HLA基因型进行推断。体细胞突变数据（.maf）和HLA基因型数据作为输入文件，用NetMHCpan（v4.0）预测新的抗原。抗原通过蛋白编码单个核苷酸变异(SNV) (Variant_Classification = “Missense_Mutation”, and Variant_Type = ‘‘SNP”)，小的插入和缺失（Indel）(Variant_Classification = “Frame_Shift_Ins’’, ‘‘Frame_Shift_Del’’, ‘‘In_Frame_Ins’’, ‘‘In_Frame_Del’’, and Variant_Type = ‘‘INS”, “DEL”) 分别进行了预测。预测产生亲和力小于500nM的肽，且对应的基因表达超过Combat value 1（根据中值表达而不是特定样本进行评估）的突变被选为新的抗原。我们参考pVAC seq（10）并根据我们的数据集的特点对算法进行了修改。

https://github.com/tianshilu/QBRC-Neoantigen-Pipeline


https://github.com/XSLiuLab/Seq2Neo

