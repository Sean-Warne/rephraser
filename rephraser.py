import random
from nltk.corpus import wordnet as wn

def rephrase_string(in_str):
    synonym_out = []
    str_list = in_str.split()

    for word in str_list:
        synsets = wn.synsets(word)
        if (len(synsets) > 1):
            rand_synset = random.randint(0, len(synsets) - 1)
        elif (len(synsets) == 1):
            rand_synset = 0
        else:
            synonym_out.append(word)

        synonyms = wn.synset(synsets[rand_synset].name()).lemma_names()
        if (len(synonyms) > 1):
            rand_synonym = random.randint(0, len(synonyms) - 1)
        else:
            rand_synonym = 0

        synonym_out.append(synonyms[rand_synonym])

    return ' '.join(synonym_out)

''' TODO
- if word is unchanged, try again until it changes or until it runs x number of times
- setup parameter for number of iterations to run
- try to determine word tense and type (verb, noun, adverb, etc.)
- don't change short words like 'a' or 'an'
- slang words
- sub in words from foreign languages
- definitions?
- lorem ipsum
- include word types other than synonyms
'''