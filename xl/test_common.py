import sys        
sys.path.insert(1, './')

import slash
from xl.common import clamp

cases = [([10, 0, 20], 10), 
         ([10, 10, 20], 10), 
         ([0, 0, 0], 0), 
         ([20, 10, 20], 20), 
         ([21, 10, 20], 20), 
         ([11, 10, 20], 11), 
         ([19, 10, 20], 19), 
         ([9, 10, 20], 10), 
         ([-9, 10, 20], 10)]

@slash.parametrize(("values", "expected_result"), cases)
def test_unicode(values, expected_result):
    #setup 
    #execute
    result = clamp(values[0], values[1], values[2])
    #assert
    assert result == expected_result