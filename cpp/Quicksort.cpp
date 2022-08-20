// ALGORITMO : QUICKSORT EN C++

#include <iostream>
using namespace std;
#include <chrono>
#include <bits/stdc++.h>

// Función para intercambiar elementos
void swap(int *a, int *b) {
  int t = *a;
  *a = *b;
  *b = t;
}

// Función para imprimir el array
void printArray(int array[], int size) {
  int i;
  for (i = 0; i < size; i++)
    cout << array[i] << " ";
  cout << endl;
}

// Función para reorganizar el array (encontrar el punto de partición)
int partition(int array[], int low, int high) {
    
  // Seleccionar el elemento que está más a la derecha como pivote
  int pivot = array[high];
  
  // Puntero para el mayor elemento
  int i = (low - 1);

  // Recorrer cada elemento de la matriz
  // compararlos con el pivote
  for (int j = low; j < high; j++) {
    if (array[j] <= pivot) {
        
      // si se encuentra un elemento más pequeño que el pivote
      // intercambiarlo con el elemento mayor apuntado por i
      i++;
      
      // intercambiar elemento en i con elemento en j
      swap(&array[i], &array[j]);
    }
  }
  
  // cambiar el pivote con el elemento mayor en i
  swap(&array[i + 1], &array[high]);
  
  // devolver el punto de partición
  return (i + 1);
}

void quickSort(int array[], int low, int high) {
  if (low < high) {
      
    // encuentra el elemento pivote tal que
    // los elementos más pequeños que el pivote están a la izquierda del pivote
    // los elementos mayores que el pivote están a la derecha del pivote
    int pi = partition(array, low, high);

    
    // llamada recursiva a la izquierda del pivote
    quickSort(array, low, pi - 1);

    // llamada recursiva a la derecha del pivote
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
    // cout << "Array desordenado: \n";
    //printArray(arr, n);

	  auto begin = chrono::high_resolution_clock::now();
 
   quickSort(arr, 0, n - 1);

	  auto end = chrono::high_resolution_clock::now();
	  double elapsed = chrono::duration_cast<std::chrono::nanoseconds>(end - begin).count();

	  elapsed *= 1e-6;
     //cout << "Array ordenado de manera ascendente: \n";
     cout << "Tiempo total: " << fixed << elapsed << setprecision(9);
	
	  return EXIT_SUCCESS;
}