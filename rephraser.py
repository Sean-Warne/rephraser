import random
from functools import reduce
from nltk.corpus import wordnet as wn

def rephrase_string(in_str, retry_max = 10, use_antonyms = False, out_style = 'default'):
    synonym_out = []
    str_list = in_str.split()

    for word in str_list:
        if (len(word) <= 2):
            continue

        # do while... until retry count is met or word doesn't match the original
        retry_count = 0
        while True:
            retry_count += 1
            
            # generate a list of all synonyms
            synonyms = []
            for synset in wn.synsets(word): 
                synonyms.append(wn.synset(synset.name()).lemma_names())
            
            # flatten and remove duplicates
            synonyms = list(set(reduce(list.__add__, synonyms)))

            # get a random synonym for the word
            synonym = synonyms[random.randint(0, len(synonyms) - 1)]
            if (retry_count == retry_max or word != synonym):
                synonym_out.append(synonym)
                break

    match out_style:
        case 'title':
            rephrased = ' '.join(synonym_out).title().replace('_', ' ')
        case 'username':
            rephrased = '-'.join(synonym_out).title().replace('_', '').replace('-', '').replace("'", '')
        case _:
            rephrased = ' '.join(synonym_out).replace('_', ' ')

    return rephrased

''' TODO
- slang words
- sub in words from foreign languages
- add option for antonyms
- navigate up the synonym tree (get synonyms of a synonym); e.g. sad doesn't show unhappy as a syn but unhappy does show sad.
'''