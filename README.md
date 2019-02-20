Simulator for system of robots with local state machines (cellular automota). 

# Requirements
Python 3.6 (I recommend the [miniconda3](https://docs.conda.io/en/latest/miniconda.html) distribution)

## Setup
Run the following commands for *each new terminal* you open, to set up the environment correctly. 
The first time you run the script, all dependencies (miniconda3, matplotlib, scipy, and numpy) will be downloaded (if necessary) and installed.

### Windows 10
Open powershell, ```cd``` to the clone repository, and run:
```ps1
Set-ExecutionPolicy Unrestricted -Scope Process     # grants permission to run the script
. .\init.ps1        # The preceding dot is important!
```

### Linux
Open terminal (bash), ```cd``` to the clone repository, and run:
```bash
chmod +x ./init.sh  # only needs to be run the first time
. ./init.sh         # The preceding dot is important!
```

# Usage 
Modify [main.py](./main.py) to change the behavior of the system. 
To run the simulation:
```bash
python main.py
```