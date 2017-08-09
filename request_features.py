import geograpy

def analyse(filename):

    extract_keywords()
    extract_locations()
    extract_dates()
    extract_fileformats()
    extract_licences()

def extract_keywords(request):
    pass


def extract_locations(request):
    places = geograpy.get_place_context(text=request)

    print places.countries
    print places.regions
    print places.cities
    print places.other 


def extract_dates(request):
    pass


def extract_fileformats(request):
    pass


def extract_licences(request):
    pass

if __name__ == "__main__":
    analyse("requests.txt")

