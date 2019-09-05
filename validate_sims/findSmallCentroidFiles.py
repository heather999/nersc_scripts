import os
import sys
import glob
import json

def find_small_centroid_files(raw_image_dir, min_size=4e6):
    visit_dirs = sorted(glob.glob(os.path.join(raw_image_dir, '00*', '00*')))
    visits = []
    raftNames = []
    detectorNames = []
    sizes = []
    nvisits = len(visit_dirs)
    for i, visit_dir in enumerate(visit_dirs):
        if i % (nvisits//20) == 0:
            sys.stdout.write('.')
        centroid_files = sorted(glob.glob(os.path.join(visit_dir, 'centroid*')))
        for item in centroid_files:
            size = os.stat(item).st_size
            if size < min_size:
                tokens = os.path.basename(item).split('_')
                visits.append(int(tokens[1]))
                raftNames.append(tokens[2])
                detectorNames.append(tokens[3])
                sizes.append(size)
    return dict(visit=visits, raftName=raftNames, detectorName=detectorNames, size=sizes)

raw_image_dir = '/global/cscratch1/sd/desc/DC2/Run2.1.1i/run_agntest20190807/run/outputs'
run2_1_1i_wfd = find_small_centroid_files(raw_image_dir)

with open('run2_1_1i_wfd.json', 'w') as fp:
    json.dump(run2_1_1i_wfd, fp)
