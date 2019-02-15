
$scriptdir = Split-Path $MyInvocation.MyCommand.Path
Set-Location $scriptdir

if (Test-Path "$pwd\Miniconda3-latest-Windows-x86_64.exe") {
    Write-Output "Installer already downloaded!"
} else {
    Write-Output "$pwd\Miniconda3-latest-Windows-x86_64.exe not found"
    Write-Output "Downloading installer now!"
    Invoke-WebRequest `
        -Uri https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe `
        -OutFile Miniconda3-latest-Windows-x86_64.exe
}

if (Test-Path "$pwd\miniconda3") {
    Write-Output "Miniconda3 already installed!"
} else {
    Write-Output "$pwd\miniconda3 does not exist" 
    Write-Output "Installing Miniconda3 now!"
    Start-Process -Wait -FilePath .\Miniconda3-latest-Windows-x86_64.exe `
        -ArgumentList "/InstallationType=JustMe 
                    /AddToPath=0 
                    /RegisterPython=0 
                    /NoRegistry=1 
                    /S 
                    /D=$pwd\miniconda3"
}

if ($env:Path.Contains("$pwd\miniconda3")) {
    Write-Output "$pwd\miniconda3 is already on the Path"
} else {
    Write-Output "Adding $pwd\miniconda3 to the Path"
    $env:Path = "$pwd\miniconda3;" + `
                "$pwd\miniconda3\Library\usr\bin;" + `
                "$pwd\miniconda3\Library\mingw-w64\bin;" + `
                "$pwd\miniconda3\Library\bin;" + `
                "$pwd\miniconda3\Scripts;" + `
                "$env:Path"
}

if (Test-Path "$pwd\pypi") {
    Write-Output "Dependencies already downloaded!"
} else {
    Write-Output "$pwd\pypi does not exist" 
    Write-Output "Downloading dependencies now!"
    pip download -r requirements.txt -d .\pypi 
}

Write-Output "Installing cellsim dependencies"
pip install -r requirements.txt --find-links=.\pypi

