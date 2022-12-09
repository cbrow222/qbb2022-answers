## Week 6 -- 10 points possible

1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 13 of 10 points possible

1. Given data question: What percentage of reads are valid interactions?

2. Given data question: What constitutes the majority of invalid 3C pairs?/What does it mean?

3. Script set up to (0.5 pts each)

  * read in data  
  * Filter data based on location --> you don't need for loops to do this. You can use vectorized boolean indexing like the following:

  ```
  data1 = data1[numpy.where((data1['F1'] >= start_bin) &
                                (data1['F2'] < end_bin))]
  ```

4. Script set up to log transform the scores

5. Script set up to shift the data by subtracting minimum value

6. Script set up to convert sparse data into square matrix --> you don't need a for loop for this. You can again use some vectorized operations like the following:

```
data1['F1'] -= start_bin
data1['F2'] -= start_bin
mat1[data1['F1'], data1['F2']] = data1['score']
mat1[data1['F2'], data1['F1']] = data1['score']
```

7. Script set up to (0.33 pts each)

  * remove distance dependent signal
  * smooth
  * subtract

8. Turned in the plot of the 3 heatmaps (ddCTCF, dCTCF, and difference) for subset dataset (0.33 pts each ddCTCF/dCTCF/difference)

* I wouldn't expect the dCTCF heatmap to be mostly black. But I see that you mention this in your README. The problem in the code seems to occur within in your `for j in range(len(data2)):` loop. You tell it to store `score` in `mat2[xcoord,ycoord]` and `mat2[ycoord,xcoord]`, but you save the mat2 score in the variable `mcore` not `score`. `score` was the variable in the previous for loop, so it must just be using the last value from the first for loop over and over again.

9. Turned in the plot of the 3 heatmaps (ddCTCF, dCTCF, and difference) for full dataset (0.33 pts each ddCTCF/dCTCF/difference)

* I wouldn't expect the dCTCF heatmap to be mostly black. But I see that you mention this in your README. (see description above for what I think the problem is)

10. Heatmap questions (0.33 pts each)

  * See the highlighted difference from the original figure?
  * impact of sequencing depth? --> great
  * highlighted signal indicates? --> yes, I believe it's supposed to refer to the differential interactions in the ddCTCF vs dCTCF genotypes

Possible Bonus points:

1. Insulation script set up to (0.25 pts each)

  * read in data
  * filter data based on location
  * log transform the data
  * shift the data by subtracting minimum value

2. Insulation script set up to (0.5 pts each)

  * convert sparse data into square matrix
  * find the insulation score by taking mean of 5x5 squares of interactions around target

  This is what I did to find the insulation score. I see what you're trying, but this is what I would recommend instead as it's looking both 5 downstream (the i-5:i) and 5 upstream (the i:i+5):

  ```
  starting_x = 10400000 + 200000 #first X coordinate should be 200K downstream of the upstream boundary of the heatmap, since you need to look 5 bins up and downstream to calculate the score
  for i in numpy.arange(5, N-4): #start at 5 since looking 5 below, and go until N-4 since looking 5 above
      scores.append(numpy.mean(mat[(i - 5):i, i:(i + 5)]))
      x_vals.append(starting_x)
      starting_x += 40000
  ```

3. Turned in the plot of the heatmap + insulation scores below (0.5 pts each panel)

* I don't expect the two large black bands in the heatmap
