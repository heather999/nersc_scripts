import os, sys
import glob 


outdir='/global/cscratch1/sd/heatherk/DC2/Run2.1.1i/test6months'
rootdir='/global/cscratch1/sd/desc/DC2/Run2.1.1i/run_agntest20190807/run/outputs/00385844to00445379/*/'

badFiles = open("/global/cscratch1/sd/heatherk/DC2/Run2.1.1i/test6months/bad_run2.1.1i-00385844to00445379.txt", 'w')
#goodFiles = open("/global/cscratch1/sd/heatherk/DC2/Run2.1i/good_run2.1i-y2_00445379to00497969.txt", 'w')


fileIter = glob.iglob(os.path.join(rootdir,'lsst_a*.fits')) 

for f in fileIter :
    #os.system ("/global/cscratch1/sd/heatherk/fits/fitsverify/fitsverify -e -q %s |grep -c "17 errors" % (f))
    retcode =  os.popen("/global/cscratch1/sd/heatherk/fits/fitsverify-Aug2019/fitsverify/fitsverify -e -q %s | grep -c 'verification OK'" % f).read()
    if int(retcode) != 1 :
        print("Found bad " + f)
        badFiles.write(f+"\n")

    
badFiles.close() 
