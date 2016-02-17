
#                   scala.collection.generic.AtomicIndexFlag                   #

```scala
trait AtomicIndexFlag extends Signalling
```

A mixin trait that implements index flag behaviour using atomic integers. The
 `setIndex` operation is wait-free, while conditional set operations
 `setIndexIfGreater` and `setIndexIfLesser` are lock-free and support only
monotonic changes.

* Source
  * [Signalling.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/Signalling.scala#L1)


--------------------------------------------------------------------------------
      Concrete Value Members From scala.collection.generic.AtomicIndexFlag
--------------------------------------------------------------------------------


### `def setIndexFlag(f: Int): Unit`                                         ###

Sets the value of the index flag.

The index flag holds an integer which carries some operation-specific meaning.
For instance, `takeWhile` operation sets the index flag to the position of the
element where the predicate fails. Other workers may check this index against
the indices they are working on and return if this index is smaller than their
index. Examples of operations using this are `takeWhile` , `dropWhile` , `span`
and `indexOf` .

* f
  * the value to which the index flag is set.

* Definition Classes
  * AtomicIndexFlag → Signalling

(defined at scala.collection.generic.AtomicIndexFlag)


### `def setIndexFlagIfGreater(f: Int): Unit`                                ###

Sets the value of the index flag if argument is greater than current value. This
method does this atomically.

The index flag holds an integer which carries some operation-specific meaning.
For instance, `takeWhile` operation sets the index flag to the position of the
element where the predicate fails. Other workers may check this index against
the indices they are working on and return if this index is smaller than their
index. Examples of operations using this are `takeWhile` , `dropWhile` , `span`
and `indexOf` .

* f
  * the value to which the index flag is set

* Definition Classes
  * AtomicIndexFlag → Signalling

(defined at scala.collection.generic.AtomicIndexFlag)


### `def setIndexFlagIfLesser(f: Int): Unit`                                 ###

Sets the value of the index flag if argument is lesser than current value. This
method does this atomically.

The index flag holds an integer which carries some operation-specific meaning.
For instance, `takeWhile` operation sets the index flag to the position of the
element where the predicate fails. Other workers may check this index against
the indices they are working on and return if this index is smaller than their
index. Examples of operations using this are `takeWhile` , `dropWhile` , `span`
and `indexOf` .

* f
  * the value to which the index flag is set

* Definition Classes
  * AtomicIndexFlag → Signalling

(defined at scala.collection.generic.AtomicIndexFlag)


--------------------------------------------------------------------------------
        Concrete Value Members From scala.collection.generic.Signalling
--------------------------------------------------------------------------------


### `abstract def abort(): Unit`                                             ###

Sends an abort signal to other workers.

Abort flag being true means that a worker can abort and produce whatever result,
since its result will not affect the final result of computation. An example of
operations using this are `find` , `forall` and `exists` methods.

* Definition Classes
  * Signalling
(defined at scala.collection.generic.Signalling)
