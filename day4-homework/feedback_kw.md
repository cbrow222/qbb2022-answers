# day 4 homework feedback

Fantastic work all around! You've done exactly what was asked, including accurate and insightful comparisons to the paper.

For the numpy array that goes from 0.55 to 1.05 incremented by 0.05, is 1.05 included in the array itself? Or is it an exclusive end value?

Also, for the heatmap, great job using just a single colorbar! if you wanted to resize the axes, there's somethinng called gridspec which follows a different overall structure to subplots: https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure.add_gridspec or just a constrained layout: https://matplotlib.org/stable/gallery/subplots_axes_and_figures/demo_constrained_layout.html. But what you have is fantastic! I alternatively sometimes will use 3 subplots and use the first two axes (both without colorbars) and then plot just the colorbar on the third axis without a heatmap
