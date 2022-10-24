from setuptools import setup


with open('README.md', encoding='utf-8') as file:
    readme = file.read()

setup(
    name='tempyrature',
    version='1.0.1',
    description='A simple temperature converter.',
    long_description=readme,
    author='Lobooooooo14',
    url='https://github.com/lobooooooo14/tempyrature',
    packages=['tempyrature'],
    license='Apache License 2.0',
    long_description_content_type='text/markdown',
    project_urls={
        'Github': 'https://github.com/lobooooooo14/tempyrature'
    },
    keywords=['scale', 'conversor', 'temperature'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ]
)