
#                                 scala.Tuple5                                 #

```scala
case class Tuple5[+T1, +T2, +T3, +T4, +T5](_1: T1, _2: T2, _3: T3, _4: T4, _5: T5) extends Product5[T1, T2, T3, T4, T5] with Product with Serializable
```

A tuple of 5 elements; the canonical representation of a scala.Product5.

* _1
  * Element 1 of this Tuple5
* _2
  * Element 2 of this Tuple5
* _3
  * Element 3 of this Tuple5
* _4
  * Element 4 of this Tuple5
* _5
  * Element 5 of this Tuple5

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [Tuple5.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Tuple5.scala#L1)


--------------------------------------------------------------------------------
                       Value Members From scala.Product5
--------------------------------------------------------------------------------


### `def productElement(n: Int): Any`                                        ###

Returns the n-th projection of this product if 0 < n <= productArity, otherwise
throws an `IndexOutOfBoundsException` .

* n
  * number of the projection to be returned
* returns
  * same as `._(n+1)` , for example `productElement(0)` is the same as `._1` .

* Definition Classes
  * Product5 → Product
* Annotations
  * @ throws (clazz = classOf[IndexOutOfBoundsException])
* Exceptions thrown
  *

(defined at scala.Product5)


--------------------------------------------------------------------------------
                    Instance Constructors From scala.Tuple5
--------------------------------------------------------------------------------


### `new Tuple5(_1: T1, _2: T2, _3: T3, _4: T4, _5: T5)`                     ###

Create a new tuple with 5 elements. Note that it is more idiomatic to create a
Tuple5 via `(t1, t2, t3, t4, t5)`

* _1
  * Element 1 of this Tuple5
* _2
  * Element 2 of this Tuple5
* _3
  * Element 3 of this Tuple5
* _4
  * Element 4 of this Tuple5
* _5
  * Element 5 of this Tuple5
(defined at scala.Tuple5)
