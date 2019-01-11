all: llists #clean

CC =			gcc
CFLAGS =		-O -Wall
LIBS =			-lm

SOURCES =		linked_lists.c main.c
OBJECTS =		linked_lists.o main.o


llists: $(OBJECTS)
	$(CC) -o llists $(CFLAGS) $(OBJECTS) $(LIBS)

clean: $(OBJECTS)
	rm -rf *.o
