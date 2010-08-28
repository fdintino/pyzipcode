
from pysqlite2 import dbapi2 as sqlite3
import os
try:
    from settings import db_location
except:
    from pyzipcode.settings import db_location

conn = sqlite3.connect(db_location)
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS ZipCodes;")
c.execute("CREATE TABLE ZipCodes(zip INTEGER, city TEXT, state TEXT, longitude DOUBLE, latitude DOUBLE);")
c.execute("CREATE INDEX zip_index ON ZipCodes(zip);")
c.execute("CREATE INDEX city_index ON ZipCodes(city);")
c.execute("CREATE INDEX state_index ON ZipCodes(state);")

fi = open('zips.txt')
lines = fi.readlines()
states = {}
cities = {}
zips = {}
for line in lines:
    zip, state, city, longt, lat = line.split(',')[1:-2]
    zip = int(zip.strip('"'))
    state = state.strip('"')
    city = city.strip('"')
    
    c.execute("INSERT INTO ZipCodes values(%s, '%s', '%s', %s, %s)" % (
        zip,
        city,
        state,
        float(longt),
        float(lat)
    ))
    
conn.commit()

# We can also close the cursor if we are done with it
c.close()
