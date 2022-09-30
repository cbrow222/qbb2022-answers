Excellent work. You nailed needleman-wunsch and your alignment stats are (almost) exactly what I would have expected. There were a few minor errors:

First, the way you're doing traceback, your final alignments are actually reversed. You can either add new characters to the beginning of each alignment (rather than appending to the end), or the quicker option is to just reverse your alignments before writing it to the output. (-0.25).

Secondly, remember to initialize the first row and column of the traceback matrix, if you don't your program could run forever if there are leading gaps (which is actually the case in the DNA alignment) (-0.5)

Finally, your while condition is `i>0 and j>0`, but that will actually terminate as soon as either i or j become 0, which is not what we want if there are leading gaps (this is actually saving your DNA alignment from running forever, as a result of that second error). Because of this, your count for the number of gaps in the DNA alignment is slightly off (-0.25)

9/10
