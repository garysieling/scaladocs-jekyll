
#                           scala.concurrent.SyncVar                           #

```scala
class SyncVar[A] extends AnyRef
```

A class to provide safe concurrent access to a mutable cell. All methods are
synchronized.

* A
  * type of the contained value

* Source
  * [SyncVar.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/SyncVar.scala#L1)
* Version
  * 1.0, 10/03/2003


--------------------------------------------------------------------------------
             Deprecated Value Members From scala.concurrent.SyncVar
--------------------------------------------------------------------------------


### `def set(x: A): Unit`                                                    ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ Use `put` instead, as `set` is potentially
    error-prone

(defined at scala.concurrent.SyncVar)


--------------------------------------------------------------------------------
              Instance Constructors From scala.concurrent.SyncVar
--------------------------------------------------------------------------------


### `new SyncVar()`                                                          ###

(defined at scala.concurrent.SyncVar)


--------------------------------------------------------------------------------
                  Value Members From scala.concurrent.SyncVar
--------------------------------------------------------------------------------


### `def get(timeout: Long): Option[A]`                                      ###

Wait at least `timeout` milliseconds (possibly more) for this `SyncVar` to
become defined and then get its value.

* timeout
  * time in milliseconds to wait
* returns
  * `None` if variable is undefined after `timeout` , `Some(value)` otherwise

(defined at scala.concurrent.SyncVar)


### `def put(x: A): Unit`                                                    ###

Place a value in the SyncVar. If the SyncVar already has a stored value, wait
until another thread takes it.

(defined at scala.concurrent.SyncVar)


### `def take(timeout: Long): A`                                             ###

Wait at least `timeout` milliseconds (possibly more) for this `SyncVar` to
become defined and then get the stored value, unsetting it as a side effect.

* timeout
  * the amount of milliseconds to wait
* returns
  * the value or a throws an exception if the timeout occurs

* Exceptions thrown
  * NoSuchElementException on timeout
(defined at scala.concurrent.SyncVar)
