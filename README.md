Exaile testing with pytest 
======

This repository contains Exaile version 4.1.3 tested with the pytest module. As the original repository already contains its own set of test cases we have decided to omit those for clarity. 
The total amount of test cases from this repository is 268 test cases, with 212 passing and 56 failing. For more details regarding the test cases please refer to our document. 

Below is the steps to setup and run the test cases:
- Install python version 3.7+.
- Setup Exaile for your specific operating software with the guide of Exaile's [documentation](https://exaile.readthedocs.io/en/stable/dev/getting_started.html).
- Install the newest version of pytest using `pip install -U pytest`.
- Navigate to this repository's directory and run `pytest` from root.

To view the coverage report, either generate it using `coverage run -m pytest && coverage html` or open the existing webpage at `htmlcov/index.html`.

# How to run slash tests.
## Prerequisites
### Installing gi module

```
pip install meson
pip install ninja
sudo apt-get install itstool
sudo apt install libcairo2-dev libxt-dev libgirepository1.0-dev
pip install pycairo PyGObject
```

### Installing berkleyDB dependencies

```
./wget_berkley.sh
unzip V997917-01.zip
cd db-18.1.40
cd build_unix/
../dist/configure --prefix=/usr/local --enable-cxx
make
mkdir db-18.1.40/docs/bdb-sql db-18.1.40/docs/gsg_db_server
make install

sudo apt-get install libdb++-dev
pip3 install bsddb3
```

### Tests and assets.
Extract test_slash.zip file to test_slash folder.

## Slash Framework and Common Libraries
```
pip install setuptools
pip install slash
pip install pandas
```

## Slash Testing Output and Coverage

```
slash run tests_slash/xl/test.py --with-coverage --cov xl --cov-report html
coverage html -d dir_name
```
Coverage is in the HTML format storaged in the "dir_name" folder. Full report accesable in index.html file.

Change test.py for getting report for each test.  

List of files with tests:
1. test_common.py
2. test_settings.py
3. test_unicode.py

### Exaile Automation Test Suite

This Python script contains an automation test suite for Exaile, a music player application. The script utilizes the PyAutoGUI library for GUI automation and subprocess for running the Exaile executable.

#### Instructions for Use:

1. **Requirements:**
   - Python 3.x
   - PyAutoGUI library

2. **Setup:**
   - Ensure that Python 3.x is installed on your system.
   - Install the PyAutoGUI library using `pip install pyautogui`.
   - Set the `exe_path` variable in the script to the path of the Exaile executable (`exaile.exe`).

3. **Running the Tests:**
   - Run the script using `python exaile_automation.py`.
   - The script will open Exaile, perform various actions such as switching tabs, creating playlists, playing music, and taking screenshots after each action.
   - Screenshots are saved in the `testResultImg` folder.

4. **Test Cases Covered:**
   - Opening and closing Exaile.
   - Switching between different tabs (Collection, Radio, Playlists, etc.).
   - Creating a new playlist and closing the last playlist.
   - Opening file-related actions like opening files, URLs, directories, etc.
   - Playing, pausing, stopping, and navigating through music tracks.
   - Adjusting volume, muting/unmuting, and searching for music.
   - Refreshing the music collection and setting repeat/shuffle options.

5. **Additional Notes:**
   - Ensure that Exaile is properly installed and configured before running the script.
   - Modify the `buttonPos` dictionary in the script if the positions of GUI elements change in the application.

#### Disclaimer:
This automation script is provided as-is and may require adjustments based on specific system configurations and Exaile version. Use with caution and test thoroughly before applying to production environments.
