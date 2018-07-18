/*
* @autor BetaFish <yale2a1@gmail.com>
* @since 2016-06-04
*
* xor을 이용해서 test를 출력한다.
* 원래 코드 :
*int main(){
*	int i = 0;
*	char *ptr;
*	char input[17] = {0, };
*	char test[17] = {15,19,6,14,21,11,7,11,33,21,26,40,1,11,4,74,0};
*	printf("Please Input Your FLAG : ");
*	scanf("%s", input);
*	for(i = 0; i < 16; i++)
*		test[i] ^= input[i];
*if(!strcmp(test, "HackabilityCheck"))
*	printf("Good :\n");
*}
*/
#include <stdio.h>
#include <stdlib.h>

int main(){
	int i = 0;
	char *ptr;
	char input[17] = {0, };
	char test[17] = {15,19,6,14,21,11,7,11,33,21,26,40,1,11,4,74,0};
	char A[17] = "HackabilityCheck";

	for(i = 0; i < 16; i++)
		input[i] = A[i] ^ test[i];
    printf("%s", input);
    return 0;
}
