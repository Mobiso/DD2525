#include <stdio.h>
#include <stdlib.h> 
#include <unistd.h>

int main() {

	char guess[2];
	read(STDIN_FILENO, guess, 2);
    //can be found by giving an argument larger than 5 
	char secret_string[] = "You were not meant to find this....";
	char words[6][10] = {"big","large","chungus","fatty","acid","thor"};
	printf("You found the word: %s\n",words[atoi(guess)]);
	
	return 0;
}
