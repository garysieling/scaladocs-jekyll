
#                       scala.util.control.Exception.By                       #

```scala
class By[T, R] extends AnyRef
```

Returns a partially constructed `Catch` object, which you must give an exception
handler function as an argument to `by` . Example:

```scala
handling(ex1, ex2) by (_.printStackTrace)
```

* Source
  * [Exception.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/control/Exception.scala#L1)


--------------------------------------------------------------------------------
           Instance Constructors From scala.util.control.Exception.By
--------------------------------------------------------------------------------


### `new By(f: (T) ⇒ R)`                                                     ###

(defined at scala.util.control.Exception.By)


--------------------------------------------------------------------------------
               Value Members From scala.util.control.Exception.By
--------------------------------------------------------------------------------


### `def by(x: T): R`                                                        ###
(defined at scala.util.control.Exception.By)
