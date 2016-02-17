
#                            scala.reflect.ClassTag                            #

```scala
trait ClassTag[T] extends ClassManifestDeprecatedApis[T] with Equals with Serializable
```

A `ClassTag[T]` stores the erased class of a given type `T` , accessible via the
 `runtimeClass` field. This is particularly useful for instantiating `Array` s
whose element types are unknown at compile time.

 `ClassTag` s are a weaker special case of scala.reflect.api.TypeTags#TypeTag s,
in that they wrap only the runtime class of a given type, whereas a `TypeTag`
contains all static type information. That is, `ClassTag` s are constructed from
knowing only the top-level class of a type, without necessarily knowing all of
its argument types. This runtime information is enough for runtime `Array`
creation.

For example:

```scala
scala> def mkArray[T : ClassTag](elems: T*) = Array[T](elems: _*)
mkArray: [T](elems: T*)(implicit evidence$1: scala.reflect.ClassTag[T])Array[T]

scala> mkArray(42, 13)
res0: Array[Int] = Array(42, 13)

scala> mkArray("Japan","Brazil","Germany")
res1: Array[String] = Array(Japan, Brazil, Germany)
```

See scala.reflect.api.TypeTags for more examples, or the
[Reflection Guide: TypeTags](http://docs.scala-lang.org/overviews/reflection/typetags-manifests.html)
for more details.

* Annotations
  * @ implicitNotFound (msg = "No ClassTag available for ${T}")
* Source
  * [ClassTag.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/reflect/ClassTag.scala#L1)


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


### `def <:<(that: ClassManifest[_]): Boolean`                               ###

Tests whether the type represented by this manifest is a subtype of the type
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


### `def arrayManifest: ClassManifest[Array[T]]`                             ###

* Definition Classes
  * ClassManifestDeprecatedApis
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ Use wrap instead

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


### `def typeArguments: List[OptManifest[_]]`                                ###

* Definition Classes
  * ClassManifestDeprecatedApis
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ Use scala.reflect.runtime.universe.TypeTag to
    capture type structure instead

(defined at scala.reflect.ClassManifestDeprecatedApis)


--------------------------------------------------------------------------------
               Concrete Value Members From scala.reflect.ClassTag
--------------------------------------------------------------------------------


### `def canEqual(x: Any): Boolean`                                          ###

A method that should be called from every well-designed equals method that is
open to be overridden in a subclass. See
[Programming in Scala, Chapter 28](http://www.artima.com/pins1ed/object-equality.html)
for discussion and design.

* returns
  * true if this instance can possibly equal `that` , otherwise false

* Definition Classes
  * ClassTag → Equals → ClassManifestDeprecatedApis

(defined at scala.reflect.ClassTag)


### `def equals(x: Any): Boolean`                                            ###

The universal equality method defined in `AnyRef` .

* Definition Classes
  * ClassTag → Equals → AnyRef → Any

(defined at scala.reflect.ClassTag)


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

(defined at scala.reflect.ClassTag)


### `def unapply(x: Boolean): Option[T]`                                     ###

(defined at scala.reflect.ClassTag)


### `def unapply(x: Byte): Option[T]`                                        ###

(defined at scala.reflect.ClassTag)


### `def unapply(x: Char): Option[T]`                                        ###

(defined at scala.reflect.ClassTag)


### `def unapply(x: Double): Option[T]`                                      ###

(defined at scala.reflect.ClassTag)


### `def unapply(x: Float): Option[T]`                                       ###

(defined at scala.reflect.ClassTag)


### `def unapply(x: Int): Option[T]`                                         ###

(defined at scala.reflect.ClassTag)


### `def unapply(x: Long): Option[T]`                                        ###

(defined at scala.reflect.ClassTag)


### `def unapply(x: Short): Option[T]`                                       ###

(defined at scala.reflect.ClassTag)


### `def unapply(x: Unit): Option[T]`                                        ###

(defined at scala.reflect.ClassTag)


### `def wrap: ClassTag[Array[T]]`                                           ###

Produces a `ClassTag` that knows how to instantiate an `Array[Array[T]]`

(defined at scala.reflect.ClassTag)


--------------------------------------------------------------------------------
              Deprecated Value Members From scala.reflect.ClassTag
--------------------------------------------------------------------------------


### `abstract def runtimeClass: Class[_]`                                    ###

A class representing the type `U` to which `T` would be erased. Note that there
is no subtyping relationship between `T` and `U` .
(defined at scala.reflect.ClassTag)
