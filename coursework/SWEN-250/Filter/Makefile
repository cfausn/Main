test_filter: test_filter.o filter.o
	gcc -o test_filter test_filter.o filter.o

test_filter.o: test_filter.c filter.h
	gcc -c test_filter.c

filter.o: filter.c filter.h
	gcc -c filter.c

clean:
	rm -f test_filter test_filter.exe
	rm -f *.o *.bak *~*
