geograpy is unmaintained right now; there are a few lines that need to be changed in the lib files to make it work again:
* in ```geograpy/places.py``` replace ```country.name``` with ```country_name```
* in ```geograpy/extraction.py``` replace ```ne.node``` with ```ne.label()```