
#                    scala.concurrent.duration.DurationInt                    #

```scala
implicit final class DurationInt extends AnyVal with DurationConversions
```

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/duration/package.scala#L1)


--------------------------------------------------------------------------------
                        Value Members From scala.Any###
--------------------------------------------------------------------------------


### `final def ##(): Int`                                                    ###

Equivalent to `x.hashCode` except for boxed numeric types and `null` . For
numerics, it returns a hash value which is consistent with value equality: if
two value type instances compare as true, then ## will produce the same hash
value for each of them. For `null` returns a hashcode where `null.hashCode`
throws a `NullPointerException` .

* returns
  * a hash value consistent with ==

* Definition Classes
  * Any

(defined at scala.Any###)


--------------------------------------------------------------------------------
        Value Members From scala.concurrent.duration.DurationConversions
--------------------------------------------------------------------------------


### `def day: FiniteDuration`                                                ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def day[C](c: C)(implicit ev: Classifier[C]): R`                        ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def days: FiniteDuration`                                               ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def days[C](c: C)(implicit ev: Classifier[C]): R`                       ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def hour: FiniteDuration`                                               ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def hour[C](c: C)(implicit ev: Classifier[C]): R`                       ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def hours: FiniteDuration`                                              ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def hours[C](c: C)(implicit ev: Classifier[C]): R`                      ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def micro: FiniteDuration`                                              ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def micro[C](c: C)(implicit ev: Classifier[C]): R`                      ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def micros: FiniteDuration`                                             ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def micros[C](c: C)(implicit ev: Classifier[C]): R`                     ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def microsecond: FiniteDuration`                                        ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def microsecond[C](c: C)(implicit ev: Classifier[C]): R`                ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def microseconds: FiniteDuration`                                       ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def microseconds[C](c: C)(implicit ev: Classifier[C]): R`               ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def milli: FiniteDuration`                                              ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def milli[C](c: C)(implicit ev: Classifier[C]): R`                      ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def millis: FiniteDuration`                                             ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def millis[C](c: C)(implicit ev: Classifier[C]): R`                     ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def millisecond: FiniteDuration`                                        ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def millisecond[C](c: C)(implicit ev: Classifier[C]): R`                ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def milliseconds: FiniteDuration`                                       ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def milliseconds[C](c: C)(implicit ev: Classifier[C]): R`               ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def minute: FiniteDuration`                                             ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def minute[C](c: C)(implicit ev: Classifier[C]): R`                     ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def minutes: FiniteDuration`                                            ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def minutes[C](c: C)(implicit ev: Classifier[C]): R`                    ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def nano: FiniteDuration`                                               ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def nano[C](c: C)(implicit ev: Classifier[C]): R`                       ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def nanos: FiniteDuration`                                              ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def nanos[C](c: C)(implicit ev: Classifier[C]): R`                      ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def nanosecond: FiniteDuration`                                         ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def nanosecond[C](c: C)(implicit ev: Classifier[C]): R`                 ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def nanoseconds: FiniteDuration`                                        ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def nanoseconds[C](c: C)(implicit ev: Classifier[C]): R`                ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def second: FiniteDuration`                                             ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def second[C](c: C)(implicit ev: Classifier[C]): R`                     ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def seconds: FiniteDuration`                                            ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


### `def seconds[C](c: C)(implicit ev: Classifier[C]): R`                    ###

* Definition Classes
  * DurationConversions

(defined at scala.concurrent.duration.DurationConversions)


--------------------------------------------------------------------------------
        Instance Constructors From scala.concurrent.duration.DurationInt
--------------------------------------------------------------------------------


### `new DurationInt(n: Int)`                                                ###

(defined at scala.concurrent.duration.DurationInt)


--------------------------------------------------------------------------------
            Value Members From scala.concurrent.duration.DurationInt
--------------------------------------------------------------------------------


### `def durationIn(unit: TimeUnit): FiniteDuration`                         ###

* Attributes
  * protected
* Definition Classes
  * DurationInt → DurationConversions
(defined at scala.concurrent.duration.DurationInt)
