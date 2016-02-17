
#                             scala.deprecatedName                             #

```scala
class deprecatedName extends Annotation with StaticAnnotation
```

An annotation that designates the name of the parameter to which it is applied
as deprecated. Using that name in a named argument generates a deprecation
warning.

For instance, evaluating the code below in the Scala interpreter

```scala
def inc(x: Int, @deprecatedName('y) n: Int): Int = x + n
inc(1, y = 2)
```

will produce the following output:

```scala
warning: there were 1 deprecation warnings; re-run with -deprecation for details
res0: Int = 3
```

* Annotations
  * @ param ()
* Source
  * [deprecatedName.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/deprecatedName.scala#L1)
* Since
  * 2.8.1


--------------------------------------------------------------------------------
                Instance Constructors From scala.deprecatedName
--------------------------------------------------------------------------------


### `new deprecatedName()`                                                   ###
(defined at scala.deprecatedName)
