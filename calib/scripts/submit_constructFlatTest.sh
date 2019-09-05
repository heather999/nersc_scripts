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
export REPODIR=/global/cscratch1/sd/descdm/DC2/Run2.1i/calibration/calib_repo

export RERUN=$1
source ${ROOTDIR}/setupdm.sh


/usr/bin/time --verbose constructFlat.py $REPODIR --rerun construct_calib:flat_test --longlog --id visit=5000000..5000500 raftName=R22 detectorName=S11 -C /global/cscratch1/sd/descdm/DC2/Run2.1i/calibration/flat_test.py --calib /global/cscratch1/sd/descdm/DC2/Run2.1i/calibration/calib_repo/CALIB --batch-type=smp --cores 20 |& tee constructFlat_test.log

#/usr/bin/time --verbose singleFrameDriver.py $REPODIR --rerun $RERUN --id visit=$2 --longlog --cores 40 --batch-type=smp --mpiexec="-launcher ssh" --clobber-versions |& tee singleFrame_k_$3_batch_$2.log


