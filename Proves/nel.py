import findspark
findspark.init()
import pyspark
sc = pyspark.SparkContext()
sqlContext = pyspark.sql.SQLContext(sc)
import os

from sift.corporasift.co import wikipedia, wikidata
from sift.models import text, links
wikipedia_base_path = '/data0/linking/wikipedia/dumps/20150901/'
wikidata_base_path = '/n/schwa11/data0/linking/wikidata/dumps/20150713'

wikipedia_corpus = wikipedia.WikipediaCorpus()(sc, wikipedia_base_path)
docs = wikipedia.WikipediaArticles()(wikipedia_corpus).cache()

docs.take(1)

wikipedia_pfx = 'en.wikipedia.org/wiki/'

ec_model = links\
    .EntityCounts(min_count=5, filter_target=wikipedia_pfx)\
    .build(docs)\
    .map(links.EntityCounts.format_item)

enc_model = links\
    .EntityNameCounts(lowercase=True, filter_target=wikipedia_pfx)\
    .build(docs)\
    .filter(lambda (name, counts): sum(counts.itervalues()) > 1)\
    .map(links.EntityNameCounts.format_item)

ec_model.take(1)

from nel.model import data
from nel.model.store import file

os.environ['NEL_DATASTORE_URI'] = 'file:///data0/nel/'

# we can use model.toLocalIterator if models don't fit in memory
data.ObjectStore\
    .Get('models:ecounts[wikipedia]')\
    .save_many(ec_model.collect())
# DEBUG:nel:Using file object store for (models:ecounts[wikipedia])...
# DEBUG:nel:Loading mmap store: /data0/nel/models/ecounts[wikipedia].index ...
# DEBUG:nel:Loading mmap store: /data0/nel/models/ecounts[wikipedia].index ...


data.ObjectStore\
    .Get('models:necounts[wikipedia]')\
    .save_many(enc_model.collect())

# DEBUG:nel:Using file object store for (models:necounts[wikipedia])...
# DEBUG:nel:Loading mmap store: /data0/nel/models/necounts[wikipedia].index ...
# DEBUG:nel:Loading mmap store: /data0/nel/models/necounts[wikipedia].index ...

from nel.doc import Doc
from nel.harness.format import from_sift

from nel.process.pipelinenel.proc  import Pipeline
from nel.process.candidates import NameCounts
from nel.features.probability import EntityProbability, NameProbability


candidate_generation = [
    NameCounts('wikipedia', 10)
]
feature_extraction = [
    EntityProbability('wikipedia'),
    NameProbability('wikipedia')
]
# INFO:nel:Preparing name model candidate generator (model=wikipedia, limit=10)...
# DEBUG:nel:Using file object store for (models:necounts[wikipedia])...
# DEBUG:nel:Loading mmap store: /data0/nel/models/necounts[wikipedia].index ...
# DEBUG:nel:Using file object store for (models:ecounts[wikipedia])...
# DEBUG:nel:Loading mmap store: /data0/nel/models/ecounts[wikipedia].index ...
# DEBUG:nel:Using file object store for (models:necounts[wikipedia])...
# DEBUG:nel:Loading mmap store: /data0/nel/models/necounts[wikipedia].index ...

training_pipeline = Pipeline(candidate_generation + feature_extraction)
training_docs = [from_sift(doc) for doc in docs.takeSample(False, 100)]
train = [training_pipeline(doc) for doc in training_docs]
from nel.learn import ranking
from nel.features import meta
from nel.model import resolution
from nel.process import resolve

ranker = ranking.TrainLinearRanker(name='ranker', features=[f.id for f in feature_extraction])(train)
# INFO:nel:Computing feature statistics over 100 documents...
# INFO:nel:Building training set, feature mapping = PolynomialMapper...
# INFO:nel:Fitting model over 9394 instances...
# INFO:nel:Training set pairwise classification: 93.2% (8751/9394)
# INFO:nel:Done.

classifier_feature = meta.ClassifierScore(ranker)
linking = [
    classifier_feature,
    resolve.FeatureRankResolver(classifier_feature.id)
]

linking_pipeline = Pipeline(candidate_generation + feature_extraction + linking)

sample = [from_sift(doc) for doc in docs.takeSample(False, 10)]

# clear existing links
for doc in sample:
    for chain in doc.chains:
        chain.resolution = None
        for mention in chain.mentions:
            mention.resolution = None

linked_sample = [linking_pipeline(doc) for doc in sample]
[d.id for d in linked_sample]
sample[0].chains[0].resolution.id

from  nel.harness.formatnel.harn  import inject_markdown_links
from IPython.display import display, Markdown

display(Markdown(inject_markdown_links(linked_sample[0].text, linked_sample[0])))



from  nel.processnel.proce  import tag, coref

mention_detection = [
    tag.SpacyTagger(),
    coref.SpanOverlap()
]
# DEBUG:nel:Using spacy entity tagger (None)...
# INFO:nel:Using mention text span-overlap coreference clusterer...

full_pipeline = Pipeline(mention_detection + candidate_generation + feature_extraction + linking)

linked_sample = [full_pipeline(doc) for doc in sample]
display(Markdown(inject_markdown_links(linked_sample[0].text, linked_sample[0], 'https://')))
