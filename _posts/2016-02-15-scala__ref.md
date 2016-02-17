
#                                  scala.ref                                  #

```scala
package ref
```


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class PhantomReference[+T <: AnyRef] extends ReferenceWrapper[T]`       ###

* Source
  * [PhantomReference.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/ref/PhantomReference.scala#L1)


### `trait Reference[+T <: AnyRef] extends () ⇒ T`                           ###

* Source
  * [Reference.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/ref/Reference.scala#L1)
* See also
  * `java.lang.ref.Reference`


### `class ReferenceQueue[+T <: AnyRef] extends AnyRef`                      ###

* Source
  * [ReferenceQueue.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/ref/ReferenceQueue.scala#L1)


### `trait ReferenceWrapper[+T <: AnyRef] extends Reference[T] with Proxy`   ###

* Source
  * [ReferenceWrapper.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/ref/ReferenceWrapper.scala#L1)


### `class SoftReference[+T <: AnyRef] extends ReferenceWrapper[T]`          ###

* Source
  * [SoftReference.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/ref/SoftReference.scala#L1)


### `class WeakReference[+T <: AnyRef] extends ReferenceWrapper[T]`          ###

A wrapper class for java.lang.ref.WeakReference The new functionality is (1)
results are Option values, instead of using null. (2) There is an extractor that
maps the weak reference itself into an option.

* Source
  * [WeakReference.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/ref/WeakReference.scala#L1)


--------------------------------------------------------------------------------
                                 Value Members
--------------------------------------------------------------------------------


### `object SoftReference`                                                   ###

A companion object that implements an extractor for `SoftReference` values

* Source
  * [SoftReference.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/ref/SoftReference.scala#L1)


### `object WeakReference`                                                   ###

An extractor for weak reference values

* Source
  * [WeakReference.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/ref/WeakReference.scala#L1)

