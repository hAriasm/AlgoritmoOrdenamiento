// C++ program to implement Tree Sort 
#include <iostream>
#include <chrono>
#include <bits/stdc++.h>    
using namespace std;

struct Node
{
	int key;
	struct Node *left, *right;
};

// A utility function to create a new BST Node
struct Node *newNode(int item)
{
	struct Node *temp = new Node;
	temp->key = item;
	temp->left = temp->right = NULL;
	return temp;
}

// Stores inorder traversal of the BST
// in arr[]
void storeSorted(Node *root, int arr[], int &i)
{
	if (root != NULL)
	{
		storeSorted(root->left, arr, i);
		arr[i++] = root->key;
		storeSorted(root->right, arr, i);
	}
}

/* A utility function to insert a new
Node with given key in BST */
Node* insert(Node* node, int key)
{
	/* If the tree is empty, return a new Node */
	if (node == NULL) return newNode(key);

	/* Otherwise, recur down the tree */
	if (key < node->key)
		node->left = insert(node->left, key);
	else if (key > node->key)
		node->right = insert(node->right, key);

	/* return the (unchanged) Node pointer */
	return node;
}

// This function sorts arr[0..n-1] using Tree Sort
void treeSort(int arr[], int n)
{
	struct Node *root = NULL;

	// Construct the BST
	root = insert(root, arr[0]);
	for (int i=1; i<n; i++)
		root = insert(root, arr[i]);

	// Store inorder traversal of the BST
	// in arr[]
	int i = 0;
	storeSorted(root, arr, i);
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

// Driver Program to test above functions
int main(int argc, char **argv)
{
	//create input array
  
	int N = atoi(argv[1]);
	int arr[N] = {};

	if (!readDataFile(arr, N, argv[2]))
	{
		return EXIT_FAILURE;
	}

	// srand(time(NULL));
	// for(int i = 0; i < N; i++) {
	// 	arr[i] = rand()%N;
	// }

	// printArray(arr, N);

	auto begin = chrono::high_resolution_clock::now();
 
	treeSort(arr,N);

	auto end = chrono::high_resolution_clock::now();
	double elapsed = chrono::duration_cast<std::chrono::nanoseconds>(end - begin).count();

	elapsed *= 1e-6;

	// cout << endl;
	// cout << "Sorted array is \n";
	// printArray(arr, N);

	cout << "Tiempo total: " << fixed << elapsed << setprecision(9);

	return EXIT_SUCCESS; 
}
