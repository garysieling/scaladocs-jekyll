
#                                  scala.Int                                  #

```scala
object Int extends AnyValCompanion
```

* Source
  * [Int.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Int.scala#L1)


--------------------------------------------------------------------------------
                          Value Members From scala.Int
--------------------------------------------------------------------------------


### `def box(x: Int): Integer`                                               ###

Transform a value type into a boxed reference type.

Runtime implementation determined by `scala.runtime.BoxesRunTime.boxToInteger` .
See
[src/library/scala/runtime/BoxesRunTime.java](https://github.com/scala/scala).

* x
  * the Int to be boxed
* returns
  * a java.lang.Integer offering `x` as its underlying value.

(defined at scala.Int)


### `implicit def int2double(x: Int): Double`                                ###

(defined at scala.Int)


### `implicit def int2float(x: Int): Float`                                  ###

(defined at scala.Int)


### `implicit def int2long(x: Int): Long`                                    ###

(defined at scala.Int)


### `def unbox(x: AnyRef): Int`                                              ###

Transform a boxed type into a value type. Note that this method is not typesafe:
it accepts any Object, but will throw an exception if the argument is not a
java.lang.Integer.

Runtime implementation determined by `scala.runtime.BoxesRunTime.unboxToInt` .
See
[src/library/scala/runtime/BoxesRunTime.java](https://github.com/scala/scala).

* x
  * the java.lang.Integer to be unboxed.
* returns
  * the Int resulting from calling intValue() on `x`

* Exceptions thrown
  * ClassCastException if the argument is not a java.lang.Integer
(defined at scala.Int)
