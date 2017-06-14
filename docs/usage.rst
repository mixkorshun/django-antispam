.. _usage:

Usage
=====

Honeypot field
--------------

Honey pot is a spam protection technique to detect and block automatic spam spiders on your website.
Also known as **spamtrap** technique.

.. seealso:: You can read more about this technique at `Wikipedia <https://en.wikipedia.org/wiki/Spamtrap>`_.

Protection of form is very simple, just add an HoneypotField to your form:

..  code-block:: python

    from django import forms
    from antispam.honeypot.forms import HoneypotField

    class MyForm(forms.Form):
        name = forms.CharField()
        spam_honeypot_field = HoneypotField()

HoneypotField use standard form validation behaviour to work.
If spam submit was detected - ``ValidationError`` with ``spam-protection`` code will be raised.


Akismet
-------

Akismet is an advanced hosted anti-spam service aimed at thwarting the underbelly of the web.

.. seealso:: You can read more at Akismet `official website <https://akismet.com/>`_.

Use Akismet protection in your project:

..  code-block:: python

    from django import forms
    from antispam import akismet

    class MyForm(forms.Form):
        name = forms.CharField()
        email = forms.EmailField()

        comment = forms.TextField()

        def __init__(**kwargs):
            self.request = kwargs.pop('request', None)

            super().__init__(**kwargs)

        def clean():
            if akismet.check(
                request=akismet.Request.from_django_request(self.request) if self.request else None,
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

            super().clean()


CAPTCHA
-------
CAPTCHA – Completely Automated Public Turing test to tell Computers and Humans Apart. We support CAPTCHA implementation
called **reCAPTCHA V2**.

**reCAPTCHA** is a free service that protects your website from spam and abuse. reCAPTCHA uses an advanced risk analysis engine
and adaptive CAPTCHAs to keep automated software from engaging in abusive activities on your site.
It does this while letting your valid users pass through with ease.

.. seealso:: You can read more at google reCAPTCHA `official website <https://www.google.com/recaptcha>`_.

Use ReCAPTCHA protection in your project form:

..  code-block:: python

    from django import forms
    from antispam.captcha.forms import ReCAPTCHA

    class MyForm(forms.Form):
        name = forms.CharField()

        captcha = ReCAPTCHA()

**django-antispam** package provide 2 widgets of reCAPTCHA:
 * ``antispam.captcha.widgets.ReCAPTCHA`` - default reCAPTCHA v2 widget
 * ``antispam.captcha.widgets.InvisibleReCAPTCHA`` - reCAPTCHA Invisible widget
