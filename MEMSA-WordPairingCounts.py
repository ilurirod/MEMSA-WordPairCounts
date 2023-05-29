# -*- coding: utf-8 -*-
"""
Created on Mon May 29 11:01:03 2023

@author: ILURIROD
"""

import re
from nltk.tokenize import word_tokenize
#Sample minimal text preprocessing. Customize as needed
def TEXT_PREPROCESS(string): 
    text = string.lower()
    text= re.sub(r'http\S+', ' ', text)
    text = re.sub('&',' and ',text)
    text = re.sub('<[^>]+>',' ',text) ## Remove anything in between angle brackets <> (usually format tags or outside-text comments)
    text = re.sub('[^\w\s]',' ',text) ## Remove punctuation, symbols, nonwords
    text = re.sub('\s+',' ',text) ## Remove duplicate spaces
    return text

n = 4 ## This is the search window: Find WordA within n words of WordB
WordA = ["debt"] #This list has the central word. It can include more than one, e.g. loan, loans...
WordB = ["weigh", "burden"] #This list has the secondary word. These are treated not as words but as "beginning with" to be inclusive with plurals, conjugations...
combined = [(f,s) for f in WordA for s in WordB] #All combinations of central word and secondary word
RegExList=[] #We create a list of regular expressions to search for all possible combinations above
for x,y in combined:
    RegExList.append(f"({y}[a-z]* (\w+ ){{0,{n-1}}}{x})|({x} (\w+ ){{0,{n-1}}}{y}[a-z]*)")
#Sample text   
Text = ["The inescapable weight of my student debt",
        "Debt weighs heavily on retirement security, happiness",
        "The Burden of Debt on Mental and Physical Health. The physical burdens of debt", 
        "The unsustainable $17 trillion debt that is burdening our economy"]
#Computation of Hits (found a central-secondary words match within n words) and frequencies (measured in hits per-mil over total word count). In MEMSA, this represents the presence of topic-relevant metaphors
for line in Text:
    TotalMetaphorHits=0
    for RegEx in RegExList:
        Hits = len(re.findall(RegEx,TEXT_PREPROCESS(line)))
        TotalMetaphorHits = TotalMetaphorHits+Hits
    print(f"Metaphor hits: {TotalMetaphorHits}")
    print(f"Metaphor frequency: {TotalMetaphorHits/len(word_tokenize(TEXT_PREPROCESS(line)))*1000} per 1000 words")