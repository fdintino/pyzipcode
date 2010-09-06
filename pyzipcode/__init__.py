from settings import db_location
from pysqlite2 import dbapi2 as sqlite3
import math
import time

class ConnectionManager(object):
    """
    Assumes a database that will work with cursor objects
    """
    
    def __init__(self):
        # test out the connection...
        conn = sqlite3.connect(db_location)
        conn.close()
            
    def query(self, sql):
        conn = None
        retry_count = 0
        while not conn and retry_count <= 10:
        # If there is trouble reading the file, retry for 10 attempts
        # then just give up...
            try:
                conn = sqlite3.connect(db_location)
            except sqlite3.OperationalError, x:
                retry_count += 1
                time.sleep(0.001)
        
        if not conn and retry_count > 10:
            raise sqlite3.OperationalError("Can't connect to sqlite database.")
                
        cursor = conn.cursor()
        cursor.execute(sql)
        res = cursor.fetchall()
        conn.close()
        return res

ZIP_QUERY = "SELECT * FROM ZipCodes WHERE zip='%s'"
ZIP_RANGE_QUERY = "SELECT * FROM ZipCodes WHERE longitude >= %s and longitude <= %s AND latitude >= %s and latitude <= %s"
ZIP_FIND_QUERY = "SELECT * FROM ZipCodes WHERE city LIKE '%s' AND state LIKE '%s'"

class ZipCode(object):
    def __init__(self, data):
        self.zip = data[0]
        self.city = data[1]
        self.state = data[2]
        self.longitude = data[3]
        self.latitude = data[4]
        self.timezone = data[5]
        self.dst = data[6]

def format_result(zips):
    if len(zips) > 0:
        return [ZipCode(zip) for zip in zips]
    else:
        return None

class ZipNotFoundException(Exception):
    pass
    
class ZipCodeDatabase(object):
    
    def __init__(self, conn_manager=None):
        if conn_manager is None:
            conn_manager = ConnectionManager()
        self.conn_manager = conn_manager
        
    def get_zipcodes_around_radius(self, zip, radius):
        zips = self.get(zip)
        if zips is None:
            raise ZipNotFoundException("Could not find zip code you're searching by.")
        else:
            zip = zips[0]
        
        radius = float(radius)
        
        long_range = (zip.longitude-(radius/69.0), zip.longitude+(radius/69.0))
        lat_range = (zip.latitude-(radius/49.0), zip.latitude+(radius/49.0))
        
        return format_result(self.conn_manager.query(ZIP_RANGE_QUERY % (
            long_range[0], long_range[1],
            lat_range[0], lat_range[1]
        )))
                    
    def find_zip(self, city=None, state=None):
        if city is None:
            city = "%"
        else:
            city = city.upper()
            
        if state is None:
            state = "%"
        else:
            state = state.upper()
            
        return format_result(self.conn_manager.query(ZIP_FIND_QUERY % (city, state)))
        
    def get(self, zip):
        return format_result(self.conn_manager.query(ZIP_QUERY % zip))
            
    def __getitem__(self, zip):
        zip = self.get(str(zip))
        if zip is None:
            raise IndexError("Couldn't find zip")
        else:
            return zip[0]
            
    
        
        
        
        
