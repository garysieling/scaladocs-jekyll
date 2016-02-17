
#                                scala.sys.Prop                                #

```scala
trait Prop[+T] extends AnyRef
```

A lightweight interface wrapping a property contained in some unspecified map.
Generally it'll be the system properties but this is not a requirement.

See `scala.sys.SystemProperties` for an example usage.

* Source
  * [Prop.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/Prop.scala#L1)
* Version
  * 2.9
* Since
  * 2.9


--------------------------------------------------------------------------------
                   Abstract Value Members From scala.sys.Prop
--------------------------------------------------------------------------------


### `abstract def set(newValue: String): String`                             ###

Sets the property.

* newValue
  * the new string value
* returns
  * the old value, or null if it was unset.

(defined at scala.sys.Prop)


### `abstract def setValue[T1 >: T](value: T1): T`                           ###

Sets the property with a value of the represented type.

(defined at scala.sys.Prop)


--------------------------------------------------------------------------------
                   Concrete Value Members From scala.sys.Prop
--------------------------------------------------------------------------------


### `abstract def clear(): Unit`                                             ###

Removes the property from the underlying map.
(defined at scala.sys.Prop)
