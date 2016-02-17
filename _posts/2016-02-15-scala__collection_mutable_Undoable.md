
#                      scala.collection.mutable.Undoable                      #

```scala
trait Undoable extends AnyRef
```

Classes that mix in the `Undoable` class provide an operation `undo` which can
be used to undo the last operation.

* Source
  * [Undoable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/Undoable.scala#L1)
* Version
  * 1.0, 08/07/2003
* Since
  * 1


--------------------------------------------------------------------------------
         Concrete Value Members From scala.collection.mutable.Undoable
--------------------------------------------------------------------------------


### `abstract def undo(): Unit`                                              ###

Undo the last operation.
(defined at scala.collection.mutable.Undoable)
