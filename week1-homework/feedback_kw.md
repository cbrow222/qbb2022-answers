# Week 1 Genome Assembly -- Feedback

1 + 1 + 1 + 1 + 0.75 + 1 + 1 + 0.9075 + 1 + 1  = 9.66 points out of 10 possible points


1. Question 1.1, 1.4 how many reads (0.5 pts each)

  * good --> +1

2. Question 1.2, 1.4 simulation script(s)

  * good work overall! Instead of hardcoding the number of reads in the for loop, you could use your `reads` variable.
  * Also, you're simulating one less read than expected since you're starting your range functions at 1.
  * Consider using a single script that accepts command line/user input or a function that you can pass the changing variables to
  * --> +1

3. Question 1.2, 1.4 plotting script(s)

  * nice plotting code --> +1

4. Question 1.2, 1.4 histograms with overlaid Poisson distributions (0.5 pts each)

  * good plots overall! maybe use a few less bins, just looking at whole number/integers for coverage? --> +1

5. Question 1.3, 1.4 how much of genome not sequenced/comparison to Poisson expectations (0.5 pts each, 0.25 for answer and 0.25 for code)

  * 1.2 I see code and answer for observations, but nothing for Poisson
  * 1.4 I see answer and code for both
  * --> +0.75

6. Question 2 De novo assembly (0.5 pts each, 0.25 for answer and 0.25 for code)

  * number of contigs --> +0.5
  * total length of contigs --> +0.5

7. Question 2 De novo assembly cont (0.5 pts each, 0.25 for answer and 0.25 for code)

  * size of largest contig -->+0.5
  * contig n50 size --> +0.5

8. whole genome alignment (0.33 pts each, 0.33/2 for answer and 0.33/2 for code)

  * average identity --> +0.33
  * length of longest alignment --> +0.33
  * how many insertions and deletions in assembly ; how many deletions were there? --> 0.2475 (+ 0.33/4 for half answer + 0.33/2 for explanation/code)

9. decoding the insertion (0.5 pts each, 0.25 for answer and 0.25 for code)

  * position of insertion in assembly --> 0.5
  * length of novel insertion ; you want to add one to that length. Length is end - start + 1, or 710 bases --> +0.5

10. decoding the insertion cont (0.5 pts each, 0.25 for answer and 0.25 for code)

  * DNA sequence of encoded message --> +0.5
  * secret message --> +0.5
