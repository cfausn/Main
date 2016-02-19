# Activity source files and the object files derived from them.
SOURCES = test_linked.c linked.c memory.c assert.c
OBJS = $(SOURCES:.c=.o)

# Primary target - test_linked executable

test_linked: $(OBJS)
	gcc -o test_linked $(OBJS)

sizeof_example: sizeof_example.c
	gcc -o sizeof_example sizeof_example.c

# Object file dependencies.
# See .c.o rule for how C files are converted to object files implicitly.

test_linked.o: test_linked.c linked.h memory.h assert.h

linked.o: linked.c linked.h memory.h

memory.o: memory.c assert.h memory.h

# Clean up the directory

clean:
	rm -f test_linked test_linked.exe
	rm -f sizeof_example sizeof_example.exe
	rm -f *.o *.bak *~*

# Implicit rule for converting .c files to .o files when the
# .o file is out of date.
.c.o:
	gcc -c $<
