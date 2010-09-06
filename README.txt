Introduction
============

This package will allow you to get zip code information. The data used in this 
package is retrieved from http://pablotron.org/files/zipcodes-csv-10-Aug-2004.zip

pyzipcode uses a local sqlite database to run. You can replace it with your own
other storage mechanism with a little effort.

Here is some basic usage..

	>>> from pyzipcode import ZipCodeDatabase
	>>> zcdb = ZipCodeDatabase()
	>>> zipcode = zcdb[54115]
	>>> zipcode.zip
	u'54115'
	>>> zipcode.city
	u'De Pere'
	>>> zipcode.state
	u'WI'
	>>> zipcode.longitude
	-88.078959999999995
	>>> zipcode.latitude
	44.42042
	>>> zipcode.timezone
	-6
	
	
Search zip codes...

	>>> from pyzipcode import ZipCodeDatabase
	>>> zcdb = ZipCodeDatabase()
	>>> len(zcdb.find_zip(city="Oshkosh"))
	7
	

Get a list of zipcodes around a radius of a zipcode
	
	>>> from pyzipcode import ZipCodeDatabase
	>>> zcdb = ZipCodeDatabase()
	>>> [z.zip for z in zcdb.get_zipcodes_around_radius('54901', 10)]
	[u'54901', u'54902', u'54903', u'54904', u'54906', u'54927', u'54952', u'54956', u'54957', u'54979', u'54985']