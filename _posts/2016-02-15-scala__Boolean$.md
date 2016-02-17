
#                                scala.Boolean                                #

```scala
object Boolean extends AnyValCompanion
```

* Source
  * [Boolean.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Boolean.scala#L1)


--------------------------------------------------------------------------------
                        Value Members From scala.Boolean
--------------------------------------------------------------------------------


### `def box(x: Boolean): java.lang.Boolean`                                 ###

Transform a value type into a boxed reference type.

Runtime implementation determined by `scala.runtime.BoxesRunTime.boxToBoolean` .
See
[src/library/scala/runtime/BoxesRunTime.java](https://github.com/scala/scala).

* x
  * the Boolean to be boxed
* returns
  * a java.lang.Boolean offering `x` as its underlying value.

(defined at scala.Boolean)


### `def unbox(x: AnyRef): Boolean`                                          ###

Transform a boxed type into a value type. Note that this method is not typesafe:
it accepts any Object, but will throw an exception if the argument is not a
java.lang.Boolean.

Runtime implementation determined by
 `scala.runtime.BoxesRunTime.unboxToBoolean` . See
[src/library/scala/runtime/BoxesRunTime.java](https://github.com/scala/scala).

* x
  * the java.lang.Boolean to be unboxed.
* returns
  * the Boolean resulting from calling booleanValue() on `x`

* Exceptions thrown
  * ClassCastException if the argument is not a java.lang.Boolean
(defined at scala.Boolean)
