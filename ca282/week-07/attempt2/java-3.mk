java = $(wildcard *.java)
class = $(patsubst %.java, %.class, $(java))

build: $(class)
	@true

%.class: %.java
	javac $<

clean: $(class)
	rm -fv $(class)

.PHONY: clean