
#                       scala.annotation.TypeConstraint                       #

```scala
trait TypeConstraint extends Annotation
```

A marker for annotations that, when applied to a type, should be treated as a
constraint on the annotated type.

A proper constraint should restrict the type based only on information mentioned
within the type. A Scala compiler can use this assumption to rewrite the
contents of the constraint as necessary. To contrast, a type annotation whose
meaning depends on the context where it is written down is not a proper
constrained type, and this marker should not be applied. A Scala compiler will
drop such annotations in cases where it would rewrite a type constraint.

* Source
  * [TypeConstraint.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/TypeConstraint.scala#L1)
* Version
  * 1.1, 2007-11-5
* Since
  * 2.6

