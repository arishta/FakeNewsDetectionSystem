import numpy as np # linear algebra
import pandas as pd #data processing
import os
import re
import nltk

def get_all_query(title, author, text):
    total= title + author + text
    total = [total]
    return total
