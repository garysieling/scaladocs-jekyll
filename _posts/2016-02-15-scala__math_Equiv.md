
#                               scala.math.Equiv                               #

```scala
trait Equiv[T] extends Serializable
```

A trait for representing equivalence relations. It is important to distinguish
between a type that can be compared for equality or equivalence and a
representation of equivalence on some type. This trait is for representing the
latter.

An [equivalence relation](http://en.wikipedia.org/wiki/Equivalence_relation) is
a binary relation on a type. This relation is exposed as the `equiv` method of
the `Equiv` trait. The relation must be:

1. reflexive: `equiv(x, x) == true` for any x of type `T` .
2. symmetric: `equiv(x, y) == equiv(y, x)` for any `x` and `y` of type `T` .
3. transitive: if `equiv(x, y) == true` and `equiv(y, z) == true` , then
    `equiv(x, z) == true` for any `x` , `y` , and `z` of type `T` .

* Source
  * [Equiv.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Equiv.scala#L1)
* Version
  * 1.0, 2008-04-03
* Since
  * 2.7


--------------------------------------------------------------------------------
                  Abstract Value Members From scala.math.Equiv
--------------------------------------------------------------------------------


### `abstract def equiv(x: T, y: T): Boolean`                                ###

Returns `true` iff `x` is equivalent to `y` .
(defined at scala.math.Equiv)
