# Topic
Fibonacci Heap
## Group Member
Javeria Batool(19B-021-CS)
Rameen Irfan (19B-012-CS)
### Explanation
Fibonacci heap is a complete tree. It follows the property of Min Heap that is the parent node is smaller than its children.
In Fibonacci Heap there is pointer (H .min) which points towards the minimum node.

Fibonacci Heap supports merge heap operation.

  1. Make a Heap: Creates and returns a new heap containing no elements.
  2. Insert: Inserts element x, whose key has already been ﬁlled in, into heap H.
  3. Find Minimum: Returns a pointer to the element in heap H whose key is minimum.
  4. Union: Creates and returns a new heap that contains all the elements of heaps H1 and H2. Heaps H1 and H2 are “destroyed” by this operation.
  5. Decrease Key: Assigns to element x within heap H the new key value k, which we assume to be no greater than its current key value.
  6. Delete Value: Deletes element x from heap H.

