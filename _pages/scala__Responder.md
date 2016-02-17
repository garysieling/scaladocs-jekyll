
#                               scala.Responder                               #

```scala
abstract class Responder[+A] extends Serializable
```

Instances of responder are the building blocks of small programs written in
continuation passing style. By using responder classes in for comprehensions,
one can embed domain-specific languages in Scala while giving the impression
that programs in these DSLs are written in direct style.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ This class will be removed
* Source
  * [Responder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Responder.scala#L1)
* Version
  * 1.0
* Since
  * 2.1


--------------------------------------------------------------------------------
                  Abstract Value Members From scala.Responder
--------------------------------------------------------------------------------


### `abstract def respond(k: (A) ⇒ Unit): Unit`                              ###

(defined at scala.Responder)


--------------------------------------------------------------------------------
                  Concrete Value Members From scala.Responder
--------------------------------------------------------------------------------


### `def filter(p: (A) ⇒ Boolean): Responder[A]`                             ###

(defined at scala.Responder)


### `def flatMap[B](f: (A) ⇒ Responder[B]): Responder[B]`                    ###

(defined at scala.Responder)


### `def foreach(k: (A) ⇒ Unit): Unit`                                       ###

(defined at scala.Responder)


### `def map[B](f: (A) ⇒ B): Responder[B]`                                   ###

(defined at scala.Responder)


--------------------------------------------------------------------------------
                   Instance Constructors From scala.Responder
--------------------------------------------------------------------------------


### `new Responder()`                                                        ###
(defined at scala.Responder)
