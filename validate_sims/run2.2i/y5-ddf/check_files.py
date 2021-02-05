import os, sys
import argparse
import glob 

parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("--indir", required=True, type=str, help="input file")
args = parser.parse_args()

#rootdir='/global/cscratch1/sd/descim/Run2.2i/y1-wfd/run/outputs/*/'

#badFiles = open("/global/cscratch1/sd/heatherk/nersc_scripts/validate_sims/run2.2i/y1-wfd/run2.2i-y1-wfd.txt", 'w')
badFiles = open(args.indir+".txt", 'w')
#goodFiles = open("/global/cscratch1/sd/heatherk/DC2/Run2.1i/good_run2.1i-y2_00445379to00497969.txt", 'w')


with open(args.indir) as inputf:
    dirlist = inputf.readlines()
dirlist = [x.strip() for x in dirlist]    

counter = 0
for x in dirlist :
    fileIter = glob.iglob(os.path.join(x,'lsst_a*.fits')) 
    for f in fileIter :
        #os.system ("/global/cscratch1/sd/heatherk/fits/fitsverify/fitsverify -e -q %s |grep -c "17 errors" % (f))
        retcode =  os.popen("/global/cscratch1/sd/heatherk/fits/fitsverify-Aug2019/fitsverify/fitsverify -e -q %s | grep -c 'verification OK'" % f).read()
        if int(retcode) != 1 :
            print("Found bad " + f)
            badFiles.write(f+"\n")
        counter = counter + 1
        if counter % 100 == 0 :
            print("At file: " + str(counter))

    
badFiles.close() 
