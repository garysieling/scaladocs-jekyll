
#                      scala.sys.process.ProcessCreation                      #

```scala
trait ProcessCreation extends AnyRef
```

Factories for creating scala.sys.process.ProcessBuilder. They can be found on
and used through scala.sys.process.Process 's companion object.

* Source
  * [Process.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/process/Process.scala#L1)


--------------------------------------------------------------------------------
              Value Members From scala.sys.process.ProcessCreation
--------------------------------------------------------------------------------


### `def apply(value: Boolean): ProcessBuilder`                              ###

Creates a scala.sys.process.ProcessBuilder from a `Boolean` . This can be to
force an exit value.

(defined at scala.sys.process.ProcessCreation)


### `def apply(file: File): FileBuilder`                                     ###

Creates a scala.sys.process.ProcessBuilder from a `java.io.File` . This
 `ProcessBuilder` can then be used as a `Source` or a `Sink` , so one can pipe
things from and to it.

(defined at scala.sys.process.ProcessCreation)


### `def apply(builder: JProcessBuilder): ProcessBuilder`                    ###

Creates a scala.sys.process.ProcessBuilder from a `java.lang.ProcessBuilder` .

Example:

```scala
apply((new java.lang.ProcessBuilder("ls", "-l")) directory new java.io.File(System.getProperty("user.home")))
```

(defined at scala.sys.process.ProcessCreation)


### `def apply(command: Seq[String]): ProcessBuilder`                        ###

Creates a scala.sys.process.ProcessBuilder from a sequence of `String` , where
the head is the command and each element of the tail is a parameter.

Example:

```scala
apply("cat" :: files)
```

(defined at scala.sys.process.ProcessCreation)


### `def apply(command: Seq[String], cwd: File, extraEnv: (String, String)*): ProcessBuilder` ###

Creates a scala.sys.process.ProcessBuilder with working dir set to `File` and
extra environment variables.

Example:

```scala
apply("java" :: javaArgs, new java.io.File("/opt/app"), "CLASSPATH" -> "library.jar")
```

(defined at scala.sys.process.ProcessCreation)


### `def apply(command: Seq[String], cwd: Option[File], extraEnv: (String, String)*): ProcessBuilder` ###

Creates a scala.sys.process.ProcessBuilder with working dir optionally set to
 `File` and extra environment variables.

Example:

```scala
apply("java" :: javaArgs, params.get("cwd"), "CLASSPATH" -> "library.jar")
```

(defined at scala.sys.process.ProcessCreation)


### `def apply(command: String): ProcessBuilder`                             ###

Creates a scala.sys.process.ProcessBuilder from a `String` , including the
parameters.

Example:

```scala
apply("cat file.txt")
```

(defined at scala.sys.process.ProcessCreation)


### `def apply(command: String, cwd: File, extraEnv: (String, String)*): ProcessBuilder` ###

Creates a scala.sys.process.ProcessBuilder with working dir set to `File` and
extra environment variables.

Example:

```scala
apply("java", new java.io.File("/opt/app"), "CLASSPATH" -> "library.jar")
```

(defined at scala.sys.process.ProcessCreation)


### `def apply(command: String, cwd: Option[File], extraEnv: (String, String)*): ProcessBuilder` ###

Creates a scala.sys.process.ProcessBuilder with working dir optionally set to
 `File` and extra environment variables.

Example:

```scala
apply("java", params.get("cwd"), "CLASSPATH" -> "library.jar")
```

(defined at scala.sys.process.ProcessCreation)


### `def apply(command: String, arguments: Seq[String]): ProcessBuilder`     ###

Creates a scala.sys.process.ProcessBuilder from a command represented by a
 `String` , and a sequence of `String` representing the arguments.

Example:

```scala
apply("cat", files)
```

(defined at scala.sys.process.ProcessCreation)


### `def apply(name: String, exitValue: ⇒ Int): ProcessBuilder`              ###

Creates a scala.sys.process.ProcessBuilder from a `String` name and a `Boolean` .
This can be used to force an exit value, with the name being used for
 `toString` .

(defined at scala.sys.process.ProcessCreation)


### `def apply(url: URL): URLBuilder`                                        ###

Creates a scala.sys.process.ProcessBuilder from a `java.net.URL` . This
 `ProcessBuilder` can then be used as a `Source` , so that one can pipe things
from it.

(defined at scala.sys.process.ProcessCreation)


### `def applySeq[T](builders: Seq[T])(implicit convert: (T) ⇒ Source): Seq[Source]` ###

Creates a sequence of scala.sys.process.ProcessBuilder.Source from a sequence of
something else for which there's an implicit conversion to `Source` .

(defined at scala.sys.process.ProcessCreation)


### `def cat(files: Seq[Source]): ProcessBuilder`                            ###

Creates a scala.sys.process.ProcessBuilder from a non-empty sequence of
scala.sys.process.ProcessBuilder.Source, which can then be piped to something
else.

This will concatenate the output of all sources.

(defined at scala.sys.process.ProcessCreation)


### `def cat(file: Source, files: Source*): ProcessBuilder`                  ###

Creates a scala.sys.process.ProcessBuilder from one or more
scala.sys.process.ProcessBuilder.Source, which can then be piped to something
else.

This will concatenate the output of all sources. For example:

```scala
import scala.sys.process._
import scala.sys.process.Process.cat
import java.net.URL
import java.io.File

val spde = new URL("http://technically.us/spde.html")
val dispatch = new URL("http://dispatch.databinder.net/Dispatch.html")
val build = new File("project/build.properties")
cat(spde, dispatch, build) #| "grep -i scala" !
```
(defined at scala.sys.process.ProcessCreation)
