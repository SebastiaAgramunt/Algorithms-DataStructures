
#include <stdio.h>
#include <stdlib.h>

void swap(int* a, int* b){
	int a_val = *a;

	*a = *b;
	*b = a_val;
}

void printArray(int arr[], int size)  
{  
    int i;  
    for (i = 0; i < size; i++){
    	printf("%d ", arr[i]);
    }  
    printf("\n");
}

int partition(int arr[], int low, int high){
	int i = low-1; //starting at -1
	int pivot = arr[high]; //starting at lenght -1 (last element)

	for(int j=low; j<=high-1; j++){
		if(arr[j] < pivot){
			i++;
			swap(&arr[i], &arr[j]);
		}
	}
	swap(&arr[i+1], &arr[high]);
	return(i+1);
}

void quicksort(int arr[], int low, int high){
	if(low < high){
		int mid = partition(arr, low, high);

		quicksort(arr, low, mid-1);
		quicksort(arr, mid+1, high);

	}
}

int main(void){

	//int size = 7;
	//int array[] = {10, 9, 20, 5, 3, 13, 7};

	int size = 7;
	int *arr = (int*)malloc(size*sizeof(int));

	arr[0] = 10;
	arr[1] = 9;
	arr[2] = 20;
	arr[3] = 5;
	arr[4] = 3;
	arr[5] = 13;
	arr[6] = 7;
    
    printf("Initial array: \n"); 
    printArray(arr, size);

    quicksort(arr, 0, size-1); 

    printf("Sorted array: \n"); 
    printArray(arr, size); 

	return 0;
}
