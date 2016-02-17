
#                    scala.collection.generic.FilterMonadic                    #

```scala
trait FilterMonadic[+A, +Repr] extends Any
```

A template trait that contains just the `map` , `flatMap` , `foreach` and
 `withFilter` methods of trait `TraversableLike` .

* Source
  * [FilterMonadic.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/FilterMonadic.scala#L1)


--------------------------------------------------------------------------------
       Abstract Value Members From scala.collection.generic.FilterMonadic
--------------------------------------------------------------------------------


### `abstract def flatMap[B, That](f: (A) ⇒ GenTraversableOnce[B])(implicit bf: CanBuildFrom[Repr, B, That]): That` ###

(defined at scala.collection.generic.FilterMonadic)


### `abstract def foreach[U](f: (A) ⇒ U): Unit`                              ###

(defined at scala.collection.generic.FilterMonadic)


### `abstract def map[B, That](f: (A) ⇒ B)(implicit bf: CanBuildFrom[Repr, B, That]): That` ###

(defined at scala.collection.generic.FilterMonadic)


### `abstract def withFilter(p: (A) ⇒ Boolean): FilterMonadic[A, Repr]`      ###
(defined at scala.collection.generic.FilterMonadic)
