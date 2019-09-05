#!/bin/bash

ALLDIR=/global/cscratch1/sd/desc/DC2/data/Run1.2p/w_2018_39/rerun/coadd-v4/deepCoadd_results
NEWDIR=/global/cscratch1/sd/desc/DC2/data/Run1.2p/w_2018_39/rerun/coadd-v4/deepCoadd-results

for CURDIR in $ALLDIR/*;
do
    echo $CURDIR
    SUBDIR=$(echo "$CURDIR" | cut -d / -f 13) 
    echo $SUBDIR
    BAND=$(echo "$SUBDIR" | cut -d _ -f 1)
    echo $BAND
    TRACT=$(echo "$SUBDIR" | cut -d _ -f 2 | cut -d t -f 2)
    echo $TRACT
    PATCH=$(echo "$SUBDIR" | cut -d _ -f 3 | cut -d p -f 2)
    echo $PATCH
    FULLNEWDIR="${NEWDIR}/${BAND}/${TRACT}/${PATCH}/"
    echo $FULLNEWDIR
    OUT=$(echo ls  "$CURDIR/*")
    echo $OUT
    ln -s $CURDIR/* $FULLNEWDIR
    mv $FULLNEWDIR/forced-$BAND-$TRACT-$PATCH.fits $FULLNEWDIR/forced_src-$BAND-$TRACT-$PATCH.fits
done


