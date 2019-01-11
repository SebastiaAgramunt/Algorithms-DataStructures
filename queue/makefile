all: queue #clean

CC =			gcc
CFLAGS =		-O -Wall
LIBS =			-lm

SOURCES =		queue.c main.c
OBJECTS =		queue.o main.o


queue: $(OBJECTS)
	$(CC) -o queue $(CFLAGS) $(OBJECTS) $(LIBS)

clean: $(OBJECTS)
	rm -rf *.o
