https://gatk.broadinstitute.org/hc/en-us/articles/360035531092?id=11682

```
#拷贝数变化比值 copy ratio 的中位数绝对偏差（median absolute deviation, MAD）
dengjunxue.standardizedMAD.txt  # 标准化后的 copy ratios 的 MAD
dengjunxue.denoisedMAD.txt # 降噪后的 copy ratios 的 MAD
dengjunxue.deltaMAD.txt # 标准化后的 MAD 和降噪后的 MAD 的差
dengjunxue.scaledDeltaMAD.txt # (降噪后的 MAD - 标准化后的 MAD ) / (标准化后的 MAD )
```