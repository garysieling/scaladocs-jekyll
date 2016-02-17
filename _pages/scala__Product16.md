
#                               scala.Product16                               #

```scala
trait Product16[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8, +T9, +T10, +T11, +T12, +T13, +T14, +T15, +T16] extends Product
```

Product16 is a cartesian product of 16 components.

* Source
  * [Product16.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product16.scala#L1)
* Since
  * 2.3


--------------------------------------------------------------------------------
                    Abstract Value Members From scala.Equals
--------------------------------------------------------------------------------


### `abstract def canEqual(that: Any): Boolean`                              ###

A method that should be called from every well-designed equals method that is
open to be overridden in a subclass. See
[Programming in Scala, Chapter 28](http://www.artima.com/pins1ed/object-equality.html)
for discussion and design.

* that
  * the value being probed for possible equality
* returns
  * true if this instance can possibly equal `that` , otherwise false

* Definition Classes
  * Equals

(defined at scala.Equals)


--------------------------------------------------------------------------------
                  Concrete Value Members From scala.Product16
--------------------------------------------------------------------------------


### `abstract def _1: T1`                                                    ###

A projection of element 1 of this Product.

* returns
  * A projection of element 1.

(defined at scala.Product16)


### `def productElement(n: Int): Any`                                        ###

Returns the n-th projection of this product if 0 < n <= productArity, otherwise
throws an `IndexOutOfBoundsException` .

* n
  * number of the projection to be returned
* returns
  * same as `._(n+1)` , for example `productElement(0)` is the same as `._1` .

* Definition Classes
  * Product16 → Product
* Annotations
  * @ throws (clazz = classOf[IndexOutOfBoundsException])
* Exceptions thrown
  *
(defined at scala.Product16)
