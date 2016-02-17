
#                                  scala.Char                                  #

```scala
object Char extends AnyValCompanion
```

* Source
  * [Char.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Char.scala#L1)


--------------------------------------------------------------------------------
                         Value Members From scala.Char
--------------------------------------------------------------------------------


### `def box(x: Char): Character`                                            ###

Transform a value type into a boxed reference type.

Runtime implementation determined by
 `scala.runtime.BoxesRunTime.boxToCharacter` . See
[src/library/scala/runtime/BoxesRunTime.java](https://github.com/scala/scala).

* x
  * the Char to be boxed
* returns
  * a java.lang.Character offering `x` as its underlying value.

(defined at scala.Char)


### `implicit def char2double(x: Char): Double`                              ###

(defined at scala.Char)


### `implicit def char2float(x: Char): Float`                                ###

(defined at scala.Char)


### `implicit def char2int(x: Char): Int`                                    ###

(defined at scala.Char)


### `implicit def char2long(x: Char): Long`                                  ###

(defined at scala.Char)


### `def unbox(x: AnyRef): Char`                                             ###

Transform a boxed type into a value type. Note that this method is not typesafe:
it accepts any Object, but will throw an exception if the argument is not a
java.lang.Character.

Runtime implementation determined by `scala.runtime.BoxesRunTime.unboxToChar` .
See
[src/library/scala/runtime/BoxesRunTime.java](https://github.com/scala/scala).

* x
  * the java.lang.Character to be unboxed.
* returns
  * the Char resulting from calling charValue() on `x`

* Exceptions thrown
  * ClassCastException if the argument is not a java.lang.Character
(defined at scala.Char)
