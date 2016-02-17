
#                            scala.Predef.Ensuring                            #

```scala
implicit final class Ensuring[A] extends AnyVal
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
                Instance Constructors From scala.Predef.Ensuring
--------------------------------------------------------------------------------


### `new Ensuring(self: A)`                                                  ###

(defined at scala.Predef.Ensuring)


--------------------------------------------------------------------------------
                    Value Members From scala.Predef.Ensuring
--------------------------------------------------------------------------------


### `def ensuring(cond: (A) ⇒ Boolean): A`                                   ###

(defined at scala.Predef.Ensuring)


### `def ensuring(cond: (A) ⇒ Boolean, msg: ⇒ Any): A`                       ###

(defined at scala.Predef.Ensuring)


### `def ensuring(cond: Boolean): A`                                         ###

(defined at scala.Predef.Ensuring)


### `def ensuring(cond: Boolean, msg: ⇒ Any): A`                             ###
(defined at scala.Predef.Ensuring)
