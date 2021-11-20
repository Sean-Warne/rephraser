import random
from nltk.corpus import wordnet as wn

def rephrase_string(in_str, retry_max = 10):
    synonym_out = []
    str_list = in_str.split()

    for word in str_list:
        if (len(word) <= 2):
            continue

        # do while... until retry count is met or word doesn't match the original
        retry_count = 0
        while True:
            retry_count += 1
            
            synsets = wn.synsets(word)
            if (len(synsets) > 1):
                rand_int = random.randint(0, len(synsets) - 1)
            elif (len(synsets) == 1):
                rand_int = 0
            else:
                synonym_out.append(word)
                break

            synonyms = wn.synset(synsets[rand_int].name()).lemma_names()
            if (len(synonyms) > 1):
                rand_int = random.randint(0, len(synonyms) - 1)
            else:
                rand_int = 0

            synonym = synonyms[rand_int]
            if (retry_count == retry_max or word != synonym):
                synonym_out.append(synonym)
                break

    return ' '.join(synonym_out).replace('_', ' ').title()

''' TODO
- try to determine word tense and type (verb, noun, adverb, etc.)
- slang words
- sub in words from foreign languages
- definitions?
- lorem ipsum
- include word types other than synonyms
- navigate up the synonym tree (get synonyms of a synonym); populate array with all options before choosing randomly (more time + mem)
'''