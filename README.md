# Get your boilerplate for Avent of code

## How to install & use

1. [**Fork**](https://github.com/JulienDoma/aocboilerplate/fork) the repo on your github account. 🚫 **DO NOT** clone it directly
2. Clone the forked repo on your computer
3. Create a python virtual environnement for AOC
4. `pyenv local <your_python_venv_name>` to activate it
5. Install the package in it with `make install`
6. Rename `.env.sample` file to `.env`
7. Fill you cookies session id in `.env` **SESSION** variable from [aoc](https://adventofcode.com/) website
8. Log in with your prefered method.
9. Once logged, you can access this by opening web console => Network => refresh the page and click on the first request GET, you should be able to find the session id in the headers request.
- You're good to go !

## How to create files

From your terminal :

`python aoc_input/create_day.py <year> <day>`

For example with the 2015 1st puzzle : `python aoc_input/create_day.py 2015 1`

## Troubleshoot

If you encounter any issue while creating a new day, do `make check`

If you have any of the following message, please, check the installation process according to the error:
- 🚫 .env file is missing => instruction `6`
- 🚫 SESSION variable not found in .env => `.env` should not be empty
- 🚫 SESSION variable is empty => instruction `9`