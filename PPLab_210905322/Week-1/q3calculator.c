#include "mpi.h"
#include <stdio.h>
#include <math.h>

int main(int argc,char *argv[])
{
    int rank,size;
    int x=10,y=4;
    MPI_Init(&argc,&argv);
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    MPI_Comm_size(MPI_COMM_WORLD,&size);
    if(rank==0)
    {
        printf("rank:%d \t\t %d + %d = %d\n",rank,x,y,x+y);
    }
    else if(rank==1)
    {
        printf("rank:%d \t\t %d - %d = %d\n",rank,x,y,x-y);
    }
    else if(rank==2)
    {
        printf("rank:%d \t\t %d * %d = %d\n",rank,x,y,x*y);
    }
    else if(rank==3)
    {
        printf("rank:%d \t\t %d / %d = %d\n",rank,x,y,x/y);
    }
    MPI_Finalize();
}