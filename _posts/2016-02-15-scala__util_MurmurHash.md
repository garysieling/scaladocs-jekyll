
#                            scala.util.MurmurHash                            #

```scala
class MurmurHash[T] extends (T) ⇒ Unit
```

A class designed to generate well-distributed non-cryptographic hashes. It is
designed to be passed to a collection's foreach method, or can take individual
hash values with append. Its own hash code is set equal to the hash code of
whatever it is hashing.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ Use the object MurmurHash3 instead.
* Source
  * [MurmurHash.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/MurmurHash.scala#L1)


--------------------------------------------------------------------------------
                       Value Members From scala.Function1
--------------------------------------------------------------------------------


### `def andThen[A](g: (Unit) ⇒ A): (T) ⇒ A`                                 ###

Composes two instances of Function1 in a new Function1, with this function
applied first.

* A
  * the result type of function `g`
* g
  * a function R => A
* returns
  * a new function `f` such that `f(x) == g(apply(x))`

* Definition Classes
  * Function1
* Annotations
  * @ unspecialized ()

(defined at scala.Function1)


### `def compose[A](g: (A) ⇒ T): (A) ⇒ Unit`                                 ###

Composes two instances of Function1 in a new Function1, with this function
applied last.

* A
  * the type to which function `g` can be applied
* g
  * a function A => T1
* returns
  * a new function `f` such that `f(x) == apply(g(x))`

* Definition Classes
  * Function1
* Annotations
  * @ unspecialized ()

(defined at scala.Function1)


--------------------------------------------------------------------------------
                Instance Constructors From scala.util.MurmurHash
--------------------------------------------------------------------------------


### `new MurmurHash(seed: Int)`                                              ###

(defined at scala.util.MurmurHash)


--------------------------------------------------------------------------------
                    Value Members From scala.util.MurmurHash
--------------------------------------------------------------------------------


### `def append(i: Int): Unit`                                               ###

Incorporate a known hash value.

(defined at scala.util.MurmurHash)


### `def apply(t: T): Unit`                                                  ###

Incorporate the hash value of one item.

* returns
  * the result of function application.

* Definition Classes
  * MurmurHash → Function1
(defined at scala.util.MurmurHash)
