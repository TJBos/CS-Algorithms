//count number of inversions in array

let ar = [1,3,5,2,4,6]

//we have 3 inversions here: [3,2], [5,2] and [5,4]
//we can find this by brute force like so;

const countInversions = (array) => {
  let counter = 0;
  for (i=0; i < array.length; i++) {
    for (j=i+1; j < array.length; j++) {
      if (array[i] > array[j]) {
        counter++
      }
    }
  }
  return counter
}

countInversions(ar); //output is 3

//since this uses a nested loop, this algo has a quadratic runrime; T(n) = O(n^2)
//Let's try to solve this problem with a divide and conquer strategy