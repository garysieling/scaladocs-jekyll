
#                                scala.Tuple14                                #

```scala
case class Tuple14[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8, +T9, +T10, +T11, +T12, +T13, +T14](_1: T1, _2: T2, _3: T3, _4: T4, _5: T5, _6: T6, _7: T7, _8: T8, _9: T9, _10: T10, _11: T11, _12: T12, _13: T13, _14: T14) extends Product14[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14] with Product with Serializable
```

A tuple of 14 elements; the canonical representation of a scala.Product14.

* _1
  * Element 1 of this Tuple14
* _2
  * Element 2 of this Tuple14
* _3
  * Element 3 of this Tuple14
* _4
  * Element 4 of this Tuple14
* _5
  * Element 5 of this Tuple14
* _6
  * Element 6 of this Tuple14
* _7
  * Element 7 of this Tuple14
* _8
  * Element 8 of this Tuple14
* _9
  * Element 9 of this Tuple14
* _10
  * Element 10 of this Tuple14
* _11
  * Element 11 of this Tuple14
* _12
  * Element 12 of this Tuple14
* _13
  * Element 13 of this Tuple14
* _14
  * Element 14 of this Tuple14

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [Tuple14.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Tuple14.scala#L1)


--------------------------------------------------------------------------------
                       Value Members From scala.Product14
--------------------------------------------------------------------------------


### `def productElement(n: Int): Any`                                        ###

Returns the n-th projection of this product if 0 < n <= productArity, otherwise
throws an `IndexOutOfBoundsException` .

* n
  * number of the projection to be returned
* returns
  * same as `._(n+1)` , for example `productElement(0)` is the same as `._1` .

* Definition Classes
  * Product14 → Product
* Annotations
  * @ throws (clazz = classOf[IndexOutOfBoundsException])
* Exceptions thrown
  *

(defined at scala.Product14)


--------------------------------------------------------------------------------
                    Instance Constructors From scala.Tuple14
--------------------------------------------------------------------------------


### `new Tuple14(_1: T1, _2: T2, _3: T3, _4: T4, _5: T5, _6: T6, _7: T7, _8: T8, _9: T9, _10: T10, _11: T11, _12: T12, _13: T13, _14: T14)` ###

Create a new tuple with 14 elements. Note that it is more idiomatic to create a
Tuple14 via `(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14)`

* _1
  * Element 1 of this Tuple14
* _2
  * Element 2 of this Tuple14
* _3
  * Element 3 of this Tuple14
* _4
  * Element 4 of this Tuple14
* _5
  * Element 5 of this Tuple14
* _6
  * Element 6 of this Tuple14
* _7
  * Element 7 of this Tuple14
* _8
  * Element 8 of this Tuple14
* _9
  * Element 9 of this Tuple14
* _10
  * Element 10 of this Tuple14
* _11
  * Element 11 of this Tuple14
* _12
  * Element 12 of this Tuple14
* _13
  * Element 13 of this Tuple14
* _14
  * Element 14 of this Tuple14
(defined at scala.Tuple14)
