import subprocess
import os, sys
import time, glob
import argparse

parser = argparse.ArgumentParser(description='Process input params.')
parser.add_argument('--rootdir', type=str, help='input directory containing sim FITS files', required=True)
parser.add_argument('--outfile', type=str, help='outputFile', required=True)
parser.add_argument('--maxproc', type=int, help='max num proceses', default=10)
args = parser.parse_args()

rootdir=args.rootdir+"/*"
#print(rootdir)
#rootdir='/global/cscratch1/sd/heatherk/DC2/Run2.1i/y5-ddf/shortfits/*/'
#outdir='/global/cscratch1/sd/heatherk/DC2/Run2.1i/y5-ddf/nersc_scripts_new/validate_sims'

command = "/global/cscratch1/sd/heatherk/fits/fitsverify-Aug2019/fitsverify/fitsverify -e -q "
processes = set()
max_processes = args.maxproc

badFiles = open(args.outfile, 'w')


def checkOutput(proc):
   out = str(proc.stdout)
   found = out.find("verification OK")
   #print(str(proc.stdout))
   if found == -1: 
       #print("fverify did not return OK " + proc.args)
       badFiles.write(proc.args+"\n")

fileIter = glob.iglob(os.path.join(rootdir,'lsst_a*.fits')) 

for f in fileIter :
    cmd2 = command + f
    processes.add(subprocess.run(cmd2, shell=True, stdout=subprocess.PIPE, encoding='utf-8'))
    if len(processes) >= max_processes:
        time.sleep(.1)
        for p in processes:
            if p is not None:
                checkOutput(p)
        processes.difference_update(
            [p for p in processes if p is not None])

#Check if all the child processes were closed
for p in processes:
    if p is None:
        p.wait()
    checkOutput(p)

badFiles.close() 
