all: qsort #clean

CC =			gcc
CFLAGS =		-O -Wall
LIBS =			-lm

SOURCES =		binary_search.c quicksort.c main.c
OBJECTS =		binary_search.o quicksort.o main.o

EXENAME =		bin_search


qsort: $(OBJECTS)
	$(CC) -o $(EXENAME) $(CFLAGS) $(OBJECTS) $(LIBS)

clean: $(OBJECTS)
	rm -rf *.o
	rm -rf $(EXENAME)
