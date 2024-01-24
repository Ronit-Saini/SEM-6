#include <stdio.h>
#include <string.h>
#include "mpi.h"
int main(int argc, char* argv[])
{
	int rank,size,x;
    char word[100];
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	MPI_Status status;
	if(rank==0){
		printf("Enter a string in the master process: ");
		scanf("%s",word);
		MPI_Ssend(word,100,MPI_CHAR,1,1,MPI_COMM_WORLD);
		printf("I have sent %s from process 0\n",word);
		//fflush(stdout);
        MPI_Recv(word,100,MPI_CHAR,1,1,MPI_COMM_WORLD,&status);
        printf("I have recieved %s in process 0\n",word);
	}
	else{
		MPI_Recv(word,100,MPI_CHAR,0,1,MPI_COMM_WORLD,&status);
		printf("I have recieved %s in process 1\n",word);
		for(int i=0;i<strlen(word);i++)
        {
            word[i]^=32;
        }
        MPI_Ssend(word,100,MPI_CHAR,0,1,MPI_COMM_WORLD);
        printf("I have sent %s from process 1\n",word);
	}
	MPI_Finalize();
	return 0;
}