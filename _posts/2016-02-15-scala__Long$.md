
#                                  scala.Long                                  #

```scala
object Long extends AnyValCompanion
```

* Source
  * [Long.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Long.scala#L1)


--------------------------------------------------------------------------------
                         Value Members From scala.Long
--------------------------------------------------------------------------------


### `def box(x: Long): java.lang.Long`                                       ###

Transform a value type into a boxed reference type.

Runtime implementation determined by `scala.runtime.BoxesRunTime.boxToLong` .
See
[src/library/scala/runtime/BoxesRunTime.java](https://github.com/scala/scala).

* x
  * the Long to be boxed
* returns
  * a java.lang.Long offering `x` as its underlying value.

(defined at scala.Long)


### `implicit def long2double(x: Long): Double`                              ###

(defined at scala.Long)


### `implicit def long2float(x: Long): Float`                                ###

(defined at scala.Long)


### `def unbox(x: AnyRef): Long`                                             ###

Transform a boxed type into a value type. Note that this method is not typesafe:
it accepts any Object, but will throw an exception if the argument is not a
java.lang.Long.

Runtime implementation determined by `scala.runtime.BoxesRunTime.unboxToLong` .
See
[src/library/scala/runtime/BoxesRunTime.java](https://github.com/scala/scala).

* x
  * the java.lang.Long to be unboxed.
* returns
  * the Long resulting from calling longValue() on `x`

* Exceptions thrown
  * ClassCastException if the argument is not a java.lang.Long
(defined at scala.Long)
