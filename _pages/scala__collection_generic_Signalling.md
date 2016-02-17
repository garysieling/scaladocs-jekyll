
#                     scala.collection.generic.Signalling                     #

```scala
trait Signalling extends AnyRef
```

A message interface serves as a unique interface to the part of the collection
capable of receiving messages from a different task.

One example of use of this is the `find` method, which can use the signalling
interface to inform worker threads that an element has been found and no further
search is necessary.

* Source
  * [Signalling.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/Signalling.scala#L1)


--------------------------------------------------------------------------------
        Abstract Value Members From scala.collection.generic.Signalling
--------------------------------------------------------------------------------


### `abstract def setIndexFlag(f: Int): Unit`                                ###

Sets the value of the index flag.

The index flag holds an integer which carries some operation-specific meaning.
For instance, `takeWhile` operation sets the index flag to the position of the
element where the predicate fails. Other workers may check this index against
the indices they are working on and return if this index is smaller than their
index. Examples of operations using this are `takeWhile` , `dropWhile` , `span`
and `indexOf` .

* f
  * the value to which the index flag is set.

(defined at scala.collection.generic.Signalling)


### `abstract def setIndexFlagIfGreater(f: Int): Unit`                       ###

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

(defined at scala.collection.generic.Signalling)


### `abstract def setIndexFlagIfLesser(f: Int): Unit`                        ###

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

(defined at scala.collection.generic.Signalling)


--------------------------------------------------------------------------------
        Concrete Value Members From scala.collection.generic.Signalling
--------------------------------------------------------------------------------


### `abstract def abort(): Unit`                                             ###

Sends an abort signal to other workers.

Abort flag being true means that a worker can abort and produce whatever result,
since its result will not affect the final result of computation. An example of
operations using this are `find` , `forall` and `exists` methods.
(defined at scala.collection.generic.Signalling)
