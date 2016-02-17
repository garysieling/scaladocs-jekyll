
#                                 scala.throws                                 #

```scala
class throws[T <: Throwable] extends Annotation with StaticAnnotation
```

Annotation for specifying the exceptions thrown by a method. For example:

```scala
class Reader(fname: String) {
  private val in = new BufferedReader(new FileReader(fname))
  @throws[IOException]("if the file doesn't exist")
  def read() = in.read()
}
```

* Source
  * [throws.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/throws.scala#L1)
* Version
  * 1.0, 19/05/2006
* Since
  * 2.1


--------------------------------------------------------------------------------
                    Instance Constructors From scala.throws
--------------------------------------------------------------------------------


### `new throws(clazz: Class[T])`                                            ###
(defined at scala.throws)
