files = ${wildcard *.java}
target = ${files:.java=.class}

build: ${target}
	@true

%.class: %.java
	javac $<

.PHONY: build