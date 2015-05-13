Markdown2PDF
============

Markdown2pdf is a command-line tool to convert markdown file into pdf,
was originally designed for myself to create resume.

.. image:: https://travis-ci.org/kxxoling/markdown2pdf.svg?branch=master
    :target: https://travis-ci.org/kxxoling/markdown2pdf
    :alt: Building Status

.. image:: https://landscape.io/github/kxxoling/markdown2pdf/master/landscape.svg?style=flat
    :target: https://landscape.io/github/kxxoling/markdown2pdf/master
    :alt: Code Health

.. image:: https://pypip.in/download/markdown2pdf/badge.svg?period=week
    :target: https://pypi.python.org/pypi/markdown2pdf/
    :alt: Downloads


Installation
------------

To install Markdown2PDF you may need to install PDF convertion tool first,

Install Markdown2PDF by pip:

.. code-block:: shell

    pip install markdown2pdf


Usage
-----

You can use Markdown2PDF via simple command ``md2pdf``:

.. code-block:: shell

    md2pdf resume.md

You can also appoint a theme by argument ``--theme``:

.. code-block:: shell

    md2pdf resume.md --theme=github

Or, you can even using your self defined theme:

.. code-block:: shell

    md2pdf resume.md --theme=path_to_style.css

By now, Markdown2PDF contains multi builtin themes:

* github (from GitHub.Inc)

* solarized-dark (from mixu/markdown-styles)

* ghostwriter (from mixu/markdown-styles)


Trouble shooting
----------------

1. ``ffi.h no such file or directory``

.. code-block:: shell

    apt-get install libffi-dev

2. ``OSError: library not found: 'libcairo.so.2'``

This means you need to get some requirements installed first, see this page:
[WeasyPrint fails with error on OSX](https://github.com/Kozea/WeasyPrint/issues/79).
