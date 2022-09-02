#USAGE: python Brown_tail.py input_filename [number_lines to return]
import sys #import module
filename = sys.argv[1] #SET input filename
if len(sys.argv) > 2: #IF user-specified number of lines present
    n_lines = int(sys.argv[2]) #SET desired number of lines
else: #otherwise
    n_lines = 10 #SET desired number of lines
line_list=[]
for i, line in enumerate(open(filename)): #loop through lines
    line_list.append(line) #Store line in list
for i,line in enumerate(line_list): #loop through list
    if i >= (len(line_list)-n_lines): #if desired line
        print (line.strip('\r\n')) #Print the line
