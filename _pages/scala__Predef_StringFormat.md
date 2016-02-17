
#                          scala.Predef.StringFormat                          #

```scala
implicit final class StringFormat[A] extends AnyVal
```

* Source
  * [Predef.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Predef.scala#L1)


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


--------------------------------------------------------------------------------
              Instance Constructors From scala.Predef.StringFormat
--------------------------------------------------------------------------------


### `new StringFormat(self: A)`                                              ###

(defined at scala.Predef.StringFormat)


--------------------------------------------------------------------------------
                  Value Members From scala.Predef.StringFormat
--------------------------------------------------------------------------------


### `def formatted(fmtstr: String): String`                                  ###

Returns string formatted according to given `format` string. Format strings are
as for `String.format` (@see java.lang.String.format).

* Annotations
  * @ inline ()
(defined at scala.Predef.StringFormat)
