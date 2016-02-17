
#                       scala.collection.script.Message                       #

```scala
trait Message[+A] extends AnyRef
```

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

