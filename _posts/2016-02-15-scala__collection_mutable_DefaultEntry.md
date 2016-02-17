
#                    scala.collection.mutable.DefaultEntry                    #

```scala
final class DefaultEntry[A, B] extends HashEntry[A, DefaultEntry[A, B]] with Serializable
```

Class used internally for default map model.

* Source
  * [DefaultEntry.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/DefaultEntry.scala#L1)
* Since
  * 2.3


--------------------------------------------------------------------------------
        Instance Constructors From scala.collection.mutable.DefaultEntry
--------------------------------------------------------------------------------


### `new DefaultEntry(key: A, value: B)`                                     ###

(defined at scala.collection.mutable.DefaultEntry)


--------------------------------------------------------------------------------
             Value Members From scala.collection.mutable.HashEntry
--------------------------------------------------------------------------------


### `var next: DefaultEntry[A, B]`                                           ###

* Definition Classes
  * HashEntry
(defined at scala.collection.mutable.HashEntry)
