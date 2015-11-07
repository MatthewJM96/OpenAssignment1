#!/usr/bin/env bash
python_version=$(python --version 2>&1 | awk '{print $2}' | head -c 1)
VENV=${1:-venv$python_version}  # default environment is

# If we don't have a virtual environment already, then create one
if [ ! -d "$VENV" ]; then
    if [ "$python_version"  == "3" ]; then
        # virtualenv and pip comes with python3
        python -m venv $VENV
    elif [ "$python_version"  == "2" ]; then
        # Check for pip and install if not available
        pip --version 2>/dev/null
        if [ $? != 0 ]; then
            # Get pip
            curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | sudo python
        fi
        # Check for virtualenv and install if not available
        virtualenv --version 2>/dev/null
        if [ $? != 0 ]; then
            pip install virtualenv
        fi
        virtualenv $VENV
    fi
fi

# Source into that environment
if [ -d "$VENV" ]; then
    source $VENV/bin/activate
    pip install -r requirements.txt
else
    >&2 echo "ERROR: Could not open virtualenv"
fi