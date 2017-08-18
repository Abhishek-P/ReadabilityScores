"""
@Author: Abhishek P
Date: 17/08/17
Readability Scores using the text stats
Built as part of ReadabilityScores


Indices to be calculated:
1. Flei
"""
SCORES = { "fk", "dc"}

def flesch_kincaid_score(stats):
    return 0.39 * (stats["word_count"]/stats["sentence_count"]) \
           + 11.8 * (stats["syllable_count"]/stats["word_count"]) - 15.59


def dale_chall_score(stats):
    pass


def gunning_fog_score(stats):
    pass


def smog_score(stats):
    pass


def coleman_liau_score(stats):
    pass


def automated_score(stats):
    pass

def fry_score(stats):
    pass