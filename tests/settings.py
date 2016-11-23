#!/usr/bin/env python
# -*- coding: utf-8 -*-

HELPER_SETTINGS = dict(
    INSTALLED_APPS=[
        'djangocms_text_ckeditor',
    ],
    CMS_LANGUAGES={
        1: [{
            'code': 'en',
            'name': 'English',
        }]
    },
    LANGUAGE_CODE='en',
)


def run():
    from djangocms_helper import runner
    runner.cms('djangocms_inline_comment')

if __name__ == '__main__':
    run()
