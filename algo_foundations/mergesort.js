///recursion
//e.g. calculate factorial

function factorial(num, output=1) {
    //base case: num == 1
    if (num == 1) return output
    output *= num 
    return factorial(num-1, output)
}

//console.log(factorial(5));

///MERGE SORT///
 let arr1 = [1, 5, 7, 3, 8, 4, 6, 2]

function mergeSort(array) {
    //step 1 is to split arrays in 2 halfs; assume array even elements for now//
    let half1 = array.slice(0, array.length/2)
    let half2 = array.slice(array.length/2);
    //each half of the array is being recursively sorted??
    console.log(half1, half2)
    //final step is to merge the 2 halfs.
}
mergeSort(arr1);
