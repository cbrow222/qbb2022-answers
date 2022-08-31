#!/usr/bin/env python3

import sys

def parse_vcf(fname): #define function

#preset variables for use
    vcf = [] #place to save data
    info_description = {} #dictionary for info descriptions
    info_type = {} #dictionary for info types
    format_description = {} #dictionary for format descriptions
    type_map = {
        "Float": float,
        "Integer": int,
        "String": str
        } #relating types from header to python names
    malformed = 0 #how many lines don't conform

    #trying to open file
    try:
        fs = open(fname) #open file
    except: #if the file doesn't exist
        raise FileNotFoundError(f"{fname} does not appear to exist", file=sys.stderr)

#looping through the lines
    for h, line in enumerate(fs): #loop through lines labelled with their numeber
    
        #looking at the header
        if line.startswith("#"):
            try:
                #do you have a FORMAT line
                if line.startswith("##FORMAT"):
                    fields = line.split("=<")[1].rstrip(">\r\n") + "," #Segment line and remove unnecessary characters
                    #initializing some things
                    i = 0 #format line counters
                    start = 0
                    in_string = False
                    while i < len(fields): #keep looping until you've moved through all the Format lines
                        if fields[i] == "," and not in_string: #if there is a line 
                            name, value = fields[start:i].split('=') #split on the "="
                            
                            #identify the fields for storage
                            if name == "ID": #the identity
                                ID = value
                            elif name == "Description": #the description
                                desc = value
                            start = i + 1 #increase start
                        elif fields[i] == '"': #if the field is empty
                            in_string = not in_string #make in_string True
                        i += 1 #add 1 to i, move through count, will cause exit of the while loop when the fields have all been moved through
                    format_description[ID] = desc.strip('"') #store format info in a dicationary
                
                #info lines
                elif line.startswith("##INFO"): #identify line
                    fields = line.split("=<")[1].rstrip(">\r\n") + "," #split up the line
                    
                    #initialize some things
                    i = 0 #line counter
                    start = 0
                    in_string = False
                    while i < len(fields): #keep looping while there are more info lines
                        if fields[i] == "," and not in_string: #if you have a field
                            name, value = fields[start:i].split('=') #split on the "="
                            
                            #identify the fields for storage
                            if name == "ID": #identification
                                ID = value
                            elif name == "Description": #description
                                desc = value
                            elif name == "Type": #data type
                                Type = value
                            start = i + 1 #increment start
                        elif fields[i] == '"': #if line is empty
                            in_string = not in_string #set in_string to True
                        i += 1 #increment i, will cause exit to for loop when all the line have run
                    info_description[ID] = desc.strip('"') #store the info description in a dictionary
                    info_type[ID] = Type #store the info type in a dictionary
                
                #the header line
                elif line.startswith('#CHROM'): #ID the line
                    fields = line.lstrip("#").rstrip().split("\t") #make it tab delineated
                    vcf.append(fields) #add it to fields
            except: #if something is wrong
                raise RuntimeError("Malformed header")
       
       #dealing with the actual data lines
        else:
            try:
                fields = line.rstrip().split("\t") #make each line tab delineated
                fields[1] = int(fields[1]) #make POS an int, because it is
                if fields[5] != ".": #if field 5 is a .
                    fields[5] = float(fields[5]) #how to handle it so you don't get and error
                
                info = {} #initialize dictionary to store line 7
                
                #dealing with field 7 
                for entry in fields[7].split(";"): #split by ; and loop through
                    temp = entry.split("=") #split by = temporarily save
                    if len(temp) == 1: #if is only one part
                        info[temp[0]] = None #dictionary key has no value
                    else: #if there is more than one part
                        name, value = temp #name the two parts
                        Type = info_type[name] #set the type to something python recognizes
                        info[name] = type_map[Type](value) #save the info in the dictionary with the value in the correct type
                fields[7] = info #put the dictionary back into the file you will save
                
                #dealing with lines past 8
                if len(fields) > 8: #if you have more fields, if you have genotyping data
                    fields[8] = fields[8].split(":") #split them on :
                    if len(fields[8]) > 1: #if they have multiple parts
                        for i in range(9, len(fields)): #loop through all the parts
                            fields[i] = fields[i].split(':') #split all the parts apart
                    else: #if there is only one part
                        fields[8] = fields[8][0] #make that element back into a str
                vcf.append(fields) #add the fields to the vcf you are storing
           
            except: #if something goes wrong
                malformed += 1 #add one to the malformed lines
                
    vcf[0][7] = info_description #add the info descriptions to the header
    if len(vcf[0]) > 8: #if you have more than 8 lines in the header
        vcf[0][8] = format_description #add the format descriptions to the header
    
    if malformed > 0: #if you have a malformed line
        print(f"There were {malformed} malformed entries", file=sys.stderr) #display message
    return vcf #end the function

#are you running the function from the script of calling it from elsewhere
if __name__ == "__main__": #identify how it is being run and keep going if it is the main
    fname = sys.argv[1] #the function name is user provider
    vcf = parse_vcf(fname) #run the function
    for i in range(10): #loop 10 lines
        print(vcf[i]) #print those lines
