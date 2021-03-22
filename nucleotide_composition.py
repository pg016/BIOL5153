# set the name of input sequnce file
filename = 'dna.txt'

# open the input file and assign to a file handle named "infile"
infile = open(filename, 'r') #creating a file handle

# read the file & save contents of file as variable
dna_seq = infile.read().rstrip() #the .rstrip() method removes "enter"

# close the file connection
infile.close()

# find the length of DNA sequence 
seqlen = len(dna_seq)
print("sequence length is:", seqlength, "bp")

# count number of each nucleotides in the sequence and divide by total number of characters

freqA = dna_seq.count("A") / seqlen
freqT = dna_seq.count("T") / seqlen
freqG = dna_seq.count("G") / seqlen
freqC = dna_seq.count("C") / seqlen
freqGC = round ((dna_seq.count("G") + dna_seq.count ("C') )/ seqlen, 3)

# check to see if all the frequencies of the nucleotides add upto 1
if "freqA +freqT +freqG +freqC) ==1
 # print frequencies of each nucleotide for the sequence
 print("freqA:", round(freqA, 3))
 print("freqT:", round(freqA, 3))
 print("freqG:", round(freqA, 3))
 print("freqC:", round(freqA, 3))
 print("G+C content:", round(freqA, 3))
 else:
 print ("None found")