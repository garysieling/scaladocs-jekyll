
#                                 scala.Short                                 #

```scala
object Short extends AnyValCompanion
```

* Source
  * [Short.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Short.scala#L1)


--------------------------------------------------------------------------------
                         Value Members From scala.Short
--------------------------------------------------------------------------------


### `def box(x: Short): java.lang.Short`                                     ###

Transform a value type into a boxed reference type.

Runtime implementation determined by `scala.runtime.BoxesRunTime.boxToShort` .
See
[src/library/scala/runtime/BoxesRunTime.java](https://github.com/scala/scala).

* x
  * the Short to be boxed
* returns
  * a java.lang.Short offering `x` as its underlying value.

(defined at scala.Short)


### `implicit def short2double(x: Short): Double`                            ###

(defined at scala.Short)


### `implicit def short2float(x: Short): Float`                              ###

(defined at scala.Short)


### `implicit def short2int(x: Short): Int`                                  ###

(defined at scala.Short)


### `implicit def short2long(x: Short): Long`                                ###

(defined at scala.Short)


### `def unbox(x: AnyRef): Short`                                            ###

Transform a boxed type into a value type. Note that this method is not typesafe:
it accepts any Object, but will throw an exception if the argument is not a
java.lang.Short.

Runtime implementation determined by `scala.runtime.BoxesRunTime.unboxToShort` .
See
[src/library/scala/runtime/BoxesRunTime.java](https://github.com/scala/scala).

* x
  * the java.lang.Short to be unboxed.
* returns
  * the Short resulting from calling shortValue() on `x`

* Exceptions thrown
  * ClassCastException if the argument is not a java.lang.Short
(defined at scala.Short)
