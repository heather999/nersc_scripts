#!/bin/bash

#ALLDIR=/global/cscratch1/sd/desc/DC2/data/Run1.2i/rerun/coadd-v1/deepCoadd_results
NEWDIR=/global/cscratch1/sd/desc/DC2/data/Run1.2i/rerun/coadd-v1/deepCoadd-results

for BAND in $NEWDIR/*;
do
    echo $BAND
    MYBAND=$(echo "$BAND" | cut -d / -f 12 )
    for TRACT in $BAND/*;
    do
        MYTRACT=$(echo "$TRACT" | cut -d / -f 13 )
        for PATCH in $TRACT/*;
        do
            MYPATCH=$(echo "$PATCH" | cut -d / -f 14 )
            OLD=${PATCH}/forced-${MYBAND}-${MYTRACT}-${MYPATCH}.fits 
            NEW=${PATCH}/forced_src-${MYBAND}-${MYTRACT}-${MYPATCH}.fits
           echo $OLD
           echo $NEW
           mv $OLD $NEW
        done
    done
 

done


