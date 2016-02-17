
#                              scala.DelayedInit                              #

```scala
trait DelayedInit extends AnyRef
```

Classes and objects (but note, not traits) inheriting the `DelayedInit` marker
trait will have their initialization code rewritten as follows: `code` becomes
 `delayedInit(code)` .

Initialization code comprises all statements and all value definitions that are
executed during initialization.

Example:

```scala
trait Helper extends DelayedInit {
  def delayedInit(body: => Unit) = {
    println("dummy text, printed before initialization of C")
    body // evaluates the initialization code of C
  }
}

class C extends Helper {
  println("this is the initialization code of C")
}

object Test extends App {
  val c = new C
}
```

Should result in the following being printed:

```scala
dummy text, printed before initialization of C
this is the initialization code of C
```

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ DelayedInit semantics can be surprising. Support
    for `App` will continue. See the release notes for more details:
    https://github.com/scala/scala/releases/tag/v2.11.0-RC1
* Source
  * [DelayedInit.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/DelayedInit.scala#L1)
* See also
  * "Delayed Initialization" subsection of the Scala Language Specification
    (section 5.1)


--------------------------------------------------------------------------------
                 Abstract Value Members From scala.DelayedInit
--------------------------------------------------------------------------------


### `abstract def delayedInit(x: ⇒ Unit): Unit`                              ###
(defined at scala.DelayedInit)
