
#                   scala.collection.mutable.UnrolledBuffer                   #

```scala
object UnrolledBuffer extends ClassTagTraversableFactory[UnrolledBuffer] with Serializable
```

* Source
  * [UnrolledBuffer.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/UnrolledBuffer.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = UnrolledBuffer[_]`                                          ###

* Attributes
  * protected[this]
* Definition Classes
  * GenericClassTagCompanion


### `class GenericCanBuildFrom[A] extends CanBuildFrom[CC[_], A, CC[A]]`     ###

* Definition Classes
  * ClassTagTraversableFactory


### `class Unrolled[T] extends AnyRef`                                       ###

Unrolled buffer node.

* Source
  * [UnrolledBuffer.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/UnrolledBuffer.scala#L1)


--------------------------------------------------------------------------------
      Value Members From scala.collection.generic.GenericClassTagCompanion
--------------------------------------------------------------------------------


### `def apply[A](elems: A*)(implicit ord: ClassTag[A]): UnrolledBuffer[A]`  ###

* Definition Classes
  * GenericClassTagCompanion

(defined at scala.collection.generic.GenericClassTagCompanion)


### `def empty[A](implicit arg0: ClassTag[A]): UnrolledBuffer[A]`            ###

* Definition Classes
  * GenericClassTagCompanion

(defined at scala.collection.generic.GenericClassTagCompanion)


--------------------------------------------------------------------------------
           Value Members From scala.collection.mutable.UnrolledBuffer
--------------------------------------------------------------------------------


### `implicit def canBuildFrom[T](implicit t: ClassTag[T]): CanBuildFrom[Coll, T, UnrolledBuffer[T]]` ###

The standard `CanBuildFrom` instance for `Traversable` objects.

(defined at scala.collection.mutable.UnrolledBuffer)


### `def newBuilder[T](implicit t: ClassTag[T]): Builder[T, UnrolledBuffer[T]]` ###

* Definition Classes
  * UnrolledBuffer → GenericClassTagCompanion
(defined at scala.collection.mutable.UnrolledBuffer)
