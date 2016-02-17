
#                          scala.util.DynamicVariable                          #

```scala
class DynamicVariable[T] extends AnyRef
```

 `DynamicVariables` provide a binding mechanism where the current value is found
through dynamic scope, but where access to the variable itself is resolved
through static scope.

The current value can be retrieved with the value method. New values should be
pushed using the `withValue` method. Values pushed via `withValue` only stay
valid while the `withValue` 's second argument, a parameterless closure,
executes. When the second argument finishes, the variable reverts to the
previous value.

```scala
someDynamicVariable.withValue(newValue) {
  // ... code called in here that calls value ...
  // ... will be given back the newValue ...
}
```

Each thread gets its own stack of bindings. When a new thread is created, the
 `DynamicVariable` gets a copy of the stack of bindings from the parent thread,
and from then on the bindings for the new thread are independent of those for
the original thread.

* Source
  * [DynamicVariable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/DynamicVariable.scala#L1)
* Version
  * 1.1, 2007-5-21


--------------------------------------------------------------------------------
             Instance Constructors From scala.util.DynamicVariable
--------------------------------------------------------------------------------


### `new DynamicVariable(init: T)`                                           ###

(defined at scala.util.DynamicVariable)


--------------------------------------------------------------------------------
                 Value Members From scala.util.DynamicVariable
--------------------------------------------------------------------------------


### `def value_=(newval: T): Unit`                                           ###

Change the currently bound value, discarding the old value. Usually withValue()
gives better semantics.

(defined at scala.util.DynamicVariable)


### `def withValue[S](newval: T)(thunk: ⇒ S): S`                             ###

Set the value of the variable while executing the specified thunk.

* newval
  * The value to which to set the variable
* thunk
  * The code to evaluate under the new setting
(defined at scala.util.DynamicVariable)
