kpPlotBAMDensity可以从看全基因组层面看，基本的覆盖情况，成图快；
kpPlotBAMCoverage成图慢，不适合全基因组看，适合选择小区域进行
 + And one last important thing: each graphical device has its own units, pdf work with inches but png works with pixels, so the png call you've written would produce a tiiiiny png file of 15 per 7 pixels. I usually work with png file between 1000 and 3000 pixels in their longest side.

kpPlotCoverage = kpPlotDensity with window.size set to 1 
kpPlotDensity 

The actual representation of the data is also different than that of kpPlotDensity: kpPlotCoverage uses kpBars to create the plot, giving it a histogram-like appearance.

