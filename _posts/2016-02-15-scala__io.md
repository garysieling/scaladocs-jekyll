
#                                   scala.io                                   #

```scala
package io
```


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `trait AnsiColor extends AnyRef`                                         ###

* Source
  * [AnsiColor.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/io/AnsiColor.scala#L1)


### `class BufferedSource extends Source`                                    ###

This object provides convenience methods to create an iterable representation of
a source file.

* Source
  * [BufferedSource.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/io/BufferedSource.scala#L1)


### `class Codec extends AnyRef`                                             ###

A class for character encoding/decoding preferences.

* Source
  * [Codec.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/io/Codec.scala#L1)


### `trait LowPriorityCodecImplicits extends AnyRef`                         ###

* Self Type
  * Codec.type
* Source
  * [Codec.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/io/Codec.scala#L1)


### `abstract class Source extends Iterator[Char] with Closeable`            ###

An iterable representation of source data. It may be reset with the optional
 `reset` method.

Subclasses must supply the underlying iterator.

Error handling may be customized by overriding the report method.

The current input and position, as well as the next character methods delegate
to the positioner.

The default positioner encodes line and column numbers in the position passed to
 `report` . This behavior can be changed by supplying a custom positioner.

* Source
  * [Source.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/io/Source.scala#L1)
* Version
  * 1.0


--------------------------------------------------------------------------------
                                 Value Members
--------------------------------------------------------------------------------


### `object AnsiColor extends AnsiColor`                                     ###

* Source
  * [AnsiColor.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/io/AnsiColor.scala#L1)


### `object Codec extends LowPriorityCodecImplicits`                         ###

* Source
  * [Codec.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/io/Codec.scala#L1)


### `object Source`                                                          ###

This object provides convenience methods to create an iterable representation of
a source file.

* Source
  * [Source.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/io/Source.scala#L1)
* Version
  * 1.0, 19/08/2004


### `object StdIn extends StdIn`                                             ###

* Source
  * [StdIn.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/io/StdIn.scala#L1)

