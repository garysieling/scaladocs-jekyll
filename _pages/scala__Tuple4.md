
#                                 scala.Tuple4                                 #

```scala
case class Tuple4[+T1, +T2, +T3, +T4](_1: T1, _2: T2, _3: T3, _4: T4) extends Product4[T1, T2, T3, T4] with Product with Serializable
```

A tuple of 4 elements; the canonical representation of a scala.Product4.

* _1
  * Element 1 of this Tuple4
* _2
  * Element 2 of this Tuple4
* _3
  * Element 3 of this Tuple4
* _4
  * Element 4 of this Tuple4

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [Tuple4.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Tuple4.scala#L1)


--------------------------------------------------------------------------------
                       Value Members From scala.Product4
--------------------------------------------------------------------------------


### `def productElement(n: Int): Any`                                        ###

Returns the n-th projection of this product if 0 < n <= productArity, otherwise
throws an `IndexOutOfBoundsException` .

* n
  * number of the projection to be returned
* returns
  * same as `._(n+1)` , for example `productElement(0)` is the same as `._1` .

* Definition Classes
  * Product4 → Product
* Annotations
  * @ throws (clazz = classOf[IndexOutOfBoundsException])
* Exceptions thrown
  *

(defined at scala.Product4)


--------------------------------------------------------------------------------
                    Instance Constructors From scala.Tuple4
--------------------------------------------------------------------------------


### `new Tuple4(_1: T1, _2: T2, _3: T3, _4: T4)`                             ###

Create a new tuple with 4 elements. Note that it is more idiomatic to create a
Tuple4 via `(t1, t2, t3, t4)`

* _1
  * Element 1 of this Tuple4
* _2
  * Element 2 of this Tuple4
* _3
  * Element 3 of this Tuple4
* _4
  * Element 4 of this Tuple4
(defined at scala.Tuple4)
