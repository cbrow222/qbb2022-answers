#!/usr/bin/env python3

import sys

def parse_bed(fname):  #define function
    
    #make sure file exists
    try:
        fs = open(fname, 'r') #opening file
    except:
        raise FileNotFoundError("That file doesn’t appear to exist")
    
    #initialize place to put data, data types and bad line counter
    bed = []
    field_types = [str, int, int, str, float, str, int, int, str, int, str, str]
    count_bad_lines = 0
    
    #checking field numbers
    for i, line in enumerate(fs):
        if line.startswith("#"): #ignore comment lines
            continue
        fields = line.rstrip().split() #separate line into fields
        fieldN = len(fields) #how many fields
        if fieldN < 3: #what to do with not enough fields
            print(f"This file is not correctly formatted", file=sys.stderr)
            continue
        if (fieldN == 10) or (fieldN == 11): #what to do with 10 or 11 fields
            print(f"This file is not correctly formatted", file=sys.stderr)
            continue
        
        #data formatting
        try:
            for j in range(min(len(field_types), len(fields))): #loop through fields
                if j == 8: #dealing with RGB color
                    fields[j]=fields[j].split(",") #split into 3 values
                    if len(fields[j]) != 3: #what to do with incorrect number of values
                        print(f"line {j} appears malformed", file=sys.stderr)
                        count_bad_lines += 1 #keeping track of bad lines
                        continue
                    #make each value and integer
                    fields[j][0] = int(fields[j][0])
                    fields[j][1] = int(fields[j][1])
                    fields[j][2] = int(fields[j][2])
                elif (j == 10) or (j==11): #what to do with Block starts and lengths
                    fields[j]=fields[j].rstrip(",").split(",") #split on the commas
                    if len(fields[j]) != fields[9]: #checking if it matches block number column
                        print(f"line {j} appears malformed", file=sys.stderr)
                        count_bad_lines += 1 #keeping track of bad lines
                        continue
                    for k in range(len(fields[j])): #converting to integers
                        fields[j][k]=int(fields[j][k])
                else: #dealing with all the other columns
                    fields[j] = field_types[j](fields[j]) #converting columns
            bed.append(fields) #adding fields to the file for saving
        except: #error handling/printing to stderr
            print(f"Line {i} appears malformed", file=sys.stderr)
            count_bad_lines += 1 #keeping track of bad lines
    if count_bad_lines>0: #printing out number of bad lines if they are present
        print(f"{count_bad_lines} lines were malformed", file=sys.stderr)
    fs.close() #closing file
    return bed #returning value

#instructions if run as a script
if __name__ == "__main__":
    fname = sys.argv[1]
    bed = parse_bed(fname)
