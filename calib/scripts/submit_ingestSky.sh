#!/bin/bash -l

#SBATCH --partition=regular
#SBATCH --nodes=1
#SBATCH --time=8:00:00
#SBATCH --job-name=k_bias
#SBATCH --constraint=knl
#SBATCH --license=cscratch1
#SBATCH --signal=B:USR1@120

export OMP_NUM_THREADS=1
#export KMP_AFFINITY=disabled


export ROOTDIR=/global/cscratch1/sd/descdm/DC2/Run2.1i/calibration/w_2019_14
export REPODIR=/global/cscratch1/sd/descdm/DC2/Run2.1i/calibration/w_2019_14/calib_repo

export RERUN=$1
source ${ROOTDIR}/setupdm-w14.sh


/usr/bin/time --verbose ingestCalibs.py $REPODIR --output $REPODIR/CALIB --validity 4000 $ROOTDIR/../sky_frames/*/*.fits --longlog -j 63 --mode copy |& tee ingestSkyFrames_5.log



