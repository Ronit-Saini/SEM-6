#include <stdio.h>
#include <mpi.h>

int main(int argc, char* argv[]){
    int rank,size,n,arr[10],B[10],c,i;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    MPI_Comm_size(MPI_COMM_WORLD,&size);
 
    if (rank == 0) 
    {
        n = size;
        printf("Enter the numbers: ");
        fflush(stdout);
 
        for (i = 0; i < n;i++) 
        {
            scanf("%d", &arr[i]);
        }
    }

    MPI_Scatter(arr, 1, MPI_INT, &c, 1, MPI_INT, 0, MPI_COMM_WORLD);
    printf("Process [%d] received = %d\n", rank, c);
    fflush(stdout);

    c=c*c;
    MPI_Gather(&c,1,MPI_INT,B,1,MPI_INT,0,MPI_COMM_WORLD);

    if(rank==0){
        printf("The result gathered in the root:\n");
        for(i=0;i<n;i++){
            printf("%d\t",B[i]);
        }
    }

    MPI_Finalize();
    return 0;
 
}