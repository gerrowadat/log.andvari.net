#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Dave O\'Connor'
SITENAME = u'log.andvari.net'
SITEURL = 'http://localhost:8888'

THEME = 'theme'

TIMEZONE = 'Europe/Dublin'

DEFAULT_LANG = u'en'

STATIC_PATHS = ['static', 'images']

#PLUGIN_PATHS = ['plugins']
PLUGINS = ['thumbnailer']
# 'optimize_images'

# Thumbnailer
IMAGE_PATH = 'images'
THUMBNAIL_DIR = 'images/thumbs'
THUMBNAIL_KEEP_NAME = True

TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100

DISQUS_SITENAME = 'andvarilog'
TWITTER_USERNAME = 'gerrowadat'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('About', '/pages/about.html'),
          ('GitHub', 'http://github.com/gerrowadat'),)

# Social widget
SOCIAL = (('twitter', 'http://www.twitter.com/gerrowadat'),
        ('linkedin', 'http://ie.linkedin.com/in/gerrowadat/'),)

DEFAULT_PAGINATION = 5
