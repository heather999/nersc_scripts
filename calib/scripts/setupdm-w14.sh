#!/bin/sh

## cvmfsSetup.sh - from Heather Kelly (1/30/2019) to set up DMstack
## envrironment within which to run the BF kernel generation code.
## Work in progress!


export STACKCVMFS=/cvmfs/sw.lsst.eu/linux-x86_64/lsst_distrib
export LSST_STACK_VERSION=w_2019_14

export LOCALDIR=/global/common/software/lsst/cori-haswell-gcc/DC2/calibration

module unload python
module swap PrgEnv-intel PrgEnv-gnu
module load pe_archive
module swap gcc gcc/6.3.0
module rm craype-network-aries
module rm cray-libsci
module unload craype
export CC=gcc

source $STACKCVMFS/$LSST_STACK_VERSION/loadLSST.bash
setup lsst_distrib
setup -r $LOCALDIR/obs_lsst -j

export OMP_NUM_THREADS=1

