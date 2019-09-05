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

/usr/bin/time --verbose ingestImages.py $REPODIR /global/cscratch1/sd/descdm/DC2/Run2.1i/calibration/bf_flats_20190408/20k/*.fits --mode link |& tee ingestImageFlat_20k.log
/usr/bin/time --verbose ingestImages.py $REPODIR /global/cscratch1/sd/descdm/DC2/Run2.1i/calibration/bf_flats_20190408/40k/*.fits --mode link |& tee ingestImageFlat_40k.log
/usr/bin/time --verbose ingestImages.py $REPODIR /global/cscratch1/sd/descdm/DC2/Run2.1i/calibration/bf_flats_20190408/60k/*.fits --mode link |& tee ingestImageFlat_60k.log
/usr/bin/time --verbose ingestImages.py $REPODIR /global/cscratch1/sd/descdm/DC2/Run2.1i/calibration/bf_flats_20190408/80k/*.fits --mode link |& tee ingestImageFlat_80k.log






