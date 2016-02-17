
#                          scala.util.Try#WithFilter                          #

```scala
class WithFilter extends AnyRef
```

We need a whole WithFilter class to honor the "doesn't create a new collection"
contract even though it seems unlikely to matter much in a collection with max
size 1.

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.12")
* Source
  * [Try.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/Try.scala#L1)


--------------------------------------------------------------------------------
              Instance Constructors From scala.util.Try.WithFilter
--------------------------------------------------------------------------------


### `new WithFilter(p: (T) ⇒ Boolean)`                                       ###

(defined at scala.util.Try.WithFilter)


--------------------------------------------------------------------------------
                  Value Members From scala.util.Try.WithFilter
--------------------------------------------------------------------------------


### `def flatMap[U](f: (T) ⇒ Try[U]): Try[U]`                                ###

(defined at scala.util.Try.WithFilter)


### `def foreach[U](f: (T) ⇒ U): Unit`                                       ###

(defined at scala.util.Try.WithFilter)


### `def map[U](f: (T) ⇒ U): Try[U]`                                         ###

(defined at scala.util.Try.WithFilter)


### `def withFilter(q: (T) ⇒ Boolean): WithFilter`                           ###
(defined at scala.util.Try.WithFilter)
