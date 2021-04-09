#This script will parse a GFF File and extract features from the gene
# inputs: 1)GFF file 2)FASTA file(genome seq)

#Create and Argument parser object
parser= argparse.ArgumentParser(description='This script parse a GFF file')

#add positional ArgumentParser
parser.add_argument("gff" , help= 'name of GFF file')
parser.add_argument("fasta", help= 'name of FASTA file')

#parse the ArgumentParser
args = parser.parse_args()

#read in the FASTA file
genome = SeqIO.read(args.fasta, 'fasta')
print(genome.id)
#print (genome.seq)

#open and read in GFF file 
with open(args.gff, 'r') as gff_in:
  #create csv reader object
  reader = csv.reader(gff_in, delimiter= '\t')
  #loop over all the lines in our reader object, i.e. parsed file
  for line in reader:
   start = int(line[3]) - 1
   end = int(line[4]) + 1
   feature = line [8]
   print (feature)
   #extract the sequence 
   print(genome.seq[start:end])