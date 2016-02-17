
#                              scala.specialized                              #

```scala
class specialized extends Annotation with StaticAnnotation
```

Annotate type parameters on which code should be automatically specialized. For
example:

```scala
class MyList[@specialized T] ...
```

Type T can be specialized on a subset of the primitive types by specifying a
list of primitive types to specialize at:

```scala
class MyList[@specialized(Int, Double, Boolean) T] ..
```

* Source
  * [specialized.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/specialized.scala#L1)
* Since
  * 2.8


--------------------------------------------------------------------------------
                  Instance Constructors From scala.specialized
--------------------------------------------------------------------------------


### `new specialized()`                                                      ###
(defined at scala.specialized)
