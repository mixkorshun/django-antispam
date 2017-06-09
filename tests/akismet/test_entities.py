from unittest import TestCase
from unittest.mock import Mock

from antispam.akismet.entities import Request, Author, Site, Comment


class RequestTests(TestCase):
    def test_to_params(self):
        req = Request('127.0.0.2', 'python/tests', 'https://localmachine')

        self.assertEqual({
            'user_ip': '127.0.0.2',
            'user_agent': 'python/tests',
            'referrer': 'https://localmachine',
        }, req.as_params())

    def test_from_django_request(self):
        req = Request.from_django_request(Mock(META={
            'REMOTE_ADDR': '127.0.0.2',
            'HTTP_USER_AGENT': 'python/tests',
            'HTTP_REFERRER': 'referrer',
        }))

        self.assertEqual('127.0.0.2', req.ip_address)
        self.assertEqual('python/tests', req.user_agent)
        self.assertEqual('referrer', req.referrer)


class AuthorTests(TestCase):
    def test_to_params(self):
        author = Author('Mike', 'mike@mail.loc', 'http://mike.example.com', role='moderator')

        self.assertEqual({
            'comment_author': 'Mike',
            'comment_author_email': 'mike@mail.loc',
            'comment_author_url': 'http://mike.example.com',
            'user_role': 'moderator',
        }, author.as_params())

    def test_from_django_user(self):
        author = Author.from_django_user(Mock(
            get_full_name=Mock(return_value='Mike Hoff'),
            email='mike@mail.loc',
            is_staff=True
        ))

        self.assertEqual('Mike Hoff', author.name)
        self.assertEqual('mike@mail.loc', author.email)
        self.assertEqual(None, author.url)
        self.assertEqual('administrator', author.role)


class SiteTests(TestCase):
    def test_to_params(self):
        site = Site('http://mike.example.com/', language_code='it')

        self.assertEqual({
            'blog': 'http://mike.example.com/',
            'blog_lang': 'it',
        }, site.as_params())


class CommentTests(TestCase):
    def test_to_params(self):
        comment = Comment('<my comment>', type='comment', permalink='http://mike.example.com/comment-1/')

        self.assertEqual({
            'comment_content': '<my comment>',
            'comment_date': comment.created.timestamp(),
            'comment_type': 'comment',
            'permalink': 'http://mike.example.com/comment-1/',
        }, comment.as_params())

    def test_to_params_related_resources(self):
        author = Author('Mike', 'mike@mail.loc', 'http://mike.example.com', role='moderator')
        site = Site('http://mike.example.com/', language_code='it')

        comment = Comment('<my comment>', author=author, site=site)

        params = comment.as_params()

        self.assertLess(author.as_params().items(), params.items(), 'all author params should be in comment params')
        self.assertLess(site.as_params().items(), params.items(), 'all site params should be in comment params')
