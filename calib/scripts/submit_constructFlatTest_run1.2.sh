#!/bin/bash -l

#SBATCH --partition=regular
#SBATCH --nodes=1
#SBATCH --time=10:00:00
#SBATCH --job-name=k_flat
#SBATCH --constraint=knl
#SBATCH --license=cscratch1
#SBATCH --signal=B:USR1@120

export OMP_NUM_THREADS=1
export KMP_AFFINITY=disabled


export ROOTDIR=/global/cscratch1/sd/descdm/DC2/Run2.1i/calibration
export REPODIR=/global/cscratch1/sd/descdm/DC2/Run2.1i/calibration/calib_repo_run1.2

export RERUN=$1
source ${ROOTDIR}/setupdm.sh


/usr/bin/time --verbose constructFlat.py $REPODIR --rerun flat_test --longlog --id visit=5000000..5000009 raftName=R22 detectorName=S11 --calib /global/cscratch1/sd/descdm/DC2/Run2.1i/calibration/calib_repo_run1.2/CALIB --batch-type=smp --cores 20 |& tee constructFlat_test_run1_2.log



