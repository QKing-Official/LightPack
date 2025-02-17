# LightPack
A lightweight opensource package manager and shell
LightPack Package Manager

LightPack is a lightweight package manager that allows you to easily download, install, and run custom Python packages from a remote repository.

Features

Install packages with a simple command.

Run installed packages directly from the LightPack shell.

Automatically fetch required dependencies.

Easy-to-use interactive shell.

Installation

Clone the Repository

To use LightPack, clone the repository:

$ curl -O https://raw.githubusercontent.com/QKing-Official/LightPack/main/package_manager.py
(git clone https://github.com/QKing-Official/LightPack.git for whole repo including all packages)
$ cd LightPack

Run the Package Manager

Start the interactive shell by running:

$ python package_manager.py

Usage

Once inside the LightPack shell, you can use the following commands:

Install a Package

To install a package, use:

lightpack-shell> install <package_name>

Example:

lightpack-shell> install hello-world

Run an Installed Package

To run an installed package, use:

lightpack-shell> run <package_name>

Example:

lightpack-shell> run hello-world

Exit the Shell

To exit LightPack, use:

lightpack-shell> exit

Available Packages

Here are some useful packages available for installation:

hello-world – Prints "Hello, World!"

weather – Fetches real-time weather data.

calculator – A simple CLI calculator.

todo – A basic to-do list manager.

Creating Your Own Packages

You can create your own packages and host them in the repository.

Package Structure

Each package should have:

A main script: <package_name>.py

(Optional) An installer script: install.py

Example structure:

/packages/
    /hello-world/
        hello-world.py
        install.py (optional)

Adding Your Package to LightPack

Add your package to the packages/ directory.

Push the changes to the repository.

Users can now install your package using install <package_name>.

Contributing

Feel free to contribute new packages or improve existing ones. Fork the repo, make your changes, and submit a pull request.
