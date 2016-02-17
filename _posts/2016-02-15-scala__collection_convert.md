
#                           scala.collection.convert                           #

```scala
package convert
```

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/convert/package.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `trait DecorateAsJava extends AnyRef`                                    ###

A collection of decorators that allow converting between Scala and Java
collections using `asScala` and `asJava` methods.

The following conversions are supported via `asJava` , `asScala`

*  `scala.collection.Iterable` <=> `java.lang.Iterable`
*  `scala.collection.Iterator` <=> `java.util.Iterator`
*  `scala.collection.mutable.Buffer` <=> `java.util.List`
*  `scala.collection.mutable.Set` <=> `java.util.Set`
*  `scala.collection.mutable.Map` <=> `java.util.Map`
*  `scala.collection.mutable.concurrent.Map` <=>
    `java.util.concurrent.ConcurrentMap`

In all cases, converting from a source type to a target type and back again will
return the original source object, e.g.

```scala
import scala.collection.JavaConverters._

val sl = new scala.collection.mutable.ListBuffer[Int]
val jl : java.util.List[Int] = sl.asJava
val sl2 : scala.collection.mutable.Buffer[Int] = jl.asScala
assert(sl eq sl2)
```

The following conversions are also supported, but the direction from Scala to
Java is done by the more specifically named methods: `asJavaCollection` ,
 `asJavaEnumeration` , `asJavaDictionary` .

*  `scala.collection.Iterable` <=> `java.util.Collection`
*  `scala.collection.Iterator` <=> `java.util.Enumeration`
*  `scala.collection.mutable.Map` <=> `java.util.Dictionary`

In addition, the following one way conversions are provided via `asJava` :

*  `scala.collection.Seq` => `java.util.List`
*  `scala.collection.mutable.Seq` => `java.util.List`
*  `scala.collection.Set` => `java.util.Set`
*  `scala.collection.Map` => `java.util.Map`

The following one way conversion is provided via `asScala` :

*  `java.util.Properties` => `scala.collection.mutable.Map`

* Source
  * [DecorateAsJava.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/convert/DecorateAsJava.scala#L1)
* Since
  * 2.8.1


### `trait DecorateAsScala extends AnyRef`                                   ###

* Source
  * [DecorateAsScala.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/convert/DecorateAsScala.scala#L1)


### `trait WrapAsJava extends AnyRef`                                        ###

* Source
  * [WrapAsJava.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/convert/WrapAsJava.scala#L1)


### `trait WrapAsScala extends AnyRef`                                       ###

* Source
  * [WrapAsScala.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/convert/WrapAsScala.scala#L1)


--------------------------------------------------------------------------------
                                 Value Members
--------------------------------------------------------------------------------


### `object WrapAsJava extends WrapAsJava`                                   ###

* Source
  * [WrapAsJava.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/convert/WrapAsJava.scala#L1)


### `object WrapAsScala extends WrapAsScala`                                 ###

* Source
  * [WrapAsScala.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/convert/WrapAsScala.scala#L1)


### `object Wrappers extends Wrappers with Serializable`                     ###

* Annotations
  * @ SerialVersionUID ()
* Source
  * [Wrappers.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/convert/Wrappers.scala#L1)


--------------------------------------------------------------------------------
                  Value Members From scala.collection.convert
--------------------------------------------------------------------------------


### `val decorateAll: DecorateAsJava with DecorateAsScala`                   ###

(defined at scala.collection.convert)


### `val decorateAsJava: DecorateAsJava`                                     ###

(defined at scala.collection.convert)


### `val decorateAsScala: DecorateAsScala`                                   ###

(defined at scala.collection.convert)


### `val wrapAll: WrapAsJava with WrapAsScala`                               ###

(defined at scala.collection.convert)


### `val wrapAsJava: WrapAsJava`                                             ###

(defined at scala.collection.convert)


### `val wrapAsScala: WrapAsScala`                                           ###
(defined at scala.collection.convert)
