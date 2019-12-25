#include <stdio.h>
#include <stdlib.h>
#include "quicksort.h"

// arr is already sorted here
int binary_search_helper(int* arr, int low, int high, int val){

	if(high>=low){
		int mid = low + (high-low)/2;

		printf("%d  %d  %d  %d  %d\n",low, mid, high,arr[mid], val);
		if(arr[mid] == val){
			//int* i = &arr[mid];
			//i = &mid;
			return mid;
		}
		if(arr[mid]>val){
			return binary_search_helper(arr, low, mid-1, val);
		}else{
			return binary_search_helper(arr, mid+1, high, val); 
		}
	}else{
		return -1;
	}
}

int binary_search(int* arr, int low, int high, int val){
	quicksort(arr, low, high);
	return binary_search_helper(arr, low, high, val);;
}