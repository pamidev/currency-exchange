# Currency Exchange
> This Python program converts currency exchange rates into Polish zlotys (PLN) according 
> to the average exchange rates from Table A of the [National Bank of Poland](http://www.nbp.pl/) 
> on a selected day (beginning from 2002-01-02).


## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Acknowledgements](#acknowledgements)


## General Information
The purpose of the program is to use an external API (_Application Programming Interface_) 
to convert exchange rates based on the data provided by the user. 
Thanks to this project, I learned how to use APIs and apply them to my another programming projects.

[More about APIs](https://www.ibm.com/topics/rest-apis).


## Technologies Used
- [Python](https://www.python.org/) - version 3.9.13
- Python third-party packages:
  - [_requests_](https://pypi.org/project/requests/) - version 2.29.0
  - [_python-dateutil_](https://pypi.org/project/python-dateutil/) - version 2.8.2
- [NBP Web API](https://api.nbp.pl/en.html)


## Features
- The user can provide up to two arguments (date and three-letter currency code) 
when running the program.
- The program can also be run with one argument or none. It doesn't matter what user entered - the date
or the currency code.
- If the user does not enter any data when starting the program, 
the program will ask for it itself.
- Date can be entered in any way, for example: 
_13.12.2011_, _"15 May 2015"_ or _2016-06-16_, or even _20091209_.

> Note that the date with spaces must be entered in _"quotation marks"_.


## Screenshots
![Example screenshot](./img/screenshot.png)


## Setup
I assume you know how to cloning this repository. If not, I refer you to 
[this publication](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

At the beginning You need to make sure you have Python version up to 3.9, 
as one of the packages does not work with the latest versions of Python.

> If You don't have any Python version, download and install [from here](https://www.python.org/).

To verify Python version, type in terminal:
```bash
$ python --version
```
If You are seeing this answer (* - any digits):
```bash
$ python --version
$ Python 3.9.*
```
We are at home! Now You need to install _virtual environment_ like this:
```bash
$ python -m venv venv
$ cd venv\Scripts
$ activate
$ cd ..
$ cd ..
```
and install dependencies in the previously created _virtual environment_:
```bash
$ pip install -r requirements.txt
```
After installing this, run the program like bellow.


## Usage
How does one go about using it? It's simple. 
To run program without any arguments type in terminal:
```bash
$ python currency-exchange.py
```
or to run program with GBP currency code for example as one of arguments:
```bash
$ python currency-exchange.py gbp
```
or to run program with two arguments (date and currency code):
```bash
$ python currency-exchange.py 20.11.2019 usd
```


## Acknowledgements
- This program was inspired by one of exercises of
[the Practical Python](https://praktycznypython.pl/) educational program.
- Many thanks to [Krzysztof Mędrela](https://medrela.com/).
