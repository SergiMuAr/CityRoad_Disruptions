# import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree

def get_continuous_chunks(text):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    prev = None
    continuous_chunk = []
    current_chunk = []

    for i in chunked:
        if type(i) == Tree:
            current_chunk.append(" ".join([token for token, pos in i.leaves()]))
        elif current_chunk:
            named_entity = " ".join(current_chunk)
            if named_entity not in continuous_chunk:
                continuous_chunk.append(named_entity)
                current_chunk = []
        else:
            continue

    if continuous_chunk:
        named_entity = " ".join(current_chunk)
        if named_entity not in continuous_chunk:
            continuous_chunk.append(named_entity)

    return continuous_chunk

txt = "⚠️🚗🚚Encara : Embús a l'AP-7 de Sant Cugat a Santa Perpètua -&gt;Girona per una topada d’un camió i dos turismes . Ara hi ha un carril tallat .També aturats a Santa Perpètua -&gt;sud. Afecta la B-30" 
print (get_continuous_chunks(txt))

## https://nlpforhackers.io/named-entity-extraction/

# import os
# import string
# import collections
# import pickle
# from collections import Iterable

# from nltk.tag import ClassifierBasedTagger
# from nltk.chunk import ChunkParserI, conlltags2tree, tree2conlltags
# from nltk import pos_tag, word_tokenize
# from nltk.stem import SnowballStemmer

# ner_tags = collections.Counter()

# corpus_root = "gmb-2.2.0"  # Make sure you set the proper path to the unzipped corpus


# def to_conll_iob(annotated_sentence):
#     """
#     `annotated_sentence` = list of triplets [(w1, t1, iob1), ...]
#     Transform a pseudo-IOB notation: O, PERSON, PERSON, O, O, LOCATION, O
#     to proper IOB notation: O, B-PERSON, I-PERSON, O, O, B-LOCATION, O
#     """
#     proper_iob_tokens = []
#     for idx, annotated_token in enumerate(annotated_sentence):
#         tag, word, ner = annotated_token

#         if ner != 'O':
#             if idx == 0:
#                 ner = "B-" + ner
#             elif annotated_sentence[idx - 1][2] == ner:
#                 ner = "I-" + ner
#             else:
#                 ner = "B-" + ner
#         proper_iob_tokens.append((tag, word, ner))
#     return proper_iob_tokens
    
# def features(tokens, index, history):
#     """
#     `tokens`  = a POS-tagged sentence [(w1, t1), ...]
#     `index`   = the index of the token we want to extract features for
#     `history` = the previous predicted IOB tags
#     """
 
#     # init the stemmer
#     stemmer = SnowballStemmer('english')
 
#     # Pad the sequence with placeholders
#     tokens = [('[START2]', '[START2]'), ('[START1]', '[START1]')] + list(tokens) + [('[END1]', '[END1]'), ('[END2]', '[END2]')]
#     history = ['[START2]', '[START1]'] + list(history)
 
#     # shift the index with 2, to accommodate the padding
#     index += 2
 
#     word, pos = tokens[index]
#     prevword, prevpos = tokens[index - 1]
#     prevprevword, prevprevpos = tokens[index - 2]
#     nextword, nextpos = tokens[index + 1]
#     nextnextword, nextnextpos = tokens[index + 2]
#     previob = history[index - 1]
#     contains_dash = '-' in word
#     contains_dot = '.' in word
#     allascii = all([True for c in word if c in string.ascii_lowercase])
 
#     allcaps = word == word.capitalize()
#     capitalized = word[0] in string.ascii_uppercase
 
#     prevallcaps = prevword == prevword.capitalize()
#     prevcapitalized = prevword[0] in string.ascii_uppercase
 
#     nextallcaps = prevword == prevword.capitalize()
#     nextcapitalized = prevword[0] in string.ascii_uppercase
 
#     return {
#         'word': word,
#         'lemma': stemmer.stem(word),
#         'pos': pos,
#         'all-ascii': allascii,
 
#         'next-word': nextword,
#         'next-lemma': stemmer.stem(nextword),
#         'next-pos': nextpos,
 
#         'next-next-word': nextnextword,
#         'nextnextpos': nextnextpos,
 
#         'prev-word': prevword,
#         'prev-lemma': stemmer.stem(prevword),
#         'prev-pos': prevpos,
 
#         'prev-prev-word': prevprevword,
#         'prev-prev-pos': prevprevpos,
 
#         'prev-iob': previob,
 
#         'contains-dash': contains_dash,
#         'contains-dot': contains_dot,
 
#         'all-caps': allcaps,
#         'capitalized': capitalized,
 
#         'prev-all-caps': prevallcaps,
#         'prev-capitalized': prevcapitalized,
 
#         'next-all-caps': nextallcaps,
#         'next-capitalized': nextcapitalized,
#     }

# def read_gmb(corpus_root):
#     for root, dirs, files in os.walk(corpus_root):
#         for filename in files:
#             if filename.endswith(".tags"):
#                 with open(os.path.join(root, filename), 'rb') as file_handle:
#                     file_content = file_handle.read().decode('utf-8').strip()
#                     annotated_sentences = file_content.split('\n\n')
#                     for annotated_sentence in annotated_sentences:
#                         annotated_tokens = [seq for seq in annotated_sentence.split('\n') if seq]

#                         standard_form_tokens = []

#                         for idx, annotated_token in enumerate(annotated_tokens):
#                             annotations = annotated_token.split('\t')
#                             word, tag, ner = annotations[0], annotations[1], annotations[3]

#                             if ner != 'O':
#                                 ner = ner.split('-')[0]

#                             if tag in ('LQU', 'RQU'):  # Make it NLTK compatible
#                                 tag = "``"

#                             standard_form_tokens.append((word, tag, ner))

#                         conll_tokens = to_conll_iob(standard_form_tokens)

#                         # Make it NLTK Classifier compatible - [(w1, t1, iob1), ...] to [((w1, t1), iob1), ...]
#                         # Because the classfier expects a tuple as input, first item input, second the class
#                         yield [((w, t), iob) for w, t, iob in conll_tokens]


# class NamedEntityChunker(ChunkParserI):
#     def __init__(self, train_sents, **kwargs):
#         assert isinstance(train_sents, Iterable)

#         self.feature_detector = features
#         self.tagger = ClassifierBasedTagger(
#             train=train_sents,
#             feature_detector=features,
#             **kwargs)

#     def parse(self, tagged_sent):
#         chunks = self.tagger.tag(tagged_sent)

#         # Transform the result from [((w1, t1), iob1), ...]
#         # to the preferred list of triplets format [(w1, t1, iob1), ...]
#         iob_triplets = [(w, t, c) for ((w, t), c) in chunks]

#         # Transform the list of triplets to nltk.Tree format
#         return conlltags2tree(iob_triplets)


      
# reader = read_gmb(corpus_root)
# data = list(reader)
# training_samples = data[:int(len(data) * 0.9)]
# test_samples = data[int(len(data) * 0.9):]
# chunker = NamedEntityChunker(training_samples[:2000])

# print(chunker.parse(pos_tag(word_tokenize("I'm going to Germany this Monday."))))
# print("#training samples = %s" % len(training_samples))  # training samples = 55809
# print("#test samples = %s" % len(test_samples))  # test samples = 6201

# from nltk import ne_chunk, pos_tag, word_tokenize
# from nltk.tree import Tree
# from nltk.chunk import conlltags2tree, tree2conlltags
 
# sentence = "⚠️🚗🚚Encara : Embús a l'AP-7 de Sant Cugat a Santa Perpètua -&gt;Girona per una topada d’un camió i dos turismes . Ara hi ha un carril tallat .També aturats a Santa Perpètua -&gt;sud. Afecta la B-30"
# ne_tree = ne_chunk(pos_tag(word_tokenize(sentence)))
 
# iob_tagged = tree2conlltags(ne_tree)
# print (iob_tagged)