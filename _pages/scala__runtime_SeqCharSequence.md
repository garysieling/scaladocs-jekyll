
#                        scala.runtime.SeqCharSequence                        #

```scala
final class SeqCharSequence extends CharSequence
```

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use Predef.SeqCharSequence
* Source
  * [SeqCharSequence.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/runtime/SeqCharSequence.scala#L1)


--------------------------------------------------------------------------------
                   Value Members From java.lang.CharSequence
--------------------------------------------------------------------------------


### `def chars(): IntStream`                                                 ###

* Definition Classes
  * CharSequence

(defined at java.lang.CharSequence)


### `def codePoints(): IntStream`                                            ###

* Definition Classes
  * CharSequence

(defined at java.lang.CharSequence)


--------------------------------------------------------------------------------
            Instance Constructors From scala.runtime.SeqCharSequence
--------------------------------------------------------------------------------


### `new SeqCharSequence(xs: collection.IndexedSeq[Char])`                   ###

(defined at scala.runtime.SeqCharSequence)


--------------------------------------------------------------------------------
                Value Members From scala.runtime.SeqCharSequence
--------------------------------------------------------------------------------


### `def charAt(index: Int): Char`                                           ###

* Definition Classes
  * SeqCharSequence → CharSequence

(defined at scala.runtime.SeqCharSequence)


### `def subSequence(start: Int, end: Int): CharSequence`                    ###

* Definition Classes
  * SeqCharSequence → CharSequence

(defined at scala.runtime.SeqCharSequence)


### `val xs: collection.IndexedSeq[Char]`                                    ###
(defined at scala.runtime.SeqCharSequence)
