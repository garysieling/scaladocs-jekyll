
#                           scala.Option#WithFilter                           #

```scala
class WithFilter extends AnyRef
```

We need a whole WithFilter class to honor the "doesn't create a new collection"
contract even though it seems unlikely to matter much in a collection with max
size 1.

* Source
  * [Option.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Option.scala#L1)


--------------------------------------------------------------------------------
               Instance Constructors From scala.Option.WithFilter
--------------------------------------------------------------------------------


### `new WithFilter(p: (A) ⇒ Boolean)`                                       ###

(defined at scala.Option.WithFilter)


--------------------------------------------------------------------------------
                   Value Members From scala.Option.WithFilter
--------------------------------------------------------------------------------


### `def flatMap[B](f: (A) ⇒ Option[B]): Option[B]`                          ###

(defined at scala.Option.WithFilter)


### `def foreach[U](f: (A) ⇒ U): Unit`                                       ###

(defined at scala.Option.WithFilter)


### `def map[B](f: (A) ⇒ B): Option[B]`                                      ###

(defined at scala.Option.WithFilter)


### `def withFilter(q: (A) ⇒ Boolean): WithFilter`                           ###
(defined at scala.Option.WithFilter)
