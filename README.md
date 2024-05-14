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