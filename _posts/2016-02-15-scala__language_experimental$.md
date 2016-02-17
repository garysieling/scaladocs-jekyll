
#                         scala.language.experimental                         #

```scala
object experimental
```

The experimental object contains features that have been recently added but have
not been thoroughly tested in production yet.

Experimental features *may undergo API changes* in future releases, so
production code should not rely on them.

Programmers are encouraged to try out experimental features and
[report any bugs or API inconsistencies](http://issues.scala-lang.org) they
encounter so they can be improved in future releases.

* Source
  * [language.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/language.scala#L1)


--------------------------------------------------------------------------------
                 Value Members From scala.language.experimental
--------------------------------------------------------------------------------


### `implicit lazy val macros: macros`                                       ###

Where enabled, macro definitions are allowed. Macro implementations and macro
applications are unaffected; they can be used anywhere.

 *Why introduce the feature?* Macros promise to make the language more regular,
replacing ad-hoc language constructs with a general powerful abstraction
capability that can express them. Macros are also a more disciplined and
powerful replacement for compiler plugins.

 *Why control it?* For their very power, macros can lead to code that is hard to
debug and understand.
(defined at scala.language.experimental)
