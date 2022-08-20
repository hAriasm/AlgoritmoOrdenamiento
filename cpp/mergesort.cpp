//------------------------------
// LIBRERIAS
//------------------------------
#include <iostream>
#include <vector>
using namespace std;
#include <chrono>
#include <bits/stdc++.h>

//-------------------------------------
// ALGORITMO DE ORDENAMIENTO MERGESORT
//-------------------------------------
void merge(vector<int>&arreglo,int inicio, int mitad, int final){
    int i,j,k;
    int elementosIzq = mitad - inicio + 1;
    int elementosDer = final - mitad;

    vector<int>izquierda(elementosIzq);
    vector<int>derecha(elementosDer);

    for(int i = 0; i < elementosIzq; i++){
        izquierda[i] = arreglo[inicio+i];
    }
    for(int j = 0; j < elementosDer; j++){
        derecha[j] = arreglo[mitad + 1 + j];
    }

    i = 0;
    j = 0;
    k = inicio;

    while(i < elementosIzq && j < elementosDer){
        if(izquierda[i] <= derecha[j]){
            arreglo[k] = izquierda[i];
            i++;
        }else{
            arreglo[k] = derecha[j];
            j++;
        }
        k++;
    }

    while(j < elementosDer){
        arreglo[k] = derecha[j];
        j++;
        k++;
    }

    while(i < elementosIzq){
        arreglo[k] = izquierda[i];
        i++;
        k++;
    }

}

void mergeSort(vector<int>&arreglo,int inicio, int final){
    if(inicio < final){
        int mitad = inicio + (final - inicio)/2;
        mergeSort(arreglo,inicio,mitad);
        mergeSort(arreglo,mitad+1,final);
        merge(arreglo,inicio,mitad,final);
    }
}

void imprimirArreglo(vector<int>arreglo){
    for(int i = 0; i < arreglo.size(); i++){
        cout << arreglo[i] << " ";
    }
    cout << endl;
}

//----------------------------------------------------
// ALGORITMO DE LECTURA DE ARCHIVO .TXT CON "N" DATOS
//----------------------------------------------------

bool readDataFile(vector<int>&arr, int N, string dataFileName)
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

//------------------------------
// EJECUCION DEL PROGRAMA 
//------------------------------

// LLAMADO A PROGRAMA DE LECTURA DE ARCHIVO
int main(int argc, char **argv) {

    int N = atoi(argv[1]);

   vector<int>arr(N);
	  if (!readDataFile(arr, N, argv[2]))
	  {
		return EXIT_FAILURE;
	  }

// INICIO DE TEMPORIZADOR 
   auto begin = chrono::high_resolution_clock::now();

// EJECUCION DE PROGRAMA DE ORDENAMIENTO
    mergeSort(arr,0,arr.size()-1);
    auto end = chrono::high_resolution_clock::now();
	  double elapsed = chrono::duration_cast<std::chrono::nanoseconds>(end - begin).count();
	  elapsed *= 1e-6;
// FIN DE TEMPORIZADOR

// IMPRESION DE TIEMPO DE EJECUCION DE PROGRAMA DE ORDENAMIENTO      
     cout << "Tiempo total: " << fixed << elapsed << setprecision(9);

    return 0;
}