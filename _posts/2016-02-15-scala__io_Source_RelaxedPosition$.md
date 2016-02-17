
#                       scala.io.Source#RelaxedPosition                       #

```scala
object RelaxedPosition extends Position
```

A Position implementation which ignores errors in the positions.

* Source
  * [Source.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/io/Source.scala#L1)


--------------------------------------------------------------------------------
                      Value Members From scala.io.Position
--------------------------------------------------------------------------------


### `final def column(pos: Int): Int`                                        ###

Returns the column number of the encoded position.

* Definition Classes
  * Position

(defined at scala.io.Position)


### `final def encode(line: Int, column: Int): Int`                          ###

Encodes a position into a single integer.

* Definition Classes
  * Position

(defined at scala.io.Position)


### `final def line(pos: Int): Int`                                          ###

Returns the line number of the encoded position.

* Definition Classes
  * Position

(defined at scala.io.Position)


### `def toString(pos: Int): String`                                         ###

Returns a string representation of the encoded position.

* Definition Classes
  * Position

(defined at scala.io.Position)


--------------------------------------------------------------------------------
               Value Members From scala.io.Source.RelaxedPosition
--------------------------------------------------------------------------------


### `def checkInput(line: Int, column: Int): Unit`                           ###

Definable behavior for overflow conditions.

* Definition Classes
  * RelaxedPosition → Position
(defined at scala.io.Source.RelaxedPosition)
