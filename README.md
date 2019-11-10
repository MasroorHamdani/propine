# propineglobal
# Install python
brew install python3

# Test if python is installed
python3

# Install pip
easy_install pip

# Install Virtual Environment
python3 -m pip install --user virtualenv

# Create Virtual Environment
python3 -m virtualenv env

# Activate virtual Environment
source env/bin/activate

# Install requirements
pip install -r requirement.txt

# Run application

# For 2nd Question run below command with arguments
python main.py      # No Argument passed

python main.py qdate="01/12/2017" token=BTC     # date and token both passed

python main.py qdate="01/12/2017"   # Only Date passed

python main.py token=BTC    # Only Towekn passed


# For 3rd Question ramda.js is the file.
It contains both the functions, I tried it on jsfiddle.
Adding the Link for JsFiddle Below:
https://jsfiddle.net/x6kb12af/29/

# For 1st Question lift.md is the file.