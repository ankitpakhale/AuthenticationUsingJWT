# Authentication using JWT

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/ankitpakhale/AuthenticationUsingJWT.git
$ cd AuthenticationUsingJWT
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv jwtenv
$ source jwtenv/bin/activate
```

Then install the dependencies:

```sh
(jwtenv)$ pip install -r requirements.txt
```
Note the `(jwtenv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(jwtenv)$ cd AuthenticationUsingJWT
(jwtenv)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

## Tests

To run the tests, `cd` into the directory where `manage.py` is:
```sh
(jwtenv)$ python manage.py test authentication
```