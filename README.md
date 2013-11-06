Just a very basic python project example to show a simple nose testing setup

Clone this repo somewhere on your computer
```bash
git clone https://github.com/necrolyte2/pytesting.git
```

Make sure to install nose
```bash
pip install nose
```

Then to run all the tests you can simply do this while in the project directory
```bash
nosetests
```

Or to run a specific test file
```bash
nosetests mymodule/tests/test_mymodule.py
```

Or to run a specific testclass in a test file
```bash
nosetests mymodule/tests/test_mymodule.py:TestMyModule
```

Or to run a specific test in a testclass in a test file
```bash
nosetests mymodule/tests/test_mymodule.py:TestMyModule.test_addtwoints
```
test
