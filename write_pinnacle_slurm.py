#!/bin/bash

# This script generates a slurm file for the AHPCC cluster

# define some variables
name = 'name' #name of the job
queue = 'comp6'# queue to run job
wall = 3 #walltimein hours 
nodes=1 #nodes to ask 
ppn=1 #processors to ask
walltime=5


# This prints header info for slurm script
print('#SBATCH -J' , job_name) #name of job 
print('#SBATCH --partition' , queue) #name of queue for job
print('#SBATCH -o' , name+'.txt') #name of STDOUT file
print('#SBATCH -e' , name+'.err') #name of STDERR file
print('#SBATCH --mail-type=ALL')  #sets email alerts on job
print('#SBATCH --mail-user=pg016@uark.edu') #sends email to   
print('#SBATCH --nodes=1'+str(nodes)) #number of nodes
print('#SBATCH --ntasks-per-node='+str(ppn)) #number of processors
print('#SBATCH --time='+str(wall)+':00:00') #walltime asked
print()

print('export OMP_NUM_THREADS=32')
print()
 
print('# load required modules')
print('module load java')
 
# cd into the working directory 
print(' cd $SLURM_SUBMIT_DIR')

# copy files from storage to scratch
print('# input files needed to run job')
print('files=')
print('rsync -av files /scratch/$SLURM_JOB_ID')

# cd onto the scratch disk to run the job
print('cd /scratch/$SLURM_JOB_ID/')
print()

# commands for job
print('# insert commands here')
print()
 
# copy output files back to storage
print('rsync -av' , name, '$SLURM_SUBMIT_DIR')

