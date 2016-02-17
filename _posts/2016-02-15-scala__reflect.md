
#                                scala.reflect                                #

```scala
package reflect
```

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/reflect/package.scala#L1)


--------------------------------------------------------------------------------

--------------------------------------------------------------------------------


### `object ClassManifestFactory`                                            ###

 `ClassManifestFactory` defines factory methods for manifests. It is intended
for use by the compiler and should not be used in client code.

Unlike `ClassManifest` , this factory isn't annotated with a deprecation
warning. This is done to prevent avalanches of deprecation warnings in the code
that calls methods with manifests.

In a perfect world, we would just remove the @deprecated annotation from
 `ClassManifest` the object and then delete it in 2.11. After all, that object
is explicitly marked as internal, so noone should use it. However a lot of
existing libraries disregarded the scaladoc that comes with `ClassManifest` , so
we need to somehow nudge them into migrating prior to removing stuff out of the
blue. Hence we've introduced this design decision as the lesser of two evils.

* Source
  * [ClassManifestDeprecatedApis.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/reflect/ClassManifestDeprecatedApis.scala#L1)


### `object ClassTag extends Serializable`                                   ###

Class tags corresponding to primitive types and constructor/extractor for
ClassTags.

* Source
  * [ClassTag.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/reflect/ClassTag.scala#L1)


### `object ManifestFactory`                                                 ###

 `ManifestFactory` defines factory methods for manifests. It is intended for use
by the compiler and should not be used in client code.

Unlike `Manifest` , this factory isn't annotated with a deprecation warning.
This is done to prevent avalanches of deprecation warnings in the code that
calls methods with manifests. Why so complicated? Read up the comments for
 `ClassManifestFactory` .

* Source
  * [Manifest.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/reflect/Manifest.scala#L1)


### `object NameTransformer`                                                 ###

Provides functions to encode and decode Scala symbolic names. Also provides some
constants.

* Source
  * [NameTransformer.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/reflect/NameTransformer.scala#L1)


### `object NoManifest extends OptManifest[Nothing] with Serializable`       ###

One of the branches of an scala.reflect.OptManifest.

* Source
  * [NoManifest.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/reflect/NoManifest.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `abstract class AnyValManifest[T <: AnyVal] extends Manifest[T] with Equals` ###

* Annotations
  * @ SerialVersionUID ()
* Source
  * [Manifest.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/reflect/Manifest.scala#L1)


### `type ClassManifest[T] = ClassTag[T]`                                    ###

A `ClassManifest[T]` is an opaque descriptor for type `T` .


### `trait ClassManifestDeprecatedApis[T] extends OptManifest[T]`            ###

* Self Type
  * ClassManifest [T]
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ Use scala.reflect.ClassTag instead
* Source
  * [ClassManifestDeprecatedApis.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/reflect/ClassManifestDeprecatedApis.scala#L1)


### `trait ClassTag[T] extends ClassManifestDeprecatedApis[T] with Equals with Serializable` ###

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


### `trait Manifest[T] extends ClassManifest[T] with Equals`                 ###

A `Manifest[T]` is an opaque descriptor for type T. Its supported use is to give
access to the erasure of the type as a `Class` instance, as is necessary for the
creation of native `Arrays` if the class is not known at compile time.

The type-relation operators `<:<` and `=:=` should be considered approximations
only, as there are numerous aspects of type conformance which are not yet
adequately represented in manifests.

Example usages:

```scala
def arr[T] = new Array[T](0)                          // does not compile
def arr[T](implicit m: Manifest[T]) = new Array[T](0) // compiles
def arr[T: Manifest] = new Array[T](0)                // shorthand for the preceding

// Methods manifest, classManifest, and optManifest are in [[scala.Predef]].
def isApproxSubType[T: Manifest, U: Manifest] = manifest[T] <:< manifest[U]
isApproxSubType[List[String], List[AnyRef]] // true
isApproxSubType[List[String], List[Int]]    // false

def methods[T: ClassManifest] = classManifest[T].erasure.getMethods
def retType[T: ClassManifest](name: String) =
  methods[T] find (_.getName == name) map (_.getGenericReturnType)

retType[Map[_, _]]("values")  // Some(scala.collection.Iterable)
```

* Annotations
  * @ implicitNotFound (msg = "No Manifest available for ${T}.")
* Source
  * [Manifest.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/reflect/Manifest.scala#L1)


### `trait OptManifest[+T] extends Serializable`                             ###

A `OptManifest[T]` is an optional scala.reflect.Manifest.

It is either a `Manifest` or the value `NoManifest` .

* Source
  * [OptManifest.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/reflect/OptManifest.scala#L1)

