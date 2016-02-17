
#                       scala.collection.JavaConversions                       #

```scala
object JavaConversions extends WrapAsScala with WrapAsJava
```

A collection of implicit conversions supporting interoperability between Scala
and Java collections.

The following conversions are supported:

```scala
scala.collection.Iterable <=> java.lang.Iterable
scala.collection.Iterable <=> java.util.Collection
scala.collection.Iterator <=> java.util.{ Iterator, Enumeration }
scala.collection.mutable.Buffer <=> java.util.List
scala.collection.mutable.Set <=> java.util.Set
scala.collection.mutable.Map <=> java.util.{ Map, Dictionary }
scala.collection.concurrent.Map <=> java.util.concurrent.ConcurrentMap
```

In all cases, converting from a source type to a target type and back again will
return the original source object, eg.

```scala
import scala.collection.JavaConversions._

val sl = new scala.collection.mutable.ListBuffer[Int]
val jl : java.util.List[Int] = sl
val sl2 : scala.collection.mutable.Buffer[Int] = jl
assert(sl eq sl2)
```

In addition, the following one way conversions are provided:

```scala
scala.collection.Seq         => java.util.List
scala.collection.mutable.Seq => java.util.List
scala.collection.Set         => java.util.Set
scala.collection.Map         => java.util.Map
java.util.Properties         => scala.collection.mutable.Map[String, String]
```

* Source
  * [JavaConversions.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/JavaConversions.scala#L1)
* Since
  * 2.8


--------------------------------------------------------------------------------
             Value Members From scala.collection.convert.WrapAsJava
--------------------------------------------------------------------------------


### `implicit def asJavaCollection[A](it: Iterable[A]): Collection[A]`       ###

Implicitly converts a Scala Iterable to an immutable Java Collection.

If the Scala Iterable was previously obtained from an implicit or explicit call
of `asSizedIterable(java.util.Collection)` then the original Java Collection
will be returned.

* it
  * The SizedIterable to be converted.
* returns
  * A Java Collection view of the argument.

* Definition Classes
  * WrapAsJava

(defined at scala.collection.convert.WrapAsJava)


### `implicit def asJavaDictionary[A, B](m: mutable.Map[A, B]): Dictionary[A, B]` ###

Implicitly converts a Scala mutable `Map` to a Java `Dictionary` .

The returned Java `Dictionary` is backed by the provided Scala `Dictionary` and
any side-effects of using it via the Java interface will be visible via the
Scala interface and vice versa.

If the Scala `Dictionary` was previously obtained from an implicit or explicit
call of `asMap(java.util.Dictionary)` then the original Java Dictionary will be
returned.

* m
  * The `Map` to be converted.
* returns
  * A Java `Dictionary` view of the argument.

* Definition Classes
  * WrapAsJava

(defined at scala.collection.convert.WrapAsJava)


### `implicit def asJavaEnumeration[A](it: Iterator[A]): java.util.Enumeration[A]` ###

Implicitly converts a Scala Iterator to a Java Enumeration. The returned Java
Enumeration is backed by the provided Scala Iterator and any side-effects of
using it via the Java interface will be visible via the Scala interface and vice
versa.

If the Scala Iterator was previously obtained from an implicit or explicit call
of `asIterator(java.util.Enumeration)` then the original Java Enumeration will
be returned.

* it
  * The Iterator to be converted.
* returns
  * A Java Enumeration view of the argument.

* Definition Classes
  * WrapAsJava

(defined at scala.collection.convert.WrapAsJava)


### `implicit def asJavaIterable[A](i: Iterable[A]): java.lang.Iterable[A]`  ###

Implicitly converts a Scala Iterable to a Java Iterable. The returned Java
Iterable is backed by the provided Scala Iterable and any side-effects of using
it via the Java interface will be visible via the Scala interface and vice
versa.

If the Scala Iterable was previously obtained from an implicit or explicit call
of `asIterable(java.lang.Iterable)` then the original Java Iterable will be
returned.

* i
  * The Iterable to be converted.
* returns
  * A Java Iterable view of the argument.

* Definition Classes
  * WrapAsJava

(defined at scala.collection.convert.WrapAsJava)


### `implicit def asJavaIterator[A](it: Iterator[A]): java.util.Iterator[A]` ###

Implicitly converts a Scala Iterator to a Java Iterator. The returned Java
Iterator is backed by the provided Scala Iterator and any side-effects of using
it via the Java interface will be visible via the Scala interface and vice
versa.

If the Scala Iterator was previously obtained from an implicit or explicit call
of `asIterator(java.util.Iterator)` then the original Java Iterator will be
returned.

* it
  * The Iterator to be converted.
* returns
  * A Java Iterator view of the argument.

* Definition Classes
  * WrapAsJava

(defined at scala.collection.convert.WrapAsJava)


### `implicit def bufferAsJavaList[A](b: Buffer[A]): java.util.List[A]`      ###

Implicitly converts a Scala mutable Buffer to a Java List. The returned Java
List is backed by the provided Scala Buffer and any side-effects of using it via
the Java interface will be visible via the Scala interface and vice versa.

If the Scala Buffer was previously obtained from an implicit or explicit call of
 `asBuffer(java.util.List)` then the original Java List will be returned.

* b
  * The Buffer to be converted.
* returns
  * A Java List view of the argument.

* Definition Classes
  * WrapAsJava

(defined at scala.collection.convert.WrapAsJava)


### `implicit def mapAsJavaConcurrentMap[A, B](m: concurrent.Map[A, B]): ConcurrentMap[A, B]` ###

Implicitly converts a Scala mutable `concurrent.Map` to a Java `ConcurrentMap` .

The returned Java `ConcurrentMap` is backed by the provided Scala
 `concurrent.Map` and any side-effects of using it via the Java interface will
be visible via the Scala interface and vice versa.

If the Scala `concurrent.Map` was previously obtained from an implicit or
explicit call of `mapAsScalaConcurrentMap(java.util.concurrent.ConcurrentMap)`
then the original Java ConcurrentMap will be returned.

* m
  * The Scala `concurrent.Map` to be converted.
* returns
  * A Java `ConcurrentMap` view of the argument.

* Definition Classes
  * WrapAsJava

(defined at scala.collection.convert.WrapAsJava)


### `implicit def mapAsJavaMap[A, B](m: Map[A, B]): java.util.Map[A, B]`     ###

Implicitly converts a Scala `Map` to a Java `Map` .

The returned Java `Map` is backed by the provided Scala `Map` and any
side-effects of using it via the Java interface will be visible via the Scala
interface and vice versa.

If the Scala `Map` was previously obtained from an implicit or explicit call of
 `asMap(java.util.Map)` then the original Java `Map` will be returned.

* m
  * The `Map` to be converted.
* returns
  * A Java `Map` view of the argument.

* Definition Classes
  * WrapAsJava

(defined at scala.collection.convert.WrapAsJava)


### `implicit def mutableMapAsJavaMap[A, B](m: mutable.Map[A, B]): java.util.Map[A, B]` ###

Implicitly converts a Scala mutable Map to a Java Map. The returned Java Map is
backed by the provided Scala Map and any side-effects of using it via the Java
interface will be visible via the Scala interface and vice versa.

If the Scala Map was previously obtained from an implicit or explicit call of
 `asMap(java.util.Map)` then the original Java Map will be returned.

* m
  * The Map to be converted.
* returns
  * A Java Map view of the argument.

* Definition Classes
  * WrapAsJava

(defined at scala.collection.convert.WrapAsJava)


### `implicit def mutableSeqAsJavaList[A](seq: mutable.Seq[A]): java.util.List[A]` ###

Implicitly converts a Scala mutable Seq to a Java List. The returned Java List
is backed by the provided Scala Seq and any side-effects of using it via the
Java interface will be visible via the Scala interface and vice versa.

If the Scala Seq was previously obtained from an implicit or explicit call of
 `asSeq(java.util.List)` then the original Java List will be returned.

* seq
  * The Seq to be converted.
* returns
  * A Java List view of the argument.

* Definition Classes
  * WrapAsJava

(defined at scala.collection.convert.WrapAsJava)


### `implicit def mutableSetAsJavaSet[A](s: mutable.Set[A]): java.util.Set[A]` ###

Implicitly converts a Scala mutable Set to a Java Set. The returned Java Set is
backed by the provided Scala Set and any side-effects of using it via the Java
interface will be visible via the Scala interface and vice versa.

If the Scala Set was previously obtained from an implicit or explicit call of
 `asSet(java.util.Set)` then the original Java Set will be returned.

* s
  * The Set to be converted.
* returns
  * A Java Set view of the argument.

* Definition Classes
  * WrapAsJava

(defined at scala.collection.convert.WrapAsJava)


### `implicit def seqAsJavaList[A](seq: Seq[A]): java.util.List[A]`          ###

Implicitly converts a Scala Seq to a Java List. The returned Java List is backed
by the provided Scala Seq and any side-effects of using it via the Java
interface will be visible via the Scala interface and vice versa.

If the Scala Seq was previously obtained from an implicit or explicit call of
 `asSeq(java.util.List)` then the original Java List will be returned.

* seq
  * The Seq to be converted.
* returns
  * A Java List view of the argument.

* Definition Classes
  * WrapAsJava

(defined at scala.collection.convert.WrapAsJava)


### `implicit def setAsJavaSet[A](s: Set[A]): java.util.Set[A]`              ###

Implicitly converts a Scala Set to a Java Set. The returned Java Set is backed
by the provided Scala Set and any side-effects of using it via the Java
interface will be visible via the Scala interface and vice versa.

If the Scala Set was previously obtained from an implicit or explicit call of
asSet(java.util.Set) then the original Java Set will be returned.

* s
  * The Set to be converted.
* returns
  * A Java Set view of the argument.

* Definition Classes
  * WrapAsJava

(defined at scala.collection.convert.WrapAsJava)


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
