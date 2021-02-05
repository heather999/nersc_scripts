#!/bin/bash
arr=("$@")
echo ${arr[@]}
for i in "${arr[@]}" 
do
  echo $i
  shifter --image=lsstdesc/desc-drp-stack:v19-dc2-run2.2-v5 /bin/bash -s <<HEREDOC
source /opt/lsst/software/stack/loadLSST.bash
setup lsst_distrib
echo $i
python /opt/lsst/software/stack/DC2-production-0.4.0/scripts/merge_parquet_files.py $PWD/object_$i_*.parquet -o $PWD/object_tract_$i.parquet --assume-consistent-schema |& tee merge-$i.log
HEREDOC
done
