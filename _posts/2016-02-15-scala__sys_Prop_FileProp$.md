
#                           scala.sys.Prop.FileProp                           #

```scala
implicit object FileProp extends CreatorImpl[File]
```

* Source
  * [Prop.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/Prop.scala#L1)


--------------------------------------------------------------------------------
                    Value Members From scala.sys.CreatorImpl
--------------------------------------------------------------------------------


### `def apply(key: String): Prop[File]`                                     ###

Creates a Prop[T] of this type based on the given key.

* Definition Classes
  * CreatorImpl → Creator
(defined at scala.sys.CreatorImpl)
