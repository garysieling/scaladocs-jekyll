
#                          scala.sys.SystemProperties                          #

```scala
object SystemProperties
```

The values in SystemProperties can be used to access and manipulate designated
system properties. See `scala.sys.Prop` for particulars.

* Source
  * [SystemProperties.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/SystemProperties.scala#L1)

Example:

```scala
if (!headless.isSet) headless.enable()
```


--------------------------------------------------------------------------------
            Deprecated Value Members From scala.sys.SystemProperties
--------------------------------------------------------------------------------


### `def noTraceSupression: BooleanProp`                                     ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.12.0)_ Use noTraceSuppression

(defined at scala.sys.SystemProperties)


--------------------------------------------------------------------------------
                 Value Members From scala.sys.SystemProperties
--------------------------------------------------------------------------------


### `def exclusively[T](body: ⇒ T): T`                                       ###

An unenforceable, advisory only place to do some synchronization when mutating
system properties.

(defined at scala.sys.SystemProperties)


### `lazy val headless: BooleanProp`                                         ###

(defined at scala.sys.SystemProperties)


### `def help(key: String): String`                                          ###

(defined at scala.sys.SystemProperties)


### `lazy val noTraceSuppression: BooleanProp`                               ###

(defined at scala.sys.SystemProperties)


### `lazy val preferIPv4Stack: BooleanProp`                                  ###

(defined at scala.sys.SystemProperties)


### `lazy val preferIPv6Addresses: BooleanProp`                              ###

(defined at scala.sys.SystemProperties)


### `implicit def systemPropertiesToCompanion(p: SystemProperties): SystemProperties.type` ###
(defined at scala.sys.SystemProperties)
