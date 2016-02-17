
#                                 scala.Equals                                 #

```scala
trait Equals extends Any
```

An interface containing operations for equality. The only method not already
present in class `AnyRef` is `canEqual` .

* Source
  * [Equals.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Equals.scala#L1)


--------------------------------------------------------------------------------
                    Abstract Value Members From scala.Equals
--------------------------------------------------------------------------------


### `abstract def canEqual(that: Any): Boolean`                              ###

A method that should be called from every well-designed equals method that is
open to be overridden in a subclass. See
[Programming in Scala, Chapter 28](http://www.artima.com/pins1ed/object-equality.html)
for discussion and design.

* that
  * the value being probed for possible equality
* returns
  * true if this instance can possibly equal `that` , otherwise false
(defined at scala.Equals)
