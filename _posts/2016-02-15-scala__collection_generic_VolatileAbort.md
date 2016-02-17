
#                    scala.collection.generic.VolatileAbort                    #

```scala
trait VolatileAbort extends Signalling
```

A mixin trait that implements abort flag behaviour using volatile variables.

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

* Definition Classes
  * Signalling

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

* Definition Classes
  * Signalling

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

* Definition Classes
  * Signalling

(defined at scala.collection.generic.Signalling)


--------------------------------------------------------------------------------
        Concrete Value Members From scala.collection.generic.Signalling
--------------------------------------------------------------------------------


### `abstract def indexFlag: Int`                                            ###

Returns the value of the index flag.

The index flag holds an integer which carries some operation-specific meaning.
For instance, `takeWhile` operation sets the index flag to the position of the
element where the predicate fails. Other workers may check this index against
the indices they are working on and return if this index is smaller than their
index. Examples of operations using this are `takeWhile` , `dropWhile` , `span`
and `indexOf` .

* returns
  * the value of the index flag

* Definition Classes
  * Signalling
(defined at scala.collection.generic.Signalling)
