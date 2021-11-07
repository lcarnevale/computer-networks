# Computer Networks Programming in Python
[<img src="https://img.shields.io/badge/python-v3.X-blue">](python|v3.X)

Python introduction to Computer Networks @ University of Messina:

- [Lecture 01](lecture01): Application layer
- [Lecture 02](lecture02): Transport layer

## Best practice
Running with the system Python and libraries limits you to one specific Python version, chosen by your OS provider. Trying to run all Python applications on one Python installation makes it likely that version conflicts will occur among the collection of libraries. It's also possible that changes to the system Python will break other OS features that depend on it.

Virtual environments, or "virtualenvs" are lightweight, self-contained Python installations, designed to be set up with a minimum of fuss, and to "just work" without requiring extensive configuration or specialized knowledge.

virtualenv avoids the need to install Python packages globally. When a virtualenv is active, pip will install packages within the environment, which does not affect the base Python installation in any way.

```bash
sudo pip3 install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
```

## Install Requirements
```bash
pip install -r requirements.txt
```