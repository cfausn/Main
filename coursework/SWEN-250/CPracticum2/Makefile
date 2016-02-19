# Practica source files and the object files derived from them.
SOURCES = test_zoo.c zoo.c memory.c assert.c
OBJS = $(SOURCES:.c=.o)

# Primary target - test_zoo executable

test_zoo: $(OBJS)
	gcc -o test_zoo -ggdb $(OBJS)

# Object file dependencies.
# See .c.o rule for how C files are converted to object files implicitly.

test_zoo.o: test_zoo.c zoo.h memory.h assert.h

zoo.o: zoo.c zoo.h memory.h

memory.o: memory.c assert.h memory.h

# Clean up the directory

clean:
	rm -f test_zoo test_zoo.exe
	rm -f *.o *.bak *~*

# Implicit rule for converting .c files to .o files when the
# .o file is out of date.
.c.o:
	gcc -c -ggdb $<
