files = ${wildcard *.java}
target = ${files:.java=.class}

build: ${target}
	@true

%.class: %.java
	javac $<

clean:
	rm -fv ${target}

.PHONY: build clean