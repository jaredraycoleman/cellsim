Simulator for system of robots with local state machines (cellular automota). 

# Requirements
Python 3.6 (I recommend the [miniconda3](https://docs.conda.io/en/latest/miniconda.html) distribution)

## Installation Script 
### Windows 10
To run a completely portable installation on Windows 10, open powershell and run:
```ps1
Set-ExecutionPolicy Unrestricted -Scope Process
. .\init.ps1
```

### Linux
```bash
chmod +x ./init.sh
. ./init.sh
```

## Python requirements
Install the required python packages by running:
```bash
pip install -r requirements.txt
```

# Usage 
Modify [main.py](./main.py) to change the behavior of the system. To run the simulation:
```bash
python main.py
```