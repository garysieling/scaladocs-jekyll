
#                   scala.collection.convert.DecorateAsJava                   #

```scala
trait DecorateAsJava extends AnyRef
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
  * [DecorateAsJava.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/convert/DecorateAsJava.scala#L1)
* Since
  * 2.8.1


--------------------------------------------------------------------------------
           Value Members From scala.collection.convert.DecorateAsJava
--------------------------------------------------------------------------------


### `implicit def asJavaCollectionConverter[A](i: Iterable[A]): Decorators.AsJavaCollection[A]` ###

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

(defined at scala.collection.convert.DecorateAsJava)


### `implicit def asJavaDictionaryConverter[A, B](m: mutable.Map[A, B]): Decorators.AsJavaDictionary[A, B]` ###

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

(defined at scala.collection.convert.DecorateAsJava)


### `implicit def asJavaEnumerationConverter[A](i: Iterator[A]): Decorators.AsJavaEnumeration[A]` ###

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

(defined at scala.collection.convert.DecorateAsJava)


### `implicit def asJavaIterableConverter[A](i: Iterable[A]): Decorators.AsJava[java.lang.Iterable[A]]` ###

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

(defined at scala.collection.convert.DecorateAsJava)


### `implicit def asJavaIteratorConverter[A](i: Iterator[A]): Decorators.AsJava[java.util.Iterator[A]]` ###

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

(defined at scala.collection.convert.DecorateAsJava)


### `implicit def bufferAsJavaListConverter[A](b: Buffer[A]): Decorators.AsJava[java.util.List[A]]` ###

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

(defined at scala.collection.convert.DecorateAsJava)


### `implicit def mapAsJavaConcurrentMapConverter[A, B](m: concurrent.Map[A, B]): Decorators.AsJava[ConcurrentMap[A, B]]` ###

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

(defined at scala.collection.convert.DecorateAsJava)


### `implicit def mapAsJavaMapConverter[A, B](m: Map[A, B]): Decorators.AsJava[java.util.Map[A, B]]` ###

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

(defined at scala.collection.convert.DecorateAsJava)


### `implicit def mutableMapAsJavaMapConverter[A, B](m: mutable.Map[A, B]): Decorators.AsJava[java.util.Map[A, B]]` ###

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

(defined at scala.collection.convert.DecorateAsJava)


### `implicit def mutableSeqAsJavaListConverter[A](b: mutable.Seq[A]): Decorators.AsJava[java.util.List[A]]` ###

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

(defined at scala.collection.convert.DecorateAsJava)


### `implicit def mutableSetAsJavaSetConverter[A](s: mutable.Set[A]): Decorators.AsJava[java.util.Set[A]]` ###

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

(defined at scala.collection.convert.DecorateAsJava)


### `implicit def seqAsJavaListConverter[A](b: Seq[A]): Decorators.AsJava[java.util.List[A]]` ###

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

(defined at scala.collection.convert.DecorateAsJava)


### `implicit def setAsJavaSetConverter[A](s: Set[A]): Decorators.AsJava[java.util.Set[A]]` ###

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
(defined at scala.collection.convert.DecorateAsJava)
