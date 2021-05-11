#!/usr/bin/env python

import os
import re
import markdown
import requests
from bs4 import BeautifulSoup
from absl import app
from absl import flags


FLAGS = flags.FLAGS
flags.DEFINE_string('content_dir', 'content/', 'Markdown/image directory root')
flags.DEFINE_string('ignore_link_re', '.+?thumbs/thumb.+', 'RE for links ot ignore')


def verifyLink(path):
    if re.match(FLAGS.ignore_link_re, path):
        return (True, 'ignored by --ignore-link_re')

    if path.startswith('http'):
        try:
            # I would do head() but some web servers 403 it. *shrug*
            r = requests.get(path)
        except Exception as e:
            return (False, '[%s]: %s' % (path, str(e)))
        if r.status_code != 200:
            return (False, '[%s] %s' % (r.status_code, path))
        return (True, 'ok')
    elif path.startswith('/'):
        abspath = os.path.abspath('%s/%s' % (FLAGS.content_dir, path))
        if not os.path.exists(abspath):
            return (False, '[not found in %s]: %s' % (FLAGS.content_dir, path))
        return (True, 'ok')
    else:
        return (False, 'Not sure what to do with %s' % (path, ))

def verifyMarkdown(md_file):
    with open(md_file.path) as f:
        content = f.read()
    html = markdown.markdown(content)
    s = BeautifulSoup(html, 'html.parser')

    errors = []

    for a in s.find_all('a'):
        (ok, msg) = verifyLink(a.get('href'))
        if not ok:
            errors.append((md_file, msg),)

    for i in s.find_all('img'):
        (ok, msg) = verifyLink(i.get('src'))
        if not ok:
            errors.append((md_file, msg),)
    return errors

def main(argv):
  for f in os.scandir(path=FLAGS.content_dir):
      if f.path.endswith('.md'):
        errors = verifyMarkdown(f)
        if errors:
            for e in errors:
                print('%s: %s' % (e[0].path, e[1]))


if __name__ == '__main__':
    app.run(main)
