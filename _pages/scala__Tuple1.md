
#                                 scala.Tuple1                                 #

```scala
case class Tuple1[+T1](_1: T1) extends Product1[T1] with Product with Serializable
```

A tuple of 1 elements; the canonical representation of a scala.Product1.

* _1
  * Element 1 of this Tuple1

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [Tuple1.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Tuple1.scala#L1)


--------------------------------------------------------------------------------
                       Value Members From scala.Product1
--------------------------------------------------------------------------------


### `def productElement(n: Int): Any`                                        ###

Returns the n-th projection of this product if 0 < n <= productArity, otherwise
throws an `IndexOutOfBoundsException` .

* n
  * number of the projection to be returned
* returns
  * same as `._(n+1)` , for example `productElement(0)` is the same as `._1` .

* Definition Classes
  * Product1 → Product
* Annotations
  * @ throws (clazz = classOf[IndexOutOfBoundsException])
* Exceptions thrown
  *

(defined at scala.Product1)


--------------------------------------------------------------------------------
                    Instance Constructors From scala.Tuple1
--------------------------------------------------------------------------------


### `new Tuple1(_1: T1)`                                                     ###

Create a new tuple with 1 elements.

* _1
  * Element 1 of this Tuple1
(defined at scala.Tuple1)
