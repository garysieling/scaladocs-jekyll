
#                      scala.concurrent.duration.IntMult                      #

```scala
implicit final class IntMult extends AnyVal
```

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/duration/package.scala#L1)


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
          Instance Constructors From scala.concurrent.duration.IntMult
--------------------------------------------------------------------------------


### `new IntMult(i: Int)`                                                    ###

(defined at scala.concurrent.duration.IntMult)


--------------------------------------------------------------------------------
              Value Members From scala.concurrent.duration.IntMult
--------------------------------------------------------------------------------


### `def *(d: Duration): Duration`                                           ###

(defined at scala.concurrent.duration.IntMult)


### `def *(d: FiniteDuration): FiniteDuration`                               ###
(defined at scala.concurrent.duration.IntMult)
