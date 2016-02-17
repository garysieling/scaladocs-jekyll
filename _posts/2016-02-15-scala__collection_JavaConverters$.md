
#                       scala.collection.JavaConverters                       #

```scala
object JavaConverters extends DecorateAsJava with DecorateAsScala
```

A collection of decorators that allow converting between Scala and Java
collections using `asScala` and `asJava` methods.

The following conversions are supported via `asJava` , `asScala`

*  `scala.collection.Iterable` <=> `java.lang.Iterable`
*  `scala.collection.Iterator` <=> `java.util.Iterator`
*  `scala.collection.mutable.Buffer` <=> `java.util.List`
*  `scala.collection.mutable.Set` <=> `java.util.Set`
*  `scala.collection.mutable.Map` <=> `java.util.Map`
*  `scala.collection.mutable.concurrent.Map` <=>
    `java.util.concurrent.ConcurrentMap`

In all cases, converting from a source type to a target type and back again will
return the original source object, e.g.

```scala
import scala.collection.JavaConverters._

val sl = new scala.collection.mutable.ListBuffer[Int]
val jl : java.util.List[Int] = sl.asJava
val sl2 : scala.collection.mutable.Buffer[Int] = jl.asScala
assert(sl eq sl2)
```

The following conversions are also supported, but the direction from Scala to
Java is done by the more specifically named methods: `asJavaCollection` ,
 `asJavaEnumeration` , `asJavaDictionary` .

*  `scala.collection.Iterable` <=> `java.util.Collection`
*  `scala.collection.Iterator` <=> `java.util.Enumeration`
*  `scala.collection.mutable.Map` <=> `java.util.Dictionary`

In addition, the following one way conversions are provided via `asJava` :

*  `scala.collection.Seq` => `java.util.List`
*  `scala.collection.mutable.Seq` => `java.util.List`
*  `scala.collection.Set` => `java.util.Set`
*  `scala.collection.Map` => `java.util.Map`

The following one way conversion is provided via `asScala` :

*  `java.util.Properties` => `scala.collection.mutable.Map`

* Source
  * [JavaConverters.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/JavaConverters.scala#L1)
* Since
  * 2.8.1


--------------------------------------------------------------------------------
           Value Members From scala.collection.convert.DecorateAsJava
--------------------------------------------------------------------------------


### `implicit def asJavaCollectionConverter[A](i: Iterable[A]): convert.Decorators.AsJavaCollection[A]` ###

Adds an `asJavaCollection` method that implicitly converts a Scala `Iterable` to
an immutable Java `Collection` .

If the Scala `Iterable` was previously obtained from an implicit or explicit
call of `asSizedIterable(java.util.Collection)` then the original Java
 `Collection` will be returned.

* i
  * The `SizedIterable` to be converted.
* returns
  * An object with an `asJava` method that returns a Java `Collection` view of
    the argument.

* Definition Classes
  * DecorateAsJava

(defined at scala.collection.convert.DecorateAsJava)


### `implicit def asJavaDictionaryConverter[A, B](m: mutable.Map[A, B]): convert.Decorators.AsJavaDictionary[A, B]` ###

Adds an `asJavaDictionary` method that implicitly converts a Scala mutable
 `Map` to a Java `Dictionary` .

The returned Java `Dictionary` is backed by the provided Scala `Dictionary` and
any side-effects of using it via the Java interface will be visible via the
Scala interface and vice versa.

If the Scala `Dictionary` was previously obtained from an implicit or explicit
call of `asMap(java.util.Dictionary)` then the original Java `Dictionary` will
be returned.

* m
  * The `Map` to be converted.
* returns
  * An object with an `asJavaDictionary` method that returns a Java
     `Dictionary` view of the argument.

* Definition Classes
  * DecorateAsJava

(defined at scala.collection.convert.DecorateAsJava)


### `implicit def asJavaEnumerationConverter[A](i: Iterator[A]): convert.Decorators.AsJavaEnumeration[A]` ###

Adds an `asJavaEnumeration` method that implicitly converts a Scala `Iterator`
to a Java `Enumeration` . The returned Java `Enumeration` is backed by the
provided Scala `Iterator` and any side-effects of using it via the Java
interface will be visible via the Scala interface and vice versa.

If the Scala `Iterator` was previously obtained from an implicit or explicit
call of `asIterator(java.util.Enumeration)` then the original Java
 `Enumeration` will be returned.

* i
  * The `Iterator` to be converted.
* returns
  * An object with an `asJavaEnumeration` method that returns a Java
     `Enumeration` view of the argument.

* Definition Classes
  * DecorateAsJava

(defined at scala.collection.convert.DecorateAsJava)


### `implicit def asJavaIterableConverter[A](i: Iterable[A]): convert.Decorators.AsJava[java.lang.Iterable[A]]` ###

Adds an `asJava` method that implicitly converts a Scala `Iterable` to a Java
 `Iterable` .

The returned Java `Iterable` is backed by the provided Scala `Iterable` and any
side-effects of using it via the Java interface will be visible via the Scala
interface and vice versa.

If the Scala `Iterable` was previously obtained from an implicit or explicit
call of `asIterable(java.lang.Iterable)` then the original Java `Iterable` will
be returned.

* i
  * The `Iterable` to be converted.
* returns
  * An object with an `asJavaCollection` method that returns a Java `Iterable`
    view of the argument.

* Definition Classes
  * DecorateAsJava

(defined at scala.collection.convert.DecorateAsJava)


### `implicit def asJavaIteratorConverter[A](i: Iterator[A]): convert.Decorators.AsJava[java.util.Iterator[A]]` ###

Adds an `asJava` method that implicitly converts a Scala `Iterator` to a Java
 `Iterator` . The returned Java `Iterator` is backed by the provided Scala
 `Iterator` and any side-effects of using it via the Java interface will be
visible via the Scala interface and vice versa.

If the Scala `Iterator` was previously obtained from an implicit or explicit
call of `asIterator(java.util.Iterator)` then the original Java `Iterator` will
be returned by the `asJava` method.

* i
  * The `Iterator` to be converted.
* returns
  * An object with an `asJava` method that returns a Java `Iterator` view of the
    argument.

* Definition Classes
  * DecorateAsJava

(defined at scala.collection.convert.DecorateAsJava)


### `implicit def bufferAsJavaListConverter[A](b: Buffer[A]): convert.Decorators.AsJava[java.util.List[A]]` ###

Adds an `asJava` method that implicitly converts a Scala mutable `Buffer` to a
Java `List` .

The returned Java `List` is backed by the provided Scala `Buffer` and any
side-effects of using it via the Java interface will be visible via the Scala
interface and vice versa.

If the Scala `Buffer` was previously obtained from an implicit or explicit call
of `asBuffer(java.util.List)` then the original Java `List` will be returned.

* b
  * The `Buffer` to be converted.
* returns
  * An object with an `asJava` method that returns a Java `List` view of the
    argument.

* Definition Classes
  * DecorateAsJava

(defined at scala.collection.convert.DecorateAsJava)


### `implicit def mapAsJavaConcurrentMapConverter[A, B](m: concurrent.Map[A, B]): convert.Decorators.AsJava[ConcurrentMap[A, B]]` ###

Adds an `asJava` method that implicitly converts a Scala mutable
 `concurrent.Map` to a Java `ConcurrentMap` .

The returned Java `ConcurrentMap` is backed by the provided Scala
 `concurrent.Map` and any side-effects of using it via the Java interface will
be visible via the Scala interface and vice versa.

If the Scala `concurrent.Map` was previously obtained from an implicit or
explicit call of `asConcurrentMap(java.util.concurrent.ConcurrentMap)` then the
original Java `ConcurrentMap` will be returned.

* m
  * The Scala `concurrent.Map` to be converted.
* returns
  * An object with an `asJava` method that returns a Java `ConcurrentMap` view
    of the argument.

* Definition Classes
  * DecorateAsJava

(defined at scala.collection.convert.DecorateAsJava)


### `implicit def mapAsJavaMapConverter[A, B](m: Map[A, B]): convert.Decorators.AsJava[java.util.Map[A, B]]` ###

Adds an `asJava` method that implicitly converts a Scala `Map` to a Java `Map` .

The returned Java `Map` is backed by the provided Scala `Map` and any
side-effects of using it via the Java interface will be visible via the Scala
interface and vice versa.

If the Scala `Map` was previously obtained from an implicit or explicit call of
 `asMap(java.util.Map)` then the original Java `Map` will be returned.

* m
  * The `Map` to be converted.
* returns
  * An object with an `asJava` method that returns a Java `Map` view of the
    argument.

* Definition Classes
  * DecorateAsJava

(defined at scala.collection.convert.DecorateAsJava)


### `implicit def mutableMapAsJavaMapConverter[A, B](m: mutable.Map[A, B]): convert.Decorators.AsJava[java.util.Map[A, B]]` ###

Adds an `asJava` method that implicitly converts a Scala mutable `Map` to a Java
 `Map` .

The returned Java `Map` is backed by the provided Scala `Map` and any
side-effects of using it via the Java interface will be visible via the Scala
interface and vice versa.

If the Scala `Map` was previously obtained from an implicit or explicit call of
 `asMap(java.util.Map)` then the original Java `Map` will be returned.

* m
  * The `Map` to be converted.
* returns
  * An object with an `asJava` method that returns a Java `Map` view of the
    argument.

* Definition Classes
  * DecorateAsJava

(defined at scala.collection.convert.DecorateAsJava)


### `implicit def mutableSeqAsJavaListConverter[A](b: mutable.Seq[A]): convert.Decorators.AsJava[java.util.List[A]]` ###

Adds an `asJava` method that implicitly converts a Scala mutable `Seq` to a Java
 `List` .

The returned Java `List` is backed by the provided Scala `Seq` and any
side-effects of using it via the Java interface will be visible via the Scala
interface and vice versa.

If the Scala `Seq` was previously obtained from an implicit or explicit call of
 `asSeq(java.util.List)` then the original Java `List` will be returned.

* b
  * The `Seq` to be converted.
* returns
  * An object with an `asJava` method that returns a Java `List` view of the
    argument.

* Definition Classes
  * DecorateAsJava

(defined at scala.collection.convert.DecorateAsJava)


### `implicit def mutableSetAsJavaSetConverter[A](s: mutable.Set[A]): convert.Decorators.AsJava[java.util.Set[A]]` ###

Adds an `asJava` method that implicitly converts a Scala mutable `Set` > to a
Java `Set` .

The returned Java `Set` is backed by the provided Scala `Set` and any
side-effects of using it via the Java interface will be visible via the Scala
interface and vice versa.

If the Scala `Set` was previously obtained from an implicit or explicit call of
 `asSet(java.util.Set)` then the original Java `Set` will be returned.

* s
  * The `Set` to be converted.
* returns
  * An object with an `asJava` method that returns a Java `Set` view of the
    argument.

* Definition Classes
  * DecorateAsJava

(defined at scala.collection.convert.DecorateAsJava)


### `implicit def seqAsJavaListConverter[A](b: Seq[A]): convert.Decorators.AsJava[java.util.List[A]]` ###

Adds an `asJava` method that implicitly converts a Scala `Seq` to a Java `List` .

The returned Java `List` is backed by the provided Scala `Seq` and any
side-effects of using it via the Java interface will be visible via the Scala
interface and vice versa.

If the Scala `Seq` was previously obtained from an implicit or explicit call of
 `asSeq(java.util.List)` then the original Java `List` will be returned.

* b
  * The `Seq` to be converted.
* returns
  * An object with an `asJava` method that returns a Java `List` view of the
    argument.

* Definition Classes
  * DecorateAsJava

(defined at scala.collection.convert.DecorateAsJava)


### `implicit def setAsJavaSetConverter[A](s: Set[A]): convert.Decorators.AsJava[java.util.Set[A]]` ###

Adds an `asJava` method that implicitly converts a Scala `Set` to a Java `Set` .

The returned Java `Set` is backed by the provided Scala `Set` and any
side-effects of using it via the Java interface will be visible via the Scala
interface and vice versa.

If the Scala `Set` was previously obtained from an implicit or explicit call of
 `asSet(java.util.Set)` then the original Java `Set` will be returned.

* s
  * The `Set` to be converted.
* returns
  * An object with an `asJava` method that returns a Java `Set` view of the
    argument.

* Definition Classes
  * DecorateAsJava

(defined at scala.collection.convert.DecorateAsJava)


--------------------------------------------------------------------------------
          Value Members From scala.collection.convert.DecorateAsScala
--------------------------------------------------------------------------------


### `implicit def asScalaBufferConverter[A](l: java.util.List[A]): convert.Decorators.AsScala[Buffer[A]]` ###

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

* Definition Classes
  * DecorateAsScala

(defined at scala.collection.convert.DecorateAsScala)


### `implicit def asScalaIteratorConverter[A](i: java.util.Iterator[A]): convert.Decorators.AsScala[Iterator[A]]` ###

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

* Definition Classes
  * DecorateAsScala

(defined at scala.collection.convert.DecorateAsScala)


### `implicit def asScalaSetConverter[A](s: java.util.Set[A]): convert.Decorators.AsScala[mutable.Set[A]]` ###

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

* Definition Classes
  * DecorateAsScala

(defined at scala.collection.convert.DecorateAsScala)


### `implicit def collectionAsScalaIterableConverter[A](i: Collection[A]): convert.Decorators.AsScala[Iterable[A]]` ###

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

* Definition Classes
  * DecorateAsScala

(defined at scala.collection.convert.DecorateAsScala)


### `implicit def dictionaryAsScalaMapConverter[A, B](p: Dictionary[A, B]): convert.Decorators.AsScala[mutable.Map[A, B]]` ###

Adds an `asScala` method that implicitly converts a Java `Dictionary` to a Scala
mutable `Map[String, String]` . The returned Scala `Map[String, String]` is
backed by the provided Java `Dictionary` and any side-effects of using it via
the Scala interface will be visible via the Java interface and vice versa.

* p
  * The `Dictionary` to be converted.
* returns
  * An object with an `asScala` method that returns a Scala mutable
     `Map[String, String]` view of the argument.

* Definition Classes
  * DecorateAsScala

(defined at scala.collection.convert.DecorateAsScala)


### `implicit def enumerationAsScalaIteratorConverter[A](i: java.util.Enumeration[A]): convert.Decorators.AsScala[Iterator[A]]` ###

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

* Definition Classes
  * DecorateAsScala

(defined at scala.collection.convert.DecorateAsScala)


### `implicit def iterableAsScalaIterableConverter[A](i: java.lang.Iterable[A]): convert.Decorators.AsScala[Iterable[A]]` ###

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

* Definition Classes
  * DecorateAsScala

(defined at scala.collection.convert.DecorateAsScala)


### `implicit def mapAsScalaConcurrentMapConverter[A, B](m: ConcurrentMap[A, B]): convert.Decorators.AsScala[concurrent.Map[A, B]]` ###

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

* Definition Classes
  * DecorateAsScala

(defined at scala.collection.convert.DecorateAsScala)


### `implicit def mapAsScalaMapConverter[A, B](m: java.util.Map[A, B]): convert.Decorators.AsScala[mutable.Map[A, B]]` ###

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

* Definition Classes
  * DecorateAsScala

(defined at scala.collection.convert.DecorateAsScala)


### `implicit def propertiesAsScalaMapConverter(p: Properties): convert.Decorators.AsScala[mutable.Map[String, String]]` ###

Adds an `asScala` method that implicitly converts a Java `Properties` to a Scala
mutable `Map[String, String]` . The returned Scala `Map[String, String]` is
backed by the provided Java `Properties` and any side-effects of using it via
the Scala interface will be visible via the Java interface and vice versa.

* p
  * The `Properties` to be converted.
* returns
  * An object with an `asScala` method that returns a Scala mutable
     `Map[String, String]` view of the argument.

* Definition Classes
  * DecorateAsScala
(defined at scala.collection.convert.DecorateAsScala)
