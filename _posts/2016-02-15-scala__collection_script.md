
#                           scala.collection.script                           #

```scala
package script
```


--------------------------------------------------------------------------------
                            Deprecated Value Members
--------------------------------------------------------------------------------


### `object End extends Location with Product with Serializable`             ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Scripting is deprecated.
* Source
  * [Location.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/script/Location.scala#L1)


### `object NoLo extends Location with Product with Serializable`            ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Scripting is deprecated.
* Source
  * [Location.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/script/Location.scala#L1)


### `object Start extends Location with Product with Serializable`           ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Scripting is deprecated.
* Source
  * [Location.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/script/Location.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `case class Include[+A](location: Location, elem: A) extends Message[A] with Product with Serializable` ###

This observable update refers to inclusion operations that add new elements to
collection classes.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Scripting is deprecated.
* Source
  * [Message.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/script/Message.scala#L1)
* Version
  * 1.0, 08/07/2003


### `case class Index(n: Int) extends Location with Product with Serializable` ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Scripting is deprecated.
* Source
  * [Location.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/script/Location.scala#L1)


### `sealed abstract class Location extends AnyRef`                          ###

Class `Location` describes locations in messages implemented by class
scala.collection.script.Message.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Scripting is deprecated.
* Source
  * [Location.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/script/Location.scala#L1)
* Version
  * 1.0, 10/05/2004
* Since
  * 2.8


### `trait Message[+A] extends AnyRef`                                       ###

Class `Message` represents messages that are issued by observable collection
classes whenever a data structure is changed. Class `Message` has several
subclasses for the various kinds of events: `Update`  `Remove` , `Include` ,
 `Reset` , and `Script` .

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Scripting is deprecated.
* Source
  * [Message.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/script/Message.scala#L1)
* Version
  * 1.0, 08/07/2003
* Since
  * 2.8


### `case class Remove[+A](location: Location, elem: A) extends Message[A] with Product with Serializable` ###

This observable update refers to removal operations of elements from collection
classes.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Scripting is deprecated.
* Source
  * [Message.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/script/Message.scala#L1)
* Version
  * 1.0, 08/07/2003


### `case class Reset[+A]() extends Message[A] with Product with Serializable` ###

This command refers to reset operations.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Scripting is deprecated.
* Source
  * [Message.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/script/Message.scala#L1)
* Version
  * 1.0, 08/07/2003


### `class Script[A] extends ArrayBuffer[Message[A]] with Message[A]`        ###

Objects of this class represent compound messages consisting of a sequence of
other messages.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Scripting is deprecated.
* Source
  * [Message.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/script/Message.scala#L1)
* Version
  * 1.0, 10/05/2004


### `trait Scriptable[A] extends AnyRef`                                     ###

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


### `case class Update[+A](location: Location, elem: A) extends Message[A] with Product with Serializable` ###

This observable update refers to destructive modification operations of elements
from collection classes.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Scripting is deprecated.
* Source
  * [Message.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/script/Message.scala#L1)
* Version
  * 1.0, 08/07/2003

