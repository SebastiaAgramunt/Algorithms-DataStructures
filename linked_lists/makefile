all: llists #clean

CC =			gcc
CFLAGS =		-O -Wall
LIBS =			-lm

SOURCES =		linked_lists.c main.c
OBJECTS =		linked_lists.o main.o
EXEFILE =               llists

llists: $(OBJECTS)
	$(CC) -o $(EXEFILE) $(CFLAGS) $(OBJECTS) $(LIBS)

clean: $(OBJECTS)
	rm -rf *.o
	rm -rf $(EXEFILE)
