
#                                 scala.Float                                 #

```scala
object Float extends AnyValCompanion
```

* Source
  * [Float.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Float.scala#L1)


--------------------------------------------------------------------------------
                         Value Members From scala.Float
--------------------------------------------------------------------------------


### `def box(x: Float): java.lang.Float`                                     ###

Transform a value type into a boxed reference type.

Runtime implementation determined by `scala.runtime.BoxesRunTime.boxToFloat` .
See
[src/library/scala/runtime/BoxesRunTime.java](https://github.com/scala/scala).

* x
  * the Float to be boxed
* returns
  * a java.lang.Float offering `x` as its underlying value.

(defined at scala.Float)


### `implicit def float2double(x: Float): Double`                            ###

(defined at scala.Float)


### `def unbox(x: AnyRef): Float`                                            ###

Transform a boxed type into a value type. Note that this method is not typesafe:
it accepts any Object, but will throw an exception if the argument is not a
java.lang.Float.

Runtime implementation determined by `scala.runtime.BoxesRunTime.unboxToFloat` .
See
[src/library/scala/runtime/BoxesRunTime.java](https://github.com/scala/scala).

* x
  * the java.lang.Float to be unboxed.
* returns
  * the Float resulting from calling floatValue() on `x`

* Exceptions thrown
  * ClassCastException if the argument is not a java.lang.Float
(defined at scala.Float)
