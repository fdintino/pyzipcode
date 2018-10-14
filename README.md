**Note: this fork is not maintained.** Please reference the
[original project](https://bitbucket.org/vangheem/pyzipcode) of which this is
a fork.
[This stackoverflow post](https://gis.stackexchange.com/questions/2682/sources-for-us-zip-code-boundaries)
also contains some useful resources.

It is important to recognize the limitations of a project such as pyzipcode.
[Zipcodes are not areas](http://www.georeference.org/doc/zip_codes_are_not_areas.htm)
but instead refer to the addresses on a mail delivery route, or else the
location of a post office. Converting them to polygons is hypothetically
possible, but it is open to interpretation. Technically, only mailing
addresses have zipcodes and the space between mailboxes have no zipcode. In
practice, mail routes follow roads, and one can create polygons by drawing
boundaries around the roads and addresses of a route, but the resulting
polygons are often non-contiguous. Computing the centroid of this polygon (as
pyzipcode does) is extremely fraught; it is quite likely that the centroid is
not even within the polygon! Zipcodes also change fairly frequently as postal
routes change and new addresses are created, so any data source which is not
updated regularly quickly becomes useless.


