// Quick sort in C++

#include <iostream>
using namespace std;
#include <chrono>
#include <bits/stdc++.h>

// function to swap elements
void swap(int *a, int *b) {
  int t = *a;
  *a = *b;
  *b = t;
}

// function to print the array
void printArray(int array[], int size) {
  int i;
  for (i = 0; i < size; i++)
    cout << array[i] << " ";
  cout << endl;
}

// function to rearrange array (find the partition point)
int partition(int array[], int low, int high) {
    
  // select the rightmost element as pivot
  int pivot = array[high];
  
  // pointer for greater element
  int i = (low - 1);

  // traverse each element of the array
  // compare them with the pivot
  for (int j = low; j < high; j++) {
    if (array[j] <= pivot) {
        
      // if element smaller than pivot is found
      // swap it with the greater element pointed by i
      i++;
      
      // swap element at i with element at j
      swap(&array[i], &array[j]);
    }
  }
  
  // swap pivot with the greater element at i
  swap(&array[i + 1], &array[high]);
  
  // return the partition point
  return (i + 1);
}

void quickSort(int array[], int low, int high) {
  if (low < high) {
      
    // find the pivot element such that
    // elements smaller than pivot are on left of pivot
    // elements greater than pivot are on righ of pivot
    int pi = partition(array, low, high);

    // recursive call on the left of pivot
    quickSort(array, low, pi - 1);

    // recursive call on the right of pivot
    quickSort(array, pi + 1, high);
  }
}
//---------------------------------------------------------------

bool readDataFile(int arr[], int N, string dataFileName)
{
	string filename(dataFileName);
	int number;

	ifstream input_file(filename);
	if (!input_file.is_open())
	{
		cerr << "Could not open the file - '"
			 << filename << "'" << endl;
		return false;
	}

	int i = 0;

	while (input_file >> number)
	{
		arr[i++] = number;
	}
	input_file.close();

	return true;
}

//----------------------------------------------------------------------------

// Driver code
int main(int argc, char **argv) {

    int N = atoi(argv[1]);
    int arr[N] = {};

	  if (!readDataFile(arr, N, argv[2]))
	  {
		return EXIT_FAILURE;
	  }

    int n = sizeof(arr) / sizeof(arr[0]);
    cout << "Unsorted Array: \n";
    printArray(arr, n);

	  auto begin = chrono::high_resolution_clock::now();
 
   quickSort(arr, 0, n - 1);

	  auto end = chrono::high_resolution_clock::now();
	  double elapsed = chrono::duration_cast<std::chrono::nanoseconds>(end - begin).count();

	  elapsed *= 1e-6;
   cout << "Sorted array in ascending order: \n";
    printArray(arr, n);
   cout << "Tiempo total: " << fixed << elapsed << setprecision(9);
	
	  return EXIT_SUCCESS;
}
