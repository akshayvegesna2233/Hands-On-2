b Argue Selection sort Correctness

Selection sort is a straightforward sorting technique, but it may not be the optimal choice for extensive datasets. Let's examine its correctness and efficiency:

## Correctness

Selection sort operates by partitioning the input into sorted and unsorted sections. The algorithm works as follows:

1. It scans the unsorted portion to identify the smallest element.
2. This minimum value is then swapped with the first unsorted element.
3. The process repeats until the entire array is in order.

The algorithm's correctness can be verified through loop invariants. Each iteration ensures that the smallest unsorted element finds its proper place, guaranteeing that the array will eventually be fully sorted.

## Performance Aspects

The time complexity of selection sort is O(n^2), where n represents the number of elements. This quadratic complexity arises because:

- For each element, the algorithm must search through the unsorted region to find the minimum.
- In the worst case, this involves n comparisons for each of the n elements.

While selection sort correctly sorts arrays, its efficiency diminishes with larger datasets. More sophisticated algorithms like merge sort or quicksort, with their average-case O(n log n) time complexities, generally outperform selection sort when dealing with substantial amounts of data.


c. System Specifications:

System information: CPU: Windows 10.0.22621 Total RAM: 16805036032 bytes System: Intel64 Family 6 Model 140 Stepping 1, GenuineIntel

Storage information: C:\ - Total: 368129863680 bytes, Free: 243057664000 bytes D:\ - Total: 318787022848 bytes, Free: 257257058304 bytes E:\ - Total: 335544315904 bytes, Free: 316200505344 bytes G:\ - Total: 16106127360 bytes, Free: 661610496 bytes
