import sys
import requests
import ssl

file = "2016-02-15-scala__util_control_Breaks_TryBlock.md"

def run(file):
  contents = ""

  with open(file, 'r') as myfile:
    contents=myfile.read().replace('\n', '\n')

  titleparts = contents.split("\n")[1][1:-1].strip().split("#")
  title = ""
  subtitle = ""

  try:
    title = titleparts[1]
  except:
    try:
      title = titleparts[0]
    except:
      print("no title")

  try: 
    subtitle = titleparts[0]
  except:
    print("no subtitle")
  category = subtitle
  tags = " ".join(["scala", title, subtitle])
  code = ""

  template = """---
layout: post
title:  "$title"
tags: $tags
category: $category
---

$contents

{% highlight scala %}
$code
{% endhighlight %}"""

  # url = "https://raw.githubusercontent.com/scala/scala/6d09a1ba5fffadd1d886afb66ab4496291fda3dd/src/library/scala/util/control/Breaks.scala"
  #        https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/control/Breaks.scala#L1
  #        https://raw.githubusercontent.com/scala/scala/6d09a1ba5f/src/library/scala/util/control/Breaks.scala#L1
  import re
  urlregex = re.compile(r'github.com([^)]*)')
  match = urlregex.search(contents)

  if match:
    url = "https://raw.githubusercontent.com" + str.replace(match.group(1), "/tree/", "/")
    code = requests.get(url).content
    
    code = str.replace(code, "{", "&#123;")
    code = str.replace(code, "}", "&#125;")

  endmatch = re.compile(r'\s+#{1,10}\n')
  contents = re.sub(endmatch, "\n", contents)

  blockmatch = re.compile('([-]+)\n\s+(.*)\n([-])+\n')
  contents = re.sub(blockmatch, "####\\2\n", contents)

  codematch = re.compile('```scala\n([^`]*)```\n')
  contents = re.sub(codematch, "{% highlight scala %}\n\\1{% endhighlight %}", contents)

  # replace duplicated things

  replaced = \
    str.replace(
      str.replace(
        str.replace(
          str.replace(
            str.replace(template, "$title", title),
            "$tags", tags,
          ), "$category", category,
        ), "$code", code,
      ), "$contents", contents)

  print("writing " + file)
  fout = open("_posts/" + str.replace(file, "_pre/", ""), "w+")
  fout.write(replaced)
  fout.close()

import glob, os
for file in glob.glob("_pre/*.md"):
#  try:
  run(file)
#  except:
#    print "Unexpected error:", sys.exc_info()[0]

