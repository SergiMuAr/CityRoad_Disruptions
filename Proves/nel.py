import findspark
findspark.init()
import pyspark
sc = pyspark.SparkContext()
sqlContext = pyspark.sql.SQLContext(sc)

import os
from sift.corpora import wikipedia, wikidata
from sift.models import text, links
wikipedia_base_path = '/data0/linking/wikipedia/dumps/20150901/'
wikidata_base_path = '/n/schwa11/data0/linking/wikidata/dumps/20150713'

wikipedia_corpus = wikipedia.WikipediaCorpus()(sc, wikipedia_base_path)
docs = wikipedia.WikipediaArticles()(wikipedia_corpus).cache()
docs.take(1)
