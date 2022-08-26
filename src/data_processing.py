from typing import List
import string

import pandas as pd


PUNCTUATION = set(string.punctuation)


def split_name_fn(common_words: List[str]):
    def split_name(x):
        x = ''.join(ch for ch in x if ch not in PUNCTUATION)
        x_split = x.upper().split()
        name = ' '.join([w for w in x_split if w not in common_words])
        number = x_split[-1] if x_split[-1].isnumeric() else None
        return (name, number)
    return split_name
