df <- read.table("1.txt", sep ="\t", header = T)
rownames(df)<- df$X
df <- df[,-grep("^X$",colnames(df))]
df
#进行不连续校正的卡方检验
result <- chisq.test(df, correct=F)
result

#获取期望次数
expected_count_l1=0
expected_count_g5=0
expected_count_g1l5=0

for (i in as.vector(result$expected)){
    if (i<1){
      expected_count_l1 = expected_count_l1+1
    } else if (i>5){
      expected_count_g5 = expected_count_g5+1
    } else if (i<5 && i>=1){
      expected_count_g1l5 = expected_count_g1l5+1
    }
}

print( paste("The minimum expected count:", min(as.vector(result$expected)), sep = " "))
print(paste("Cells have expected count less than 1:",expected_count_l1, sep = " "))
print(paste("Cells have expected count greater than 1 and less than 5:",expected_count_g1l5, sep = " "))
#print(expected_count_g1l5/length(as.vector(result$expected)))

# 判断使用何种检验
#1. 当T>=5, n>=40 时，直接用Pearson 卡方检验；
#2. 当1 =<T < 5 , n >= 40 时， 用连续性校正公式；
#3. 当T<1 , 或者 n < 40, 或做卡方检验后所得的P值接近检验水准a 时，用确切概率（Fisher exact test ）。

# 
if (expected_count_l1 > 0){
   result2 <- fisher.test(df)
   print("Fisher Exact Test Selected")
   print(result2)
   print(paste("P value:", result2$p.value, sep = " "))

} else if (expected_count_g5 > 0){
   result2 <- chisq.test(df, correct=F)
   print(paste("P value:", result2$p.value, sep = " "))
   print(paste("Expected Count", result2$expected, sep = " "))
#sqrt(result2$statistic/(sum(df) + result2$statistic)) # 列联系数
#E <- result2$expected
#O <- result2$observed
#(O-E)^2/E

} else {
   result2 <- result
#sqrt(result2$statistic/(sum(df) + result2$statistic)) # 列联系数
}




