
#                       scala.collection.script.Include                       #

```scala
case class Include[+A](location: Location, elem: A) extends Message[A] with Product with Serializable
```

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


--------------------------------------------------------------------------------
           Instance Constructors From scala.collection.script.Include
--------------------------------------------------------------------------------


### `new Include(elem: A)`                                                   ###

(defined at scala.collection.script.Include)


--------------------------------------------------------------------------------
               Value Members From scala.collection.script.Include
--------------------------------------------------------------------------------


### `val location: Location`                                                 ###
(defined at scala.collection.script.Include)
