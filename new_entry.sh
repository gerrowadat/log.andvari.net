#!/bin/bash

TODAY=`date +20%y%m%d`
POST_DATE=`date +"%Y-%m-%d %H:%M"`
TITLE_DATE=`date +"%B %d %Y"`

CAPTION=$1

cat >>content/$TODAY.md <<EOF
Title: $TITLE_DATE
Tags: log 
Date: $POST_DATE 
Category: Log 
 
<a href="/images/$TODAY-$CAPTION.jpg">![Image](/images/thumbs/thumbnail_square/$TODAY-$CAPTION.jpg)</a>
 
Stuff

EOF

vim content/$TODAY.md
