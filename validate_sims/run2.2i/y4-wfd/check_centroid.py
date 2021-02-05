import os, sys
import argparse
import glob 
import gzip


parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("--indir", required=True, type=str, help="input file")
args = parser.parse_args()

#rootdir='/global/cscratch1/sd/descim/Run2.2i/y1-wfd/run/outputs/*/'

badFiles = open(args.indir+"_centroid.txt", 'w')


with open(args.indir) as inputf:
    dirlist = inputf.readlines()
dirlist = [x.strip() for x in dirlist]    

counter = 0
for x in dirlist :
    fileIter = glob.iglob(os.path.join(x,'centroid*.txt.gz')) 
    for f in fileIter :
        counter = counter + 1
        if counter % 100 == 0 :
            print("At file: " + str(counter))
        try:
            linelist = gzip.open(f, 'rt').readlines()
        except Exception as e:
            print("Found bad " + f)
            badFiles.write(f+"\n")
            continue
        #retcode =  os.popen("gzip.open(%s, 'rt').readlines() | grep -c 'Err'" % f).read()
        #if int(retcode) != 1 :
        #if retcode :
        #    print("Found bad " + f)
        #    badFiles.write(f+"\n")
        if os.stat(f).st_size == 0 :
            print("Found bad " + f)
            badFiles.write(f+"\n")

    
badFiles.close() 
