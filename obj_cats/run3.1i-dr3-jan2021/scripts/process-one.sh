#!/bin/bash
shifter --image=lsstdesc/desc-drp-stack:v19-dc2-run2.2-v5 /bin/bash -s <<HEREDOC
source /opt/lsst/software/stack/loadLSST.bash
setup lsst_distrib
echo $1
python /opt/lsst/software/stack/DC2-production-0.4.0/scripts/make_object_catalog.py /global/cfs/cdirs/lsst/production/DC2_ImSim/Run3.1i/desc_dm_drp/nersc/v19.0.0-v1/Run3.1i/DR3/repo/rerun/dr3-multiband $1 -o $PWD |& tee objCat-$1.log
python /opt/lsst/software/stack/DC2-production-0.4.0/scripts/merge_parquet_files.py $PWD/object_$1_*.parquet -o $PWD/object_tract_$1.parquet --assume-consistent-schema |& tee merge-$1.log
HEREDOC
