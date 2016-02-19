SOURCES = test_dmv_schedule.c dmv_schedule.c assert.c
HEADERS = dmv_schedule.h assert.h
OBJS = $(SOURCES:.c=.o)

# Primary target - test_dmv_schedule executable

test_dmv_schedule: $(OBJS)
	gcc -o test_dmv_schedule -ggdb $(OBJS)

# Object file dependencies.
# See .c.o rule for how C files are converted to object files implicitly.

test_dmv_schedule.o: test_dmv_schedule.c dmv_schedule.h assert.h

dmv_schedule.o: dmv_schedule.c dmv_schedule.h

assert.o: assert.c assert.h

# Clean up the directory

clean:
	rm -f test_dmv_schedule test_dmv_schedule.exe
	rm -f *.o *.bak *~*

# Implicit rule for converting .c files to .o files when the
# .o file is out of date.

.c.o:
	gcc -c -ggdb $<
