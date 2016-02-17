
#                      scala.util.control.Exception.Catch                      #

```scala
class Catch[+T] extends Described
```

A container class for catch/finally logic.

Pass a different value for rethrow if you want to probably unwisely allow
catching control exceptions and other throwables which the rest of the world may
expect to get through.

* Source
  * [Exception.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/control/Exception.scala#L1)


--------------------------------------------------------------------------------
         Instance Constructors From scala.util.control.Exception.Catch
--------------------------------------------------------------------------------


### `new Catch(pf: Catcher[T], fin: Option[Finally] = None, rethrow: (Throwable) ⇒ Boolean = shouldRethrow)` ###

(defined at scala.util.control.Exception.Catch)


--------------------------------------------------------------------------------
             Value Members From scala.util.control.Exception.Catch
--------------------------------------------------------------------------------


### `def andFinally(body: ⇒ Unit): Catch[T]`                                 ###

(defined at scala.util.control.Exception.Catch)


### `def apply[U >: T](body: ⇒ U): U`                                        ###

Apply this catch logic to the supplied body.

(defined at scala.util.control.Exception.Catch)


### `def either[U >: T](body: ⇒ U): Either[Throwable, U]`                    ###

Apply this catch logic to the supplied body, mapping the result into
Either[Throwable, T] - Left(exception) if an exception was caught, Right(T)
otherwise.

(defined at scala.util.control.Exception.Catch)


### `val fin: Option[Finally]`                                               ###

(defined at scala.util.control.Exception.Catch)


### `def opt[U >: T](body: ⇒ U): Option[U]`                                  ###

Apply this catch logic to the supplied body, mapping the result into
 `Option[T]` - `None` if any exception was caught, `Some(T)` otherwise.

(defined at scala.util.control.Exception.Catch)


### `def or[U >: T](other: Catch[U]): Catch[U]`                              ###

(defined at scala.util.control.Exception.Catch)


### `def or[U >: T](pf2: Catcher[U]): Catch[U]`                              ###

Create a new Catch with additional exception handling logic.

(defined at scala.util.control.Exception.Catch)


### `val pf: Catcher[T]`                                                     ###

(defined at scala.util.control.Exception.Catch)


### `val rethrow: (Throwable) ⇒ Boolean`                                     ###

(defined at scala.util.control.Exception.Catch)


### `def toEither: Catch[Either[Throwable, T]]`                              ###

(defined at scala.util.control.Exception.Catch)


### `def toOption: Catch[Option[T]]`                                         ###

Convenience methods.

(defined at scala.util.control.Exception.Catch)


### `def toTry: Catch[Try[T]]`                                               ###

(defined at scala.util.control.Exception.Catch)


### `def withApply[U](f: (Throwable) ⇒ U): Catch[U]`                         ###

Create a `Catch` object with the same `isDefinedAt` logic as this one, but with
the supplied `apply` method replacing the current one.

(defined at scala.util.control.Exception.Catch)


### `def withTry[U >: T](body: ⇒ U): Try[U]`                                 ###

Apply this catch logic to the supplied body, mapping the result into Try[T] -
Failure if an exception was caught, Success(T) otherwise.

(defined at scala.util.control.Exception.Catch)


--------------------------------------------------------------------------------
           Value Members From scala.util.control.Exception.Described
--------------------------------------------------------------------------------


### `def withDesc(s: String): Catch.this.type`                               ###

* Definition Classes
  * Described
(defined at scala.util.control.Exception.Described)
