
#                    scala.collection.mutable.ArrayBuilder                    #

```scala
object ArrayBuilder extends Serializable
```

A companion object for array builders.

* Source
  * [ArrayBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ArrayBuilder.scala#L1)
* Since
  * 2.8


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class ofBoolean extends ArrayBuilder[Boolean]`                          ###

A class for array builders for arrays of `boolean` s. It can be reused.

* Source
  * [ArrayBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ArrayBuilder.scala#L1)


### `class ofByte extends ArrayBuilder[Byte]`                                ###

A class for array builders for arrays of `byte` s. It can be reused.

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [ArrayBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ArrayBuilder.scala#L1)


### `class ofChar extends ArrayBuilder[Char]`                                ###

A class for array builders for arrays of `char` s. It can be reused.

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [ArrayBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ArrayBuilder.scala#L1)


### `class ofDouble extends ArrayBuilder[Double]`                            ###

A class for array builders for arrays of `double` s. It can be reused.

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [ArrayBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ArrayBuilder.scala#L1)


### `class ofFloat extends ArrayBuilder[Float]`                              ###

A class for array builders for arrays of `float` s. It can be reused.

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [ArrayBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ArrayBuilder.scala#L1)


### `class ofInt extends ArrayBuilder[Int]`                                  ###

A class for array builders for arrays of `int` s. It can be reused.

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [ArrayBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ArrayBuilder.scala#L1)


### `class ofLong extends ArrayBuilder[Long]`                                ###

A class for array builders for arrays of `long` s. It can be reused.

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [ArrayBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ArrayBuilder.scala#L1)


### `class ofRef[T <: AnyRef] extends ArrayBuilder[T]`                       ###

A class for array builders for arrays of reference types.

This builder can be reused.

* T
  * type of elements for the array builder, subtype of `AnyRef` with a
     `ClassTag` context bound.

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [ArrayBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ArrayBuilder.scala#L1)


### `class ofShort extends ArrayBuilder[Short]`                              ###

A class for array builders for arrays of `short` s. It can be reused.

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [ArrayBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ArrayBuilder.scala#L1)


### `class ofUnit extends ArrayBuilder[Unit]`                                ###

A class for array builders for arrays of `Unit` type. It can be reused.

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [ArrayBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ArrayBuilder.scala#L1)


--------------------------------------------------------------------------------
            Value Members From scala.collection.mutable.ArrayBuilder
--------------------------------------------------------------------------------


### `def make[T]()(implicit arg0: ClassTag[T]): ArrayBuilder[T]`             ###

Creates a new arraybuilder of type `T` .

* T
  * type of the elements for the array builder, with a `ClassTag` context bound.
* returns
  * a new empty array builder.
(defined at scala.collection.mutable.ArrayBuilder)
