https://www.jianshu.com/p/4c019467cb56

WISECONDOR的局限
对性染色体的拷贝数检测效果不佳。WISECONDOR 使用 Stouffer’s z-score sliding window 的方法进行segment 并检测拷贝数异常。当bins size 很小时（15kb 运行了24h）这种算法运行很慢，而且当染色体有大量异常时会出错。尤其异常片段内的异常无法检测出来。


https://www.jianshu.com/p/a56ba0942bda
