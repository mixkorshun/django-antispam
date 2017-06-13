django-antispam
===============

.. image:: https://travis-ci.org/mixkorshun/django-antispam.svg?branch=master
   :alt: build status
   :target: https://travis-ci.org/mixkorshun/django-antispam
.. image:: https://codecov.io/gh/mixkorshun/django-antispam/branch/master/graph/badge.svg
   :alt: codecov
   :target: https://codecov.io/gh/mixkorshun/django-antispam
.. image:: https://badge.fury.io/py/django-antispam.svg
   :alt: pypi
   :target: https://pypi.python.org/pypi/django-antispam
.. image:: https://img.shields.io/badge/code%20style-pep8-orange.svg
   :alt: pep8
   :target: https://www.python.org/dev/peps/pep-0008/
.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :alt: MIT
   :target: https://opensource.org/licenses/MIT

Various anti-spam protection tools for django applications.

See the documentation_ for more details.

Installation
------------

The package can be installed using::

    pip install django-antispam

Add the following settings::

    INSTALLED_APPS += (
        'antispam',
    )

    # to use Akismet protection

    AKISMET_API_KEY = '<akismet api-key>'

    AKISMET_SITE_URL = '<base site url>'

    AKISMET_TEST_MODE = False


Contributing
------------

If you have any valuable contribution, suggestion or idea,
please let us know as well because we will look into it.

Pull requests are welcome too.


.. _documentation: https://django-antispam.readthedocs.io/
