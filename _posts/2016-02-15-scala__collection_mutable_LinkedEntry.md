
#                     scala.collection.mutable.LinkedEntry                     #

```scala
final class LinkedEntry[A, B] extends HashEntry[A, LinkedEntry[A, B]] with Serializable
```

Class for the linked hash map entry, used internally.

* Source
  * [LinkedEntry.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/LinkedEntry.scala#L1)
* Since
  * 2.8


--------------------------------------------------------------------------------
             Value Members From scala.collection.mutable.HashEntry
--------------------------------------------------------------------------------


### `var next: LinkedEntry[A, B]`                                            ###

* Definition Classes
  * HashEntry

(defined at scala.collection.mutable.HashEntry)


--------------------------------------------------------------------------------
        Instance Constructors From scala.collection.mutable.LinkedEntry
--------------------------------------------------------------------------------


### `new LinkedEntry(key: A, value: B)`                                      ###

(defined at scala.collection.mutable.LinkedEntry)


--------------------------------------------------------------------------------
            Value Members From scala.collection.mutable.LinkedEntry
--------------------------------------------------------------------------------


### `var earlier: LinkedEntry[A, B]`                                         ###

(defined at scala.collection.mutable.LinkedEntry)


### `var later: LinkedEntry[A, B]`                                           ###
(defined at scala.collection.mutable.LinkedEntry)
