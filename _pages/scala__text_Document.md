
#                             scala.text.Document                             #

```scala
abstract class Document extends AnyRef
```

A basic pretty-printing library, based on Lindig's strict version of Wadler's
adaptation of Hughes' pretty-printer.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ This class will be removed.
* Source
  * [Document.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/text/Document.scala#L1)
* Version
  * 1.0


--------------------------------------------------------------------------------
                 Instance Constructors From scala.text.Document
--------------------------------------------------------------------------------


### `new Document()`                                                         ###

(defined at scala.text.Document)


--------------------------------------------------------------------------------
                     Value Members From scala.text.Document
--------------------------------------------------------------------------------


### `def :/:(hd: Document): Document`                                        ###

(defined at scala.text.Document)


### `def :/:(hd: String): Document`                                          ###

(defined at scala.text.Document)


### `def ::(hd: Document): Document`                                         ###

(defined at scala.text.Document)


### `def ::(hd: String): Document`                                           ###

(defined at scala.text.Document)


### `def format(width: Int, writer: Writer): Unit`                           ###

Format this document on `writer` and try to set line breaks so that the result
fits in `width` columns.
(defined at scala.text.Document)
