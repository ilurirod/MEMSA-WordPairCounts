# MEMSA-WordPairingCounts
This is a sample script to conduct Dictionary Analysis in text using word pairs (word A within N words of word B) instead of single words.

Conceptualization and Uses

One utility of Dictionary Analysis with word pairs is that each word disambiguates and contextualizes the other, virtually enriching word counts with a rule based on word embeddings.
This methodology was proposed in (CITATION) as a way to allow metaphor search in big text data. Traditional single-word Dictionary analysis with metaphor words (e.g. burden, weight) cannot distinguish between metaphorical and literal uses of the word. Further, the dictionary would count as a positive result whenever those words are used, even when they refer metaphorically to any target rather than one specific topic of study (e.g. “the weight of evidence” versus "the weight of debt"). We can reconcile dictionary-based methods with metaphors by enriching them with a rule-based criterion: the metaphor source word (e.g., “weight”) occurs within a short distance of the target word (e.g. “debt”). We leverage the advantage that metaphor words often occur in close proximity to their targets, an extremely convenient linguistic pattern that facilitates metaphor analysis in big data (Stefanowitsch 2006; Gil 2019). By working with word pairs rather than single words, we further disambiguate metaphorical versus literal use with a high accuracy (Deignan 2008), because words like “lean” are only ever used metaphorically (“efficient”) when they are in proximity to specific target domains (“business”).
In this context, word pairs correspond to the TARGET, e.g. debt, and SOURCE, e.g. weight, of each metaphor, e.g. in the conceptual metaphor DEBT IS WEIGHT. It takes advantage of the tendency of some metaphors in language to form patterns where SOURCE and TARGET are in close linguistic proximity (e.g. "weight of debt", burden of my debt", "debt load").


How to Use

This script is a minimal working example and should be customized to specific uses. This script reads a Text variable and treats each line as a separate document/article/text. Then, it goes through each document and counts how many times a word pair occurs, i.e. how many time word/s in the list of secondary words occur within a distance *n* of the word/s in the list of central words. For each document in the file, the script outputs: 1) Total count of word-pairs found, and 2) Word-pair frequency per thousand words. This can be customized to visualize, or only save the documents with metaphor hits.

Text preprocessing is included but should be customized to fit the needs of the user and the characteristics of the database. Text preprocessing can have an impact on window definition (the *n* words within to find matches) and results.



