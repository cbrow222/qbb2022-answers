# Feedback day2-lunch

This script looks good. Just a couple of subtle issues to watch out for.

In your for loop for converting the fields data types, when you are processing the itemRGB, blockSizes, and blockStarts fields, you have a check to make sure the lines are correctly formatted. If they aren't, you add one to the count and `continue`. The problem comes from the fact that `continue` skips to the beginning of the next loop in the for loop. In this case, it jumps to the next value of j for converting the next field, not the next line of the file. That means that you could count lines with incorrect numbers of items in these fields as being malformed, but also include them in your final bed list. You can also get double-counting of malformed lines, as you note in the readme. 

One solution would be to throw an error, just like would happen if you try to convert a variable that can't be converted. it would look like `raise RunTimeError` or whatever error you thought was most appropriate. This would cause the code to exit the `try` statement and move to `except`, where it would get counted and not included in the bed list. Another solution would be to do these checks after finishing the type conversion for loop. Then the `continue` statements would work as intended.

All in all, this is a good script and you appear to be pretty comfortable with this level of python. Great work and keep it up!