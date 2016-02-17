
#                         scala.sys.ShutdownHookThread                         #

```scala
class ShutdownHookThread extends Thread
```

A minimal Thread wrapper to enhance shutdown hooks. It knows how to unregister
itself.

* Source
  * [ShutdownHookThread.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/ShutdownHookThread.scala#L1)
* Version
  * 2.9
* Since
  * 2.9


--------------------------------------------------------------------------------
                 Deprecated Value Members From java.lang.Thread
--------------------------------------------------------------------------------


### `final def stop(arg0: java.lang.Throwable): Unit`                        ###

* Definition Classes
  * Thread
* Annotations
  * @Deprecated @ deprecated
* Deprecated
  * _(Since version)_ see corresponding Javadoc for more information.

(defined at java.lang.Thread)


--------------------------------------------------------------------------------
                      Value Members From java.lang.Thread
--------------------------------------------------------------------------------


### `def clone(): AnyRef`                                                    ###

Create a copy of the receiver object.

The default implementation of the `clone` method is platform dependent.

* returns
  * a copy of the receiver object.

* Attributes
  * protected[java.lang]
* Definition Classes
  * Thread → AnyRef
* Annotations
  * @ throws (...)
* Note
  * not specified by SLS as a member of AnyRef

(defined at java.lang.Thread)


### `def getState(): State`                                                  ###

* Definition Classes
  * Thread

(defined at java.lang.Thread)


### `def getUncaughtExceptionHandler(): UncaughtExceptionHandler`            ###

* Definition Classes
  * Thread

(defined at java.lang.Thread)


### `final def join(arg0: Long): Unit`                                       ###

* Definition Classes
  * Thread
* Annotations
  * @ throws (...)

(defined at java.lang.Thread)


### `final def join(arg0: Long, arg1: Int): Unit`                            ###

* Definition Classes
  * Thread
* Annotations
  * @ throws (...)

(defined at java.lang.Thread)


### `def setContextClassLoader(arg0: ClassLoader): Unit`                     ###

* Definition Classes
  * Thread

(defined at java.lang.Thread)


### `final def setDaemon(arg0: Boolean): Unit`                               ###

* Definition Classes
  * Thread

(defined at java.lang.Thread)


### `final def setName(arg0: String): Unit`                                  ###

* Definition Classes
  * Thread

(defined at java.lang.Thread)


### `final def setPriority(arg0: Int): Unit`                                 ###

* Definition Classes
  * Thread

(defined at java.lang.Thread)


### `def setUncaughtExceptionHandler(arg0: UncaughtExceptionHandler): Unit`  ###

* Definition Classes
  * Thread
(defined at java.lang.Thread)
