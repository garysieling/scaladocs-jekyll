
#                                 scala.Symbol                                 #

```scala
object Symbol extends UniquenessCache[String, Symbol] with Serializable
```

* Source
  * [Symbol.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Symbol.scala#L1)


--------------------------------------------------------------------------------
                        Value Members From scala.Symbol
--------------------------------------------------------------------------------


### `def apply(name: String): Symbol`                                        ###

* Definition Classes
  * Symbol → UniquenessCache

(defined at scala.Symbol)


### `def keyFromValue(sym: Symbol): Option[String]`                          ###

* Attributes
  * protected
* Definition Classes
  * Symbol → UniquenessCache

(defined at scala.Symbol)


### `def valueFromKey(name: String): Symbol`                                 ###

* Attributes
  * protected
* Definition Classes
  * Symbol → UniquenessCache

(defined at scala.Symbol)


--------------------------------------------------------------------------------
                    Value Members From scala.UniquenessCache
--------------------------------------------------------------------------------


### `def unapply(other: Symbol): Option[String]`                             ###

* Definition Classes
  * UniquenessCache
(defined at scala.UniquenessCache)
