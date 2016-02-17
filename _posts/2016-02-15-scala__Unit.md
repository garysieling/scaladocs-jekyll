
#                                  scala.Unit                                  #

```scala
abstract final class Unit extends AnyVal
```

 `Unit` is a subtype of scala.AnyVal. There is only one value of type `Unit` ,
 `()` , and it is not represented by any object in the underlying runtime
system. A method with return type `Unit` is analogous to a Java method which is
declared `void` .

* Source
  * [Unit.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Unit.scala#L1)


--------------------------------------------------------------------------------
                        Value Members From scala.Any###
--------------------------------------------------------------------------------


### `final def ##(): Int`                                                    ###

Equivalent to `x.hashCode` except for boxed numeric types and `null` . For
numerics, it returns a hash value which is consistent with value equality: if
two value type instances compare as true, then ## will produce the same hash
value for each of them. For `null` returns a hashcode where `null.hashCode`
throws a `NullPointerException` .

* returns
  * a hash value consistent with ==

* Definition Classes
  * Any
(defined at scala.Any###)
