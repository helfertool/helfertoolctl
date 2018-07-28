.PHONY: all install

all:

install:
	mkdir -p $(DESTDIR)/usr/sbin
	install --mode=755 helfertoolctl $(DESTDIR)/usr/sbin

	mkdir -p $(DESTDIR)/lib/systemd/system
	install --mode=644 systemd/helfertool.service $(DESTDIR)/lib/systemd/system

	mkdir -p $(DESTDIR)/usr/share/helfertool
	install --mode=644 share/unavailable.html $(DESTDIR)/usr/share/helfertool

uninstall:
	rm $(DESTDIR)/usr/sbin/helfertoolctl
	rm $(DESTDIR)/lib/systemd/system/helfertool.service
	rm $(DESTDIR)//usr/share/helfertool/unavailable.html
