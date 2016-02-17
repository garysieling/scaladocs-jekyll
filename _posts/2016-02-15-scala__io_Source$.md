
#                               scala.io.Source                               #

```scala
object Source
```

This object provides convenience methods to create an iterable representation of
a source file.

* Source
  * [Source.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/io/Source.scala#L1)
* Version
  * 1.0, 19/08/2004


--------------------------------------------------------------------------------
                       Value Members From scala.io.Source
--------------------------------------------------------------------------------


### `def createBufferedSource(inputStream: InputStream, bufferSize: Int = DefaultBufSize, reset: () ⇒ Source = null, close: () ⇒ Unit = null)(implicit codec: Codec): BufferedSource` ###

Reads data from inputStream with a buffered reader, using the encoding in
implicit parameter codec.

* inputStream
  * the input stream from which to read
* bufferSize
  * buffer size (defaults to Source.DefaultBufSize)
* reset
  * a () => Source which resets the stream (if unset, reset() will throw an
    Exception)
* close
  * a () => Unit method which closes the stream (if unset, close() will do
    nothing)
* codec
  * (implicit) a scala.io.Codec specifying behavior (defaults to Codec.default)
* returns
  * the buffered source

(defined at scala.io.Source)


### `def fromBytes(bytes: Array[Byte])(implicit codec: Codec): Source`       ###

Create a `Source` from array of bytes, decoding the bytes according to codec.

* returns
  * the created `Source` instance.

(defined at scala.io.Source)


### `def fromBytes(bytes: Array[Byte], enc: String): Source`                 ###

(defined at scala.io.Source)


### `def fromChar(c: Char): Source`                                          ###

Creates a Source instance from a single character.

(defined at scala.io.Source)


### `def fromChars(chars: Array[Char]): Source`                              ###

creates Source from array of characters, with empty description.

(defined at scala.io.Source)


### `def fromFile(file: File)(implicit codec: Codec): BufferedSource`        ###

creates Source from file, using default character encoding, setting its
description to filename.

(defined at scala.io.Source)


### `def fromFile(file: File, bufferSize: Int)(implicit codec: Codec): BufferedSource` ###

Creates Source from `file` , using given character encoding, setting its
description to filename. Input is buffered in a buffer of size `bufferSize` .

(defined at scala.io.Source)


### `def fromFile(file: File, enc: String): BufferedSource`                  ###

same as fromFile(file, enc, Source.DefaultBufSize)

(defined at scala.io.Source)


### `def fromFile(file: File, enc: String, bufferSize: Int): BufferedSource` ###

(defined at scala.io.Source)


### `def fromFile(name: String)(implicit codec: Codec): BufferedSource`      ###

creates Source from file with given name, setting its description to filename.

(defined at scala.io.Source)


### `def fromFile(name: String, enc: String): BufferedSource`                ###

creates Source from file with given name, using given encoding, setting its
description to filename.

(defined at scala.io.Source)


### `def fromFile(uri: URI)(implicit codec: Codec): BufferedSource`          ###

creates `ource` from file with given file `URI` .

(defined at scala.io.Source)


### `def fromFile(uri: URI, enc: String): BufferedSource`                    ###

creates Source from file with given file: URI

(defined at scala.io.Source)


### `def fromInputStream(is: InputStream)(implicit codec: Codec): BufferedSource` ###

(defined at scala.io.Source)


### `def fromInputStream(is: InputStream, enc: String): BufferedSource`      ###

(defined at scala.io.Source)


### `def fromIterable(iterable: Iterable[Char]): Source`                     ###

Creates a Source from an Iterable.

* iterable
  * the Iterable
* returns
  * the Source

(defined at scala.io.Source)


### `def fromRawBytes(bytes: Array[Byte]): Source`                           ###

Create a `Source` from array of bytes, assuming one byte per character
(ISO-8859-1 encoding.)

(defined at scala.io.Source)


### `def fromResource(resource: String, classLoader: ClassLoader = ...)(implicit codec: Codec): BufferedSource` ###

Reads data from a classpath resource, using either a context classloader
(default) or a passed one.

* resource
  * name of the resource to load from the classpath
* classLoader
  * classloader to be used, or context classloader if not specified
* returns
  * the buffered source

(defined at scala.io.Source)


### `def fromString(s: String): Source`                                      ###

creates Source from a String, with no description.

(defined at scala.io.Source)


### `def fromURI(uri: URI)(implicit codec: Codec): BufferedSource`           ###

creates `Source` from file with given file: URI

(defined at scala.io.Source)


### `def fromURL(s: String)(implicit codec: Codec): BufferedSource`          ###

same as fromURL(new URL(s))

(defined at scala.io.Source)


### `def fromURL(s: String, enc: String): BufferedSource`                    ###

same as fromURL(new URL(s))(Codec(enc))

(defined at scala.io.Source)


### `def fromURL(url: URL)(implicit codec: Codec): BufferedSource`           ###

same as fromInputStream(url.openStream())(codec)

(defined at scala.io.Source)


### `def fromURL(url: URL, enc: String): BufferedSource`                     ###

same as fromInputStream(url.openStream())(Codec(enc))

(defined at scala.io.Source)


### `def stdin: BufferedSource`                                              ###

Creates a `Source` from System.in.
(defined at scala.io.Source)
