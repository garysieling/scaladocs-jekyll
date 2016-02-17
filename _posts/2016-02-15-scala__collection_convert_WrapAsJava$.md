
#                     scala.collection.convert.WrapAsJava                     #

```scala
object WrapAsJava extends WrapAsJava
```

* Source
  * [WrapAsJava.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/convert/WrapAsJava.scala#L1)


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
