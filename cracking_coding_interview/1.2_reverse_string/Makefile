all: rev_str #clean

CC =			gcc
CFLAGS =		-O -Wall
LIBS =			-lm

SOURCES =		main.c
OBJECTS =		main.o

EXENAME =		rev_str


rev_str: $(OBJECTS)
	$(CC) -o $(EXENAME) $(CFLAGS) $(OBJECTS) $(LIBS)

clean: $(OBJECTS)
	rm -rf *.o
	rm -rf $(EXENAME)