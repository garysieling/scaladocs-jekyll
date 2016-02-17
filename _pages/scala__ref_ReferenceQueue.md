
#                           scala.ref.ReferenceQueue                           #

```scala
class ReferenceQueue[+T <: AnyRef] extends AnyRef
```

* Source
  * [ReferenceQueue.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/ref/ReferenceQueue.scala#L1)


--------------------------------------------------------------------------------
              Instance Constructors From scala.ref.ReferenceQueue
--------------------------------------------------------------------------------


### `new ReferenceQueue()`                                                   ###

(defined at scala.ref.ReferenceQueue)


--------------------------------------------------------------------------------
                  Value Members From scala.ref.ReferenceQueue
--------------------------------------------------------------------------------


### `def Wrapper(jref: java.lang.ref.Reference[_]): Option[Reference[T]]`    ###

* Attributes
  * protected

(defined at scala.ref.ReferenceQueue)


### `def poll: Option[Reference[T]]`                                         ###

(defined at scala.ref.ReferenceQueue)


### `def remove(timeout: Long): Option[Reference[T]]`                        ###

(defined at scala.ref.ReferenceQueue)


### `def remove: Option[Reference[T]]`                                       ###
(defined at scala.ref.ReferenceQueue)
