#!/bin/bash
shifter --image=lsstdesc/desc-drp-stack:v19-dc2-run2.2-v5 /bin/bash -s <<HEREDOC
source /opt/lsst/software/stack/loadLSST.bash
setup lsst_distrib
echo $1
python /opt/lsst/software/stack/DC2-production-0.4.0/scripts/merge_parquet_files.py $PWD/object_$1_*.parquet -o $PWD/object_tract_$1.parquet --assume-consistent-schema |& tee merge-$1.log
HEREDOC
