
#                                scala.io.Codec                                #

```scala
class Codec extends AnyRef
```

A class for character encoding/decoding preferences.

* Source
  * [Codec.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/io/Codec.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Configure[T] = ((T) ⇒ T, Boolean)`                                 ###


### `type Handler = (CharacterCodingException) ⇒ Int`                        ###


--------------------------------------------------------------------------------
                   Instance Constructors From scala.io.Codec
--------------------------------------------------------------------------------


### `new Codec(charSet: Charset)`                                            ###

(defined at scala.io.Codec)


--------------------------------------------------------------------------------
                       Value Members From scala.io.Codec
--------------------------------------------------------------------------------


### `val charSet: Charset`                                                   ###

(defined at scala.io.Codec)


### `def decoder: CharsetDecoder`                                            ###

(defined at scala.io.Codec)


### `def decodingReplaceWith(newReplacement: String): Codec.this.type`       ###

(defined at scala.io.Codec)


### `def encoder: CharsetEncoder`                                            ###

(defined at scala.io.Codec)


### `def encodingReplaceWith(newReplacement: Array[Byte]): Codec.this.type`  ###

(defined at scala.io.Codec)


### `def onCodingException(handler: Handler): Codec.this.type`               ###

(defined at scala.io.Codec)


### `def onMalformedInput(newAction: CodingErrorAction): Codec.this.type`    ###

(defined at scala.io.Codec)


### `def onUnmappableCharacter(newAction: CodingErrorAction): Codec.this.type` ###

(defined at scala.io.Codec)


### `def wrap(body: ⇒ Int): Int`                                             ###
(defined at scala.io.Codec)
