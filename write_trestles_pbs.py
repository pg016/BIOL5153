#! /usr/bin/env python3
#This script generates a PBS file for the Trsetles cluster
#This section prints the header/required info for PBS script
jobname= 'jobID'
queue= 'tiny16core'
output_prefix= 'jobID.out'
nodes= 1
ppn= 1
walltime = 1
print('PBS -N', jobname)
print('PBS -q',queue) #which queue to use
print('PBS -j oe') #join the STDOUT and STDERR into a single file
print('PBS -o', output_prefix+ '.$PBS_JOBID') #set the name of the job output file
print('PBS -l nodes='+str(nodes)+':ppn='+str(ppn)) #how many resources to ask for (nodes = num nodes, ppn = num processors)
print("PBS -l walltime="+str(walltime)+":00:00") #set the walltime (default to 1 hr)
print()
 
#cd into working directory 
print('cd $PBS_O_WORKDIR')
print()

#load the necessary modules
print("module purge")
print("module load gcc/7.2.1")
print()

#commands for this job
print("#insert commands here")

