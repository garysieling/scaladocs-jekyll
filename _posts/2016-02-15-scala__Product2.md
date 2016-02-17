
#                                scala.Product2                                #

```scala
trait Product2[+T1, +T2] extends Product
```

Product2 is a cartesian product of 2 components.

* Source
  * [Product2.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product2.scala#L1)
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
                   Concrete Value Members From scala.Product2
--------------------------------------------------------------------------------


### `abstract def _1: T1`                                                    ###

A projection of element 1 of this Product.

* returns
  * A projection of element 1.

(defined at scala.Product2)


### `def productElement(n: Int): Any`                                        ###

Returns the n-th projection of this product if 0 < n <= productArity, otherwise
throws an `IndexOutOfBoundsException` .

* n
  * number of the projection to be returned
* returns
  * same as `._(n+1)` , for example `productElement(0)` is the same as `._1` .

* Definition Classes
  * Product2 → Product
* Annotations
  * @ throws (clazz = classOf[IndexOutOfBoundsException])
* Exceptions thrown
  *
(defined at scala.Product2)
