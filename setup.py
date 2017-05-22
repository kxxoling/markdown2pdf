from setuptools import setup


def fread(filepath):
    with open(filepath, 'r') as f:
        return f.read()


setup(
    name='Markdown2PDF',
    version='0.1.3',
    url='https://github.com/kxxoling/markdown2pdf',
    license='MIT',
    author='Kane Blueriver',
    author_email='kxxoling@gmail.com',
    description='A tool converts Markdown file to PDF, '
                'originally designed for developers\' resume release.',
    long_description=fread('README.rst'),
    packages=['markdown2pdf'],
    package_data={'markdown2pdf': ['themes/*']},
    zip_safe=False,
    platforms='any',
    install_requires=[
        'weasyprint',
        'markdown2',
    ],
    entry_points={
        'console_scripts': [
            'md2pdf = markdown2pdf:main',
        ]
    },
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
