
#                       scala.annotation.compileTimeOnly                       #

```scala
final class compileTimeOnly extends Annotation with StaticAnnotation
```

An annotation that designates that an annottee should not be referred to after
type checking (which includes macro expansion).

Examples of potential use: 1) The annottee can only appear in the arguments of
some other macro that will eliminate it from the AST during expansion. 2) The
annottee is a macro and should have been expanded away, so if hasn't, something
wrong has happened. (Comes in handy to provide better support for new macro
flavors, e.g. macro annotations, that can't be expanded by the vanilla
compiler).

* Annotations
  * @ getter () @ setter () @ beanGetter () @ beanSetter () @ companionClass ()
    @ companionMethod ()
* Source
  * [compileTimeOnly.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/compileTimeOnly.scala#L1)
* Since
  * 2.11.0


--------------------------------------------------------------------------------
          Instance Constructors From scala.annotation.compileTimeOnly
--------------------------------------------------------------------------------


### `new compileTimeOnly(message: String)`                                   ###

* message
  * the error message to print during compilation if a reference remains after
    type checking
(defined at scala.annotation.compileTimeOnly)
