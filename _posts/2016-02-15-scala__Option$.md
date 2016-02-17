
#                                 scala.Option                                 #

```scala
object Option extends Serializable
```

* Source
  * [Option.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Option.scala#L1)


--------------------------------------------------------------------------------
                        Value Members From scala.Option
--------------------------------------------------------------------------------


### `def apply[A](x: A): Option[A]`                                          ###

An Option factory which creates Some(x) if the argument is not null, and None if
it is null.

* x
  * the value
* returns
  * Some(value) if value != null, None if value == null

(defined at scala.Option)


### `implicit def option2Iterable[A](xo: Option[A]): Iterable[A]`            ###

An implicit conversion that converts an option to an iterable value
(defined at scala.Option)
