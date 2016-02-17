
#                                  scala.Null                                  #

```scala
abstract final class Null extends AnyRef
```

 `Null` is - together with scala.Nothing - at the bottom of the Scala type
hierarchy.

 `Null` is a subtype of all reference types; its only instance is the `null`
reference. Since `Null` is not a subtype of value types, `null` is not a member
of any such type. For instance, it is not possible to assign `null` to a
variable of type scala.Int.

