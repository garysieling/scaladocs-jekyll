
#                              scala.text.DocText                              #

```scala
case class DocText(txt: String) extends Document with Product with Serializable
```

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ This class will be removed.
* Source
  * [Document.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/text/Document.scala#L1)


--------------------------------------------------------------------------------
                 Instance Constructors From scala.text.DocText
--------------------------------------------------------------------------------


### `new DocText(txt: String)`                                               ###

(defined at scala.text.DocText)


--------------------------------------------------------------------------------
                     Value Members From scala.text.Document
--------------------------------------------------------------------------------


### `def :/:(hd: Document): Document`                                        ###

* Definition Classes
  * Document

(defined at scala.text.Document)


### `def :/:(hd: String): Document`                                          ###

* Definition Classes
  * Document

(defined at scala.text.Document)


### `def ::(hd: Document): Document`                                         ###

* Definition Classes
  * Document

(defined at scala.text.Document)


### `def ::(hd: String): Document`                                           ###

* Definition Classes
  * Document

(defined at scala.text.Document)


### `def format(width: Int, writer: Writer): Unit`                           ###

Format this document on `writer` and try to set line breaks so that the result
fits in `width` columns.

* Definition Classes
  * Document
(defined at scala.text.Document)
