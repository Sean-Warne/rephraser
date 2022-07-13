import random
from functools import reduce

from nltk.corpus import wordnet as wn


def rephrase_string(
    in_str, retry_max=10, use_antonyms=False, out_style="default", min_word_size=2
):
    synonym_out = []
    str_list = in_str.split()

    for word in str_list:
        if len(word) <= min_word_size:
            synonym_out.append(word)
            continue

        for i in range(0, retry_max):
            # generate a list of all synonyms
            synonyms = []
            for synset in wn.synsets(word):
                synonyms.append(wn.synset(synset.name()).lemma_names())

            if len(synonyms) > 0:
                # flatten and remove duplicates then get a random synonym for the word
                synonyms = list(set(reduce(list.__add__, synonyms)))
                synonym = synonyms[random.randint(0, len(synonyms) - 1)]
                synonym_out.append(synonym)
                break

            # last iteration and no synonym found
            if i == retry_max - 1 and word != synonym:
                synonym_out.append(word)

    match out_style:
        case "title":
            rephrased = " ".join(synonym_out).title().replace("_", " ")
        case "username":
            rephrased = (
                "-".join(synonym_out)
                .title()
                .replace("_", "")
                .replace("-", "")
                .replace("'", "")
            )
        case _:
            rephrased = " ".join(synonym_out).replace("_", " ")

    return rephrased


""" TODO
- slang words
- sub in words from foreign languages
- add option for antonyms
- navigate up the synonym tree (get synonyms of a synonym); e.g. sad doesn't show unhappy as a syn but unhappy does show sad.
"""


def main():
    phrase = "Never gonna run around and hurt you"
    print(rephrase_string(in_str=phrase, out_style="default", min_word_size=3))


if __name__ == "__main__":
    main()
