
#                        scala.reflect.NameTransformer                        #

```scala
object NameTransformer
```

Provides functions to encode and decode Scala symbolic names. Also provides some
constants.

* Source
  * [NameTransformer.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/reflect/NameTransformer.scala#L1)


--------------------------------------------------------------------------------
                Value Members From scala.reflect.NameTransformer
--------------------------------------------------------------------------------


### `def decode(name0: String): String`                                      ###

Replace `$opname` by corresponding operator symbol.

* name0
  * the string to decode
* returns
  * the string with all recognized operator symbol encodings replaced with their
    name

(defined at scala.reflect.NameTransformer)


### `def encode(name: String): String`                                       ###

Replace operator symbols by corresponding `$opname` .

* name
  * the string to encode
* returns
  * the string with all recognized opchars replaced with their encoding
(defined at scala.reflect.NameTransformer)
