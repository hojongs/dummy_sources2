#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
int main()
{
	char*argv[]={"/bin/sh", NULL};
//	execve("hello", NULL, NULL);
	printf("bye\n");
	
	return 0;
}
