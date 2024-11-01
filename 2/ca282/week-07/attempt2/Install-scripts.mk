dst = $(HOME)/local/bin
files = $(wildcard [a-z]*)

install: $(dst) $(addprefix $(dst)/, $(files))
	@true

$(dst)/%: %
	install -m 0555 $< $@

$(dst):
	mkdir -p $@

.PHONY: install