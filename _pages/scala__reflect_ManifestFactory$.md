
#                        scala.reflect.ManifestFactory                        #

```scala
object ManifestFactory
```

 `ManifestFactory` defines factory methods for manifests. It is intended for use
by the compiler and should not be used in client code.

Unlike `Manifest` , this factory isn't annotated with a deprecation warning.
This is done to prevent avalanches of deprecation warnings in the code that
calls methods with manifests. Why so complicated? Read up the comments for
 `ClassManifestFactory` .

* Source
  * [Manifest.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/reflect/Manifest.scala#L1)


--------------------------------------------------------------------------------
                Value Members From scala.reflect.ManifestFactory
--------------------------------------------------------------------------------


### `val Any: Manifest[Any]`                                                 ###

(defined at scala.reflect.ManifestFactory)


### `val AnyRef: Manifest[AnyRef]`                                           ###

(defined at scala.reflect.ManifestFactory)


### `val AnyVal: Manifest[AnyVal]`                                           ###

(defined at scala.reflect.ManifestFactory)


### `val Boolean: AnyValManifest[Boolean]`                                   ###

(defined at scala.reflect.ManifestFactory)


### `val Byte: AnyValManifest[Byte]`                                         ###

(defined at scala.reflect.ManifestFactory)


### `val Char: AnyValManifest[Char]`                                         ###

(defined at scala.reflect.ManifestFactory)


### `val Double: AnyValManifest[Double]`                                     ###

(defined at scala.reflect.ManifestFactory)


### `val Float: AnyValManifest[Float]`                                       ###

(defined at scala.reflect.ManifestFactory)


### `val Int: AnyValManifest[Int]`                                           ###

(defined at scala.reflect.ManifestFactory)


### `val Long: AnyValManifest[Long]`                                         ###

(defined at scala.reflect.ManifestFactory)


### `val Nothing: Manifest[Nothing]`                                         ###

(defined at scala.reflect.ManifestFactory)


### `val Null: Manifest[Null]`                                               ###

(defined at scala.reflect.ManifestFactory)


### `val Object: Manifest[AnyRef]`                                           ###

(defined at scala.reflect.ManifestFactory)


### `val Short: AnyValManifest[Short]`                                       ###

(defined at scala.reflect.ManifestFactory)


### `val Unit: AnyValManifest[Unit]`                                         ###

(defined at scala.reflect.ManifestFactory)


### `def abstractType[T](prefix: Manifest[_], name: String, upperBound: Class[_], args: Manifest[_]*): Manifest[T]` ###

Manifest for the abstract type `prefix # name` . `upperBound` is not strictly
necessary as it could be obtained by reflection. It was added so that erasure
can be calculated without reflection.

(defined at scala.reflect.ManifestFactory)


### `def arrayType[T](arg: Manifest[_]): Manifest[Array[T]]`                 ###

(defined at scala.reflect.ManifestFactory)


### `def classType[T](clazz: Class[T], arg1: Manifest[_], args: Manifest[_]*): Manifest[T]` ###

Manifest for the class type `clazz` , where `clazz` is a top-level or static
class and args are its type arguments.

(defined at scala.reflect.ManifestFactory)


### `def classType[T](clazz: Class[_]): Manifest[T]`                         ###

Manifest for the class type `clazz[args]` , where `clazz` is a top-level or
static class.

* Note
  * This no-prefix, no-arguments case is separate because we it's called from
    ScalaRunTime.boxArray itself. If we pass varargs as arrays into this, we get
    an infinitely recursive call to boxArray. (Besides, having a separate case
    is more efficient)

(defined at scala.reflect.ManifestFactory)


### `def classType[T](prefix: Manifest[_], clazz: Class[_], args: Manifest[_]*): Manifest[T]` ###

Manifest for the class type `clazz[args]` , where `clazz` is a class with
non-package prefix type `prefix` and type arguments `args` .

(defined at scala.reflect.ManifestFactory)


### `def intersectionType[T](parents: Manifest[_]*): Manifest[T]`            ###

Manifest for the intersection type `parents_0 with ... with parents_n` .

(defined at scala.reflect.ManifestFactory)


### `def singleType[T <: AnyRef](value: AnyRef): Manifest[T]`                ###

Manifest for the singleton type `value.type` .

(defined at scala.reflect.ManifestFactory)


### `def valueManifests: List[AnyValManifest[_]]`                            ###

(defined at scala.reflect.ManifestFactory)


### `def wildcardType[T](lowerBound: Manifest[_], upperBound: Manifest[_]): Manifest[T]` ###

Manifest for the unknown type `_ >: L <: U` in an existential.
(defined at scala.reflect.ManifestFactory)
