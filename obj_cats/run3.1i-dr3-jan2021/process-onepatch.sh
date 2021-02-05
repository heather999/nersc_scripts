#!/bin/bash
shifter --image=lsstdesc/desc-drp-stack:v19-dc2-run2.2-v5 /bin/bash -s <<HEREDOC
source /opt/lsst/software/stack/loadLSST.bash
setup lsst_distrib
echo $1
python /opt/lsst/software/stack/DC2-production-0.4.0/scripts/make_object_catalog.py /global/cscratch1/sd/descdm/DC2/Run3.1i/DR3/repo/rerun/dr3-multiband $1 -p $2 -o $PWD |& tee objCat-$1-$2.log
HEREDOC
