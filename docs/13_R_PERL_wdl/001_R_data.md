https://stackoverflow.com/questions/64392606/merge-two-columns-to-a-value-range-column-in-r

```
rangesA <- data.frame(
    chrom = c(5, 1, 9),
    start = c(100, 200, 275),
    stop = c(105, 250, 300)
)
rangesB <- data.frame(
    chrom = c(1, 5, 9),
    start = c(200, 99, 275),
    stop = c(265, 106, 290)
)
inner_join(rangesA, rangesB, by="chrom") %>% 
  filter(start.y < start.x | stop.y > stop.x)
```