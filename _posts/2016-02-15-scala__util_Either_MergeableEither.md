
#                      scala.util.Either.MergeableEither                      #

```scala
implicit final class MergeableEither[A] extends AnyVal
```

Allows use of a `merge` method to extract values from Either instances
regardless of whether they are Left or Right.

```scala
val l = Left(List(1)): Either[List[Int], Vector[Int]]
val r = Right(Vector(1)): Either[List[Int], Vector[Int]]
l.merge: Seq[Int] // List(1)
r.merge: Seq[Int] // Vector(1)
```

* Source
  * [Either.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/Either.scala#L1)


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
          Instance Constructors From scala.util.Either.MergeableEither
--------------------------------------------------------------------------------


### `new MergeableEither(x: Either[A, A])`                                   ###
(defined at scala.util.Either.MergeableEither)
