
#                                scala.Boolean                                #

```scala
abstract final class Boolean extends AnyVal
```

 `Boolean` (equivalent to Java's `boolean` primitive type) is a subtype of
scala.AnyVal. Instances of `Boolean` are not represented by an object in the
underlying runtime system.

There is an implicit conversion from scala.Boolean => scala.runtime.RichBoolean
which provides useful non-primitive operations.

* Source
  * [Boolean.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Boolean.scala#L1)


--------------------------------------------------------------------------------
                   Abstract Value Members From scala.Boolean
--------------------------------------------------------------------------------


### `abstract def !=(x: Boolean): Boolean`                                   ###

Compares two Boolean expressions and returns `true` if they evaluate to a
different value.

 `a != b` returns `true` if and only if

*  `a` is `true` and `b` is `false` or
*  `a` is `false` and `b` is `true` .

(defined at scala.Boolean)


### `abstract def &&(x: Boolean): Boolean`                                   ###

Compares two Boolean expressions and returns `true` if both of them evaluate to
true.

 `a && b` returns `true` if and only if

*  `a` and `b` are `true` .

* Note
  * This method uses 'short-circuit' evaluation and behaves as if it was
    declared as `def &&(x: => Boolean): Boolean` . If `a` evaluates to `false` ,
     `false` is returned without evaluating `b` .

(defined at scala.Boolean)


### `abstract def &(x: Boolean): Boolean`                                    ###

Compares two Boolean expressions and returns `true` if both of them evaluate to
true.

 `a & b` returns `true` if and only if

*  `a` and `b` are `true` .

* Note
  * This method evaluates both `a` and `b` , even if the result is already
    determined after evaluating `a` .

(defined at scala.Boolean)


### `abstract def ==(x: Boolean): Boolean`                                   ###

Compares two Boolean expressions and returns `true` if they evaluate to the same
value.

 `a == b` returns `true` if and only if

*  `a` and `b` are `true` or
*  `a` and `b` are `false` .

(defined at scala.Boolean)


### `abstract def ^(x: Boolean): Boolean`                                    ###

Compares two Boolean expressions and returns `true` if they evaluate to a
different value.

 `a ^ b returns true if and only if`

*  `a` is `true` and `b` is `false` or
*  `a` is `false` and `b` is `true` .

(defined at scala.Boolean)


### `abstract def |(x: Boolean): Boolean`                                    ###

Compares two Boolean expressions and returns `true` if one or both of them
evaluate to true.

 `a | b` returns `true` if and only if

*  `a` is `true` or
*  `b` is `true` or
*  `a` and `b` are `true` .

* Note
  * This method evaluates both `a` and `b` , even if the result is already
    determined after evaluating `a` .

(defined at scala.Boolean)


### `abstract def ||(x: Boolean): Boolean`                                   ###

Compares two Boolean expressions and returns `true` if one or both of them
evaluate to true.

 `a || b` returns `true` if and only if

*  `a` is `true` or
*  `b` is `true` or
*  `a` and `b` are `true` .

* Note
  * This method uses 'short-circuit' evaluation and behaves as if it was
    declared as `def ||(x: => Boolean): Boolean` . If `a` evaluates to `true` ,
     `true` is returned without evaluating `b` .

(defined at scala.Boolean)


--------------------------------------------------------------------------------
                   Concrete Value Members From scala.Boolean
--------------------------------------------------------------------------------


### `abstract def unary_!: Boolean`                                          ###

Negates a Boolean expression.

- `!a` results in `false` if and only if `a` evaluates to `true` and - `!a`
results in `true` if and only if `a` evaluates to `false` .

* returns
  * the negated expression

(defined at scala.Boolean)


--------------------------------------------------------------------------------
 Concrete Value Members From Implicit scala.LowPriorityImplicits.booleanWrapper
--------------------------------------------------------------------------------


### `def <(that: Boolean): Boolean`                                          ###

Returns true if `this` is less than `that`

* Implicit information
  * This member is added by an implicit conversion from Boolean to RichBoolean
    performed by method booleanWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * Ordered

(added by implicit convertion: scala.LowPriorityImplicits.booleanWrapper)


### `def <=(that: Boolean): Boolean`                                         ###

Returns true if `this` is less than or equal to `that` .

* Implicit information
  * This member is added by an implicit conversion from Boolean to RichBoolean
    performed by method booleanWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * Ordered

(added by implicit convertion: scala.LowPriorityImplicits.booleanWrapper)


### `def >(that: Boolean): Boolean`                                          ###

Returns true if `this` is greater than `that` .

* Implicit information
  * This member is added by an implicit conversion from Boolean to RichBoolean
    performed by method booleanWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * Ordered

(added by implicit convertion: scala.LowPriorityImplicits.booleanWrapper)


### `def >=(that: Boolean): Boolean`                                         ###

Returns true if `this` is greater than or equal to `that` .

* Implicit information
  * This member is added by an implicit conversion from Boolean to RichBoolean
    performed by method booleanWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * Ordered

(added by implicit convertion: scala.LowPriorityImplicits.booleanWrapper)


### `def compare(y: Boolean): Int`                                           ###

Result of comparing `this` with operand `that` .

Implement this method to determine how instances of A will be sorted.

Returns `x` where:

*  `x < 0` when `this < that`
*  `x == 0` when `this == that`
*  `x > 0` when `this > that`

* Implicit information
  * This member is added by an implicit conversion from Boolean to RichBoolean
    performed by method booleanWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * OrderedProxy → Ordered

(added by implicit convertion: scala.LowPriorityImplicits.booleanWrapper)


### `def compareTo(that: Boolean): Int`                                      ###

Result of comparing `this` with operand `that` .

* Implicit information
  * This member is added by an implicit conversion from Boolean to RichBoolean
    performed by method booleanWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * Ordered → Comparable

(added by implicit convertion: scala.LowPriorityImplicits.booleanWrapper)


--------------------------------------------------------------------------------
       Concrete Value Members From Implicit scala.Predef.boolean2Boolean
--------------------------------------------------------------------------------


### `def compareTo(arg0: java.lang.Boolean): Int`                            ###

* Implicit information
  * This member is added by an implicit conversion from Boolean to
    java.lang.Boolean performed by method boolean2Boolean in scala.Predef.
* Definition Classes
  * Boolean → Comparable
(added by implicit convertion: scala.Predef.boolean2Boolean)
