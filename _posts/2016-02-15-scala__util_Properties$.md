
#                            scala.util.Properties                            #

```scala
object Properties extends PropertiesTrait
```

Loads `library.properties` from the jar.

* Source
  * [Properties.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/Properties.scala#L1)


--------------------------------------------------------------------------------
                    Value Members From scala.util.Properties
--------------------------------------------------------------------------------


### `val ScalaCompilerVersion: Name`                                         ###

Scala manifest attributes.

(defined at scala.util.Properties)


--------------------------------------------------------------------------------
                 Value Members From scala.util.PropertiesTrait
--------------------------------------------------------------------------------


### `def clearProp(name: String): String`                                    ###

* Definition Classes
  * PropertiesTrait

(defined at scala.util.PropertiesTrait)


### `def envOrElse(name: String, alt: String): String`                       ###

* Definition Classes
  * PropertiesTrait

(defined at scala.util.PropertiesTrait)


### `def envOrNone(name: String): Option[String]`                            ###

* Definition Classes
  * PropertiesTrait

(defined at scala.util.PropertiesTrait)


### `def envOrSome(name: String, alt: Option[String]): Option[String]`       ###

* Definition Classes
  * PropertiesTrait

(defined at scala.util.PropertiesTrait)


### `def isJavaAtLeast(version: String): Boolean`                            ###

Compares the given specification version to the specification version of the
platform.

* version
  * a specification version of the form "major.minor"
* returns
  * `true` iff the specification version of the current runtime is equal to or
    higher than the version denoted by the given string.

* Definition Classes
  * PropertiesTrait
* Exceptions thrown
  * NumberFormatException if the given string is not a version string

Example:

```scala
// In this example, the runtime's Java specification is assumed to be at version 1.7.
isJavaAtLeast("1.6")            // true
isJavaAtLeast("1.7")            // true
isJavaAtLeast("1.8")            // false
```

(defined at scala.util.PropertiesTrait)


### `def main(args: Array[String]): Unit`                                    ###

* Definition Classes
  * PropertiesTrait

(defined at scala.util.PropertiesTrait)


### `def propIsSet(name: String): Boolean`                                   ###

* Definition Classes
  * PropertiesTrait

(defined at scala.util.PropertiesTrait)


### `def propIsSetTo(name: String, value: String): Boolean`                  ###

* Definition Classes
  * PropertiesTrait

(defined at scala.util.PropertiesTrait)


### `def propOrElse(name: String, alt: String): String`                      ###

* Definition Classes
  * PropertiesTrait

(defined at scala.util.PropertiesTrait)


### `def propOrEmpty(name: String): String`                                  ###

* Definition Classes
  * PropertiesTrait

(defined at scala.util.PropertiesTrait)


### `def propOrFalse(name: String): Boolean`                                 ###

* Definition Classes
  * PropertiesTrait

(defined at scala.util.PropertiesTrait)


### `def propOrNone(name: String): Option[String]`                           ###

* Definition Classes
  * PropertiesTrait

(defined at scala.util.PropertiesTrait)


### `def propOrNull(name: String): String`                                   ###

* Definition Classes
  * PropertiesTrait

(defined at scala.util.PropertiesTrait)


### `def scalaPropOrElse(name: String, alt: String): String`                 ###

* Definition Classes
  * PropertiesTrait

(defined at scala.util.PropertiesTrait)


### `def scalaPropOrEmpty(name: String): String`                             ###

* Definition Classes
  * PropertiesTrait

(defined at scala.util.PropertiesTrait)


### `def scalaPropOrNone(name: String): Option[String]`                      ###

* Definition Classes
  * PropertiesTrait

(defined at scala.util.PropertiesTrait)


### `def setProp(name: String, value: String): String`                       ###

* Definition Classes
  * PropertiesTrait
(defined at scala.util.PropertiesTrait)
