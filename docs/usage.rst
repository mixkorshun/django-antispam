.. _usage:

Usage
=====

Honeypot field
--------------

Honeypot is a spam protection technique to detect and block automatic spam spiders on your website.
Also known as **spamtrap** technique.

.. seealso:: You can read more about this technique at `Wikipedia <https://en.wikipedia.org/wiki/Spamtrap>`_.

Form protection is very simple, just add a ``HoneypotField`` to your form:

..  code-block:: python

    from django import forms
    from antispam.honeypot.forms import HoneypotField

    class MyForm(forms.Form):
        name = forms.CharField()
        spam_honeypot_field = HoneypotField()

HoneypotField uses standard form validation behaviour.
If spam submit was detected - ``ValidationError`` with ``spam-protection`` code will be raised.


Akismet
-------
.. image:: images/akismet.png
   :align: right
   :alt: Akismet logo
   :width: 250

Akismet is an advanced hosted anti-spam service aimed at thwarting the underbelly of the web.
It efficiently processes and analyzes masses of data from millions of sites and communities in real time.

.. seealso:: You can read more at Akismet `official website <https://akismet.com/>`__.

Use Akismet protection for your project:

..  code-block:: python

    from django import forms
    from antispam import akismet

    class MyForm(forms.Form):
        name = forms.CharField()
        email = forms.EmailField()

        comment = forms.TextField()

        def __init__(self, **kwargs):
            self.request = kwargs.pop('request', None)

            super().__init__(**kwargs)

        def clean():
            if self.request and akismet.check(
                request=akismet.Request.from_django_request(self.request),
                comment=akismet.Comment(
                    content=self.cleaned_data['comment'],
                    type='comment',

                    author=akismet.Author(
                        name=self.cleaned_data['name'],
                        email=self.cleaned_data['email']
                    )
                )
            ):
                raise ValidationError('Spam detected', code='spam-protection')

            return super().clean()


CAPTCHA
-------

CAPTCHA – Completely Automated Public Turing test to tell Computers and Humans Apart. We support CAPTCHA implementation
called **reCAPTCHA V2**.

reCAPTCHA V2
~~~~~~~~~~~~

.. image:: images/recaptcha.png
   :align: right
   :alt: reCAPTCHA v2
   :width: 250

**reCAPTCHA** is a free service that protects your website from spam and abuse. reCAPTCHA uses an advanced risk analysis engine
and adaptive CAPTCHAs to keep automated software from engaging in abusive activities on your site.

.. seealso:: You can read more at google reCAPTCHA `official website <https://www.google.com/recaptcha>`__.

To use reCAPTCHA protection in your project form, obtain keys `from Google <https://www.google.com/recaptcha/admin>`, add them to ``SETTINGS``: 

..  code-block:: python

    RECAPTCHA_SITEKEY = 'sitekey'

    RECAPTCHA_SECRETKEY = 'secretkey'
       
and add ``ReCAPTCHA`` field:

..  code-block:: python

    from django import forms
    from antispam.captcha.forms import ReCAPTCHA

    class MyForm(forms.Form):
        name = forms.CharField()

        captcha = ReCAPTCHA()

**django-antispam** package provides 2 widgets of reCAPTCHA:
 * ``antispam.captcha.widgets.ReCAPTCHA`` - default reCAPTCHA v2 widget
 * ``antispam.captcha.widgets.InvisibleReCAPTCHA`` - invisible reCAPTCHA widget

To display reCAPTCHA on website page, you should add reCAPTCHA script into the template:

..  code-block:: django

    {% load recaptcha %}

    {% block head %}
        ...

        {% recaptcha_init %}
    {% endblock %}
