from HTMLParser import HTMLParser

tab = 0

def report(data, tab):
  if (data.strip() == ''):
    return

  if (data == '(object)'):
    print "<img class='object' />"
    return
  if (data == '(trait)'):
    print "<img class='trait' />"
    return
  if (data == '(class)'):
    print "<img class='class' />"
    return
  if (data == '(case class)'):
    print "<img class='case-class' />"
    return
  
  result = ''
  for x in range(tab):
    result = result + '  '

  result = result + data
  if (tab % 2 == 1):
    print "<h2 class='package'>" + data + "</h2>"
    return
  if (tab % 2 == 0):
    print "<h3 class='package-member'>" + data + "</h2>"
    return

  print tab
  print(result)

class MyHTMLParser(HTMLParser):
  tab = 0
  def handle_starttag(self, tag, attrs):
    self.tab = self.tab + 1
  #  report(tag, tab)
  def handle_endtag(self, tag):
    self.tab = self.tab - 1
  #  report(tag, self.tab)
  def handle_data(self, data):
    report(data, self.tab)

file = 'nav.html'
myfile = open(file, 'r')
content = myfile.read()

parser = MyHTMLParser()
parser.feed(content)

