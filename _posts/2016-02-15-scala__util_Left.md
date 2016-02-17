
#                               scala.util.Left                               #

```scala
final case class Left[+A, +B](a: A) extends Either[A, B] with Product with Serializable
```

The left side of the disjoint union, as opposed to the scala.util.Right side.

* Source
  * [Either.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/Either.scala#L1)
* Version
  * 1.0, 11/10/2008


--------------------------------------------------------------------------------
                      Value Members From scala.util.Either
--------------------------------------------------------------------------------


### `def fold[X](fa: (A) ⇒ X, fb: (B) ⇒ X): X`                               ###

Applies `fa` if this is a `Left` or `fb` if this is a `Right` .

* fa
  * the function to apply if this is a `Left`
* fb
  * the function to apply if this is a `Right`
* returns
  * the results of applying the function

* Definition Classes
  * Either

Example:

```scala
val result: Either[Exception, Value] = possiblyFailingOperation()
log(result.fold(
  ex => "Operation failed with " + ex,
  v => "Operation produced value: " + v
))
```

(defined at scala.util.Either)


### `def joinLeft[A1 >: A, B1 >: B, C](implicit ev: <:<[A1, Either[C, B1]]): Either[C, B1]` ###

Joins an `Either` through `Left` .

This method requires that the left side of this Either is itself an Either type.
That is, this must be some type like:

```scala
Either[Either[C, B], B]
```

(which respects the type parameter bounds, shown below.)

If this instance is a Left[Either[C, B]] then the contained Either[C, B] will be
returned, otherwise this value will be returned unmodified.

```scala
Left[Either[Int, String], String](Right("flower")).joinLeft // Result: Right("flower")
Left[Either[Int, String], String](Left(12)).joinLeft // Result: Left(12)
Right[Either[Int, String], String]("daisy").joinLeft // Result: Right("daisy")
```

This method, and `joinRight` , are analogous to `Option#flatten`

* Definition Classes
  * Either

(defined at scala.util.Either)


### `def joinRight[A1 >: A, B1 >: B, C](implicit ev: <:<[B1, Either[A1, C]]): Either[A1, C]` ###

Joins an `Either` through `Right` .

This method requires that the right side of this Either is itself an Either
type. That is, this must be some type like:

```scala
Either[A, Either[A, C]]
```

(which respects the type parameter bounds, shown below.)

If this instance is a Right[Either[A, C]] then the contained Either[A, C] will
be returned, otherwise this value will be returned unmodified.

* Definition Classes
  * Either

Example:

```scala
joinLeft
```

(defined at scala.util.Either)


### `def left: LeftProjection[A, B]`                                         ###

Projects this `Either` as a `Left` .

* Definition Classes
  * Either

(defined at scala.util.Either)


### `def right: RightProjection[A, B]`                                       ###

Projects this `Either` as a `Right` .

* Definition Classes
  * Either

(defined at scala.util.Either)


### `def swap: Either[B, A]`                                                 ###

If this is a `Left` , then return the left value in `Right` or vice versa.

* Definition Classes
  * Either

Example:

```scala
val l: Either[String, Int] = Left("left")
val r: Either[Int, String] = l.swap // Result: Right("left")
```

(defined at scala.util.Either)


--------------------------------------------------------------------------------
                   Instance Constructors From scala.util.Left
--------------------------------------------------------------------------------


### `new Left(a: A)`                                                         ###

(defined at scala.util.Left)


--------------------------------------------------------------------------------
         Value Members From Implicit scala.util.Either.MergeableEither
--------------------------------------------------------------------------------


### `def merge: B`                                                           ###

* Implicit information
  * This member is added by an implicit conversion from Left [A, B] to
    MergeableEither [B] performed by method MergeableEither in scala.util.Either.
* Definition Classes
  * MergeableEither
(added by implicit convertion: scala.util.Either.MergeableEither)
