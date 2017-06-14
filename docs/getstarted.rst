.. _getstarted:

Get started
===========

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

    # reCAPTCHA site-wide configuration

    RECAPTCHA_SITEKEY = 'sitekey'

    RECAPTCHA_SECRETKEY = 'secretkey'

    RECAPTCHA_WIDGET = 'antispam.captcha.widgets.ReCAPTCHA'

    RECAPTCHA_TIMEOUT = 5

    RECAPTCHA_PASS_ON_ERROR = False
