.. _getstarted:

Get started
===========

Installing django-antispam
--------------------------

The package can be installed using::

    pip install django-antispam


Configuration
-------------

Add the following settings::

    INSTALLED_APPS += (
        'antispam',
    )

    # to use Akismet protection

    AKISMET_API_KEY = '<akismet api-key>'

    AKISMET_SITE_URL = '<base site url>'

    AKISMET_TEST_MODE = False

