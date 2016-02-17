
#                                 scala.remote                                 #

```scala
class remote extends Annotation with StaticAnnotation
```

An annotation that designates the class to which it is applied as remotable.

For instance, the Scala code

```scala
@remote trait Hello {
  def sayHello(): String
}
```

is equivalent to the following Java code:

```scala
public interface Hello extends java.rmi.Remote {
    String sayHello() throws java.rmi.RemoteException;
}
```

* Source
  * [remote.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/remote.scala#L1)


--------------------------------------------------------------------------------
                    Instance Constructors From scala.remote
--------------------------------------------------------------------------------


### `new remote()`                                                           ###
(defined at scala.remote)
