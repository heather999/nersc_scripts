#!/bin/bash -l

#SBATCH --partition=regular
#SBATCH --nodes=1
#SBATCH --time=11:00:00
#SBATCH --job-name=k_flat
#SBATCH --constraint=knl
#SBATCH --license=cscratch1
#SBATCH --signal=B:USR1@120

export OMP_NUM_THREADS=1
export KMP_AFFINITY=disabled


export ROOTDIR=/global/cscratch1/sd/descdm/DC2/Run2.1i/calibration
export REPODIR=/global/cscratch1/sd/descdm/DC2/Run2.1i/calibration/calib_repo

export RERUN=$1
source ${ROOTDIR}/setupdm-w14.sh


/usr/bin/time --verbose constructFlat.py $REPODIR --calib /global/cscratch1/sd/descdm/DC2/Run2.1i/calibration/calib_repo/CALIB --rerun construct_calib:flat_20190408 --longlog --id visit=5000000..5000500 --batch-type=smp --cores 20 |& tee constructFlat_20190408.log



