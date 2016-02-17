
#                 scala.collection.generic.DelegatedSignalling                 #

```scala
trait DelegatedSignalling extends Signalling
```

An implementation of the signalling interface using delegates.

* Source
  * [Signalling.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/Signalling.scala#L1)


--------------------------------------------------------------------------------
    Abstract Value Members From scala.collection.generic.DelegatedSignalling
--------------------------------------------------------------------------------


### `abstract val signalDelegate: Signalling`                                ###

A delegate that method calls are redirected to.

(defined at scala.collection.generic.DelegatedSignalling)


--------------------------------------------------------------------------------
    Concrete Value Members From scala.collection.generic.DelegatedSignalling
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
  * DelegatedSignalling → Signalling

(defined at scala.collection.generic.DelegatedSignalling)


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
  * DelegatedSignalling → Signalling

(defined at scala.collection.generic.DelegatedSignalling)


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
  * DelegatedSignalling → Signalling
(defined at scala.collection.generic.DelegatedSignalling)
