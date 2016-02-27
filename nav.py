from HTMLParser import HTMLParser

tab = 0

print "<h4 class='package'><a href='/scaladoc/scala/2016/02/15/scala.html'>Root Package</a></h4>"
print "<ol class='list-unstyled'>"

package = ''

def report(data, tab):
  global package
  if (data.strip() == ''):
    return

  if (data == '(object)'):
    #print "<img class='object' />"
    return
  if (data == '(trait)'):
    #print "<img class='trait' />"
    return
  if (data == '(class)'):
    #print "<img class='class' />"
    return
  if (data == '(case class)'):
    #print "<img class='case-class' />"
    return
  
  result = ''
  for x in range(tab):
    result = result + '  '

  result = result + data

  if (tab % 2 == 1):
    package = str.replace(data, "scala.", "")

    filename = package 
    filename = str.replace( str.replace(filename, "scala.", "scala__"), ".", "_" )

    url = "/scaladoc/scala." + package + "/2016/02/15/scala_" + filename + ".html"

    print "</ol><h4 class='package'><a href='" + url + "'>" + data + "</a></h4><ol class='list-unstyled'>"
    return
  if (tab % 2 == 0):
    cls = data
    if (package != ""):
      filename = package + "." + cls
    else:
      filename = cls

    filename = str.replace(filename, ".", "_" ) 
    href = "/scaladoc/scala." + package + cls + "/2016/02/15/scala__" + filename + ".html"
    print "<li class='package-member'><a href='" + href + "'>" + data + "</a></li>"
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
print("</ol>")
