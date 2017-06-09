from datetime import datetime

from .utils import get_client_ip


class Request:
    @classmethod
    def from_django_request(cls, request):
        return cls(
            ip_address=get_client_ip(request),
            user_agent=request.META.get('HTTP_USER_AGENT', ''),
            referrer=request.META.get('HTTP_REFERRER', ''),
        )

    def __init__(self, ip_address=None, user_agent=None, referrer=None):
        self.ip_address = ip_address
        self.user_agent = user_agent
        self.referrer = referrer

    def as_params(self):
        return {
            'user_ip': self.ip_address,
            'user_agent': self.user_agent,
            'referrer': self.referrer,
        }


class Author:
    @classmethod
    def from_django_user(cls, user):
        return cls(
            name=user.get_full_name(),
            email=user.email,
            role='administrator' if user.is_staff else None
        )

    def __init__(self, name=None, email=None, url=None, role=None):
        self.name = name
        self.email = email
        self.role = role
        self.url = url

    def as_params(self):
        return {
            'comment_author': self.name,
            'comment_author_email': self.email,
            'comment_author_url': self.url,
            'user_role': self.role,
        }


class Site:
    def __init__(self, base_url=None, language_code=None):
        self.base_url = base_url
        self.language_code = language_code

    def as_params(self):
        return {
            'blog': self.base_url,
            'blog_lang': self.language_code,
        }


class Comment:
    def __init__(self, content, type=None, permalink=None, author=None, site=None):
        self.content = content
        self.type = type
        self.permalink = permalink

        self.author = author
        self.site = site

        self.created = datetime.utcnow()

    def as_params(self):
        params = {
            'comment_type': self.type,
            'comment_content': self.content,
            'comment_date': self.created.timestamp(),
            'permalink': self.permalink,
        }

        if self.site:
            params.update(self.site.as_params())

        if self.author:
            params.update(self.author.as_params())

        return params
