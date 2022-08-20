// C++ program for implementation of Heap Sort

#include <iostream>
#include <chrono>
#include <bits/stdc++.h>

using namespace std;

// To heapify a subtree rooted with node i
// which is an index in arr[].
// n is size of heap
void heapify(int arr[], int N, int i)
{

	// Initialize largest as root
	int largest = i;

	// left = 2*i + 1
	int l = 2 * i + 1;

	// right = 2*i + 2
	int r = 2 * i + 2;

	// If left child is larger than root
	if (l < N && arr[l] > arr[largest])
		largest = l;

	// If right child is larger than largest
	// so far
	if (r < N && arr[r] > arr[largest])
		largest = r;

	// If largest is not root
	if (largest != i)
	{
		swap(arr[i], arr[largest]);

		// Recursively heapify the affected
		// sub-tree
		heapify(arr, N, largest);
	}
}

// Main function to do heap sort
void heapSort(int arr[], int N)
{

	// Build heap (rearrange array)
	for (int i = N / 2 - 1; i >= 0; i--)
		heapify(arr, N, i);

	// One by one extract an element
	// from heap
	for (int i = N - 1; i > 0; i--)
	{

		// Move current root to end
		swap(arr[0], arr[i]);

		// call max heapify on the reduced heap
		heapify(arr, i, 0);
	}
}

// A utility function to print array of size n
void printArray(int arr[], int N)
{
	for (int i = 0; i < N; ++i)
		cout << arr[i] << " ";
	cout << "\n";
}

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

int main(int argc, char **argv)
{

	int N = atoi(argv[1]);
	int arr[N] = {};

	// lectura de archivo
	if (!readDataFile(arr, N, argv[2]))
	{
		return EXIT_FAILURE;
	}

	auto begin = chrono::high_resolution_clock::now();

	// ejecucion del algoritmo
	heapSort(arr, N);

	auto end = chrono::high_resolution_clock::now();
	
	// calculo del tiempo
	double elapsed = chrono::duration_cast<std::chrono::nanoseconds>(end - begin).count();

	// Transformacion a milisegundos
	elapsed *= 1e-6;

	cout << "Tiempo total: " << fixed << elapsed << setprecision(9);

	return EXIT_SUCCESS;
}
