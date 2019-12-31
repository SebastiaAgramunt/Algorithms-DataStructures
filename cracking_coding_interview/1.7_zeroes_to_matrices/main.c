#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h> 

// This algo takes O(rows*cols)
void set_to_zero(int** matrix, int rows, int cols){
	bool *r = (bool*)malloc(rows*sizeof(bool));
	bool *c = (bool*)malloc(cols*sizeof(bool));

	for(int i=0; i<rows; i++) r[i]=false; //O(rows) both time and space
	for(int i=0; i<cols; i++) c[i]=false; //O(cols)

	//finding rows and cols that we must set to 0
	//O(rows*cols)
	for(int i=0; i<rows; i++){
		for(int j=0; j<cols; j++){
			if(matrix[i][j]==0){
				r[i] = true;
				c[j] = true;
				break;
			}
		}
	}

	// setting up 0 rows
	// O(rows)
	for(int i=0; i<rows;i++){
		if(r[i]==true){
			for(int k =0; k<cols; k++){
				matrix[i][k]=0;
			}
		}
	}

	// setting up 0 cols
	// O(cols)
	for(int i=0; i<cols;i++){
		if(c[i]==true){
			for(int k =0; k<rows; k++){
				matrix[k][i]=0;
			}
		}
	}
}

void print_matrix(int** matrix, int rows, int cols){
	for(int i=0; i < rows; i++){
		for(int j=0; j<cols; j++){
			printf("%d ", matrix[i][j]);
		}
		printf("\n");
	}
	printf("\n");
}


int main(){

	// initializing matrix
	int rows = 10;
	int cols = 15;
	int **matrix = (int**)malloc(rows*sizeof(int*));
	for(int i=0; i < rows; i++){
		matrix[i] = (int*)malloc(cols*sizeof(int));
	}

	// giving values to matrix
	for(int i=0; i < rows; i++){
		for(int j=0; j<cols; j++){
			matrix[i][j]=1;
			if(i==rows/2 && j==cols/2){
				matrix[i][j]=0;
			}
			if(i==2 && j==10){
				matrix[i][j]=0;
			}
		}
	}

	// print initial matrix
	print_matrix(matrix, rows, cols);

	set_to_zero(matrix, rows, cols);

	// print final matrix
	print_matrix(matrix, rows, cols);


	return 0;
}