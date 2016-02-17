
#                             scala.text.Document                             #

```scala
object Document
```

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ This object will be removed.
* Source
  * [Document.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/text/Document.scala#L1)


--------------------------------------------------------------------------------
                     Value Members From scala.text.Document
--------------------------------------------------------------------------------


### `def break: DocBreak.type`                                               ###

A break, which will either be turned into a space or a line break

(defined at scala.text.Document)


### `def empty: DocNil.type`                                                 ###

The empty document

(defined at scala.text.Document)


### `def group(d: Document): Document`                                       ###

A group, whose components will either be printed with all breaks rendered as
spaces, or with all breaks rendered as line breaks.

(defined at scala.text.Document)


### `def nest(i: Int, d: Document): Document`                                ###

A nested document, which will be indented as specified.

(defined at scala.text.Document)


### `def text(s: String): Document`                                          ###

A document consisting of some text literal
(defined at scala.text.Document)
