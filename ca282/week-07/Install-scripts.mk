dst = ${HOME}/local/bin
src = ${wildcard [a-z]*}

install: ${dst} ${addprefix ${dst}/, ${src}}
	@true

${dst}/%: %
	install -m 0555 $< $@
${dst}:
	mkdir -p $@

.PHONY: install