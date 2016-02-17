
#                                scala.io.Codec                                #

```scala
object Codec extends LowPriorityCodecImplicits
```

* Source
  * [Codec.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/io/Codec.scala#L1)


--------------------------------------------------------------------------------
                       Value Members From scala.io.Codec
--------------------------------------------------------------------------------


### `final val ISO8859: Codec`                                               ###

(defined at scala.io.Codec)


### `final val UTF8: Codec`                                                  ###

(defined at scala.io.Codec)


### `def apply(charSet: Charset): Codec`                                     ###

(defined at scala.io.Codec)


### `def apply(decoder: CharsetDecoder): Codec`                              ###

(defined at scala.io.Codec)


### `def apply(encoding: String): Codec`                                     ###

(defined at scala.io.Codec)


### `implicit def charset2codec(c: Charset): Codec`                          ###

(defined at scala.io.Codec)


### `implicit def decoder2codec(cd: CharsetDecoder): Codec`                  ###

(defined at scala.io.Codec)


### `def default: Codec`                                                     ###

(defined at scala.io.Codec)


### `def defaultCharsetCodec: Codec`                                         ###

Optimistically these two possible defaults will be the same thing. In practice
this is not necessarily true, and in fact Sun classifies the fact that you can
influence anything at all via -Dfile.encoding as an accident, with any anomalies
considered "not a bug".

(defined at scala.io.Codec)


### `def fileEncodingCodec: Codec`                                           ###

(defined at scala.io.Codec)


### `def fromUTF8(bytes: Array[Byte]): Array[Char]`                          ###

* Annotations
  * @migration
* Migration
  * _(Changed in version 2.9.0)_ This method was previously misnamed `toUTF8` .
    Converts from Array[Byte] to Array[Char].

(defined at scala.io.Codec)


### `def fromUTF8(bytes: Array[Byte], offset: Int, len: Int): Array[Char]`   ###

(defined at scala.io.Codec)


### `implicit def string2codec(s: String): Codec`                            ###

(defined at scala.io.Codec)


### `def toUTF8(chars: Array[Char], offset: Int, len: Int): Array[Byte]`     ###

(defined at scala.io.Codec)


### `def toUTF8(cs: CharSequence): Array[Byte]`                              ###

* Annotations
  * @migration
* Migration
  * _(Changed in version 2.9.0)_ This method was previously misnamed `fromUTF8` .
    Converts from character sequence to Array[Byte].

(defined at scala.io.Codec)


--------------------------------------------------------------------------------
             Value Members From scala.io.LowPriorityCodecImplicits
--------------------------------------------------------------------------------


### `implicit lazy val fallbackSystemCodec: Codec`                           ###

The Codec of Last Resort.

* Definition Classes
  * LowPriorityCodecImplicits
(defined at scala.io.LowPriorityCodecImplicits)
