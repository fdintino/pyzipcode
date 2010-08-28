
import unittest
import pyzipcode


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.db = pyzipcode.ZipCodeDatabase()

    def test_retrieves_zip_code_information(self):
        zip = self.db[54115]
        self.assertEquals(zip.zip, 54115)
        self.assertEquals(zip.city, "DE PERE")
        self.assertEquals(zip.state, "WI")
        
    def test_radius(self):
        zips = self.db.get_zipcodes_around_radius(54115, 30)
        self.assertTrue(54304 in [zip.zip for zip in zips])
        
    def test_find_zip_by_city(self):
        zip = self.db.find_zip(city="DE PERE")[0]
        self.assertEquals(54115, zip.zip)
        
    def test_find_zip_by_city_with_multiple_zips(self):
        zips = self.db.find_zip(city="GREEN BAY")
        self.assertTrue(54302 in [zip.zip for zip in zips])
        
    def test_find_zips_in_state(self):
        zips = self.db.find_zip(state="WI")
        self.assertTrue(54304 in [zip.zip for zip in zips])
        self.assertTrue(54901 in [zip.zip for zip in zips])

if __name__ == '__main__':
    unittest.main()