
#                      scala.collection.script.Scriptable                      #

```scala
trait Scriptable[A] extends AnyRef
```

Classes that mix in the `Scriptable` class allow messages to be sent to objects
of that class.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Scripting is deprecated.
* Source
  * [Scriptable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/script/Scriptable.scala#L1)
* Version
  * 1.0, 09/05/2004
* Since
  * 2.8


--------------------------------------------------------------------------------
         Abstract Value Members From scala.collection.script.Scriptable
--------------------------------------------------------------------------------


### `abstract def <<(cmd: Message[A]): Unit`                                 ###

Send a message to this scriptable object.
(defined at scala.collection.script.Scriptable)
