all: stack #clean

CC =			gcc
CFLAGS =		-O -Wall
LIBS =			-lm

SOURCES =		stack.c main.c
OBJECTS =		stack.o main.o
EXENAME =               stack

stack: $(OBJECTS)
	$(CC) -o $(EXENAME) $(CFLAGS) $(OBJECTS) $(LIBS)

clean: $(OBJECTS)
	rm -rf *.o
	rm -rf $(EXENAME)
