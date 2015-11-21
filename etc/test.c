#include <stdio.h>
//#include <string.h>
int main()
{
	char buf[100];
	fgets(buf, sizeof(buf), stdin);
	printf("%s\n", buf);
	return 0;
}
