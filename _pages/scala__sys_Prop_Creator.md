
#                            scala.sys.Prop.Creator                            #

```scala
trait Creator[+T] extends AnyRef
```

A creator of property instances. For any type `T` , if an implicit parameter of
type Creator[T] is in scope, a Prop[T] can be created via this object's apply
method.

* Annotations
  * @ implicitNotFound (msg =...)
* Source
  * [Prop.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/Prop.scala#L1)


--------------------------------------------------------------------------------
               Abstract Value Members From scala.sys.Prop.Creator
--------------------------------------------------------------------------------


### `abstract def apply(key: String): Prop[T]`                               ###

Creates a Prop[T] of this type based on the given key.
(defined at scala.sys.Prop.Creator)
