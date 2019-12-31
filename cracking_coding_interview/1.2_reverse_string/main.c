#include <stdio.h>
#include <stdlib.h>

void swap(int *a, int *b){
	int new_b = *a;
	*a = *b;
	*b = new_b;
}

void reverse(int *arr, int size){
	for(int i=0; i<size/2; i++){
		int j = (size - 1) - i;
		swap(arr+i, arr+j);
	}
	
}


int main(){

	int size = 7;
	int *arr = (int*)malloc(size*sizeof(int));

	arr[0] = 10;
	arr[1] = 9;
	arr[2] = 20;
	arr[3] = 5;
	arr[4] = 3;
	arr[5] = 13;
	arr[6] = 7;

	reverse(arr, size);
	for(int i=0; i<size; i++){
		printf("%d ", arr[i]);
	}

	return 0;
}