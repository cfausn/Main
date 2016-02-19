# Feel free to edit to your own preferences, but you probably don't need to
bag: bag.o main.o 
	gcc -o bag main.o bag.o
bag.o: bag.h bag.c 
	gcc -g -c bag.c
main.o: main.c
	gcc -g -c main.c
clean:
	rm -f *.o bag
test: clean bag
	./bag
debug: 
	gcc -ggdb -Wall -o bag bag.c main.c
