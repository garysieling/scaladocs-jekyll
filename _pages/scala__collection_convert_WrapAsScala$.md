
#                     scala.collection.convert.WrapAsScala                     #

```scala
object WrapAsScala extends WrapAsScala
```

* Source
  * [WrapAsScala.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/convert/WrapAsScala.scala#L1)


--------------------------------------------------------------------------------
            Value Members From scala.collection.convert.WrapAsScala
--------------------------------------------------------------------------------


### `implicit def asScalaBuffer[A](l: java.util.List[A]): Buffer[A]`         ###

Implicitly converts a Java `List` to a Scala mutable `Buffer` .

The returned Scala `Buffer` is backed by the provided Java `List` and any
side-effects of using it via the Scala interface will be visible via the Java
interface and vice versa.

If the Java `List` was previously obtained from an implicit or explicit call of
 `asScalaBuffer(scala.collection.mutable.Buffer)` then the original Scala
 `Buffer` will be returned.

* l
  * The `List` to be converted.
* returns
  * A Scala mutable `Buffer` view of the argument.

* Definition Classes
  * WrapAsScala

(defined at scala.collection.convert.WrapAsScala)


### `implicit def asScalaIterator[A](it: java.util.Iterator[A]): Iterator[A]` ###

Implicitly converts a Java `Iterator` to a Scala `Iterator` .

The returned Scala `Iterator` is backed by the provided Java `Iterator` and any
side-effects of using it via the Scala interface will be visible via the Java
interface and vice versa.

If the Java `Iterator` was previously obtained from an implicit or explicit call
of `asIterator(scala.collection.Iterator)` then the original Scala `Iterator`
will be returned.

* it
  * The `Iterator` to be converted.
* returns
  * A Scala `Iterator` view of the argument.

* Definition Classes
  * WrapAsScala

(defined at scala.collection.convert.WrapAsScala)


### `implicit def asScalaSet[A](s: java.util.Set[A]): mutable.Set[A]`        ###

Implicitly converts a Java Set to a Scala mutable Set. The returned Scala Set is
backed by the provided Java Set and any side-effects of using it via the Scala
interface will be visible via the Java interface and vice versa.

If the Java Set was previously obtained from an implicit or explicit call of
 `asScalaSet(scala.collection.mutable.Set)` then the original Scala Set will be
returned.

* s
  * The Set to be converted.
* returns
  * A Scala mutable Set view of the argument.

* Definition Classes
  * WrapAsScala

(defined at scala.collection.convert.WrapAsScala)


### `implicit def collectionAsScalaIterable[A](i: Collection[A]): Iterable[A]` ###

Implicitly converts a Java `Collection` to an Scala `Iterable` .

If the Java `Collection` was previously obtained from an implicit or explicit
call of `collectionAsScalaIterable(scala.collection.SizedIterable)` then the
original Scala `Iterable` will be returned.

* i
  * The Collection to be converted.
* returns
  * A Scala Iterable view of the argument.

* Definition Classes
  * WrapAsScala

(defined at scala.collection.convert.WrapAsScala)


### `implicit def dictionaryAsScalaMap[A, B](p: Dictionary[A, B]): mutable.Map[A, B]` ###

Implicitly converts a Java `Dictionary` to a Scala mutable `Map` .

The returned Scala `Map` is backed by the provided Java `Dictionary` and any
side-effects of using it via the Scala interface will be visible via the Java
interface and vice versa.

* p
  * The Dictionary to be converted.
* returns
  * A Scala mutable Map view of the argument.

* Definition Classes
  * WrapAsScala

(defined at scala.collection.convert.WrapAsScala)


### `implicit def enumerationAsScalaIterator[A](i: java.util.Enumeration[A]): Iterator[A]` ###

Implicitly converts a Java Enumeration to a Scala Iterator. The returned Scala
Iterator is backed by the provided Java Enumeration and any side-effects of
using it via the Scala interface will be visible via the Java interface and vice
versa.

If the Java Enumeration was previously obtained from an implicit or explicit
call of `enumerationAsScalaIterator(scala.collection.Iterator)` then the
original Scala Iterator will be returned.

* i
  * The Enumeration to be converted.
* returns
  * A Scala Iterator view of the argument.

* Definition Classes
  * WrapAsScala

(defined at scala.collection.convert.WrapAsScala)


### `implicit def iterableAsScalaIterable[A](i: java.lang.Iterable[A]): Iterable[A]` ###

Implicitly converts a Java `Iterable` to a Scala `Iterable` .

The returned Scala `Iterable` is backed by the provided Java `Iterable` and any
side-effects of using it via the Scala interface will be visible via the Java
interface and vice versa.

If the Java `Iterable` was previously obtained from an implicit or explicit call
of `iterableAsScalaIterable(scala.collection.Iterable)` then the original Scala
Iterable will be returned.

* i
  * The Iterable to be converted.
* returns
  * A Scala Iterable view of the argument.

* Definition Classes
  * WrapAsScala

(defined at scala.collection.convert.WrapAsScala)


### `implicit def mapAsScalaConcurrentMap[A, B](m: ConcurrentMap[A, B]): concurrent.Map[A, B]` ###

Implicitly converts a Java ConcurrentMap to a Scala mutable ConcurrentMap. The
returned Scala ConcurrentMap is backed by the provided Java ConcurrentMap and
any side-effects of using it via the Scala interface will be visible via the
Java interface and vice versa.

If the Java ConcurrentMap was previously obtained from an implicit or explicit
call of `asConcurrentMap(scala.collection.mutable.ConcurrentMap)` then the
original Scala ConcurrentMap will be returned.

* m
  * The ConcurrentMap to be converted.
* returns
  * A Scala mutable ConcurrentMap view of the argument.

* Definition Classes
  * WrapAsScala

(defined at scala.collection.convert.WrapAsScala)


### `implicit def mapAsScalaMap[A, B](m: java.util.Map[A, B]): mutable.Map[A, B]` ###

Implicitly converts a Java `Map` to a Scala mutable `Map` .

The returned Scala `Map` is backed by the provided Java `Map` and any
side-effects of using it via the Scala interface will be visible via the Java
interface and vice versa.

If the Java `Map` was previously obtained from an implicit or explicit call of
 `mapAsScalaMap(scala.collection.mutable.Map)` then the original Scala Map will
be returned.

If the wrapped map is synchronized (e.g. from
 `java.util.Collections.synchronizedMap` ), it is your responsibility to wrap
all non-atomic operations with `underlying.synchronized` . This includes `get` ,
as `java.util.Map` 's API does not allow for an atomic `get` when `null` values
may be present.

* m
  * The Map to be converted.
* returns
  * A Scala mutable Map view of the argument.

* Definition Classes
  * WrapAsScala

(defined at scala.collection.convert.WrapAsScala)


### `implicit def propertiesAsScalaMap(p: Properties): mutable.Map[String, String]` ###

Implicitly converts a Java `Properties` to a Scala
 `mutable Map[String, String]` .

The returned Scala `Map[String, String]` is backed by the provided Java
 `Properties` and any side-effects of using it via the Scala interface will be
visible via the Java interface and vice versa.

* p
  * The Properties to be converted.
* returns
  * A Scala mutable Map[String, String] view of the argument.

* Definition Classes
  * WrapAsScala
(defined at scala.collection.convert.WrapAsScala)
