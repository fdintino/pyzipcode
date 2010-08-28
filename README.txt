Introduction
============

This package will allow you to get zip code information. The data used in this 
package is retrieved from http://www.census.gov/tiger/tms/gazetteer/zips.txt

pyzipcode uses a local sqlite database to run. You can replace it with your own
other storage mechanism with a little effort.

Also, all longitude and latitude data is store assuming northern and western 
part of the world so there is no negative degrees...

Here is some basic usage..

	>>> from pyzipcode import ZipCodeDatabase
	>>> zcdb = ZipCodeDatabase()
	>>> zipcode = zcdb[54115]
	>>> zipcode.zip
	54115
	>>> zipcode.city
	u'DE PERE'
	>>> zipcode.state
	u'WI'
	>>> zipcode.longitude
	88.080613
	>>> zipcode.latitude
	44.438778999999997
	
	
Search zip codes...

	>>> from pyzipcode import ZipCodeDatabase
	>>> zcdb = ZipCodeDatabase()
	>>> len(zcdb.find_zip(city="Oshkosh"))
	3
	

Get a list of zipcodes around a radius of a zipcode

	
	>>> from pyzipcode import ZipCodeDatabase
	>>> zcdb = ZipCodeDatabase()
	>>> [z.zip for z in zcdb.get_zipcodes_around_radius(54901, 10)]
	[54901, 54904, 54932, 54952, 54956, 54979]