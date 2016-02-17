
#                                 scala.Symbol                                 #

```scala
final class Symbol extends Serializable
```

This class provides a simple way to get unique objects for equal strings. Since
symbols are interned, they can be compared using reference equality. Instances
of `Symbol` can be created easily with Scala's built-in quote mechanism.

For instance, the [Scala](http://scala-lang.org/#_top) term `'mysym` will invoke
the constructor of the `Symbol` class in the following way: `Symbol("mysym")` .

* Source
  * [Symbol.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Symbol.scala#L1)
* Version
  * 1.8


--------------------------------------------------------------------------------
                        Value Members From scala.Symbol
--------------------------------------------------------------------------------


### `def equals(other: Any): Boolean`                                        ###

The equality method for reference types. Default implementation delegates to
 `eq` .

See also `equals` in scala.Any.

* returns
  * `true` if the receiver object is equivalent to the argument; `false`
    otherwise.

* Definition Classes
  * Symbol → AnyRef → Any
(defined at scala.Symbol)
