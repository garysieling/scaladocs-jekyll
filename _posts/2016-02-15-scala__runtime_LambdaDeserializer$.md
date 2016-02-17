
#                       scala.runtime.LambdaDeserializer                       #

```scala
object LambdaDeserializer
```

This class is only intended to be called by synthetic `$deserializeLambda$`
method that the Scala 2.12 compiler will add to classes hosting lambdas.

It is not intended to be consumed directly.

* Source
  * [LambdaDeserializer.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/runtime/LambdaDeserializer.scala#L1)


--------------------------------------------------------------------------------
              Value Members From scala.runtime.LambdaDeserializer
--------------------------------------------------------------------------------


### `def deserializeLambda(lookup: Lookup, cache: Map[String, MethodHandle], serialized: SerializedLambda): AnyRef` ###

Deserialize a lambda by calling `LambdaMetafactory.altMetafactory` to spin up a
lambda class and instantiating this class with the captured arguments.

A cache may be provided to ensure that subsequent deserialization of the same
lambda expression is cheap, it amounts to a reflective call to the constructor
of the previously created class. However, deserialization of the same lambda
expression is not guaranteed to use the same class, concurrent deserialization
of the same lambda expression may spin up more than one class.

Assumptions:

* No additional marker interfaces are required beyond
    `{java.io,scala.}Serializable` . These are not stored in `SerializedLambda` ,
   so we can't reconstitute them.
* No additional bridge methods are passed to `altMetafactory` . Again, these are
   not stored.

* lookup
  * The factory for method handles. Must have access to the implementation
    method, the functional interface class, and `java.io.Serializable` or
     `scala.Serializable` as required.
* cache
  * A cache used to avoid spinning up a class for each deserialization of a
    given lambda. May be `null`
* serialized
  * The lambda to deserialize. Note that this is typically created by the
     `readResolve` member of the anonymous class created by `LambdaMetaFactory` .
* returns
  * An instance of the functional interface
(defined at scala.runtime.LambdaDeserializer)
