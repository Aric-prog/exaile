import sys        
sys.path.insert(1, './')

import os
os.environ["EXAILE_DIR"] = './'

import slash
import xl.settings as settings

val_to_str_tests_values = [(0, "I: 0"),(-10, "I: -10"),(-10.1, "F: -10.1"),([], "L: []"),({}, "D: {}"),(0.0, "F: 0.0"),(True, "B: True"), (10, "I: 10") , (10.1, "F: 10.1"), ([1,2,3], "L: [1, 2, 3]"), ({"key1":1},"D: {'key1': 1}")]
str_to_val_tests_strings = [("I: 0", 0),("I: -10", -10),("F: -10.1", -10.1),("L: []", []),("D: {}", {}),("F: 0.0", 0.0),("B: True", True), ("I: 10", 10) , ("F: 10.1", 10.1), ("L: [1, 2, 3]", [1,2,3]), ("D: {'key1': 1}", {"key1":1})]

@slash.parametrize(("value", "expected_result"), val_to_str_tests_values)
def test__val_to_str(value, expected_result):
    #setup 
    settingsmanager = settings.SettingsManager() 
    #execute
    result = settingsmanager._val_to_str(value)
    #assert
    assert result == expected_result
    
@slash.parametrize(("value", "expected_result"), str_to_val_tests_strings)
def test__str_to_val(value, expected_result):
    #setup 
    settingsmanager = settings.SettingsManager() 
    #execute
    result = settingsmanager._str_to_val(value)
    #assert
    assert result == expected_result

set_option_tests = [(['Section1/option1', 10], True), (['Section1/option2', 'String'], True), (['/', 10], True)]
get_option_tests = [('Section1/option1', 10), ('Section1/option2', 'String' )]
remove_default_section = [('DEFAULT', False)]
remove_option_tests = [('Section1/option1', False), ('Section1/option2', False), ('/', False) ]
save_test = [(['Section1/option3', 'test'], True )]


@slash.parametrize(("value", "expected_result"), set_option_tests)
def test_set_option(value, expected_result):
    #setup 
    settingsmanager = settings.SettingsManager('./tests_slash/assets/settings.ini') 
    #execute
    settingsmanager.set_option(value[0], value[1])
    settingsmanager.save()    
    result = settingsmanager.has_option(value[0])
    #assert
    assert result == expected_result
    
@slash.parametrize(("value", "expected_result"), set_option_tests)
def test_has_option(value, expected_result):
    #setup 
    settingsmanager = settings.SettingsManager('./tests_slash/assets/settings.ini') 
    #execute
    result = settingsmanager.has_option(value[0])
    #assert
    assert result == expected_result

@slash.parametrize(("value", "expected_result"), get_option_tests)
def test_get_option(value, expected_result):
    #setup 
    settingsmanager = settings.SettingsManager('./tests_slash/assets/settings.ini') 
    #execute
    result = settingsmanager.get_option(value)
    #assert
    assert result == expected_result

@slash.parametrize(("value", "expected_result"), remove_option_tests)
def test_remove_option(value, expected_result):
    #setup 
    settingsmanager = settings.SettingsManager('./tests_slash/assets/settings.ini') 
    #execute
    settingsmanager.remove_option(value)
    settingsmanager.save()
    result = settingsmanager.has_section(value)
    #assert
    assert result == expected_result

@slash.parametrize(("value", "expected_result"), remove_default_section)
def test_remove_default(value, expected_result):
    #setup 
    settingsmanager = settings.SettingsManager('./tests_slash/assets/settings.ini') 
    #execute
    settingsmanager.set_option('/', 10)
    settingsmanager.save()
    settingsmanager.remove_option(value)
    settingsmanager.save()
    result = settingsmanager.has_section(value)
    #assert
    assert result == expected_result

@slash.parametrize(("value", "expected_result"), save_test)
def test_save(value, expected_result):
    #setup 
    settingsmanager = settings.SettingsManager('./tests_slash/assets/settings.ini') 
    #execute
    settingsmanager.set_option(value[0], value[1])
    settingsmanager.save()
    result = settingsmanager.has_option(value[0])
    #assert
    assert result == expected_result
