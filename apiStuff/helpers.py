"""Helper Variables and Functions."""

import numpy as np
from apiStuff import db, models
import indicoio
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree


def get_rating(content):
    """Generate rating for content text."""
    indicoio.config.api_key = '11214320f4b6ce1e81f46ed4a570c7e0'
    x = indicoio.political(content)
    rating = (x['Liberal'] / (x['Liberal'] + x['Conservative'])) * 10
    return (rating)


def get_continuous_chunks(text):
    """Named Entity Recognition."""
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
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

    return continuous_chunk


def jaccard_similarity(query, document):
    """Determine similarity of two documents."""
    intersection = set(query).intersection(set(document))
    union = set(query).union(set(document))
    return len(intersection) / len(union)


def genDB():
    """Fill Database."""
    temp = models.Article('0')
    db.session.add(temp)
    db.session.commit()
    temp = models.Article('1')
    db.session.add(temp)
    db.session.commit()
    temp = models.Article('2')
    db.session.add(temp)
    db.session.commit()
    pass
