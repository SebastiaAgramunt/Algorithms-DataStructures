all: qsort #clean

CC =			gcc
CFLAGS =		-O -Wall
LIBS =			-lm

SOURCES =		quicksort.c main.c
OBJECTS =		quicksort.o main.o

EXENAME =       qsort_exe


qsort: $(OBJECTS)
	$(CC) -o $(EXENAME) $(CFLAGS) $(OBJECTS) $(LIBS)

clean: $(OBJECTS)
	rm -rf *.o
	rm -rf $(EXENAME)
