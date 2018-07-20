BINDIR = $(DESTDIR)/usr/sbin

.PHONY: all install

all:

install:
	install --mode=755 helfertoolctl $(BINDIR)/

uninstall:
	rm $(BINDIR)/helfertoolctl
