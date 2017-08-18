import pyperclip

def getHeaders():

  headers = []

  head = raw_input('Row Header: ')

  while head != '':
    headers.append(head)
    head = raw_input('Row Header: ')

  return headers

def getRows(size):

  size = int(raw_input('Entries: '))

  return [[0 for x in range(len(headers))] for y in range(size)]

def makeDFSTable(title, headers, rows):

  out = ''

  for i in range(len(headers)):
    print headers[i]
    for j in range(len(rows)):
      print rows[j]
      item = raw_input('%s %s: ' % (headers[i], (j + 1)))
      if item == '':
        item = '-'
      elif item == 'whip':
        item = 'This wicked whip can attack a whole group of enemies at once'
      elif item == 'boomerang':
        item = 'The winged weapon can be used to attack all enemies at once'
      elif item == 'med':
        item = 'Restores 30-40HP to one target'
      elif item == 'anti':
        item = 'Removes the Poisoned and Envenomated state'
      elif item == 'moon':
        item = 'Removes the Paralyzed state'
      rows[j][i] = item

  out += """<table>
  <tr>
      <th colspan="%s">%s</th>
  </tr>
  <tr>\n""" % (len(headers), title)

  for head in headers:
    out += "    <th>%s</th>\n" % head
  out += "  </tr>\n"

  for row in rows:
    out += "  <tr>\n"
    for item in row:
      out += "    <td>%s</td>\n" % item
    out += "  </tr>\n"
  out += "</table>\n"

  return out

def makeBFSTable(title, headers, rows):

  out = ''

  for i in range(len(rows)):
    for j in range(len(headers)):
      item = raw_input('%s: ' % (headers[j]))
      if item == '':
        item = '-'
      elif item == 'med':
        item = 'Restores 30-40HP to one target'
      elif item == 'anti':
        item = 'Cures Poison for one character'
      elif item == 'holy':
        item = 'When used on the field, avoids battles with low level enemies, When used in battle deals 10-15 damage to a single enemy'
      elif item == 'moon':
        item = 'Cures Sleep and Paralysis for one character'
      elif item == 'chim':
        item = 'Allows you to teleport to any town and some dungeons that you have already visited.'
      elif item == 'amor':
        item = 'Restores 70-90HP for one character'
      elif item == 'whip':
        item = 'Attacks all enemies in a group'
      elif item == 'boom':
        item = 'Causes damage to all enemies'
      rows[i][j] = item

  out += """<table>
  <tr>
      <th colspan="%s">%s</th>
  </tr>
  <tr>\n""" % (len(headers), title)

  for head in headers:
    out += "    <th>%s</th>\n" % head
  out += "  </tr>\n"

  for row in rows:
    out += "  <tr>\n"
    for item in row:
      out += "    <td>%s</td>\n" % item
    out += "  </tr>\n"
  out += "</table>\n"

  return out

title = raw_input('Table Title: ')

headers = getHeaders()

rows = getRows(len(headers))

out = makeBFSTable(title, headers, rows)

pyperclip.copy(out)
print 'Table in clipboard'
