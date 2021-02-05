#!/bin/sh

module unload python
#module swap PrgEnv-intel PrgEnv-gnu
module load cfitsio/3.47
module load python/3.6-anaconda-4.4
export LD_LIBRARY_PATH=/usr/common/software/cfitsio/3.47/lib:$LD_LIBRARY_PATH
