
#                          scala.Enumeration#ValueSet                          #

```scala
object ValueSet extends Serializable
```

A factory object for value sets

* Source
  * [Enumeration.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Enumeration.scala#L1)


--------------------------------------------------------------------------------
                 Value Members From scala.Enumeration.ValueSet
--------------------------------------------------------------------------------


### `def apply(elems: Value*): ValueSet`                                     ###

A value set consisting of given elements

(defined at scala.Enumeration.ValueSet)


### `implicit def canBuildFrom: CanBuildFrom[ValueSet, Value, ValueSet]`     ###

The implicit builder for value sets

(defined at scala.Enumeration.ValueSet)


### `val empty: ValueSet`                                                    ###

The empty value set

(defined at scala.Enumeration.ValueSet)


### `def fromBitMask(elems: Array[Long]): ValueSet`                          ###

A value set containing all the values for the zero-adjusted ids corresponding to
the bits in an array

(defined at scala.Enumeration.ValueSet)


### `def newBuilder: Builder[Value, ValueSet]`                               ###

A builder object for value sets
(defined at scala.Enumeration.ValueSet)
