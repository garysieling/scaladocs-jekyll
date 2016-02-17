
#                           scala.ref.WeakReference                           #

```scala
class WeakReference[+T <: AnyRef] extends ReferenceWrapper[T]
```

A wrapper class for java.lang.ref.WeakReference The new functionality is (1)
results are Option values, instead of using null. (2) There is an extractor that
maps the weak reference itself into an option.

* Source
  * [WeakReference.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/ref/WeakReference.scala#L1)


--------------------------------------------------------------------------------
                         Value Members From scala.Proxy
--------------------------------------------------------------------------------


### `def equals(that: Any): Boolean`                                         ###

Compares the receiver object ( `this` ) with the argument object ( `that` ) for
equivalence.

Any implementation of this method should be an
[equivalence relation](http://en.wikipedia.org/wiki/Equivalence_relation) :

* It is reflexive: for any instance `x` of type `Any` , `x.equals(x)` should
   return `true` .
* It is symmetric: for any instances `x` and `y` of type `Any` , `x.equals(y)`
   should return `true` if and only if `y.equals(x)` returns `true` .
* It is transitive: for any instances `x` , `y` , and `z` of type `Any` if
    `x.equals(y)` returns `true` and `y.equals(z)` returns `true` , then
    `x.equals(z)` should return `true` .

If you override this method, you should verify that your implementation remains
an equivalence relation. Additionally, when overriding this method it is usually
necessary to override `hashCode` to ensure that objects which are "equal" (
 `o1.equals(o2)` returns `true` ) hash to the same scala.Int. (
 `o1.hashCode.equals(o2.hashCode)` ).

* that
  * the object to compare against this object for equality.
* returns
  * `true` if the receiver object is equivalent to the argument; `false`
    otherwise.

* Definition Classes
  * Proxy → Any

(defined at scala.Proxy)


--------------------------------------------------------------------------------
               Instance Constructors From scala.ref.WeakReference
--------------------------------------------------------------------------------


### `new WeakReference(value: T)`                                            ###
(defined at scala.ref.WeakReference)
