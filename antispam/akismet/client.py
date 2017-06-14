from akismet import Akismet
from django.conf import settings


def get_connection(api_key=None, blog=None, is_test=None):
    """
    Get Akismet client object.
    
    If no connection params provided, use params from django project settings.

    :param api_key: Akismet API key
    :param blog: blog base url
    :param is_test: test mode
    :rtype akismet.Akismet
    :return: akismet client
    """

    if is_test is None:
        is_test = getattr(settings, 'AKISMET_TEST_MODE', False)

    return Akismet(
        api_key=api_key or getattr(settings, 'AKISMET_API_KEY'),
        blog=blog or getattr(settings, 'AKISMET_SITE_URL', None),
        is_test=is_test,
    )


def check(request, comment):
    """
    Checks given comment to spam by Akismet.
    
    :type request: antispam.akismet.Request
    :type request: antispam.akismet.Comment 
    :return: True if comment is spam, otherwise False
    """
    params = {}
    params.update(request.as_params())
    params.update(comment.as_params())

    client = get_connection()
    return client.check(**params)


def submit(request, comment, is_spam):
    """
    Submit given comment to Akismet.
    
    Information about comment status must be provided (spam/not spam)

    :type request: antispam.akismet.Request
    :type request: antispam.akismet.Comment 
    :type is_spam: bool
    """

    params = {}
    params.update(request.as_params())
    params.update(comment.as_params())

    connection = get_connection()
    connection.submit(is_spam=is_spam, **params)
