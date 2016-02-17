
#                         scala.reflect.AnyValManifest                         #

```scala
abstract class AnyValManifest[T <: AnyVal] extends Manifest[T] with Equals
```

* Annotations
  * @ SerialVersionUID ()
* Source
  * [Manifest.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/reflect/Manifest.scala#L1)


--------------------------------------------------------------------------------
            Concrete Value Members From scala.reflect.AnyValManifest
--------------------------------------------------------------------------------


### `def <:<(that: ClassManifest[_]): Boolean`                               ###

Tests whether the type represented by this manifest is a subtype of the type
represented by `that` manifest, subject to the limitations described in the
header.

* Definition Classes
  * AnyValManifest → ClassManifestDeprecatedApis

(defined at scala.reflect.AnyValManifest)


### `def canEqual(other: Any): Boolean`                                      ###

A method that should be called from every well-designed equals method that is
open to be overridden in a subclass. See
[Programming in Scala, Chapter 28](http://www.artima.com/pins1ed/object-equality.html)
for discussion and design.

* returns
  * true if this instance can possibly equal `that` , otherwise false

* Definition Classes
  * AnyValManifest → Manifest → ClassTag → Equals → ClassManifestDeprecatedApis

(defined at scala.reflect.AnyValManifest)


### `def equals(that: Any): Boolean`                                         ###

Note: testing for erasure here is important, as it is many times faster than <:<
and rules out most comparisons.

* Definition Classes
  * AnyValManifest → Manifest → ClassTag → Equals → AnyRef → Any

(defined at scala.reflect.AnyValManifest)


--------------------------------------------------------------------------------
            Instance Constructors From scala.reflect.AnyValManifest
--------------------------------------------------------------------------------


### `new AnyValManifest(toString: String)`                                   ###

(defined at scala.reflect.AnyValManifest)


--------------------------------------------------------------------------------
     Concrete Value Members From scala.reflect.ClassManifestDeprecatedApis
--------------------------------------------------------------------------------


### `def arrayClass[T](tp: Class[_]): Class[Array[T]]`                       ###

* Attributes
  * protected
* Definition Classes
  * ClassManifestDeprecatedApis

(defined at scala.reflect.ClassManifestDeprecatedApis)


--------------------------------------------------------------------------------
    Deprecated Value Members From scala.reflect.ClassManifestDeprecatedApis
--------------------------------------------------------------------------------


### `def >:>(that: ClassManifest[_]): Boolean`                               ###

Tests whether the type represented by this manifest is a supertype of the type
represented by `that` manifest, subject to the limitations described in the
header.

* Definition Classes
  * ClassManifestDeprecatedApis
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ Use scala.reflect.runtime.universe.TypeTag for
    subtype checking instead

(defined at scala.reflect.ClassManifestDeprecatedApis)


### `def newArray2(len: Int): Array[Array[T]]`                               ###

* Definition Classes
  * ClassManifestDeprecatedApis
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ Use wrap.newArray instead

(defined at scala.reflect.ClassManifestDeprecatedApis)


### `def newArray3(len: Int): Array[Array[Array[T]]]`                        ###

* Definition Classes
  * ClassManifestDeprecatedApis
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ Use wrap.wrap.newArray instead

(defined at scala.reflect.ClassManifestDeprecatedApis)


### `def newArray4(len: Int): Array[Array[Array[Array[T]]]]`                 ###

* Definition Classes
  * ClassManifestDeprecatedApis
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ Use wrap.wrap.wrap.newArray instead

(defined at scala.reflect.ClassManifestDeprecatedApis)


### `def newArray5(len: Int): Array[Array[Array[Array[Array[T]]]]]`          ###

* Definition Classes
  * ClassManifestDeprecatedApis
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ Use wrap.wrap.wrap.wrap.newArray instead

(defined at scala.reflect.ClassManifestDeprecatedApis)


### `def newArrayBuilder(): ArrayBuilder[T]`                                 ###

* Definition Classes
  * ClassManifestDeprecatedApis
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ Use ArrayBuilder.make(this) instead

(defined at scala.reflect.ClassManifestDeprecatedApis)


### `def newWrappedArray(len: Int): WrappedArray[T]`                         ###

* Definition Classes
  * ClassManifestDeprecatedApis
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ Create WrappedArray directly instead

(defined at scala.reflect.ClassManifestDeprecatedApis)


--------------------------------------------------------------------------------
               Concrete Value Members From scala.reflect.ClassTag
--------------------------------------------------------------------------------


### `def newArray(len: Int): Array[T]`                                       ###

Produces a new array with element type `T` and length `len`

* Definition Classes
  * ClassTag → ClassManifestDeprecatedApis

(defined at scala.reflect.ClassTag)


### `def unapply(x: Any): Option[T]`                                         ###

A ClassTag[T] can serve as an extractor that matches only objects of type T.

The compiler tries to turn unchecked type tests in pattern matches into checked
ones by wrapping a `(_: T)` type pattern as `ct(_: T)` , where `ct` is the
 `ClassTag[T]` instance. Type tests necessary before calling other extractors
are treated similarly. `SomeExtractor(...)` is turned into
 `ct(SomeExtractor(...))` if `T` in `SomeExtractor.unapply(x: T)` is
uncheckable, but we have an instance of `ClassTag[T]` .

* Definition Classes
  * ClassTag

(defined at scala.reflect.ClassTag)


### `def unapply(x: Boolean): Option[T]`                                     ###

* Definition Classes
  * ClassTag

(defined at scala.reflect.ClassTag)


### `def unapply(x: Byte): Option[T]`                                        ###

* Definition Classes
  * ClassTag

(defined at scala.reflect.ClassTag)


### `def unapply(x: Char): Option[T]`                                        ###

* Definition Classes
  * ClassTag

(defined at scala.reflect.ClassTag)


### `def unapply(x: Double): Option[T]`                                      ###

* Definition Classes
  * ClassTag

(defined at scala.reflect.ClassTag)


### `def unapply(x: Float): Option[T]`                                       ###

* Definition Classes
  * ClassTag

(defined at scala.reflect.ClassTag)


### `def unapply(x: Int): Option[T]`                                         ###

* Definition Classes
  * ClassTag

(defined at scala.reflect.ClassTag)


### `def unapply(x: Long): Option[T]`                                        ###

* Definition Classes
  * ClassTag

(defined at scala.reflect.ClassTag)


### `def unapply(x: Short): Option[T]`                                       ###

* Definition Classes
  * ClassTag

(defined at scala.reflect.ClassTag)


### `def unapply(x: Unit): Option[T]`                                        ###

* Definition Classes
  * ClassTag

(defined at scala.reflect.ClassTag)


### `def wrap: ClassTag[Array[T]]`                                           ###

Produces a `ClassTag` that knows how to instantiate an `Array[Array[T]]`

* Definition Classes
  * ClassTag

(defined at scala.reflect.ClassTag)


--------------------------------------------------------------------------------
              Deprecated Value Members From scala.reflect.ClassTag
--------------------------------------------------------------------------------


### `abstract def runtimeClass: Class[_]`                                    ###

A class representing the type `U` to which `T` would be erased. Note that there
is no subtyping relationship between `T` and `U` .

* Definition Classes
  * ClassTag

(defined at scala.reflect.ClassTag)


--------------------------------------------------------------------------------
               Concrete Value Members From scala.reflect.Manifest
--------------------------------------------------------------------------------


### `def arrayManifest: Manifest[Array[T]]`                                  ###

* Definition Classes
  * Manifest → ClassManifestDeprecatedApis

(defined at scala.reflect.Manifest)


### `def typeArguments: List[Manifest[_]]`                                   ###

* Definition Classes
  * Manifest → ClassManifestDeprecatedApis
(defined at scala.reflect.Manifest)
