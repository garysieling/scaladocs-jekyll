
#                                  scala.Unit                                  #

```scala
object Unit extends AnyValCompanion
```

* Source
  * [Unit.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Unit.scala#L1)


--------------------------------------------------------------------------------
                         Value Members From scala.Unit
--------------------------------------------------------------------------------


### `def box(x: Unit): BoxedUnit`                                            ###

Transform a value type into a boxed reference type.

* x
  * the Unit to be boxed
* returns
  * a scala.runtime.BoxedUnit offering `x` as its underlying value.

(defined at scala.Unit)


### `def unbox(x: AnyRef): Unit`                                             ###

Transform a boxed type into a value type. Note that this method is not typesafe:
it accepts any Object, but will throw an exception if the argument is not a
scala.runtime.BoxedUnit.

* x
  * the scala.runtime.BoxedUnit to be unboxed.
* returns
  * the Unit value ()

* Exceptions thrown
  * ClassCastException if the argument is not a scala.runtime.BoxedUnit
(defined at scala.Unit)
