
from pysqlite2 import dbapi2 as sqlite3
import os
import csv
try:
    from settings import db_location
except:
    from pyzipcode.settings import db_location

conn = sqlite3.connect(db_location)
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS ZipCodes;")
c.execute("CREATE TABLE ZipCodes(zip VARCHAR(5), city TEXT, state TEXT, longitude DOUBLE, latitude DOUBLE, timezone INT, dst INT);")
c.execute("CREATE INDEX zip_index ON ZipCodes(zip);")
c.execute("CREATE INDEX city_index ON ZipCodes(city);")
c.execute("CREATE INDEX state_index ON ZipCodes(state);")

reader = csv.reader(open('zipcode.csv', "rb"))
reader.next() # prime it
    
for row in reader:
    zip, city, state, lat, longt, timezone, dst = row
    
    c.execute('INSERT INTO ZipCodes values("%s", "%s", "%s", %s, %s, %s, %s)' % (
        zip,
        city,
        state,
        float(longt),
        float(lat),
        timezone,
        dst
    ))
    
conn.commit()

# We can also close the cursor if we are done with it
c.close()
