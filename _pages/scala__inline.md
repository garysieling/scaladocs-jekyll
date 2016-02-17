
#                                 scala.inline                                 #

```scala
class inline extends Annotation with StaticAnnotation
```

An annotation on methods that requests that the compiler should try especially
hard to inline the annotated method. The annotation can be used at definition
site or at callsite.

```scala
@inline   final def f1(x: Int) = x
@noinline final def f2(x: Int) = x
          final def f3(x: Int) = x

 def t1 = f1(1)              // inlined if possible
 def t2 = f2(1)              // not inlined
 def t3 = f3(1)              // may be inlined (heuristics)
 def t4 = f1(1): @noinline   // not inlined (override at callsite)
 def t5 = f2(1): @inline     // not inlined (cannot override the @noinline at f2's definition)
 def t6 = f3(1): @inline     // inlined if possible
 def t7 = f3(1): @noinline   // not inlined
}
```

Note: parentheses are required when annotating a callsite withing a larger
expression.

```scala
def t1 = f1(1) + f1(1): @noinline   // equivalent to (f1(1) + f1(1)): @noinline
def t2 = f1(1) + (f1(1): @noinline) // the second call to f1 is not inlined
```

* Source
  * [inline.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/inline.scala#L1)
* Version
  * 1.0, 2007-5-21


--------------------------------------------------------------------------------
                    Instance Constructors From scala.inline
--------------------------------------------------------------------------------


### `new inline()`                                                           ###
(defined at scala.inline)
