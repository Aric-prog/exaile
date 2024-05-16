# inserting the parent directory at position 1 in sys.path to get 
# ability import specific functions from application's modules
import sys        
sys.path.insert(1, './')

import pandas as pd
import slash
from xl.unicode import shave_marks, to_unicode

#creating cases lists for (text, expectefd_result) pairs.
def cases():

    #import list of characters
    df = pd.read_csv('./tests_slash/assets/test_letters.csv')
    text_result_pairs = []
    for index, row in df.iterrows():
        character = row['Character']
        if row['Character name'].split(' ')[0] == 'lowercase': 
            assertion = row['Character name'].split(' ')[1].lower()
        elif row['Character name'].split(' ')[0] == 'capital':
            assertion = row['Character name'].split(' ')[1].upper()
        text_result_pairs.append((character,assertion))

    #add special cases
    text_result_pairs.append(('',''))
    text_result_pairs.append((1025 * 'A',1025 * 'A'))
    return text_result_pairs

@slash.parametrize(("text", "expected_result"), cases())
def test_unicode(text, expected_result):
    #setup 
    #execute
    result = shave_marks(text)
    #assert
    assert result == expected_result
    

to_unicode_tests = [('test', 'test')]

@slash.parametrize(("value", "expected_result"), to_unicode_tests)
def test_to_unicode(value, expected_result):
    #setup 
    #execute
    result = to_unicode(value, encoding='utf-8', errors='strict')
    #assert
    assert result == expected_result