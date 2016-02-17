
#                               scala.Predef.=:=                               #

```scala
sealed abstract class =:=[From, To] extends (From) ⇒ To with Serializable
```

An instance of `A =:= B` witnesses that the types `A` and `B` are equal.

* Annotations
  * @ implicitNotFound (msg =...)
* Source
  * [Predef.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Predef.scala#L1)
* See also
  * `<:<` for expressing subtyping constraints


--------------------------------------------------------------------------------
                  Abstract Value Members From scala.Function1
--------------------------------------------------------------------------------


### `abstract def apply(v1: From): To`                                       ###

Apply the body of this function to the argument.

* returns
  * the result of function application.

* Definition Classes
  * Function1

(defined at scala.Function1)


--------------------------------------------------------------------------------
                  Concrete Value Members From scala.Function1
--------------------------------------------------------------------------------


### `def andThen[A](g: (To) ⇒ A): (From) ⇒ A`                                ###

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


### `def compose[A](g: (A) ⇒ From): (A) ⇒ To`                                ###

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


### `def toString(): java.lang.String`                                       ###

Creates a String representation of this object. The default representation is
platform dependent. On the java platform it is the concatenation of the class
name, "@", and the object's hashcode in hexadecimal.

* returns
  * a String representation of the object.

* Definition Classes
  * Function1 → AnyRef → Any
(defined at scala.Function1)
