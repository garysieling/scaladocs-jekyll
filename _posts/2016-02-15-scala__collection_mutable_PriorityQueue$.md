
#                    scala.collection.mutable.PriorityQueue                    #

```scala
object PriorityQueue extends OrderedTraversableFactory[PriorityQueue] with Serializable
```

* Source
  * [PriorityQueue.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/PriorityQueue.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = PriorityQueue[_]`                                           ###

* Attributes
  * protected[this]
* Definition Classes
  * GenericOrderedCompanion


### `class GenericCanBuildFrom[A] extends CanBuildFrom[CC[_], A, CC[A]]`     ###

* Definition Classes
  * OrderedTraversableFactory


--------------------------------------------------------------------------------
      Value Members From scala.collection.generic.GenericOrderedCompanion
--------------------------------------------------------------------------------


### `def apply[A](elems: A*)(implicit ord: Ordering[A]): PriorityQueue[A]`   ###

* Definition Classes
  * GenericOrderedCompanion

(defined at scala.collection.generic.GenericOrderedCompanion)


### `def empty[A](implicit arg0: Ordering[A]): PriorityQueue[A]`             ###

* Definition Classes
  * GenericOrderedCompanion

(defined at scala.collection.generic.GenericOrderedCompanion)


--------------------------------------------------------------------------------
           Value Members From scala.collection.mutable.PriorityQueue
--------------------------------------------------------------------------------


### `implicit def canBuildFrom[A](implicit ord: Ordering[A]): CanBuildFrom[Coll, A, PriorityQueue[A]]` ###

(defined at scala.collection.mutable.PriorityQueue)


### `def newBuilder[A](implicit ord: Ordering[A]): PriorityQueue[A]`         ###

* Definition Classes
  * PriorityQueue → GenericOrderedCompanion
(defined at scala.collection.mutable.PriorityQueue)
