
#                                scala.Product                                #

```scala
trait Product extends Equals
```

Base trait for all products, which in the standard library include at least
scala.Product1 through scala.Product22 and therefore also their subclasses
scala.Tuple1 through scala.Tuple22. In addition, all case classes implement
 `Product` with synthetically generated methods.

* Source
  * [Product.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product.scala#L1)
* Version
  * 1.0
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
                   Abstract Value Members From scala.Product
--------------------------------------------------------------------------------


### `abstract def productElement(n: Int): Any`                               ###

The n <sup>th</sup> element of this product, 0-based. In other words, for a
product `A(x1, ..., xk)` , returns `x(n+1)` where `0 < n < k` .

* n
  * the index of the element to return
* returns
  * the element `n` elements after the first element

* Exceptions thrown
  *
(defined at scala.Product)
