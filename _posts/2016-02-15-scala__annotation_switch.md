
#                           scala.annotation.switch                           #

```scala
final class switch extends Annotation with StaticAnnotation
```

An annotation to be applied to a match expression. If present, the compiler will
verify that the match has been compiled to a
[tableswitch or lookupswitch](http://docs.oracle.com/javase/specs/jvms/se7/html/jvms-3.html#jvms-3.10)
and issue an error if it instead compiles into a series of conditional
expressions. Example usage:

```scala
val Constant = 'Q'
def tokenMe(ch: Char) = (ch: @switch) match {
  case ' ' | '\t' | '\n'  => 1
  case 'A' | 'Z' | '$'    => 2
  case '5' | Constant     => 3  // a non-literal may prevent switch generation: this would not compile
  case _                  => 4
}
```

Note: for pattern matches with one or two cases, the compiler generates jump
instructions. Annotating such a match with `@switch` does not issue any warning.

* Source
  * [switch.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/switch.scala#L1)
* Since
  * 2.8


--------------------------------------------------------------------------------
               Instance Constructors From scala.annotation.switch
--------------------------------------------------------------------------------


### `new switch()`                                                           ###
(defined at scala.annotation.switch)
