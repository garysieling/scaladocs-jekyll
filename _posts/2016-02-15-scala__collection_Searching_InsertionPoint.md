
#                  scala.collection.Searching.InsertionPoint                  #

```scala
case class InsertionPoint(insertionPoint: Int) extends SearchResult with Product with Serializable
```

* Source
  * [Searching.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/Searching.scala#L1)


--------------------------------------------------------------------------------
      Instance Constructors From scala.collection.Searching.InsertionPoint
--------------------------------------------------------------------------------


### `new InsertionPoint(insertionPoint: Int)`                                ###

(defined at scala.collection.Searching.InsertionPoint)


--------------------------------------------------------------------------------
         Value Members From Implicit scala.collection.Searching.search
--------------------------------------------------------------------------------


### `val coll: SeqLike[A, InsertionPoint]`                                   ###

* Implicit information
  * This member is added by an implicit conversion from InsertionPoint to
    SearchImpl [A, InsertionPoint] performed by method search in
    scala.collection.Searching. This conversion will take place only if an
    implicit value of type IsSeqLike [InsertionPoint] is in scope.
* Definition Classes
  * SearchImpl

(added by implicit convertion: scala.collection.Searching.search)


### `final def search[B >: A](elem: B)(implicit ord: math.Ordering[B]): SearchResult` ###

Search the sorted sequence for a specific element. If the sequence is an
 `IndexedSeqLike` , a binary search is used. Otherwise, a linear search is used.

The sequence should be sorted with the same `Ordering` before calling;
otherwise, the results are undefined.

* elem
  * the element to find.
* ord
  * the ordering to be used to compare elements.
* returns
  * a `Found` value containing the index corresponding to the element in the
    sequence, or the `InsertionPoint` where the element would be inserted if the
    element is not in the sequence.

* Implicit information
  * This member is added by an implicit conversion from InsertionPoint to
    SearchImpl [A, InsertionPoint] performed by method search in
    scala.collection.Searching. This conversion will take place only if an
    implicit value of type IsSeqLike [InsertionPoint] is in scope.
* Definition Classes
  * SearchImpl
* See also
  * scala.collection.SeqLike, method `sorted` scala.math.Ordering
    scala.collection.IndexedSeqLike

(added by implicit convertion: scala.collection.Searching.search)


### `final def search[B >: A](elem: B, from: Int, to: Int)(implicit ord: math.Ordering[B]): SearchResult` ###

Search within an interval in the sorted sequence for a specific element. If the
sequence is an `IndexedSeqLike` , a binary search is used. Otherwise, a linear
search is used.

The sequence should be sorted with the same `Ordering` before calling;
otherwise, the results are undefined.

* elem
  * the element to find.
* from
  * the index where the search starts.
* to
  * the index following where the search ends.
* ord
  * the ordering to be used to compare elements.
* returns
  * a `Found` value containing the index corresponding to the element in the
    sequence, or the `InsertionPoint` where the element would be inserted if the
    element is not in the sequence.

* Implicit information
  * This member is added by an implicit conversion from InsertionPoint to
    SearchImpl [A, InsertionPoint] performed by method search in
    scala.collection.Searching. This conversion will take place only if an
    implicit value of type IsSeqLike [InsertionPoint] is in scope.
* Definition Classes
  * SearchImpl
* See also
  * scala.collection.SeqLike, method `sorted` scala.math.Ordering
    scala.collection.IndexedSeqLike
(added by implicit convertion: scala.collection.Searching.search)
