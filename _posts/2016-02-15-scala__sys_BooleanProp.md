
#                            scala.sys.BooleanProp                            #

```scala
trait BooleanProp extends Prop[Boolean]
```

A few additional conveniences for Boolean properties.

* Source
  * [BooleanProp.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/BooleanProp.scala#L1)


--------------------------------------------------------------------------------
                   Abstract Value Members From scala.sys.Prop
--------------------------------------------------------------------------------


### `abstract def option: Option[Boolean]`                                   ###

Some(value) if the property is set, None otherwise.

* Definition Classes
  * Prop

(defined at scala.sys.Prop)


### `abstract def set(newValue: String): String`                             ###

Sets the property.

* newValue
  * the new string value
* returns
  * the old value, or null if it was unset.

* Definition Classes
  * Prop

(defined at scala.sys.Prop)


### `abstract def setValue[T1 >: Boolean](value: T1): Boolean`               ###

Sets the property with a value of the represented type.

* Definition Classes
  * Prop

(defined at scala.sys.Prop)


### `abstract def zero: Boolean`                                             ###

A value of type `T` for use when the property is unset. The default
implementation delivers null for reference types and 0/0.0/false for
non-reference types.

* Attributes
  * protected
* Definition Classes
  * Prop

(defined at scala.sys.Prop)


--------------------------------------------------------------------------------
                   Concrete Value Members From scala.sys.Prop
--------------------------------------------------------------------------------


### `abstract def clear(): Unit`                                             ###

Removes the property from the underlying map.

* Definition Classes
  * Prop

(defined at scala.sys.Prop)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.sys.BooleanProp.booleanPropAsBoolean
--------------------------------------------------------------------------------


### `def &&(x: Boolean): Boolean`                                            ###

Compares two Boolean expressions and returns `true` if both of them evaluate to
true.

 `a && b` returns `true` if and only if

*  `a` and `b` are `true` .

* Implicit information
  * This member is added by an implicit conversion from BooleanProp to Boolean
    performed by method booleanPropAsBoolean in scala.sys.BooleanProp.
* Definition Classes
  * Boolean
* Note
  * This method uses 'short-circuit' evaluation and behaves as if it was
    declared as `def &&(x: => Boolean): Boolean` . If `a` evaluates to `false` ,
     `false` is returned without evaluating `b` .

(added by implicit convertion: scala.sys.BooleanProp.booleanPropAsBoolean)


### `def &(x: Boolean): Boolean`                                             ###

Compares two Boolean expressions and returns `true` if both of them evaluate to
true.

 `a & b` returns `true` if and only if

*  `a` and `b` are `true` .

* Implicit information
  * This member is added by an implicit conversion from BooleanProp to Boolean
    performed by method booleanPropAsBoolean in scala.sys.BooleanProp.
* Definition Classes
  * Boolean
* Note
  * This method evaluates both `a` and `b` , even if the result is already
    determined after evaluating `a` .

(added by implicit convertion: scala.sys.BooleanProp.booleanPropAsBoolean)


### `def ^(x: Boolean): Boolean`                                             ###

Compares two Boolean expressions and returns `true` if they evaluate to a
different value.

 `a ^ b returns true if and only if`

*  `a` is `true` and `b` is `false` or
*  `a` is `false` and `b` is `true` .

* Implicit information
  * This member is added by an implicit conversion from BooleanProp to Boolean
    performed by method booleanPropAsBoolean in scala.sys.BooleanProp.
* Definition Classes
  * Boolean

(added by implicit convertion: scala.sys.BooleanProp.booleanPropAsBoolean)


### `def |(x: Boolean): Boolean`                                             ###

Compares two Boolean expressions and returns `true` if one or both of them
evaluate to true.

 `a | b` returns `true` if and only if

*  `a` is `true` or
*  `b` is `true` or
*  `a` and `b` are `true` .

* Implicit information
  * This member is added by an implicit conversion from BooleanProp to Boolean
    performed by method booleanPropAsBoolean in scala.sys.BooleanProp.
* Definition Classes
  * Boolean
* Note
  * This method evaluates both `a` and `b` , even if the result is already
    determined after evaluating `a` .

(added by implicit convertion: scala.sys.BooleanProp.booleanPropAsBoolean)


### `def ||(x: Boolean): Boolean`                                            ###

Compares two Boolean expressions and returns `true` if one or both of them
evaluate to true.

 `a || b` returns `true` if and only if

*  `a` is `true` or
*  `b` is `true` or
*  `a` and `b` are `true` .

* Implicit information
  * This member is added by an implicit conversion from BooleanProp to Boolean
    performed by method booleanPropAsBoolean in scala.sys.BooleanProp.
* Definition Classes
  * Boolean
* Note
  * This method uses 'short-circuit' evaluation and behaves as if it was
    declared as `def ||(x: => Boolean): Boolean` . If `a` evaluates to `true` ,
     `true` is returned without evaluating `b` .
(added by implicit convertion: scala.sys.BooleanProp.booleanPropAsBoolean)
