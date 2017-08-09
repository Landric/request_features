import os
import csv
#import geograpy
#from geotext import GeoText
import nltk
from nltk.corpus import stopwords
from nltk.tag import StanfordNERTagger

def analyse(filename):
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print "Analysing: " + row[0]
            print "="*10
            extract_keywords(row[0])
            extract_locations(row[0])
            extract_dates(row[0])
            extract_fileformats(row[0])
            extract_licences(row[0])
            print "="*10

def nlp_preprocess(request):
    stop = stopwords.words('english')
    request = ' '.join([i for i in request.split() if i not in stop])
    st = StanfordNERTagger(os.path.join(os.getcwd(), 'stanford-ner', 'classifiers', 'english.muc.7class.distsim.crf.ser.gz'), os.path.join(os.getcwd(), 'stanford-ner', 'stanford-ner.jar'))
    return st.tag(request.split()) 

def extract_keywords(request):
    pass


def extract_locations(request):
    #places = geograpy.get_place_context(text=request)
    #print places.countries
    #print places.regions
    #print places.cities
    #print places.other 

    #places = GeoText(request)
    #print places.cities
    #print places.country_mentions
    #print places.nationalities
    #print places.countries
    print nlp_preprocess(request)

    for entity in nlp_preprocess(request):
        if entity[1] == "LOCATION" or entity[1] == "GPE" or entity[1] == "FACILITY":
            print entity[0]



def extract_dates(request):
    # timedates = []
    # sentences = nlp_preprocess(request)

    # for tagged_sentence in sentences:
    #     for chunk in nltk.ne_chunk(tagged_sentence):
    #         if type(chunk) == nltk.tree.Tree:
    #             if chunk.label() == 'DATE' or chunk.label() == 'TIME':
    #                 timedates.append(' '.join([c[0] for c in chunk]))
    # return timedates
    for entity in nlp_preprocess(request):
        if entity[1] == "TIME" or entity[1] == "DATE":
            print entity[0]

def extract_fileformats(request):
    pass


def extract_licences(request):
    pass

if __name__ == "__main__":
    analyse("requests_test.csv")

