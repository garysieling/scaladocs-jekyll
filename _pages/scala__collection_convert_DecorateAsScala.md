
#                   scala.collection.convert.DecorateAsScala                   #

```scala
trait DecorateAsScala extends AnyRef
```

* Source
  * [DecorateAsScala.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/convert/DecorateAsScala.scala#L1)


--------------------------------------------------------------------------------
          Value Members From scala.collection.convert.DecorateAsScala
--------------------------------------------------------------------------------


### `implicit def asScalaBufferConverter[A](l: java.util.List[A]): Decorators.AsScala[Buffer[A]]` ###

Adds an `asScala` method that implicitly converts a Java `List` to a Scala
mutable `Buffer` .

The returned Scala `Buffer` is backed by the provided Java `List` and any
side-effects of using it via the Scala interface will be visible via the Java
interface and vice versa.

If the Java `List` was previously obtained from an implicit or explicit call of
 `asList(scala.collection.mutable.Buffer)` then the original Scala `Buffer` will
be returned.

* l
  * The `List` to be converted.
* returns
  * An object with an `asScala` method that returns a Scala mutable `Buffer`
    view of the argument.

(defined at scala.collection.convert.DecorateAsScala)


### `implicit def asScalaIteratorConverter[A](i: java.util.Iterator[A]): Decorators.AsScala[Iterator[A]]` ###

Adds an `asScala` method that implicitly converts a Java `Iterator` to a Scala
 `Iterator` .

The returned Scala `Iterator` is backed by the provided Java `Iterator` and any
side-effects of using it via the Scala interface will be visible via the Java
interface and vice versa.

If the Java `Iterator` was previously obtained from an implicit or explicit call
of `asIterator(scala.collection.Iterator)` then the original Scala `Iterator`
will be returned.

* i
  * The `Iterator` to be converted.
* returns
  * An object with an `asScala` method that returns a Scala `Iterator` view of
    the argument.

(defined at scala.collection.convert.DecorateAsScala)


### `implicit def asScalaSetConverter[A](s: java.util.Set[A]): Decorators.AsScala[mutable.Set[A]]` ###

Adds an `asScala` method that implicitly converts a Java `Set` to a Scala
mutable `Set` .

The returned Scala `Set` is backed by the provided Java `Set` and any
side-effects of using it via the Scala interface will be visible via the Java
interface and vice versa.

If the Java `Set` was previously obtained from an implicit or explicit call of
 `asSet(scala.collection.mutable.Set)` then the original Scala `Set` will be
returned.

* s
  * The `Set` to be converted.
* returns
  * An object with an `asScala` method that returns a Scala mutable `Set` view
    of the argument.

(defined at scala.collection.convert.DecorateAsScala)


### `implicit def collectionAsScalaIterableConverter[A](i: Collection[A]): Decorators.AsScala[Iterable[A]]` ###

Adds an `asScala` method that implicitly converts a Java `Collection` to an
Scala `Iterable` .

If the Java `Collection` was previously obtained from an implicit or explicit
call of `asCollection(scala.collection.SizedIterable)` then the original Scala
 `SizedIterable` will be returned.

* i
  * The `Collection` to be converted.
* returns
  * An object with an `asScala` method that returns a Scala `SizedIterable` view
    of the argument.

(defined at scala.collection.convert.DecorateAsScala)


### `implicit def dictionaryAsScalaMapConverter[A, B](p: Dictionary[A, B]): Decorators.AsScala[mutable.Map[A, B]]` ###

Adds an `asScala` method that implicitly converts a Java `Dictionary` to a Scala
mutable `Map[String, String]` . The returned Scala `Map[String, String]` is
backed by the provided Java `Dictionary` and any side-effects of using it via
the Scala interface will be visible via the Java interface and vice versa.

* p
  * The `Dictionary` to be converted.
* returns
  * An object with an `asScala` method that returns a Scala mutable
     `Map[String, String]` view of the argument.

(defined at scala.collection.convert.DecorateAsScala)


### `implicit def enumerationAsScalaIteratorConverter[A](i: java.util.Enumeration[A]): Decorators.AsScala[Iterator[A]]` ###

Adds an `asScala` method that implicitly converts a Java `Enumeration` to a
Scala `Iterator` .

The returned Scala `Iterator` is backed by the provided Java `Enumeration` and
any side-effects of using it via the Scala interface will be visible via the
Java interface and vice versa.

If the Java `Enumeration` was previously obtained from an implicit or explicit
call of `asEnumeration(scala.collection.Iterator)` then the original Scala
 `Iterator` will be returned.

* i
  * The `Enumeration` to be converted.
* returns
  * An object with an `asScala` method that returns a Scala `Iterator` view of
    the argument.

(defined at scala.collection.convert.DecorateAsScala)


### `implicit def iterableAsScalaIterableConverter[A](i: java.lang.Iterable[A]): Decorators.AsScala[Iterable[A]]` ###

Adds an `asScala` method that implicitly converts a Java `Iterable` to a Scala
 `Iterable` .

The returned Scala `Iterable` is backed by the provided Java `Iterable` and any
side-effects of using it via the Scala interface will be visible via the Java
interface and vice versa.

If the Java `Iterable` was previously obtained from an implicit or explicit call
of `asIterable(scala.collection.Iterable)` then the original Scala `Iterable`
will be returned.

* i
  * The `Iterable` to be converted.
* returns
  * An object with an `asScala` method that returns a Scala `Iterable` view of
    the argument.

(defined at scala.collection.convert.DecorateAsScala)


### `implicit def mapAsScalaConcurrentMapConverter[A, B](m: ConcurrentMap[A, B]): Decorators.AsScala[concurrent.Map[A, B]]` ###

Adds an `asScala` method that implicitly converts a Java `ConcurrentMap` to a
Scala mutable `concurrent.Map` . The returned Scala `concurrent.Map` is backed
by the provided Java `ConcurrentMap` and any side-effects of using it via the
Scala interface will be visible via the Java interface and vice versa.

If the Java `ConcurrentMap` was previously obtained from an implicit or explicit
call of `mapAsScalaConcurrentMap(scala.collection.mutable.ConcurrentMap)` then
the original Scala `concurrent.Map` will be returned.

* m
  * The `ConcurrentMap` to be converted.
* returns
  * An object with an `asScala` method that returns a Scala mutable
     `concurrent.Map` view of the argument.

(defined at scala.collection.convert.DecorateAsScala)


### `implicit def mapAsScalaMapConverter[A, B](m: java.util.Map[A, B]): Decorators.AsScala[mutable.Map[A, B]]` ###

Adds an `asScala` method that implicitly converts a Java `Map` to a Scala
mutable `Map` . The returned Scala `Map` is backed by the provided Java `Map`
and any side-effects of using it via the Scala interface will be visible via the
Java interface and vice versa.

If the Java `Map` was previously obtained from an implicit or explicit call of
 `asMap(scala.collection.mutable.Map)` then the original Scala `Map` will be
returned.

If the wrapped map is synchronized (e.g. from
 `java.util.Collections.synchronizedMap` ), it is your responsibility to wrap
all non-atomic operations with `underlying.synchronized` . This includes `get` ,
as `java.util.Map` 's API does not allow for an atomic `get` when `null` values
may be present.

* m
  * The `Map` to be converted.
* returns
  * An object with an `asScala` method that returns a Scala mutable `Map` view
    of the argument.

(defined at scala.collection.convert.DecorateAsScala)


### `implicit def propertiesAsScalaMapConverter(p: Properties): Decorators.AsScala[mutable.Map[String, String]]` ###

Adds an `asScala` method that implicitly converts a Java `Properties` to a Scala
mutable `Map[String, String]` . The returned Scala `Map[String, String]` is
backed by the provided Java `Properties` and any side-effects of using it via
the Scala interface will be visible via the Java interface and vice versa.

* p
  * The `Properties` to be converted.
* returns
  * An object with an `asScala` method that returns a Scala mutable
     `Map[String, String]` view of the argument.
(defined at scala.collection.convert.DecorateAsScala)
