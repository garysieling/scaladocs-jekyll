
#                                 scala.Double                                 #

```scala
object Double extends AnyValCompanion
```

* Source
  * [Double.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Double.scala#L1)


--------------------------------------------------------------------------------
                        Value Members From scala.Double
--------------------------------------------------------------------------------


### `def box(x: Double): java.lang.Double`                                   ###

Transform a value type into a boxed reference type.

Runtime implementation determined by `scala.runtime.BoxesRunTime.boxToDouble` .
See
[src/library/scala/runtime/BoxesRunTime.java](https://github.com/scala/scala).

* x
  * the Double to be boxed
* returns
  * a java.lang.Double offering `x` as its underlying value.

(defined at scala.Double)


### `def unbox(x: AnyRef): Double`                                           ###

Transform a boxed type into a value type. Note that this method is not typesafe:
it accepts any Object, but will throw an exception if the argument is not a
java.lang.Double.

Runtime implementation determined by `scala.runtime.BoxesRunTime.unboxToDouble` .
See
[src/library/scala/runtime/BoxesRunTime.java](https://github.com/scala/scala).

* x
  * the java.lang.Double to be unboxed.
* returns
  * the Double resulting from calling doubleValue() on `x`

* Exceptions thrown
  * ClassCastException if the argument is not a java.lang.Double
(defined at scala.Double)
