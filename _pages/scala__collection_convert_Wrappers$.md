
#                      scala.collection.convert.Wrappers                      #

```scala
object Wrappers extends Wrappers with Serializable
```

* Annotations
  * @ SerialVersionUID ()
* Source
  * [Wrappers.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/convert/Wrappers.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class ConcurrentMapWrapper[A, B] extends MutableMapWrapper[A, B] with ConcurrentMap[A, B]` ###

* Definition Classes
  * Wrappers


### `case class DictionaryWrapper[A, B] extends Dictionary[A, B] with Product with Serializable` ###

* Definition Classes
  * Wrappers


### `case class IterableWrapper[A] extends AbstractCollection[A] with IterableWrapperTrait[A] with Product with Serializable` ###

* Definition Classes
  * Wrappers


### `trait IterableWrapperTrait[A] extends AbstractCollection[A]`            ###

* Definition Classes
  * Wrappers


### `case class IteratorWrapper[A] extends java.util.Iterator[A] with java.util.Enumeration[A] with Product with Serializable` ###

* Definition Classes
  * Wrappers


### `case class JCollectionWrapper[A] extends AbstractIterable[A] with Iterable[A] with Product with Serializable` ###

* Definition Classes
  * Wrappers


### `case class JConcurrentMapWrapper[A, B] extends mutable.AbstractMap[A, B] with JMapWrapperLike[A, B, JConcurrentMapWrapper[A, B]] with concurrent.Map[A, B] with Product with Serializable` ###

Wraps a concurrent Java map as a Scala one. Single-element concurrent access is
supported; multi-element operations such as maps and filters are not guaranteed
to be atomic.

* Definition Classes
  * Wrappers


### `case class JDictionaryWrapper[A, B] extends mutable.AbstractMap[A, B] with mutable.Map[A, B] with Product with Serializable` ###

* Definition Classes
  * Wrappers


### `case class JEnumerationWrapper[A] extends AbstractIterator[A] with Iterator[A] with Product with Serializable` ###

* Definition Classes
  * Wrappers


### `case class JIterableWrapper[A] extends AbstractIterable[A] with Iterable[A] with Product with Serializable` ###

* Definition Classes
  * Wrappers


### `case class JIteratorWrapper[A] extends AbstractIterator[A] with Iterator[A] with Product with Serializable` ###

* Definition Classes
  * Wrappers


### `case class JListWrapper[A] extends AbstractBuffer[A] with Buffer[A] with Product with Serializable` ###

* Definition Classes
  * Wrappers


### `case class JMapWrapper[A, B] extends mutable.AbstractMap[A, B] with JMapWrapperLike[A, B, JMapWrapper[A, B]] with Product with Serializable` ###

Wraps a Java map as a Scala one. If the map is to support concurrent access, use
JConcurrentMapWrapper instead. If the wrapped map is synchronized (e.g. from
 `java.util.Collections.synchronizedMap` ), it is your responsibility to wrap
all non-atomic operations with `underlying.synchronized` . This includes `get` ,
as `java.util.Map` 's API does not allow for an atomic `get` when `null` values
may be present.

* Definition Classes
  * Wrappers


### `trait JMapWrapperLike[A, B, +Repr <: mutable.MapLike[A, B, Repr] with mutable.Map[A, B]] extends mutable.Map[A, B] with mutable.MapLike[A, B, Repr]` ###

* Definition Classes
  * Wrappers


### `case class JPropertiesWrapper extends mutable.AbstractMap[String, String] with mutable.Map[String, String] with mutable.MapLike[String, String, JPropertiesWrapper] with Product with Serializable` ###

* Definition Classes
  * Wrappers


### `case class JSetWrapper[A] extends mutable.AbstractSet[A] with mutable.Set[A] with mutable.SetLike[A, JSetWrapper[A]] with Product with Serializable` ###

* Definition Classes
  * Wrappers


### `class MapWrapper[A, B] extends java.util.AbstractMap[A, B] with Serializable` ###

* Definition Classes
  * Wrappers
* Annotations
  * @ SerialVersionUID ()


### `case class MutableBufferWrapper[A] extends AbstractList[A] with IterableWrapperTrait[A] with Product with Serializable` ###

* Definition Classes
  * Wrappers


### `case class MutableMapWrapper[A, B] extends MapWrapper[A, B] with Product with Serializable` ###

* Definition Classes
  * Wrappers


### `case class MutableSeqWrapper[A] extends AbstractList[A] with IterableWrapperTrait[A] with Product with Serializable` ###

* Definition Classes
  * Wrappers


### `case class MutableSetWrapper[A] extends SetWrapper[A] with Product with Serializable` ###

* Definition Classes
  * Wrappers


### `case class SeqWrapper[A] extends AbstractList[A] with IterableWrapperTrait[A] with Product with Serializable` ###

* Definition Classes
  * Wrappers


### `class SetWrapper[A] extends java.util.AbstractSet[A] with Serializable` ###

* Definition Classes
  * Wrappers
* Annotations
  * @ SerialVersionUID ()


### `class ToIteratorWrapper[A] extends AnyRef`                              ###

* Definition Classes
  * Wrappers

