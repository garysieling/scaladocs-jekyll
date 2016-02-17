
#                 scala.collection.parallel.CompositeThrowable                 #

```scala
final case class CompositeThrowable(throwables: Set[Throwable]) extends Exception with Product with Serializable
```

Composite throwable - thrown when multiple exceptions are thrown at the same
time.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ This class will be removed.
* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/package.scala#L1)


--------------------------------------------------------------------------------
                     Value Members From java.lang.Throwable
--------------------------------------------------------------------------------


### `final def addSuppressed(arg0: java.lang.Throwable): Unit`               ###

* Definition Classes
  * Throwable

(defined at java.lang.Throwable)


### `def fillInStackTrace(): java.lang.Throwable`                            ###

* Definition Classes
  * Throwable

(defined at java.lang.Throwable)


### `def getCause(): java.lang.Throwable`                                    ###

* Definition Classes
  * Throwable

(defined at java.lang.Throwable)


### `final def getSuppressed(): Array[java.lang.Throwable]`                  ###

* Definition Classes
  * Throwable

(defined at java.lang.Throwable)


### `def initCause(arg0: java.lang.Throwable): java.lang.Throwable`          ###

* Definition Classes
  * Throwable

(defined at java.lang.Throwable)


### `def printStackTrace(arg0: PrintStream): Unit`                           ###

* Definition Classes
  * Throwable

(defined at java.lang.Throwable)


### `def printStackTrace(arg0: PrintWriter): Unit`                           ###

* Definition Classes
  * Throwable

(defined at java.lang.Throwable)


### `def setStackTrace(arg0: Array[StackTraceElement]): Unit`                ###

* Definition Classes
  * Throwable

(defined at java.lang.Throwable)


--------------------------------------------------------------------------------
    Instance Constructors From scala.collection.parallel.CompositeThrowable
--------------------------------------------------------------------------------


### `new CompositeThrowable(throwables: Set[Throwable])`                     ###

(defined at scala.collection.parallel.CompositeThrowable)


--------------------------------------------------------------------------------
        Value Members From scala.collection.parallel.CompositeThrowable
--------------------------------------------------------------------------------


### `val throwables: Set[Throwable]`                                         ###

(defined at scala.collection.parallel.CompositeThrowable)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from CompositeThrowable to
    CollectionsHaveToParArray [CompositeThrowable, T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (CompositeThrowable) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
