all: trie #clean

CC =			gcc
CFLAGS =		-O -Wall
LIBS =			-lm

SOURCES =		main.c
OBJECTS =		main.o

EXENAME =		trie


trie: $(OBJECTS)
	$(CC) -o $(EXENAME) $(CFLAGS) $(OBJECTS) $(LIBS)

clean: $(OBJECTS)
	rm -rf *.o
	rm -rf $(EXENAME)