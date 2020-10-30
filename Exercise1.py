#!/bin/usr/python3 
#trim adapter of 14 bases 
#first open and read file 
input_txt_contents = open('input.txt').read().upper().replace('ATTCGATTATAAGC','').split()
#open output pipe 
cleanseqs = open('Cleaned_sequences.txt','w')
for cleanones in input_txt_contents:
    cleanseqs.write(cleanones + '\n')
    cleanones
cleanseqs.close()
