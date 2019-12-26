all: bin_tree #clean

CC =			gcc
CFLAGS =		-O -Wall
LIBS =			-lm

SOURCES =		binary_tree.c main.c
OBJECTS =		binary_tree.o main.o

EXENAME =		bin_tree


bin_tree: $(OBJECTS)
	$(CC) -o $(EXENAME) $(CFLAGS) $(OBJECTS) $(LIBS)

clean: $(OBJECTS)
	rm -rf *.o
	rm -rf $(EXENAME)