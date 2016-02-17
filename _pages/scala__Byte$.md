
#                                  scala.Byte                                  #

```scala
object Byte extends AnyValCompanion
```

* Source
  * [Byte.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Byte.scala#L1)


--------------------------------------------------------------------------------
                         Value Members From scala.Byte
--------------------------------------------------------------------------------


### `def box(x: Byte): java.lang.Byte`                                       ###

Transform a value type into a boxed reference type.

Runtime implementation determined by `scala.runtime.BoxesRunTime.boxToByte` .
See
[src/library/scala/runtime/BoxesRunTime.java](https://github.com/scala/scala).

* x
  * the Byte to be boxed
* returns
  * a java.lang.Byte offering `x` as its underlying value.

(defined at scala.Byte)


### `implicit def byte2double(x: Byte): Double`                              ###

(defined at scala.Byte)


### `implicit def byte2float(x: Byte): Float`                                ###

(defined at scala.Byte)


### `implicit def byte2int(x: Byte): Int`                                    ###

(defined at scala.Byte)


### `implicit def byte2long(x: Byte): Long`                                  ###

(defined at scala.Byte)


### `implicit def byte2short(x: Byte): Short`                                ###

(defined at scala.Byte)


### `def unbox(x: AnyRef): Byte`                                             ###

Transform a boxed type into a value type. Note that this method is not typesafe:
it accepts any Object, but will throw an exception if the argument is not a
java.lang.Byte.

Runtime implementation determined by `scala.runtime.BoxesRunTime.unboxToByte` .
See
[src/library/scala/runtime/BoxesRunTime.java](https://github.com/scala/scala).

* x
  * the java.lang.Byte to be unboxed.
* returns
  * the Byte resulting from calling byteValue() on `x`

* Exceptions thrown
  * ClassCastException if the argument is not a java.lang.Byte
(defined at scala.Byte)
