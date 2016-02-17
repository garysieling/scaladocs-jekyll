
#                            scala.compat.Platform                            #

```scala
object Platform
```

* Source
  * [Platform.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/compat/Platform.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type ConcurrentModificationException = java.util.ConcurrentModificationException` ###

This is a type alias for `java.util.ConcurrentModificationException` , which may
be thrown by methods that detect an invalid modification of an object. For
example, many common collection types do not allow modifying a collection while
it is being iterated over.


### `type StackOverflowError = java.lang.StackOverflowError`                 ###

Thrown when a stack overflow occurs because a method or function recurses too
deeply.

On the JVM, this is a type alias for `java.lang.StackOverflowError` , which
itself extends `java.lang.Error` . The same rules apply to catching a
 `java.lang.Error` as for Java, that it indicates a serious problem that a
reasonable application should not try and catch.


--------------------------------------------------------------------------------
                    Value Members From scala.compat.Platform
--------------------------------------------------------------------------------


### `def arrayclear(arr: Array[Int]): Unit`                                  ###

Assigns the value of 0 to each element in the array.

* arr
  * A non-null Array[Int].

* Annotations
  * @ inline ()
* Exceptions thrown
  * `java.lang.NullPointerException` If `arr` is `null` .

(defined at scala.compat.Platform)


### `def arraycopy(src: AnyRef, srcPos: Int, dest: AnyRef, destPos: Int, length: Int): Unit` ###

Copies `length` elements of array `src` starting at position `srcPos` to the
array `dest` starting at position `destPos` . If `src` == `dest` , the copying
will behave as if the elements copied from `src` were first copied to a
temporary array before being copied back into the array at the destination
positions.

* src
  * A non-null array as source for the copy.
* srcPos
  * The starting index in the source array.
* dest
  * A non-null array as destination for the copy.
* destPos
  * The starting index in the destination array.
* length
  * The number of elements to be copied.

* Annotations
  * @ inline ()
* Exceptions thrown
  * `java.lang.ArrayStoreException` If either `src` or `dest` are not of type
    [java.lang.Array]; or if the element type of `src` is not compatible with
    that of `dest` . `java.lang.IndexOutOfBoundsException` If either `srcPos` or
     `destPos` are outside of the bounds of their respective arrays; or if
     `length` is negative; or if there are less than `length` elements available
    after `srcPos` or `destPos` in `src` and `dest` respectively.
     `java.lang.NullPointerException` If either `src` or `dest` are `null` .

(defined at scala.compat.Platform)


### `def createArray(elemClass: Class[_], length: Int): AnyRef`              ###

Creates a new array of the specified type and given length.

Note that if `elemClass` is a subclass of scala.AnyVal then the returned value
is an Array of the corresponding java primitive type. For example, the following
code `scala.compat.Platform.createArray(classOf[Int], 4)` returns an array of
the java primitive type `int` .

For a scala.AnyVal array, the values of the array are set to 0 for _numeric
value types_ (scala.Double, scala.Float, scala.Long, scala.Int, scala.Char,
scala.Short, and scala.Byte), and `false` for scala.Boolean. Creation of an
array of type scala.Unit is not possible.

For subclasses of scala.AnyRef, the values of the array are set to `null` .

The caller must cast the returned value to the correct type.

* elemClass
  * the `Class` object of the component type of the array
* length
  * the length of the new array.
* returns
  * an array of the given component type as an `AnyRef` .

* Annotations
  * @ inline ()
* Exceptions thrown
  * `java.lang.IllegalArgumentException` if componentType is scala.Unit or
     `java.lang.Void.TYPE`  `java.lang.NegativeArraySizeException` if the
    specified length is negative `java.lang.NullPointerException` If
     `elemClass` is `null` .

Example:

```scala
val a = scala.compat.Platform.createArray(classOf[Int], 4).asInstanceOf[Array[Int]] // returns Array[Int](0, 0, 0, 0)
```

(defined at scala.compat.Platform)


### `def getClassForName(name: String): Class[_]`                            ###

Returns the `Class` object associated with the class or interface with the given
string name using the current `ClassLoader` . On the JVM, invoking this method
is equivalent to: `java.lang.Class.forName(name)`

For more information, please see the Java documentation for java.lang.Class.

* name
  * the fully qualified name of the desired class.
* returns
  * the `Class` object for the class with the specified name.

* Annotations
  * @ inline ()
* Exceptions thrown
  * `java.lang.ClassNotFoundException` if the class cannot be located
     `java.lang.ExceptionInInitializerError` if the initialization provoked by
    this method fails `java.lang.LinkageError` if the linkage fails

Example:

```scala
val a = scala.compat.Platform.getClassForName("java.lang.Integer")  // returns the Class[_] for java.lang.Integer
```
(defined at scala.compat.Platform)
