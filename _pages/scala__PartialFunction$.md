
#                            scala.PartialFunction                            #

```scala
object PartialFunction
```

A few handy operations which leverage the extra bit of information available in
partial functions. Examples:

```scala
import PartialFunction._

def strangeConditional(other: Any): Boolean = cond(other) {
  case x: String if x == "abc" || x == "def"  => true
  case x: Int => true
}
def onlyInt(v: Any): Option[Int] = condOpt(v) { case x: Int => x }
```

* Source
  * [PartialFunction.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/PartialFunction.scala#L1)
* Since
  * 2.8


--------------------------------------------------------------------------------
                    Value Members From scala.PartialFunction
--------------------------------------------------------------------------------


### `def apply[A, B](f: (A) ⇒ B): PartialFunction[A, B]`                     ###

Converts ordinary function to partial one

* Since
  * 2.10

(defined at scala.PartialFunction)


### `def condOpt[T, U](x: T)(pf: PartialFunction[T, U]): Option[U]`          ###

Transforms a PartialFunction[T, U] `pf` into Function1[T, Option[U]] `f` whose
result is `Some(x)` if the argument is in `pf` 's domain and `None` otherwise,
and applies it to the value `x` . In effect, it is a `match` statement which
wraps all case results in `Some(_)` and adds `case _ => None` to the end.

* x
  * the value to test
* pf
  * the PartialFunction[T, U]
* returns
  * `Some(pf(x))` if `pf isDefinedAt x` , `None` otherwise.

(defined at scala.PartialFunction)


### `def cond[T](x: T)(pf: PartialFunction[T, Boolean]): Boolean`            ###

Creates a Boolean test based on a value and a partial function. It behaves like
a 'match' statement with an implied 'case _ => false' following the supplied
cases.

* x
  * the value to test
* pf
  * the partial function
* returns
  * true, iff `x` is in the domain of `pf` and `pf(x) == true` .
(defined at scala.PartialFunction)
