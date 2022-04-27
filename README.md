# Grupp-13
===============================================================
Getting Started:
================================================================
to use this program you will need to make an virtual enviorment
in the repo directory and download all the essential packages. 
to make a virtual enviorment you need to install chocolatey https://chocolatey.org/install
when you are done with chocolatey you will need to paste these commands in power word shell

    choco install make

to see what version you are running use 

    make --version

Now you are ready to create a venv environment open git bash and use

    python -m venv .venv 

this will create a .venv folder in the repo 
we will then want to activate the venv by using

    . .venv/Scripts/activate

now to install the required packages you use the following command in git bash

    python -m pip install -r requirements.txt

to check all the packages you isntalled use 

    python -m pip list
or 
    pip list

when you are done with the venv use

    deactivate

when you have succesfully donwloaded everything you can now play the game 
to play the game open use any type of command prompt like git bash 
and use the command when in the correct dir

    python main.py 

============================================================
Generate documentation
============================================================
to generate documentation on this project you need to install graphviz
to install graphviz you will need to use the following command in powerShell as in administrator

    choco install graphviz

after you have installed graphviz you check the version you got in git bash

    dot -V

now to generate documentation use the following command

    make doc 

this will create uml diagrams and documentation in the folder doc which is located in the pig folder
you can then open the documnenation and um in your browser 

=============================================================
How to run the liners
============================================================
to use the linters use the command

    make lint 

this will use flake 8 and pylint

=============================================================
how to run unittests
=============================================================
run all the unit tests by using the command

    make unittest

to run and get coverage on the unittest use the command

    make coverage

to run the linters and unittests at the same time use the command 

    make test 

==============================================================
how to clean up repo 
===============================================================
use these git commands to clean the dir

    make clean 

make clean removes coverage, __pychache__ and htmlcov

    make clean-doc

clean the doc folder

    make clean all 

clean all runs the clean and clean-doc
