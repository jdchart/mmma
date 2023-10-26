#!/bin/bash

# Run all of the test files.
# Don't forget to give this script permission by running: 
# chmod a+x shell/run_tests.sh

echo -e "\nRunning tests...\n"
python -m unittest discover tests
echo -e "\nTests complete!\n"