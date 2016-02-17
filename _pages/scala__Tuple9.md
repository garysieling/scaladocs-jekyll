
#                                 scala.Tuple9                                 #

```scala
case class Tuple9[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8, +T9](_1: T1, _2: T2, _3: T3, _4: T4, _5: T5, _6: T6, _7: T7, _8: T8, _9: T9) extends Product9[T1, T2, T3, T4, T5, T6, T7, T8, T9] with Product with Serializable
```

A tuple of 9 elements; the canonical representation of a scala.Product9.

* _1
  * Element 1 of this Tuple9
* _2
  * Element 2 of this Tuple9
* _3
  * Element 3 of this Tuple9
* _4
  * Element 4 of this Tuple9
* _5
  * Element 5 of this Tuple9
* _6
  * Element 6 of this Tuple9
* _7
  * Element 7 of this Tuple9
* _8
  * Element 8 of this Tuple9
* _9
  * Element 9 of this Tuple9

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [Tuple9.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Tuple9.scala#L1)


--------------------------------------------------------------------------------
                       Value Members From scala.Product9
--------------------------------------------------------------------------------


### `def productElement(n: Int): Any`                                        ###

Returns the n-th projection of this product if 0 < n <= productArity, otherwise
throws an `IndexOutOfBoundsException` .

* n
  * number of the projection to be returned
* returns
  * same as `._(n+1)` , for example `productElement(0)` is the same as `._1` .

* Definition Classes
  * Product9 → Product
* Annotations
  * @ throws (clazz = classOf[IndexOutOfBoundsException])
* Exceptions thrown
  *

(defined at scala.Product9)


--------------------------------------------------------------------------------
                    Instance Constructors From scala.Tuple9
--------------------------------------------------------------------------------


### `new Tuple9(_1: T1, _2: T2, _3: T3, _4: T4, _5: T5, _6: T6, _7: T7, _8: T8, _9: T9)` ###

Create a new tuple with 9 elements. Note that it is more idiomatic to create a
Tuple9 via `(t1, t2, t3, t4, t5, t6, t7, t8, t9)`

* _1
  * Element 1 of this Tuple9
* _2
  * Element 2 of this Tuple9
* _3
  * Element 3 of this Tuple9
* _4
  * Element 4 of this Tuple9
* _5
  * Element 5 of this Tuple9
* _6
  * Element 6 of this Tuple9
* _7
  * Element 7 of this Tuple9
* _8
  * Element 8 of this Tuple9
* _9
  * Element 9 of this Tuple9
(defined at scala.Tuple9)
