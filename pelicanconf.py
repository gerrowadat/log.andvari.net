#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Dave O\'Connor'
SITENAME = u'log.andvari.net'
SITEURL = 'http://localhost:8888'

THEME = 'themes/zurb-F5-basic'

TIMEZONE = 'Europe/Dublin'

DEFAULT_LANG = u'en'

STATIC_PATHS = ['static', 'images', 'favicon']

EXTRA_PATH_METADATA = {
        'favicon/favicon.ico': {'path': 'favicon.ico'},
        'favicon/site.webmanifest': {'path': 'site.webmanifest'},
        'favicon/android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},
        'favicon/android-chrome-512x512.png': {'path': 'android-chrome-512x512.png'},
        'favicon/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
        'favicon/favicon-16x16.png': {'path': 'favicon-16x16.png'},
        'favicon/favicon-32x32.png': {'path': 'favicon-32x32.png'},
}

#PLUGIN_PATHS = ['plugins']
PLUGINS = ['thumbnailer']
# 'optimize_images'

# Thumbnailer
IMAGE_PATH = 'images'
THUMBNAIL_DIR = 'images/thumbs'
THUMBNAIL_KEEP_NAME = True

TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('About', '/pages/about.html'),
          ('GitHub', 'http://github.com/gerrowadat'),)

# Social widget
SOCIAL = (('@gerrowadat@mastodon.ie', 'https://mastodon.ie/@gerrowadat'),
        ('@gerrowadat.bsky.social', 'https://bsky.app/profile/gerrowadat.bsky.social'),
        ('linkedin', 'http://ie.linkedin.com/in/gerrowadat/'),)

DEFAULT_PAGINATION = 5
