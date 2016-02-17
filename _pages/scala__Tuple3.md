
#                                 scala.Tuple3                                 #

```scala
case class Tuple3[+T1, +T2, +T3](_1: T1, _2: T2, _3: T3) extends Product3[T1, T2, T3] with Product with Serializable
```

A tuple of 3 elements; the canonical representation of a scala.Product3.

* _1
  * Element 1 of this Tuple3
* _2
  * Element 2 of this Tuple3
* _3
  * Element 3 of this Tuple3

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [Tuple3.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Tuple3.scala#L1)


--------------------------------------------------------------------------------
                       Value Members From scala.Product3
--------------------------------------------------------------------------------


### `def productElement(n: Int): Any`                                        ###

Returns the n-th projection of this product if 0 < n <= productArity, otherwise
throws an `IndexOutOfBoundsException` .

* n
  * number of the projection to be returned
* returns
  * same as `._(n+1)` , for example `productElement(0)` is the same as `._1` .

* Definition Classes
  * Product3 → Product
* Annotations
  * @ throws (clazz = classOf[IndexOutOfBoundsException])
* Exceptions thrown
  *

(defined at scala.Product3)


--------------------------------------------------------------------------------
                    Instance Constructors From scala.Tuple3
--------------------------------------------------------------------------------


### `new Tuple3(_1: T1, _2: T2, _3: T3)`                                     ###

Create a new tuple with 3 elements. Note that it is more idiomatic to create a
Tuple3 via `(t1, t2, t3)`

* _1
  * Element 1 of this Tuple3
* _2
  * Element 2 of this Tuple3
* _3
  * Element 3 of this Tuple3

(defined at scala.Tuple3)


--------------------------------------------------------------------------------
           Value Members From Implicit scala.Predef.tuple3ToZippedOps
--------------------------------------------------------------------------------


### `def invert[El1, CC1[X] <: TraversableOnce[X], El2, CC2[X] <: TraversableOnce[X], El3, CC3[X] <: TraversableOnce[X], That](implicit w1: <:<[T1, CC1[El1]], w2: <:<[T2, CC2[El2]], w3: <:<[T3, CC3[El3]], bf: CanBuildFrom[CC1[_], (El1, El2, El3), That]): That` ###

* Implicit information
  * This member is added by an implicit conversion from (T1, T2, T3) to Ops [T1,
    T2, T3] performed by method tuple3ToZippedOps in scala.Predef.
* Definition Classes
  * Ops

(added by implicit convertion: scala.Predef.tuple3ToZippedOps)


### `def zipped[El1, Repr1, El2, Repr2, El3, Repr3](implicit w1: (T1) ⇒ TraversableLike[El1, Repr1], w2: (T2) ⇒ IterableLike[El2, Repr2], w3: (T3) ⇒ IterableLike[El3, Repr3]): Tuple3Zipped[El1, Repr1, El2, Repr2, El3, Repr3]` ###

* Implicit information
  * This member is added by an implicit conversion from (T1, T2, T3) to Ops [T1,
    T2, T3] performed by method tuple3ToZippedOps in scala.Predef.
* Definition Classes
  * Ops
(added by implicit convertion: scala.Predef.tuple3ToZippedOps)
