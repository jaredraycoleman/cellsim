#!/bin/bash

pwd="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $pwd

if [ -f ./Miniconda3-latest-Linux-x86_64.sh ]; then
    echo "Installer already downloaded!"
else
    echo "$pwd/Miniconda3-latest-Windows-x86_64.sh not found"
    echo "Downloading installer now!"
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    chmod +x ./Miniconda3-latest-Linux-x86_64.sh
fi

if [ -d ./miniconda3 ]; then
    echo "Miniconda3 already installed!"
else 
    echo "$pwd/miniconda3 does not exist" 
    echo "Installing Miniconda3 now!"
    ./Miniconda3-latest-Linux-x86_64.sh -b -p $pwd/miniconda3
fi

if [[ $PATH == *"$pwd/miniconda3"* ]]; then
    echo "$pwd/miniconda3 is already on the Path"
else
    echo "Adding $pwd/miniconda3 to the Path"
    export PATH=$pwd/miniconda3/bin:$PATH
fi

if [ -d ./pypi ]; then
    echo "Dependencies already downloaded!"
else 
    echo "$pwd/pypi does not exist" 
    echo "Downloading dependencies now!"
    pip download -r requirements.txt -d ./pypi 
fi

echo "Installing cellsim dependencies"
pip install -r requirements.txt --find-links=./pypi
