from akismet import Akismet
from django.conf import settings


def get_connection():
    return Akismet(
        api_key=getattr(settings, 'AKISMET_API_KEY'),
        blog=getattr(settings, 'AKISMET_SITE_URL', ''),
        is_test=getattr(settings, 'AKISMET_TEST_MODE', False),
    )


def check(request, comment):
    params = {}
    params.update(request.as_params())
    params.update(comment.as_params())

    client = get_connection()
    return client.check(**params)


def submit(request, comment, is_spam):
    params = {}
    params.update(request.as_params())
    params.update(comment.as_params())

    connection = get_connection()
    connection.submit(is_spam=is_spam, **params)
