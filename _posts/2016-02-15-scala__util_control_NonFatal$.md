
#                         scala.util.control.NonFatal                         #

```scala
object NonFatal
```

Extractor of non-fatal Throwables. Will not match fatal errors like
 `VirtualMachineError` (for example, `OutOfMemoryError` and
 `StackOverflowError` , subclasses of `VirtualMachineError` ), `ThreadDeath` ,
 `LinkageError` , `InterruptedException` , `ControlThrowable` .

Note that scala.util.control.ControlThrowable, an internal Throwable, is not
matched by `NonFatal` (and would therefore be thrown).

For example, all harmless Throwables can be caught by:

```scala
try {
  // dangerous stuff
} catch {
  case NonFatal(e) => log.error(e, "Something not that bad.")
 // or
  case e if NonFatal(e) => log.error(e, "Something not that bad.")
}
```

* Source
  * [NonFatal.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/control/NonFatal.scala#L1)


--------------------------------------------------------------------------------
                 Value Members From scala.util.control.NonFatal
--------------------------------------------------------------------------------


### `def apply(t: Throwable): Boolean`                                       ###

Returns true if the provided `Throwable` is to be considered non-fatal, or false
if it is to be considered fatal

(defined at scala.util.control.NonFatal)


### `def unapply(t: Throwable): Option[Throwable]`                           ###

Returns Some(t) if NonFatal(t) == true, otherwise None
(defined at scala.util.control.NonFatal)
