#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys
import os
import yattag

doc, tag, text = yattag.Doc().tagtext()

def generate_url(d, f):
    return 'http://htmlpreview.github.io/?https://github.com/sion567/words/blob/main/%s/%s' % (d, f)


def read_dir(path):
    files = os.listdir(path)
    files.sort()
    filtered = [
        f for f in files
        if f != ".git" and not f.startswith('.') and os.path.isdir(os.path.join(path, f))
    ]
    return filtered

def read_file(path, all_files):
    files = os.listdir(path)
    files.sort()
    for f in files:
        all_files.append(f)
    return all_files

dirs = read_dir(".")
with tag('html'):
    for dir in dirs:
        with tag('h4'):
            text(dir)
        files = read_file(os.path.join(".", dir), [])
        for file in files:
            url=generate_url(dir, file)
            with tag('a', target='_blank', style='text-decoration:none', rel='noopener norefferrer', href=url):
                text(file[:8])
            doc.stag('br')

print(doc.getvalue())