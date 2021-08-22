 # Best practices for a Python web application

## Framework 
- This web application created using [Flask](https://github.com/pallets/flask). \
It was choosen because it is simple and enables to create apps effortlessly and quickly.

## Package manager
The package manager is an alternative to a virtual environment for installing project dependencies.
- [pdm](https://github.com/pdm-project/pdm) used as a package manager in this project. You can see dependencies in *pyproject.toml* . 

Pdm, unlike Poetry or Pipenv get rid of virtualenv entirely. It installs dependencies into the local package directory __ package__ and makes Python interpreters aware of it with a very simple setup.

## Formatting tools
Code formatters changes your code to be aesthetics clean and improve readability. \
Formatting tools I used:
- [black](https://github.com/psf/black) - code formatting 
- [isort](https://github.com/PyCQA/isort) - import formatting 
- [pyupgrade](https://github.com/asottile/pyupgrade) -  automatically upgrades syntax for newer versions of the language.

## Linters
Linter is a tool that analyzes source code to flag programming errors, bugs, stylistic errors, and suspicious constructs.\
Linters I used:

- [Pylint](https://github.com/PyCQA/pylint) - looks for programming errors, helps enforcing a coding standard, sniffs for code smells and offers simple refactoring suggestions

- [Darglint](https://github.com/terrencepreilly/darglint) - checks whether a docstring's description matches the actual function/method implementation.

- [Bandit](https://github.com/PyCQA/bandit) - find common security issues in Python code.

## Tests
- [pytest](https://github.com/pytest-dev/pytest/) - framework makes it easy to write small tests

## Create .gitignore

## Adding LICENSE
- [lice](https://github.com/licenses/lice)

## Static analysis 

- [Mypy](https://github.com/python/mypy/) - static type checker for python

## Requirements.txt
I generate requirements.txt using 
```
pdm list --freeze >> requirements.txt
```

## Rules & Principles
- [PEP8](https://www.python.org/dev/peps/pep-0008/) - use PEP8 format for your python code.
- avoid legacy constructions
- Avoid Obvious Comments
- [Don't Repeat Yourself Principle](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)
- Avoid Deep Nesting
- Avoid Using Magic Numbers
