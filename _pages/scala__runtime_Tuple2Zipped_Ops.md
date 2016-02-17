
#                        scala.runtime.Tuple2Zipped.Ops                        #

```scala
final class Ops[T1, T2] extends AnyVal
```

* Source
  * [Tuple2Zipped.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/runtime/Tuple2Zipped.scala#L1)


--------------------------------------------------------------------------------
                        Value Members From scala.Any###
--------------------------------------------------------------------------------


### `final def ##(): Int`                                                    ###

Equivalent to `x.hashCode` except for boxed numeric types and `null` . For
numerics, it returns a hash value which is consistent with value equality: if
two value type instances compare as true, then ## will produce the same hash
value for each of them. For `null` returns a hashcode where `null.hashCode`
throws a `NullPointerException` .

* returns
  * a hash value consistent with ==

* Definition Classes
  * Any

(defined at scala.Any###)


--------------------------------------------------------------------------------
           Instance Constructors From scala.runtime.Tuple2Zipped.Ops
--------------------------------------------------------------------------------


### `new Ops(x: (T1, T2))`                                                   ###

(defined at scala.runtime.Tuple2Zipped.Ops)


--------------------------------------------------------------------------------
               Value Members From scala.runtime.Tuple2Zipped.Ops
--------------------------------------------------------------------------------


### `def invert[El1, CC1[X] <: TraversableOnce[X], El2, CC2[X] <: TraversableOnce[X], That](implicit w1: <:<[T1, CC1[El1]], w2: <:<[T2, CC2[El2]], bf: CanBuildFrom[CC1[_], (El1, El2), That]): That` ###

(defined at scala.runtime.Tuple2Zipped.Ops)


### `def zipped[El1, Repr1, El2, Repr2](implicit w1: (T1) ⇒ TraversableLike[El1, Repr1], w2: (T2) ⇒ IterableLike[El2, Repr2]): Tuple2Zipped[El1, Repr1, El2, Repr2]` ###
(defined at scala.runtime.Tuple2Zipped.Ops)
