import os
import glob
from collections import defaultdict
import numpy as np

#see: https://lsstc.slack.com/archives/C932BQ550/p1555558718024300?thread_ts=1555516480.008700&cid=C932BQ550

data_dir = '/global/projecta/projectdirs/lsst/production/DC2_ImSim/Run2.1i/run201903/outputs/00201989to00262897'

visit_dirs = sorted(glob.glob(os.path.join(data_dir, '00*')))

visits_by_band = defaultdict(list)
for visit_dir in visit_dirs:
    centroid_files = sorted(glob.glob(os.path.join(visit_dir, 'centroid*')))
    if len(centroid_files) == 189:
        tokens = os.path.basename(centroid_files[0]).split('_')
        visits_by_band[tokens[4].split('.')[0]].append(int(tokens[1]))

print("full focal planes per band:")
for band in 'ugrizy':
    print(band, len(visits_by_band[band]))

print()
print("one per band at random:")  
for band in 'ugrizy':
    np.random.shuffle(visits_by_band[band])
    print(band, visits_by_band[band][0])
