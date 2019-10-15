# geditdone
>A parser and validator for GEDCOM files

[![Build Status](https://travis-ci.org/bak-minsu/geditdone.svg?branch=master)](https://travis-ci.org/maxlep/geditdone)

## Dependencies
> Check `requirements.txt` for the most up-to-date list of requirements

* Python 3
* Pandas 0.23.4

### Install dependencies
`pip3 install -r requirements.txt`

## Running

### Parser and validator
Run the project from the repository root using the following command:

`python3 -m geditdone testfiles/<testfile name>.ged`

### Unit testing
Run the unit tests from the repository root with the following command:

`python3 -m geditdone test`

Travis CI also runs its own tests at every commit:

https://travis-ci.org/bak-minsu/geditdone
