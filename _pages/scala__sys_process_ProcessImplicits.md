
#                      scala.sys.process.ProcessImplicits                      #

```scala
trait ProcessImplicits extends AnyRef
```

Provide implicit conversions for the factories offered by
scala.sys.process.Process 's companion object. These implicits can then be used
to decrease the noise in a pipeline of commands, making it look more shell-like.
They are available through the package object scala.sys.process.

* Source
  * [Process.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/process/Process.scala#L1)


--------------------------------------------------------------------------------
             Value Members From scala.sys.process.ProcessImplicits
--------------------------------------------------------------------------------


### `implicit def builderToProcess(builder: JProcessBuilder): ProcessBuilder` ###

Implicitly convert a `java.lang.ProcessBuilder` into a Scala one.

(defined at scala.sys.process.ProcessImplicits)


### `implicit def buildersToProcess[T](builders: Seq[T])(implicit convert: (T) ⇒ Source): Seq[Source]` ###

Return a sequence of scala.sys.process.ProcessBuilder.Source from a sequence of
values for which an implicit conversion to `Source` is available.

(defined at scala.sys.process.ProcessImplicits)


### `implicit def fileToProcess(file: File): FileBuilder`                    ###

Implicitly convert a `java.io.File` into a
scala.sys.process.ProcessBuilder.FileBuilder, which can be used as either input
or output of a process. For example:

```scala
import scala.sys.process._
"ls" #> new java.io.File("dirContents.txt") !
```

(defined at scala.sys.process.ProcessImplicits)


### `implicit def stringSeqToProcess(command: Seq[String]): ProcessBuilder`  ###

Implicitly convert a sequence of `String` into a
scala.sys.process.ProcessBuilder. The first argument will be taken to be the
command to be executed, and the remaining will be its arguments. When using
this, arguments may contain spaces.

(defined at scala.sys.process.ProcessImplicits)


### `implicit def stringToProcess(command: String): ProcessBuilder`          ###

Implicitly convert a `String` into a scala.sys.process.ProcessBuilder.

(defined at scala.sys.process.ProcessImplicits)


### `implicit def urlToProcess(url: URL): URLBuilder`                        ###

Implicitly convert a `java.net.URL` into a
scala.sys.process.ProcessBuilder.URLBuilder, which can be used as input to a
process. For example:

```scala
import scala.sys.process._
Seq("xmllint", "--html", "-") #< new java.net.URL("http://www.scala-lang.org") #> new java.io.File("fixed.html") !
```
(defined at scala.sys.process.ProcessImplicits)
