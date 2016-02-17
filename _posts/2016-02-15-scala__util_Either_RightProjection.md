
#                      scala.util.Either.RightProjection                      #

```scala
final case class RightProjection[+A, +B](e: Either[A, B]) extends Product with Serializable
```

Projects an `Either` into a `Right` .

This allows for-comprehensions over Either instances - for example

```scala
for (s <- Right("flower").right) yield s.length // Right(6)
```

Continuing the analogy with scala.Option, a `RightProjection` declares that
 `Right` should be analogous to `Some` in some code.

Analogous to `LeftProjection` , see example usage in its documentation above.

* Source
  * [Either.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/Either.scala#L1)
* Version
  * 1.0, 11/10/2008


--------------------------------------------------------------------------------
          Instance Constructors From scala.util.Either.RightProjection
--------------------------------------------------------------------------------


### `new RightProjection(e: Either[A, B])`                                   ###

(defined at scala.util.Either.RightProjection)


--------------------------------------------------------------------------------
              Value Members From scala.util.Either.RightProjection
--------------------------------------------------------------------------------


### `val e: Either[A, B]`                                                    ###

(defined at scala.util.Either.RightProjection)


### `def exists(p: (B) ⇒ Boolean): Boolean`                                  ###

Returns `false` if `Left` or returns the result of the application of the given
function to the `Right` value.

```scala
Right(12).right.exists(_ > 10)  // true
Right(7).right.exists(_ > 10)   // false
Left(12).right.exists(_ > 10)   // false
```

(defined at scala.util.Either.RightProjection)


### `def filter[X](p: (B) ⇒ Boolean): Option[Either[X, B]]`                  ###

Returns `None` if this is a `Left` or if the given predicate `p` does not hold
for the right value, otherwise, returns a `Right` .

```scala
Right(12).right.filter(_ > 10) // Some(Right(12))
Right(7).right.filter(_ > 10)  // None
Left(12).right.filter(_ > 10)  // None
```

(defined at scala.util.Either.RightProjection)


### `def flatMap[AA >: A, Y](f: (B) ⇒ Either[AA, Y]): Either[AA, Y]`         ###

Binds the given function across `Right` .

* f
  * The function to bind across `Right` .

(defined at scala.util.Either.RightProjection)


### `def forall(f: (B) ⇒ Boolean): Boolean`                                  ###

Returns `true` if `Left` or returns the result of the application of the given
function to the `Right` value.

```scala
Right(12).right.forall(_ > 10) // true
Right(7).right.forall(_ > 10)  // false
Left(12).right.forall(_ > 10)  // true
```

(defined at scala.util.Either.RightProjection)


### `def foreach[U](f: (B) ⇒ U): Any`                                        ###

Executes the given side-effecting function if this is a `Right` .

```scala
Right(12).right.foreach(x => println(x)) // prints "12"
Left(12).right.foreach(x => println(x))  // doesn't print
```

* f
  * The side-effecting function to execute.

(defined at scala.util.Either.RightProjection)


### `def getOrElse[BB >: B](or: ⇒ BB): BB`                                   ###

Returns the value from this `Right` or the given argument if this is a `Left` .

```scala
Right(12).right.getOrElse(17) // 12
Left(12).right.getOrElse(17)  // 17
```

(defined at scala.util.Either.RightProjection)


### `def map[Y](f: (B) ⇒ Y): Either[A, Y]`                                   ###

The given function is applied if this is a `Right` .

```scala
Right(12).right.map(x => "flower") // Result: Right("flower")
Left(12).right.map(x => "flower")  // Result: Left(12)
```

(defined at scala.util.Either.RightProjection)


### `def toSeq: collection.Seq[B]`                                           ###

Returns a `Seq` containing the `Right` value if it exists or an empty `Seq` if
this is a `Left` .

```scala
Right(12).right.toSeq // Seq(12)
Left(12).right.toSeq // Seq()
```
(defined at scala.util.Either.RightProjection)
