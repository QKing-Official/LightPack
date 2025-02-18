# LightPack

A lightweight opensource package manager and shell

LightPack Package Manager

LightPack is a lightweight package manager that allows you to easily download, install, and run custom Python packages from a remote repository.

##Features

Install packages with a simple command.

Run installed packages directly from the LightPack shell.

Automatically fetch required dependencies.

Easy-to-use interactive shell.

##Installation

Clone the Repository

To use LightPack, clone the repository:

$ curl -O https://raw.githubusercontent.com/QKing-Official/LightPack/main/package\_manager.py

(git clone https://github.com/QKing-Official/LightPack.git for whole repo including all packages)

$ cd LightPack

Run the Package Manager

Start the interactive shell by running:

```bash
python packag_manager.py
```

Usage

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

Exit the Shell

To exit LightPack, use:

```bash
lightpack-shell> exit
```

##Some available Packages (there are way more)

Here are some (useful) packages available for installation:

hello-world – Prints "Hello, World!"

network-info - Gives information about your network.

sys-info - Gives information about your system.

Creating Your Own Packages

You can create your own packages and host them in the repository.

Package Structure

Each package should have:

A main script: .py

(Optional) An installer script: install.py

Example structure:

```mysql
/packages/

/hello-world/

hello-world.py

install.py (optional)

```

Adding Your Package to LightPack (alternative databases for packages comming soon!)

Add your package to the packages/ directory.

Here is the format for making a package.

```python

#my\_package.py

def main\_functionality():

"""Implement the core functionality of your package."""

print("This is where the main functionality goes.")

if \_\_name\_\_ == "\_\_main\_\_":

main\_functionality()

```



```python

#install.py

import os

import sys

import subprocess

def install():

print("Installing My Package...")

\# Ensure the package directory exists

package\_dir = os.getcwd() # Current directory

script\_path = os.path.join(package\_dir, "my\_package.py")

if not os.path.exists(script\_path):

print(f"Error: {script\_path} does not exist.")

return

\# List of dependencies to install

dependencies = \["requests", "numpy", "pandas"\] # Example dependencies

try:

\# Install dependencies

for dependency in dependencies:

print(f"Installing {dependency}...")

subprocess.run(\[sys.executable, "-m", "pip", "install", dependency\], check=True)

print(f"{dependency} installed successfully.")

print("My Package installed successfully!")

except Exception as e:

print(f"Error during installation: {e}")

if \_\_name\_\_ == "\_\_main\_\_":

install()

```

Users can now install your package using install. When community packages are added i will update you all with how to use it!

Contributing
Feel free to contribute new packages or improve existing ones. Fork the repo, make your changes, and submit a pull request.
