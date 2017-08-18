import os

#start_dir = raw_input()

def renameContents(directory):
  for i in os.listdir(directory):
    path = '%s/%s' % (directory, i)
    if os.path.isdir(path):
      print 'New Path: %s' % path
      check = raw_input('Continue down path (Y/N): ')
      if check == 'Y':
        renameContents(path)
    else:
      renameFile(directory, i)

def renameFile(directory, file):
  print 'File: %s' % file
  ext = file[-4:]
  num = raw_input('Episode Number: ')
  if num != '':
    name = raw_input('Episode Title: ')
    os.rename('%s/%s' % (directory, file), '%s/%s - %s%s' % (directory, num, name, ext))

def renameDir():
  start_dir = raw_input('Starting Directory: ')
  for i in os.listdir(start_dir):
    path = '%s/%s' % (start_dir, i)
    if os.path.isdir(path):
      print 'New Path: %s' % path
      check = raw_input('Continue down path (Y/N): ')
      if check == 'Y':
        renameContents(path)
    else:
      renameFile(start_dir, i)

if __name__ == '__main__':
  renameDir()