
#                               scala.Function0                               #

```scala
trait Function0[+R] extends AnyRef
```

A function of 0 parameters.

In the following example, the definition of javaVersion is a shorthand for the
anonymous class definition anonfun0:

```scala
object Main extends App {
   val javaVersion = () => sys.props("java.version")

   val anonfun0 = new Function0[String] {
     def apply(): String = sys.props("java.version")
   }
   assert(javaVersion() == anonfun0())
}
```

* Self Type
  * () ⇒ R
* Source
  * [Function0.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Function0.scala#L1)


--------------------------------------------------------------------------------
                  Concrete Value Members From scala.Function0
--------------------------------------------------------------------------------


### `abstract def apply(): R`                                                ###

Apply the body of this function to the arguments.

* returns
  * the result of function application.
(defined at scala.Function0)
