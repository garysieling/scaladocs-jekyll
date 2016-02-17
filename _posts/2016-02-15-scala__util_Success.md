
#                              scala.util.Success                              #

```scala
final case class Success[+T](value: T) extends Try[T] with Product with Serializable
```

* Source
  * [Try.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/Try.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class WithFilter extends AnyRef`                                        ###

We need a whole WithFilter class to honor the "doesn't create a new collection"
contract even though it seems unlikely to matter much in a collection with max
size 1.

* Definition Classes
  * Try
* Annotations
  * @ deprecatedInheritance (message =..., since = "2.12")


--------------------------------------------------------------------------------
                 Instance Constructors From scala.util.Success
--------------------------------------------------------------------------------


### `new Success(value: T)`                                                  ###

(defined at scala.util.Success)


--------------------------------------------------------------------------------
                     Value Members From scala.util.Success
--------------------------------------------------------------------------------


### `def collect[U](pf: PartialFunction[T, U]): Try[U]`                      ###

Applies the given partial function to the value from this `Success` or returns
this if this is a `Failure` .

* Definition Classes
  * Success → Try

(defined at scala.util.Success)


### `def failed: Try[Throwable]`                                             ###

Inverts this `Try` . If this is a `Failure` , returns its exception wrapped in a
 `Success` . If this is a `Success` , returns a `Failure` containing an
 `UnsupportedOperationException` .

* Definition Classes
  * Success → Try

(defined at scala.util.Success)


### `def filter(p: (T) ⇒ Boolean): Try[T]`                                   ###

Converts this to a `Failure` if the predicate is not satisfied.

* Definition Classes
  * Success → Try

(defined at scala.util.Success)


### `def flatMap[U](f: (T) ⇒ Try[U]): Try[U]`                                ###

Returns the given function applied to the value from this `Success` or returns
this if this is a `Failure` .

* Definition Classes
  * Success → Try

(defined at scala.util.Success)


### `def flatten[U](implicit ev: <:<[T, Try[U]]): Try[U]`                    ###

Transforms a nested `Try` , ie, a `Try` of type `Try[Try[T]]` , into an
un-nested `Try` , ie, a `Try` of type `Try[T]` .

* Definition Classes
  * Success → Try

(defined at scala.util.Success)


### `def fold[U](fa: (Throwable) ⇒ U, fb: (T) ⇒ U): U`                       ###

Applies `fa` if this is a `Failure` or `fb` if this is a `Success` . If `fb` is
initially applied and throws an exception, then `fa` is applied with this
exception.

* fa
  * the function to apply if this is a `Failure`
* fb
  * the function to apply if this is a `Success`
* returns
  * the results of applying the function

* Definition Classes
  * Success → Try

Example:

```scala
val result: Try[Throwable, Int] = Try { string.toInt }
log(result.fold(
  ex => "Operation failed with " + ex,
  v => "Operation produced value: " + v
))
```

(defined at scala.util.Success)


### `def foreach[U](f: (T) ⇒ U): Unit`                                       ###

Applies the given function `f` if this is a `Success` , otherwise returns
 `Unit` if this is a `Failure` .

 _Note:_ If `f` throws, then this method may throw an exception.

* Definition Classes
  * Success → Try

(defined at scala.util.Success)


### `def getOrElse[U >: T](default: ⇒ U): U`                                 ###

Returns the value from this `Success` or the given `default` argument if this is
a `Failure` .

 _Note:_ : This will throw an exception if it is not a success and default
throws an exception.

* Definition Classes
  * Success → Try

(defined at scala.util.Success)


### `def map[U](f: (T) ⇒ U): Try[U]`                                         ###

Maps the given function to the value from this `Success` or returns this if this
is a `Failure` .

* Definition Classes
  * Success → Try

(defined at scala.util.Success)


### `def orElse[U >: T](default: ⇒ Try[U]): Try[U]`                          ###

Returns this `Try` if it's a `Success` or the given `default` argument if this
is a `Failure` .

* Definition Classes
  * Success → Try

(defined at scala.util.Success)


### `def recoverWith[U >: T](pf: PartialFunction[Throwable, Try[U]]): Try[U]` ###

Applies the given function `f` if this is a `Failure` , otherwise returns this
if this is a `Success` . This is like `flatMap` for the exception.

* Definition Classes
  * Success → Try

(defined at scala.util.Success)


### `def recover[U >: T](pf: PartialFunction[Throwable, U]): Try[U]`         ###

Applies the given function `f` if this is a `Failure` , otherwise returns this
if this is a `Success` . This is like map for the exception.

* Definition Classes
  * Success → Try

(defined at scala.util.Success)


### `def toEither: Either[Throwable, T]`                                     ###

Returns `Left` with `Throwable` if this is a `Failure` , otherwise returns
 `Right` with `Success` value.

* Definition Classes
  * Success → Try

(defined at scala.util.Success)


### `def transform[U](s: (T) ⇒ Try[U], f: (Throwable) ⇒ Try[U]): Try[U]`     ###

Completes this `Try` by applying the function `f` to this if this is of type
 `Failure` , or conversely, by applying `s` if this is a `Success` .

* Definition Classes
  * Success → Try

(defined at scala.util.Success)


--------------------------------------------------------------------------------
                       Value Members From scala.util.Try
--------------------------------------------------------------------------------


### `final def withFilter(p: (T) ⇒ Boolean): WithFilter`                     ###

Creates a non-strict filter, which eventually converts this to a `Failure` if
the predicate is not satisfied.

Note: unlike filter, withFilter does not create a new Try. Instead, it restricts
the domain of subsequent `map` , `flatMap` , `foreach` , and `withFilter`
operations.

As Try is a one-element collection, this may be a bit overkill, but it's
consistent with withFilter on Option and the other collections.

* p
  * the predicate used to test elements.
* returns
  * an object of class `WithFilter` , which supports `map` , `flatMap` ,
     `foreach` , and `withFilter` operations. All these operations apply to
    those elements of this Try which satisfy the predicate `p` .

* Definition Classes
  * Try
* Annotations
  * @ inline ()
(defined at scala.util.Try)
