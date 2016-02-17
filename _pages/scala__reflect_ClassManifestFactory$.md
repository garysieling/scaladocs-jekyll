
#                      scala.reflect.ClassManifestFactory                      #

```scala
object ClassManifestFactory
```

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


--------------------------------------------------------------------------------
             Value Members From scala.reflect.ClassManifestFactory
--------------------------------------------------------------------------------


### `val Any: Manifest[Any]`                                                 ###

(defined at scala.reflect.ClassManifestFactory)


### `val AnyVal: Manifest[AnyVal]`                                           ###

(defined at scala.reflect.ClassManifestFactory)


### `val Boolean: AnyValManifest[Boolean]`                                   ###

(defined at scala.reflect.ClassManifestFactory)


### `val Byte: AnyValManifest[Byte]`                                         ###

(defined at scala.reflect.ClassManifestFactory)


### `val Char: AnyValManifest[Char]`                                         ###

(defined at scala.reflect.ClassManifestFactory)


### `val Double: AnyValManifest[Double]`                                     ###

(defined at scala.reflect.ClassManifestFactory)


### `val Float: AnyValManifest[Float]`                                       ###

(defined at scala.reflect.ClassManifestFactory)


### `val Int: AnyValManifest[Int]`                                           ###

(defined at scala.reflect.ClassManifestFactory)


### `val Long: AnyValManifest[Long]`                                         ###

(defined at scala.reflect.ClassManifestFactory)


### `val Nothing: Manifest[Nothing]`                                         ###

(defined at scala.reflect.ClassManifestFactory)


### `val Null: Manifest[Null]`                                               ###

(defined at scala.reflect.ClassManifestFactory)


### `val Object: Manifest[AnyRef]`                                           ###

(defined at scala.reflect.ClassManifestFactory)


### `val Short: AnyValManifest[Short]`                                       ###

(defined at scala.reflect.ClassManifestFactory)


### `val Unit: AnyValManifest[Unit]`                                         ###

(defined at scala.reflect.ClassManifestFactory)


### `def abstractType[T](prefix: OptManifest[_], name: String, upperbound: ClassManifest[_], args: OptManifest[_]*): ClassManifest[T]` ###

ClassManifest for the abstract type `prefix # name` . `upperBound` is not
strictly necessary as it could be obtained by reflection. It was added so that
erasure can be calculated without reflection. todo: remove after next bootstrap

(defined at scala.reflect.ClassManifestFactory)


### `def abstractType[T](prefix: OptManifest[_], name: String, clazz: Class[_], args: OptManifest[_]*): ClassManifest[T]` ###

ClassManifest for the abstract type `prefix # name` . `upperBound` is not
strictly necessary as it could be obtained by reflection. It was added so that
erasure can be calculated without reflection.

(defined at scala.reflect.ClassManifestFactory)


### `def arrayType[T](arg: OptManifest[_]): ClassManifest[Array[T]]`         ###

(defined at scala.reflect.ClassManifestFactory)


### `def classType[T](clazz: Class[_]): ClassManifest[T]`                    ###

ClassManifest for the class type `clazz` , where `clazz` is a top-level or
static class.

* Note
  * This no-prefix, no-arguments case is separate because we it's called from
    ScalaRunTime.boxArray itself. If we pass varargs as arrays into this, we get
    an infinitely recursive call to boxArray. (Besides, having a separate case
    is more efficient)

(defined at scala.reflect.ClassManifestFactory)


### `def classType[T](clazz: Class[_], arg1: OptManifest[_], args: OptManifest[_]*): ClassManifest[T]` ###

ClassManifest for the class type `clazz[args]` , where `clazz` is a top-level or
static class and `args` are its type arguments

(defined at scala.reflect.ClassManifestFactory)


### `def classType[T](prefix: OptManifest[_], clazz: Class[_], args: OptManifest[_]*): ClassManifest[T]` ###

ClassManifest for the class type `clazz[args]` , where `clazz` is a class with
non-package prefix type `prefix` and type arguments `args` .

(defined at scala.reflect.ClassManifestFactory)


### `def fromClass[T](clazz: Class[T]): ClassManifest[T]`                    ###

(defined at scala.reflect.ClassManifestFactory)


### `def singleType[T <: AnyRef](value: AnyRef): Manifest[T]`                ###
(defined at scala.reflect.ClassManifestFactory)
