
#                            scala.sys.BooleanProp                            #

```scala
object BooleanProp
```

* Source
  * [BooleanProp.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/BooleanProp.scala#L1)


--------------------------------------------------------------------------------
                    Value Members From scala.sys.BooleanProp
--------------------------------------------------------------------------------


### `implicit def booleanPropAsBoolean(b: BooleanProp): Boolean`             ###

(defined at scala.sys.BooleanProp)


### `def constant(key: String, isOn: Boolean): BooleanProp`                  ###

A constant true or false property which ignores all method calls.

(defined at scala.sys.BooleanProp)


### `def keyExists[T](key: String): BooleanProp`                             ###

As an alternative, this method creates a BooleanProp which is true if the key
exists in the map and is not assigned a value other than "true", compared
case-insensitively, or the empty string. This way -Dmy.property results in a
true-valued property, but -Dmy.property=false does not.

* returns
  * A BooleanProp with a liberal truth policy

(defined at scala.sys.BooleanProp)


### `def valueIsTrue[T](key: String): BooleanProp`                           ###

The java definition of property truth is that the key be in the map and the
value be equal to the String "true", case insensitively. This method creates a
BooleanProp instance which adheres to that definition.

* returns
  * A BooleanProp which acts like java's Boolean.getBoolean
(defined at scala.sys.BooleanProp)
