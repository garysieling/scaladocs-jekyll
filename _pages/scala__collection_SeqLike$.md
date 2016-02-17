
#                           scala.collection.SeqLike                           #

```scala
object SeqLike
```

The companion object for trait `SeqLike` .

* Source
  * [SeqLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/SeqLike.scala#L1)


--------------------------------------------------------------------------------
                  Value Members From scala.collection.SeqLike
--------------------------------------------------------------------------------


### `def indexOf[B](source: Seq[B], sourceOffset: Int, sourceCount: Int, target: Seq[B], targetOffset: Int, targetCount: Int, fromIndex: Int): Int` ###

Finds a particular index at which one sequence occurs in another sequence. Both
the source sequence and the target sequence are expressed in terms other
sequences S' and T' with offset and length parameters. This function is designed
to wrap the KMP machinery in a sufficiently general way that all library
sequence searches can use it. It is unlikely you have cause to call it directly:
prefer functions such as StringBuilder#indexOf and Seq#lastIndexOf.

* source
  * the sequence to search in
* sourceOffset
  * the starting offset in source
* sourceCount
  * the length beyond sourceOffset to search
* target
  * the sequence being searched for
* targetOffset
  * the starting offset in target
* targetCount
  * the length beyond targetOffset which makes up the target string
* fromIndex
  * the smallest index at which the target sequence may start
* returns
  * the applicable index in source where target exists, or -1 if not found

(defined at scala.collection.SeqLike)


### `def lastIndexOf[B](source: Seq[B], sourceOffset: Int, sourceCount: Int, target: Seq[B], targetOffset: Int, targetCount: Int, fromIndex: Int): Int` ###

Finds a particular index at which one sequence occurs in another sequence. Like
 `indexOf` , but finds the latest occurrence rather than earliest.

* See also
  * scala.collection.SeqLike, method `indexOf`
(defined at scala.collection.SeqLike)
