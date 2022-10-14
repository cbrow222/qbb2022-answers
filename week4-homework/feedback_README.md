Really awesome job! A few minor things:

1. You probably want to give your plink commands the `--out` argument, so that you can name your output files. This will make it so that your linear regressions don't overwrite eachother (the way you have it currently, I believe they'll both output a `plink.assoc.linear` file, thereby overwriting eachother. (no points deducted)
2. One very minor suggestion I'll make from looking at your code: try not to use user-defined values in your code when possible. So in your `boxplot.py` script, you use `SNPoi` and `rowoi` to define the snp and row you're interested in, but instead of setting these variables yourself, you should derive them automatically from the data (as you did in `Manhattanplot.py`) (no points deducted)
3. You actually have a very small error in your `rowoi` for the boxplot script. I think the number you have is one larger than it should be, because the vcf array doesn't have a header. That's why your boxplot looks like there's not a strong association. (-0.5)
4. We're actually missing your manhattan plot itself, but I ran the code and the plot looks correct, so you're good to go. Just make sure you upload everything you need to in the future (no points deducted)

Otherwise, awesome work!

(9.5/10)
