import json
import sqlite3

filename = "./y1-y2-wfd_small_centroid_files.txt"
curdb = "/global/cscratch1/sd/heatherk/DC2/Run2.1i/y3-wfd/sqlite_tracking_v1_2.db"

def main():
    with open(filename, 'r') as f:
        badCentroidData = json.load(f)

    conn = sqlite3.connect(curdb)
    c = conn.cursor()

    for (x,y,z) in zip(badCentroidData['visit'],badCentroidData['raftName'],badCentroidData['detectorName']):
        t = (x,y[1:],z[1:])
        print(t)
        #c.execute('SELECT * FROM files WHERE visit_id=? AND raft_id=? AND sensor_id=?', t)
        c.execute('UPDATE files SET quality_controlled=0 WHERE visit_id=? AND raft_id=? AND sensor_id=?', t)
        #print(c.fetchone())



    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
