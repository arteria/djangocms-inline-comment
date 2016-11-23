========================
djangocms-inline-comment
========================

**django CMS Inline Comment** is a plugin for `django CMS <http://django-cms.org>`_ that allows you to add comments to the structure board, visible to editors only. You can nest other plugins inside an inline comment, which renders them invisible on a published page.

(If you are looking for a plugin for public-facing comments, please have a look at https://github.com/Nekmo/djangocms-comments, https://github.com/aldryn/aldryn-disqus, or https://github.com/mishbahr/djangocms-fbcomments.)

Installation
------------

* run ``pip install djangocms-inline-comment``
* add ``'djangocms_inline_comment'`` to your ``INSTALLED_APPS``
* run ``python manage.py migrate djangocms_inline_comment``


Running Tests
-------------

You can run tests by executing::

    virtualenv env
    source env/bin/activate
    pip install -r requirements-test.txt
    python setup.py test
