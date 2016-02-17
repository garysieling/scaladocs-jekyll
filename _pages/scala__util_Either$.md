
#                              scala.util.Either                              #

```scala
object Either extends Serializable
```

* Source
  * [Either.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/Either.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `final case class LeftProjection[+A, +B](e: Either[A, B]) extends Product with Serializable` ###

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


### `implicit final class MergeableEither[A] extends AnyVal`                 ###

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


### `final case class RightProjection[+A, +B](e: Either[A, B]) extends Product with Serializable` ###

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
                      Value Members From scala.util.Either
--------------------------------------------------------------------------------


### `def cond[A, B](test: Boolean, right: ⇒ B, left: ⇒ A): Either[A, B]`     ###

If the condition is satisfied, return the given `B` in `Right` , otherwise,
return the given `A` in `Left` .

```scala
val userInput: String = ...
Either.cond(
  userInput.forall(_.isDigit) && userInput.size == 10,
  PhoneNumber(userInput),
  "The input (%s) does not look like a phone number".format(userInput)
```
(defined at scala.util.Either)
