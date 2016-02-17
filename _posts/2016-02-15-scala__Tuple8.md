
#                                 scala.Tuple8                                 #

```scala
case class Tuple8[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8](_1: T1, _2: T2, _3: T3, _4: T4, _5: T5, _6: T6, _7: T7, _8: T8) extends Product8[T1, T2, T3, T4, T5, T6, T7, T8] with Product with Serializable
```

A tuple of 8 elements; the canonical representation of a scala.Product8.

* _1
  * Element 1 of this Tuple8
* _2
  * Element 2 of this Tuple8
* _3
  * Element 3 of this Tuple8
* _4
  * Element 4 of this Tuple8
* _5
  * Element 5 of this Tuple8
* _6
  * Element 6 of this Tuple8
* _7
  * Element 7 of this Tuple8
* _8
  * Element 8 of this Tuple8

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [Tuple8.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Tuple8.scala#L1)


--------------------------------------------------------------------------------
                       Value Members From scala.Product8
--------------------------------------------------------------------------------


### `def productElement(n: Int): Any`                                        ###

Returns the n-th projection of this product if 0 < n <= productArity, otherwise
throws an `IndexOutOfBoundsException` .

* n
  * number of the projection to be returned
* returns
  * same as `._(n+1)` , for example `productElement(0)` is the same as `._1` .

* Definition Classes
  * Product8 → Product
* Annotations
  * @ throws (clazz = classOf[IndexOutOfBoundsException])
* Exceptions thrown
  *

(defined at scala.Product8)


--------------------------------------------------------------------------------
                    Instance Constructors From scala.Tuple8
--------------------------------------------------------------------------------


### `new Tuple8(_1: T1, _2: T2, _3: T3, _4: T4, _5: T5, _6: T6, _7: T7, _8: T8)` ###

Create a new tuple with 8 elements. Note that it is more idiomatic to create a
Tuple8 via `(t1, t2, t3, t4, t5, t6, t7, t8)`

* _1
  * Element 1 of this Tuple8
* _2
  * Element 2 of this Tuple8
* _3
  * Element 3 of this Tuple8
* _4
  * Element 4 of this Tuple8
* _5
  * Element 5 of this Tuple8
* _6
  * Element 6 of this Tuple8
* _7
  * Element 7 of this Tuple8
* _8
  * Element 8 of this Tuple8
(defined at scala.Tuple8)
