
#                                scala.util.Try                                #

```scala
object Try extends Serializable
```

* Source
  * [Try.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/Try.scala#L1)


--------------------------------------------------------------------------------
                       Value Members From scala.util.Try
--------------------------------------------------------------------------------


### `def apply[T](r: ⇒ T): Try[T]`                                           ###

Constructs a `Try` using the by-name parameter. This method will ensure any
non-fatal exception is caught and a `Failure` object is returned.
(defined at scala.util.Try)
