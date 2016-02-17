
#                                  scala.None                                  #

```scala
object None extends Option[Nothing] with Product with Serializable
```

This case object represents non-existent values.

* Annotations
  * @ SerialVersionUID ()
* Source
  * [Option.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Option.scala#L1)
* Version
  * 1.0, 16/07/2003


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class WithFilter extends AnyRef`                                        ###

We need a whole WithFilter class to honor the "doesn't create a new collection"
contract even though it seems unlikely to matter much in a collection with max
size 1.

* Definition Classes
  * Option


--------------------------------------------------------------------------------
                        Value Members From scala.Option
--------------------------------------------------------------------------------


### `final def collect[B](pf: PartialFunction[Nothing, B]): Option[B]`       ###

Returns a scala.Some containing the result of applying `pf` to this scala.Option
's contained value, *if* this option is nonempty *and*  `pf` is defined for that
value. Returns `None` otherwise.

* pf
  * the partial function.
* returns
  * the result of applying `pf` to this scala.Option 's value (if possible), or
     `None` .

* Definition Classes
  * Option
* Annotations
  * @ inline ()

Example:

```scala
// Returns Some(HTTP) because the partial function covers the case.
Some("http") collect {case "http" => "HTTP"}
// Returns None because the partial function doesn't cover the case.
Some("ftp") collect {case "http" => "HTTP"}
// Returns None because the option is empty. There is no value to pass to the partial function.
None collect {case value => value}
```

(defined at scala.Option)


### `final def contains[A1 >: Nothing](elem: A1): Boolean`                   ###

Tests whether the option contains a given value as an element.

* elem
  * the element to test.
* returns
  * `true` if the option has an element that is equal (as determined by `==` )
    to `elem` , `false` otherwise.

* Definition Classes
  * Option

Example:

```scala
// Returns true because Some instance contains string "something" which equals "something".
Some("something") contains "something"
// Returns false because "something" != "anything".
Some("something") contains "anything"
// Returns false when method called on None.
None contains "anything"
```

(defined at scala.Option)


### `final def exists(p: (Nothing) ⇒ Boolean): Boolean`                      ###

Returns true if this option is nonempty *and* the predicate `p` returns true
when applied to this scala.Option 's value. Otherwise, returns false.

* p
  * the predicate to test

* Definition Classes
  * Option
* Annotations
  * @ inline ()

(defined at scala.Option)


### `final def filter(p: (Nothing) ⇒ Boolean): Option[Nothing]`              ###

Returns this scala.Option if it is nonempty *and* applying the predicate `p` to
this scala.Option 's value returns true. Otherwise, return `None` .

* p
  * the predicate used for testing.

* Definition Classes
  * Option
* Annotations
  * @ inline ()

(defined at scala.Option)


### `final def filterNot(p: (Nothing) ⇒ Boolean): Option[Nothing]`           ###

Returns this scala.Option if it is nonempty *and* applying the predicate `p` to
this scala.Option 's value returns false. Otherwise, return `None` .

* p
  * the predicate used for testing.

* Definition Classes
  * Option
* Annotations
  * @ inline ()

(defined at scala.Option)


### `final def flatMap[B](f: (Nothing) ⇒ Option[B]): Option[B]`              ###

Returns the result of applying `f` to this scala.Option 's value if this
scala.Option is nonempty. Returns `None` if this scala.Option is empty. Slightly
different from `map` in that `f` is expected to return an scala.Option (which
could be `None` ).

* f
  * the function to apply

* Definition Classes
  * Option
* Annotations
  * @ inline ()
* See also
  * foreach map

(defined at scala.Option)


### `def flatten[B](implicit ev: <:<[Nothing, Option[B]]): Option[B]`        ###

* Definition Classes
  * Option

(defined at scala.Option)


### `final def fold[B](ifEmpty: ⇒ B)(f: (Nothing) ⇒ B): B`                   ###

Returns the result of applying `f` to this scala.Option 's value if the
scala.Option is nonempty. Otherwise, evaluates expression `ifEmpty` .

* ifEmpty
  * the expression to evaluate if empty.
* f
  * the function to apply if nonempty.

* Definition Classes
  * Option
* Annotations
  * @ inline ()
* Note
  * This is equivalent to `scala.Option map f getOrElse ifEmpty` .

(defined at scala.Option)


### `final def forall(p: (Nothing) ⇒ Boolean): Boolean`                      ###

Returns true if this option is empty *or* the predicate `p` returns true when
applied to this scala.Option 's value.

* p
  * the predicate to test

* Definition Classes
  * Option
* Annotations
  * @ inline ()

(defined at scala.Option)


### `final def foreach[U](f: (Nothing) ⇒ U): Unit`                           ###

Apply the given procedure `f` to the option's value, if it is nonempty.
Otherwise, do nothing.

* f
  * the procedure to apply.

* Definition Classes
  * Option
* Annotations
  * @ inline ()
* See also
  * flatMap map

(defined at scala.Option)


### `final def getOrElse[B >: Nothing](default: ⇒ B): B`                     ###

Returns the option's value if the option is nonempty, otherwise return the
result of evaluating `default` .

* default
  * the default expression.

* Definition Classes
  * Option
* Annotations
  * @ inline ()

(defined at scala.Option)


### `def iterator: Iterator[Nothing]`                                        ###

Returns a singleton iterator returning the scala.Option 's value if it is
nonempty, or an empty iterator if the option is empty.

* Definition Classes
  * Option

(defined at scala.Option)


### `final def map[B](f: (Nothing) ⇒ B): Option[B]`                          ###

Returns a scala.Some containing the result of applying `f` to this scala.Option
's value if this scala.Option is nonempty. Otherwise return `None` .

* f
  * the function to apply

* Definition Classes
  * Option
* Annotations
  * @ inline ()
* Note
  * This is similar to `flatMap` except here, `f` does not need to wrap its
    result in an scala.Option.
* See also
  * foreach flatMap

(defined at scala.Option)


### `final def orElse[B >: Nothing](alternative: ⇒ Option[B]): Option[B]`    ###

Returns this scala.Option if it is nonempty, otherwise return the result of
evaluating `alternative` .

* alternative
  * the alternative expression.

* Definition Classes
  * Option
* Annotations
  * @ inline ()

(defined at scala.Option)


### `final def orNull[A1 >: Nothing](implicit ev: <:<[Null, A1]): A1`        ###

Returns the option's value if it is nonempty, or `null` if it is empty. Although
the use of null is discouraged, code written to use scala.Option must often
interface with code that expects and returns nulls.

* Definition Classes
  * Option
* Annotations
  * @ inline ()

Example:

```scala
val initialText: Option[String] = getInitialText
val textField = new JComponent(initialText.orNull,20)
```

(defined at scala.Option)


### `final def toLeft[X](right: ⇒ X): util.Either[Nothing, X]`               ###

Returns a scala.util.Right containing the given argument `right` if this is
empty, or a scala.util.Left containing this scala.Option 's value if this
scala.Option is nonempty.

* right
  * the expression to evaluate and return if this is empty

* Definition Classes
  * Option
* Annotations
  * @ inline ()
* See also
  * toRight

(defined at scala.Option)


### `def toList: List[Nothing]`                                              ###

Returns a singleton list containing the scala.Option 's value if it is nonempty,
or the empty list if the scala.Option is empty.

* Definition Classes
  * Option

(defined at scala.Option)


### `final def toRight[X](left: ⇒ X): util.Either[X, Nothing]`               ###

Returns a scala.util.Left containing the given argument `left` if this
scala.Option is empty, or a scala.util.Right containing this scala.Option 's
value if this is nonempty.

* left
  * the expression to evaluate and return if this is empty

* Definition Classes
  * Option
* Annotations
  * @ inline ()
* See also
  * toLeft

(defined at scala.Option)


### `final def withFilter(p: (Nothing) ⇒ Boolean): WithFilter`               ###

Necessary to keep scala.Option from being implicitly converted to
scala.collection.Iterable in `for` comprehensions.

* Definition Classes
  * Option
* Annotations
  * @ inline ()
(defined at scala.Option)
