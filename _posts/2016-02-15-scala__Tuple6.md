
#                                 scala.Tuple6                                 #

```scala
case class Tuple6[+T1, +T2, +T3, +T4, +T5, +T6](_1: T1, _2: T2, _3: T3, _4: T4, _5: T5, _6: T6) extends Product6[T1, T2, T3, T4, T5, T6] with Product with Serializable
```

A tuple of 6 elements; the canonical representation of a scala.Product6.

* _1
  * Element 1 of this Tuple6
* _2
  * Element 2 of this Tuple6
* _3
  * Element 3 of this Tuple6
* _4
  * Element 4 of this Tuple6
* _5
  * Element 5 of this Tuple6
* _6
  * Element 6 of this Tuple6

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [Tuple6.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Tuple6.scala#L1)


--------------------------------------------------------------------------------
                       Value Members From scala.Product6
--------------------------------------------------------------------------------


### `def productElement(n: Int): Any`                                        ###

Returns the n-th projection of this product if 0 < n <= productArity, otherwise
throws an `IndexOutOfBoundsException` .

* n
  * number of the projection to be returned
* returns
  * same as `._(n+1)` , for example `productElement(0)` is the same as `._1` .

* Definition Classes
  * Product6 → Product
* Annotations
  * @ throws (clazz = classOf[IndexOutOfBoundsException])
* Exceptions thrown
  *

(defined at scala.Product6)


--------------------------------------------------------------------------------
                    Instance Constructors From scala.Tuple6
--------------------------------------------------------------------------------


### `new Tuple6(_1: T1, _2: T2, _3: T3, _4: T4, _5: T5, _6: T6)`             ###

Create a new tuple with 6 elements. Note that it is more idiomatic to create a
Tuple6 via `(t1, t2, t3, t4, t5, t6)`

* _1
  * Element 1 of this Tuple6
* _2
  * Element 2 of this Tuple6
* _3
  * Element 3 of this Tuple6
* _4
  * Element 4 of this Tuple6
* _5
  * Element 5 of this Tuple6
* _6
  * Element 6 of this Tuple6
(defined at scala.Tuple6)
