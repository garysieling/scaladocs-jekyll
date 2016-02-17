
#                                 scala.Tuple2                                 #

```scala
case class Tuple2[+T1, +T2](_1: T1, _2: T2) extends Product2[T1, T2] with Product with Serializable
```

A tuple of 2 elements; the canonical representation of a scala.Product2.

* _1
  * Element 1 of this Tuple2
* _2
  * Element 2 of this Tuple2

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [Tuple2.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Tuple2.scala#L1)


--------------------------------------------------------------------------------
                       Value Members From scala.Product2
--------------------------------------------------------------------------------


### `def productElement(n: Int): Any`                                        ###

Returns the n-th projection of this product if 0 < n <= productArity, otherwise
throws an `IndexOutOfBoundsException` .

* n
  * number of the projection to be returned
* returns
  * same as `._(n+1)` , for example `productElement(0)` is the same as `._1` .

* Definition Classes
  * Product2 → Product
* Annotations
  * @ throws (clazz = classOf[IndexOutOfBoundsException])
* Exceptions thrown
  *

(defined at scala.Product2)


--------------------------------------------------------------------------------
                    Instance Constructors From scala.Tuple2
--------------------------------------------------------------------------------


### `new Tuple2(_1: T1, _2: T2)`                                             ###

Create a new tuple with 2 elements. Note that it is more idiomatic to create a
Tuple2 via `(t1, t2)`

* _1
  * Element 1 of this Tuple2
* _2
  * Element 2 of this Tuple2

(defined at scala.Tuple2)


--------------------------------------------------------------------------------
           Value Members From Implicit scala.Predef.tuple2ToZippedOps
--------------------------------------------------------------------------------


### `def invert[El1, CC1[X] <: TraversableOnce[X], El2, CC2[X] <: TraversableOnce[X], That](implicit w1: <:<[T1, CC1[El1]], w2: <:<[T2, CC2[El2]], bf: CanBuildFrom[CC1[_], (El1, El2), That]): That` ###

* Implicit information
  * This member is added by an implicit conversion from (T1, T2) to Ops [T1, T2]
    performed by method tuple2ToZippedOps in scala.Predef.
* Definition Classes
  * Ops

(added by implicit convertion: scala.Predef.tuple2ToZippedOps)


### `def zipped[El1, Repr1, El2, Repr2](implicit w1: (T1) ⇒ TraversableLike[El1, Repr1], w2: (T2) ⇒ IterableLike[El2, Repr2]): Tuple2Zipped[El1, Repr1, El2, Repr2]` ###

* Implicit information
  * This member is added by an implicit conversion from (T1, T2) to Ops [T1, T2]
    performed by method tuple2ToZippedOps in scala.Predef.
* Definition Classes
  * Ops
(added by implicit convertion: scala.Predef.tuple2ToZippedOps)
