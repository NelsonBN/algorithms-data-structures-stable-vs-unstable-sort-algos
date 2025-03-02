# Algorithms and Data Structures - Stable Vs. Unstable Sorting Algorithms

## Demo

For these examples, we will use two sorting algorithms: `Bubble Sort` and `Selection Sort`. The `Bubble Sort` algorithm is a stable sorting algorithm, while the `Selection Sort` algorithm is an unstable sorting algorithm. For both algorithms, we will sort a list of people by their age in ascending order. The list of people is shown below.

### Algorithms

- [Stable Sorting Algorithms](./src/stable_sort_algo.py)
- [Unstable Sorting Algorithms](./src/unstable_sort_algo.py)


### Input

| Name     | Age | Position |
|----------|-----|----------|
| William  | 21  | 1        |
| Smith    | 23  | 2        |
| Alex     | 27  | 3        |
| Paul     | 21  | 4        |
| Max      | 18  | 5        |
| John     | 23  | 6        |
| Bob      | 25  | 7        |
| Patrick  | 21  | 8        |
| Jane     | 23  | 9        |


### Output of stable sorting algorithms
For this example, the stable sorting algorithm is the `Bubble Sort` algorithm.

| Name     | Age | Position |
|----------|-----|----------|
| Max      | 18  | 5        |
| William  | 21  | 1        |
| Paul     | 21  | 4        |
| Patrick  | 21  | 8        |
| Smith    | 23  | 2        |
| John     | 23  | 6        |
| Jane     | 23  | 9        |
| Bob      | 25  | 7        |
| Alex     | 27  | 3        |


### Output of unstable sorting algorithms
For this example, the unstable sorting algorithm is the `Selection Sort` algorithm.

| Name     | Age | Position |
|----------|-----|----------|
| Max      | 18  | 5        |
| Paul     | 21  | 4        |
| William  | 21  | 1        |
| Patrick  | 21  | 8        |
| John     | 23  | 6        |
| Smith    | 23  | 2        |
| Jane     | 23  | 9        |
| Bob      | 25  | 7        |
| Alex     | 27  | 3        |


### Conclusion

From the output of the stable sorting algorithm, we can see that the people with the same age are sorted based on their original position in the list. For example, the people with the age of 21 are sorted in the order of their original position in the list.

| Name     | Age | Position |
|----------|-----|----------|
| William  | 21  | 1        |
| Paul     | 21  | 4        |
| Patrick  | 21  | 8        |

On the other hand, the output of the unstable sorting algorithm shows that the people with the same age are not sorted based on their original position in the list. For example, the people with the age of 21 are not sorted in the order of their original position in the list.

| Name     | Age | Position |
|----------|-----|----------|
| Paul     | 21  | 4        |
| William  | 21  | 1        |
| Patrick  | 21  | 8        |



## References
- [Other Algorithms & Data Structures](https://github.com/NelsonBN/algorithms-data-structures)
