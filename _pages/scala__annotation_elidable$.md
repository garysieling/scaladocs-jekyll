
#                          scala.annotation.elidable                          #

```scala
object elidable
```

This useless appearing code was necessary to allow people to use named constants
for the elidable annotation. This is what it takes to convince the compiler to
fold the constants: otherwise when it's time to check an elision level it's
staring at a tree like

```scala
(Select(Level, Select(FINEST, Apply(intValue, Nil))))
```

instead of the number `300` .

* Source
  * [elidable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/elidable.scala#L1)
* Since
  * 2.8

