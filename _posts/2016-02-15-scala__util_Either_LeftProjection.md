
#                       scala.util.Either.LeftProjection                       #

```scala
final case class LeftProjection[+A, +B](e: Either[A, B]) extends Product with Serializable
```

Projects an `Either` into a `Left` .

This allows for-comprehensions over Either instances - for example

```scala
for (s <- Left("flower").left) yield s.length // Left(6)
```

Continuing the analogy with scala.Option, a `LeftProjection` declares that
 `Left` should be analogous to `Some` in some code.

```scala
// using Option:
def interactWithDB(x: Query): Option[Result] =
  try {
    Some(getResultFromDatabase(x))
  } catch {
    case ex => None
  }

// this will only be executed if interactWithDB returns a Some
val report =
  for (r <- interactWithDB(someQuery)) yield generateReport(r)
if (report.isDefined)
  send(report)
else
  log("report not generated, not sure why...")
```

```scala
// using Either
def interactWithDB(x: Query): Either[Exception, Result] =
  try {
    Right(getResultFromDatabase(x))
  } catch {
    case ex => Left(ex)
  }

// this will only be executed if interactWithDB returns a Right
val report =
  for (r <- interactWithDB(someQuery).right) yield generateReport(r)
if (report.isRight)
  send(report)
else
  log("report not generated, reason was " + report.left.get)
```

* Source
  * [Either.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/Either.scala#L1)
* Version
  * 1.0, 11/10/2008


--------------------------------------------------------------------------------
          Instance Constructors From scala.util.Either.LeftProjection
--------------------------------------------------------------------------------


### `new LeftProjection(e: Either[A, B])`                                    ###

(defined at scala.util.Either.LeftProjection)


--------------------------------------------------------------------------------
              Value Members From scala.util.Either.LeftProjection
--------------------------------------------------------------------------------


### `val e: Either[A, B]`                                                    ###

(defined at scala.util.Either.LeftProjection)


### `def exists(p: (A) ⇒ Boolean): Boolean`                                  ###

Returns `false` if `Right` or returns the result of the application of the given
function to the `Left` value.

```scala
Left(12).left.exists(_ > 10)  // true
Left(7).left.exists(_ > 10)   // false
Right(12).left.exists(_ > 10) // false
```

(defined at scala.util.Either.LeftProjection)


### `def filter[Y](p: (A) ⇒ Boolean): Option[Either[A, Y]]`                  ###

Returns `None` if this is a `Right` or if the given predicate `p` does not hold
for the left value, otherwise, returns a `Left` .

```scala
Left(12).left.filter(_ > 10)  // Some(Left(12))
Left(7).left.filter(_ > 10)   // None
Right(12).left.filter(_ > 10) // None
```

(defined at scala.util.Either.LeftProjection)


### `def flatMap[BB >: B, X](f: (A) ⇒ Either[X, BB]): Either[X, BB]`         ###

Binds the given function across `Left` .

```scala
Left(12).left.flatMap(x => Left("scala")) // Left("scala")
Right(12).left.flatMap(x => Left("scala") // Right(12)
```

* f
  * The function to bind across `Left` .

(defined at scala.util.Either.LeftProjection)


### `def forall(p: (A) ⇒ Boolean): Boolean`                                  ###

Returns `true` if `Right` or returns the result of the application of the given
function to the `Left` value.

```scala
Left(12).left.forall(_ > 10)  // true
Left(7).left.forall(_ > 10)   // false
Right(12).left.forall(_ > 10) // true
```

(defined at scala.util.Either.LeftProjection)


### `def foreach[U](f: (A) ⇒ U): Any`                                        ###

Executes the given side-effecting function if this is a `Left` .

```scala
Left(12).left.foreach(x => println(x))  // prints "12"
Right(12).left.foreach(x => println(x)) // doesn't print
```

* f
  * The side-effecting function to execute.

(defined at scala.util.Either.LeftProjection)


### `def getOrElse[AA >: A](or: ⇒ AA): AA`                                   ###

Returns the value from this `Left` or the given argument if this is a `Right` .

```scala
Left(12).left.getOrElse(17)  // 12
Right(12).left.getOrElse(17) // 17
```

(defined at scala.util.Either.LeftProjection)


### `def map[X](f: (A) ⇒ X): Either[X, B]`                                   ###

Maps the function argument through `Left` .

```scala
Left(12).left.map(_ + 2) // Left(14)
Right[Int, Int](12).left.map(_ + 2) // Right(12)
```

(defined at scala.util.Either.LeftProjection)


### `def toSeq: collection.Seq[A]`                                           ###

Returns a `Seq` containing the `Left` value if it exists or an empty `Seq` if
this is a `Right` .

```scala
Left(12).left.toSeq // Seq(12)
Right(12).left.toSeq // Seq()
```
(defined at scala.util.Either.LeftProjection)
