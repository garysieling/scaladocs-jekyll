
#                                scala.sys.Prop                                #

```scala
object Prop
```

* Source
  * [Prop.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/Prop.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `trait Creator[+T] extends AnyRef`                                       ###

A creator of property instances. For any type `T` , if an implicit parameter of
type Creator[T] is in scope, a Prop[T] can be created via this object's apply
method.

* Annotations
  * @ implicitNotFound (msg =...)
* Source
  * [Prop.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/Prop.scala#L1)


--------------------------------------------------------------------------------
                                 Value Members
--------------------------------------------------------------------------------


### `implicit object DoubleProp extends CreatorImpl[Double]`                 ###

* Source
  * [Prop.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/Prop.scala#L1)


### `implicit object FileProp extends CreatorImpl[File]`                     ###

* Source
  * [Prop.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/Prop.scala#L1)


### `implicit object IntProp extends CreatorImpl[Int]`                       ###

* Source
  * [Prop.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/Prop.scala#L1)


### `implicit object StringProp extends CreatorImpl[String]`                 ###

* Source
  * [Prop.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/Prop.scala#L1)


--------------------------------------------------------------------------------
                       Value Members From scala.sys.Prop
--------------------------------------------------------------------------------


### `def apply[T](key: String)(implicit arg0: Creator[T]): Prop[T]`          ###
(defined at scala.sys.Prop)
