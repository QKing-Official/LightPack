# LightPack

A lightweight opensource package manager and shell

LightPack Package Manager

LightPack is a lightweight package manager that allows you to easily download, install, and run custom Python packages from a remote repository.

## Features

Install packages with a simple command.

Run installed packages directly from the LightPack shell.

Automatically fetch required dependencies.

Easy-to-use interactive shell.

## Installation

Clone the Repository

To use LightPack, clone the repository:

```bash
curl -O https://raw.githubusercontent.com/QKing-Official/LightPack/main/package_manager.py
```

For the whole repo (with all packages):
```bash
git clone https://github.com/QKing-Official/LightPack.git
```

```bash
cd LightPack
```

## Run the Package Manager

Start the interactive shell by running:

```bash
python packag_manager.py
```

## Usage

Once inside the LightPack shell, you can use the following commands:

Install a Package

To install a package, use:

```bash
lightpack-shell> install
```

Example:

```bash
lightpack-shell> install hello-world
```

Run an Installed Package

To run an installed package, use:

```bash
lightpack-shell> run
```

Example:

```bash
lightpack-shell> run hello-world
```

Clear the screen:
```bash
lightpack-shell> clear
```

Ask for help:
```bash
lightpack-shell> help
```

Update a package:
```bash
lightpack-shell> update <packagename>
```

Exit the Shell

To exit LightPack, use:

```bash
lightpack-shell> exit
```

For community packages installation guide scroll down.


## Some available Packages (there are way more)

Here are some (useful) packages available for installation:

hello-world – Prints "Hello, World!"

network-info - Gives information about your network.

sys-info - Gives information about your system.

These are all official, if you want to make you own or install community packages. Scroll down.

## Creating Your Own Packages

You can create your own packages and host them in the repository.

Package Structure

Each package should have:

A main script: .py

An installer script: install.py

Example structure:

```cpp
/packages/

/hello-world/

hello-world.py

install.py

```

Adding Your Package to LightPack (alternative databases for packages comming soon!)

Add your package to the packages/ directory.

Here is the format for making a package.

```python

#my_package.py

def main_functionality():

"""Implement the core functionality of your package."""

print("This is where the main functionality goes.")

if __name__ == "__main__":

main_functionality()

```





```python

#install.py

import os

import sys

import subprocess

def install():

print("Installing My Package...")

# Ensure the package directory exists

package_dir = os.getcwd() # Current directory

script_path = os.path.join(package_dir, "my_package.py")

if not os.path.exists(script_path):

print(f"Error: {script_path} does not exist.")

return

# List of dependencies to install

dependencies = ["requests", "numpy", "pandas"] # Example dependencies

try:

# Install dependencies

for dependency in dependencies:

print(f"Installing {dependency}...")

subprocess.run([sys.executable, "-m", "pip", "install", dependency], check=True)

print(f"{dependency} installed successfully.")

print("My Package installed successfully!")

except Exception as e:

print(f"Error during installation: {e}")

if __name__ == "__main__":

install()

```

Your package is done! (You can install it when you clone whole repo)
More on publication on packages in the next part

## How to make your own package repository (Publication)

To make a package repository you need to make a repository on github first.
Structure the repository like this:
```cpp
lightpackages/            
│── repo.json                      
│
└── packages/                       
    ├── example/                    
    │   ├── install.py              
    │   ├── example.py             
    │
    ├── another_package/             
    │   ├── install.py
    │   ├── another_package.py
```

The repo.json needs to contain basic data of your repository
Structure it like this:
```json
{
    "name": "Example",
    "url": "https://raw.githubusercontent.com/USER/REPOSITORYNAME/main/packages"
}
```
Replace 'Example' with the name you want your repo to be showed as inside Lightpack.
Replace 'USER' with your Github username and 'REPOSITORYNAME' with the name of your repository.
The packages or put in the packages directory and are structured as explained before.

## Install community packages/repositories

Now all users can install your packages with the following guide:

Add the repository to the community packages inside Lightpack
```bash
lightpack-shell> addrepo REPO_URL_FROM_REPO.JSON
```
Replace 'REPO_URL_FROM_REPO.JSON' with the url of the repository.

Install packages from the repository:
```bash
lightpack-shell> install PACKAGENAME:REPONAME
```

Replace 'PACKAGENAME' with the name of the package you want to install and  'REPONAME' with the name of the repo (from the repo.json).

You can uninstall packages without the need of the :REPONAME section.

## How to see what repositories i have added?

If you want to see what repositories you have added. Run the following command inside of Lightpack:
```bash
lightpack-shell> listrepos
```
It will show all the names of the repositories you added.


If you want to remove a repository, run the following command:
```bash
lightpack-shell> removerepo REPONAME
```

replace 'REPONAME' witht the name of the repo (what you saw in the listrepo command).


Contributing
Feel free to contribute new packages or improve existing ones. Fork the repo, make your changes, and submit a pull request.
