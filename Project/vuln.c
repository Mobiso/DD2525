#include <stdio.h>
#include <stdlib.h> 
int main(int argc, char* argv[]) {
	if(argc < 2){
		printf("Please give me a number between 0 and 5 (inclusive)!\n");
		return 1;
	}
	char secret_string[] = "You were not meant to find this....";
	
	char words[6][10] = {"big","large","chungus","fatty","acid","thor"};
	printf("You found the word: %s\n",words[atoi(argv[1])]);
	return 0;
}
