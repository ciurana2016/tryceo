# tryceo
Interview code.

## Requirements
1. Python version 3.8.3+
2. Internet connection to run the tests and connect to the database.

## Installation and running
Install all needed packages:
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Run (127.0.0.1:8000):
```
./manage.py runserver
```

## Files
1. __interview/database.py__ handles downloading the data into our own models.
2. __interview/geocode.py__ geocoding (batch geocoding costed money so went for 1 by 1 ).
3. __interview/geojson.py__ generates the geojson files.
4. __static/geojson/*__ gejson files by country area.
5. __static/sass/*__ where the styles live.
6. __templates/*__ where the html/js lives.

## Tests
Please run tests before and after any change.
```
./manage.py test
```

## Sass
To edit the css while coding:
```
./manage.py sass static/sass/ static/css/ --watch -t compressed
```