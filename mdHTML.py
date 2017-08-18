from BeautifulSoup import BeautifulSoup as bs, Tag
import re, os, markdown2, lxml
from lxml.html.clean import Cleaner

orig_prettify = bs.prettify
r = re.compile(r'^(\s*)', re.MULTILINE)
def prettify(self, encoding=None, indent_width=2):
  return r.sub(r'\1' * indent_width, orig_prettify(self, encoding=encoding))
bs.prettify = prettify

def cleanFile(d, f):
  ext = f[-5:]

  if ext == '.html':

    og = open('%s/%s' % (d, f)).read()

    soup = bs(og)

    tag = Tag(soup, 'link', [('rel', 'stylesheet'),('href', 'md.css')])

    soup.head.link.extract()

    soup.head.style.replaceWith(tag)

    with open('%s/%s' % (d, f), 'w+') as out:
      out.write(str(soup))

def cleanDir(start_dir):
  for i in os.listdir(start_dir):
    cleanFile(start_dir, i)

if __name__ == '__main__':
  start = raw_input('Starting Directory: ')
  cleanDir(start)
