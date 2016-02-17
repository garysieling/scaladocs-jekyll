
#                                scala.Tuple20                                #

```scala
case class Tuple20[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8, +T9, +T10, +T11, +T12, +T13, +T14, +T15, +T16, +T17, +T18, +T19, +T20](_1: T1, _2: T2, _3: T3, _4: T4, _5: T5, _6: T6, _7: T7, _8: T8, _9: T9, _10: T10, _11: T11, _12: T12, _13: T13, _14: T14, _15: T15, _16: T16, _17: T17, _18: T18, _19: T19, _20: T20) extends Product20[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20] with Product with Serializable
```

A tuple of 20 elements; the canonical representation of a scala.Product20.

* _1
  * Element 1 of this Tuple20
* _2
  * Element 2 of this Tuple20
* _3
  * Element 3 of this Tuple20
* _4
  * Element 4 of this Tuple20
* _5
  * Element 5 of this Tuple20
* _6
  * Element 6 of this Tuple20
* _7
  * Element 7 of this Tuple20
* _8
  * Element 8 of this Tuple20
* _9
  * Element 9 of this Tuple20
* _10
  * Element 10 of this Tuple20
* _11
  * Element 11 of this Tuple20
* _12
  * Element 12 of this Tuple20
* _13
  * Element 13 of this Tuple20
* _14
  * Element 14 of this Tuple20
* _15
  * Element 15 of this Tuple20
* _16
  * Element 16 of this Tuple20
* _17
  * Element 17 of this Tuple20
* _18
  * Element 18 of this Tuple20
* _19
  * Element 19 of this Tuple20
* _20
  * Element 20 of this Tuple20

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [Tuple20.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Tuple20.scala#L1)


--------------------------------------------------------------------------------
                       Value Members From scala.Product20
--------------------------------------------------------------------------------


### `def productElement(n: Int): Any`                                        ###

Returns the n-th projection of this product if 0 < n <= productArity, otherwise
throws an `IndexOutOfBoundsException` .

* n
  * number of the projection to be returned
* returns
  * same as `._(n+1)` , for example `productElement(0)` is the same as `._1` .

* Definition Classes
  * Product20 → Product
* Annotations
  * @ throws (clazz = classOf[IndexOutOfBoundsException])
* Exceptions thrown
  *

(defined at scala.Product20)


--------------------------------------------------------------------------------
                    Instance Constructors From scala.Tuple20
--------------------------------------------------------------------------------


### `new Tuple20(_1: T1, _2: T2, _3: T3, _4: T4, _5: T5, _6: T6, _7: T7, _8: T8, _9: T9, _10: T10, _11: T11, _12: T12, _13: T13, _14: T14, _15: T15, _16: T16, _17: T17, _18: T18, _19: T19, _20: T20)` ###

Create a new tuple with 20 elements. Note that it is more idiomatic to create a
Tuple20 via
 `(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20)`

* _1
  * Element 1 of this Tuple20
* _2
  * Element 2 of this Tuple20
* _3
  * Element 3 of this Tuple20
* _4
  * Element 4 of this Tuple20
* _5
  * Element 5 of this Tuple20
* _6
  * Element 6 of this Tuple20
* _7
  * Element 7 of this Tuple20
* _8
  * Element 8 of this Tuple20
* _9
  * Element 9 of this Tuple20
* _10
  * Element 10 of this Tuple20
* _11
  * Element 11 of this Tuple20
* _12
  * Element 12 of this Tuple20
* _13
  * Element 13 of this Tuple20
* _14
  * Element 14 of this Tuple20
* _15
  * Element 15 of this Tuple20
* _16
  * Element 16 of this Tuple20
* _17
  * Element 17 of this Tuple20
* _18
  * Element 18 of this Tuple20
* _19
  * Element 19 of this Tuple20
* _20
  * Element 20 of this Tuple20
(defined at scala.Tuple20)
