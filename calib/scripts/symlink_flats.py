import os
import glob
import sqlite3

# Create symlinks between i-band flat calib files and flats for ugrzy bands.
calib_dir = os.path.abspath('.')
iband_flats = sorted(glob.glob(os.path.join(calib_dir, 'flat', 'i',
                                            '2022-08-06', 'flat_i-R*')))
for band in 'ugrzy':
    flat_dir = os.path.join(calib_dir, 'flat', band, '2022-08-06')
    os.makedirs(flat_dir, exist_ok=True)
    for flat in iband_flats:
        outfile = os.path.basename(flat).replace('i-R', '{}-R'.format(band))
        try:
            os.symlink(flat, os.path.join(flat_dir, outfile))
        except FileExistsError:
            pass

# Update the calibRegistry.sqlite3 file with entries for the flats
# in the ugrzy bands.
conn = sqlite3.connect('calibRegistry.sqlite3')
curs = conn.cursor()

# Get the entries for the i-band flats.
query = 'select raftName, detectorName, detector, calibDate, validStart, validEnd from flat where filter="i"'
curs.execute(query)
entries = [x for x in curs]

for band in 'ugrzy':
    for row in entries:
        my_row = [band] + list(row)
        query = "insert into flat (filter, raftName, detectorName, detector, calibDate, validStart, validEnd) values ('{}', '{}', '{}', {}, '{}', '{}', '{}')".format(*my_row)
        try:
            curs.execute(query)
        except sqlite3.IntegrityError:
            pass
    conn.commit()
