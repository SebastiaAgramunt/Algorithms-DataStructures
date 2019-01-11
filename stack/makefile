all: stack #clean

CC =			gcc
CFLAGS =		-O -Wall
LIBS =			-lm

SOURCES =		stack.c main.c
OBJECTS =		stack.o main.o


stack: $(OBJECTS)
	$(CC) -o stack $(CFLAGS) $(OBJECTS) $(LIBS)

clean: $(OBJECTS)
	rm -rf *.o
