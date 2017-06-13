# django-antispam

[![Build Status](https://travis-ci.org/mixkorshun/django-antispam.svg?branch=master)](https://travis-ci.org/mixkorshun/django-antispam)
[![codecov](https://codecov.io/gh/mixkorshun/django-antispam/branch/master/graph/badge.svg)](https://codecov.io/gh/mixkorshun/django-antispam)
[![PyPI version](https://badge.fury.io/py/django-antispam.svg)](https://badge.fury.io/py/django-antispam)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Various anti-spam protection tools for django applications.

See the [documentation](https://django-antispam.readthedocs.io/) for more details.

## Installation

The package can be installed using:
```commandline
$ pip install django-antispam
```

And add the following settings:
```python
INSTALLED_APPS += (
    'antispam',
)

# to use Akismet protection

AKISMET_API_KEY = '<akismet api-key>'

AKISMET_SITE_URL = '<base site url>'

AKISMET_TEST_MODE = False
```