import glob, os, re


# FITS files:lsst_a_712627_R14_S00_z.fits 
# checkpoints: ./00201989to00262897/00240808/checkpoint-240808-R_3_1_S_2_0.ckpt

fits_prefix = "lsst_a_"
fits_suffix = ".fits"

# Reading a line in a file 
f = open("/global/cscratch1/sd/heatherk/run2-1i_old_psf_checkpointfiles.txt", 'r') 
myOut = open("/global/cscratch1/sd/heatherk/badFiles.txt", 'w')
myVisit = open("/global/cscratch1/sd/heatherk/visits.txt", 'w')

lastVisit = 0
for text in f:
    #text = f.readline() 
    parsePath = re.split('\/', text)
    curdir = parsePath[1] + "/" + parsePath[2]
    print(curdir)
    checkpointFile = parsePath[3]
    parseCheckpointFile = re.split('-', checkpointFile)
    visit = parseCheckpointFile[1]
    raftAndSensor = parseCheckpointFile[2]
    parseRaftAndSensor = re.split('_', raftAndSensor)
    raft = parseRaftAndSensor[0]+parseRaftAndSensor[1]+parseRaftAndSensor[2]
    print(raft)
    print(parseRaftAndSensor[5])
    print(re.split('\.', parseRaftAndSensor[5])[0])
    sensor = parseRaftAndSensor[3]+parseRaftAndSensor[4]+ re.split('\.',parseRaftAndSensor[5])[0]
    print(sensor)
    fitsFileName = fits_prefix + visit + "_" + raft + "_" +sensor + "*" + fits_suffix
    print(fits_suffix)
    print(fitsFileName)

    searchDir = "/global/projecta/projectdirs/lsst/production/DC2_ImSim/Run2.1i/old_psf_model/" + curdir
    os.chdir(searchDir)
    if len(glob.glob(fitsFileName)) > 0:
        # Found a checkpoint file and a FITS file - likely incomplete processing
        print("Found One " + searchDir + glob.glob(fitsFileName)[0])
        myOut.write(text + " " + glob.glob(fitsFileName)[0]+'\n')
        if (visit != lastVisit) :
            myVisit.write(visit+"\n")
        lastVisit = visit

f.close() 
myOut.close()
myVisit.close()

