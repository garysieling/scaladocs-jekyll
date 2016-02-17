
#                  scala.reflect.ClassManifestDeprecatedApis                  #

```scala
trait ClassManifestDeprecatedApis[T] extends OptManifest[T]
```

* Self Type
  * ClassManifest [T]
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ Use scala.reflect.ClassTag instead
* Source
  * [ClassManifestDeprecatedApis.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/reflect/ClassManifestDeprecatedApis.scala#L1)


--------------------------------------------------------------------------------
    Deprecated Value Members From scala.reflect.ClassManifestDeprecatedApis
--------------------------------------------------------------------------------


### `def <:<(that: ClassManifest[_]): Boolean`                               ###

Tests whether the type represented by this manifest is a subtype of the type
represented by `that` manifest, subject to the limitations described in the
header.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ Use scala.reflect.runtime.universe.TypeTag for
    subtype checking instead

(defined at scala.reflect.ClassManifestDeprecatedApis)


### `def >:>(that: ClassManifest[_]): Boolean`                               ###

Tests whether the type represented by this manifest is a supertype of the type
represented by `that` manifest, subject to the limitations described in the
header.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ Use scala.reflect.runtime.universe.TypeTag for
    subtype checking instead

(defined at scala.reflect.ClassManifestDeprecatedApis)


### `def arrayManifest: ClassManifest[Array[T]]`                             ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ Use wrap instead

(defined at scala.reflect.ClassManifestDeprecatedApis)


### `def newArray2(len: Int): Array[Array[T]]`                               ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ Use wrap.newArray instead

(defined at scala.reflect.ClassManifestDeprecatedApis)


### `def newArray3(len: Int): Array[Array[Array[T]]]`                        ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ Use wrap.wrap.newArray instead

(defined at scala.reflect.ClassManifestDeprecatedApis)


### `def newArray4(len: Int): Array[Array[Array[Array[T]]]]`                 ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ Use wrap.wrap.wrap.newArray instead

(defined at scala.reflect.ClassManifestDeprecatedApis)


### `def newArray5(len: Int): Array[Array[Array[Array[Array[T]]]]]`          ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ Use wrap.wrap.wrap.wrap.newArray instead

(defined at scala.reflect.ClassManifestDeprecatedApis)


### `def newArrayBuilder(): ArrayBuilder[T]`                                 ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ Use ArrayBuilder.make(this) instead

(defined at scala.reflect.ClassManifestDeprecatedApis)


### `def newWrappedArray(len: Int): WrappedArray[T]`                         ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ Create WrappedArray directly instead

(defined at scala.reflect.ClassManifestDeprecatedApis)


### `def typeArguments: List[OptManifest[_]]`                                ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ Use scala.reflect.runtime.universe.TypeTag to
    capture type structure instead

(defined at scala.reflect.ClassManifestDeprecatedApis)


--------------------------------------------------------------------------------
          Value Members From scala.reflect.ClassManifestDeprecatedApis
--------------------------------------------------------------------------------


### `def arrayClass[T](tp: Class[_]): Class[Array[T]]`                       ###

* Attributes
  * protected

(defined at scala.reflect.ClassManifestDeprecatedApis)


### `def canEqual(other: Any): Boolean`                                      ###

(defined at scala.reflect.ClassManifestDeprecatedApis)


### `def newArray(len: Int): Array[T]`                                       ###
(defined at scala.reflect.ClassManifestDeprecatedApis)
