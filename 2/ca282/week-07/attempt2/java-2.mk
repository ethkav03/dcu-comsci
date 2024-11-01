coffeescript = $(wildcard *.java)
javascript = $(patsubst %.java, %.class, $(coffeescript))

build: $(javascript)
	@true

%.class: %.java
	javac $<
