import os
import glob
from astropy.io import fits

bf_flat_dir = '/global/cscratch1/sd/descdm/DC2/Run2.1i/calibration/bf_flats'

subdirs = sorted(glob.glob(os.path.join(bf_flat_dir, '*k')))
for subdir in subdirs:
    raw_files = sorted(glob.glob(os.path.join(subdir, 'lsst_a*')))
    for raw_file in raw_files:
        with fits.open(raw_file) as hdulist:
            hdulist[0].header['RUNNUM'] = hdulist[0].header['OBSID']
            hdulist.writeto(raw_file, overwrite=True)
