from setuptools import setup, find_packages

setup(
    name='django-antispam',
    version='0.1.0',
    description='Anti-spam protection tools for django applications.',

    install_requires=[
        'django',

        'python-akismet',
    ],

    packages=find_packages(exclude=['tests.*', 'tests']),

    test_suite='tests',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
