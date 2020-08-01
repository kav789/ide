# Makefile for gif2png

VERSION = $(shell sed -n <NEWS '/::/s/^\([^:]*\).*/\1/p' | head -1)

TAR = tar

all: clean url_rewrite

url_rewrite:
	cp url_rewrite.py url_rewrite


clean:
	rm url_rewrite

version:
	@echo $(VERSION)

prefix ?= /usr
bindir ?= $(prefix)/bin
etcdir ?= /etc/squid

install:
	mkdir -p $(DESTDIR)$(etcdir)
	mkdir -p $(DESTDIR)$(bindir)
	cp url_rewrite $(DESTDIR)$(bindir)/
	cp squid.conf.url_rewrite url_rewrite.conf $(DESTDIR)$(etcdir)/

uninstall:
	rm $(DESTDIR)$(bindir)/url_rewrite
	rm $(DESTDIR)$(etcdir)/squid.conf.url_rewrite $(DESTDIR)$(etcdir)/url_rewrite.conf

EXTRA_DIST = url_rewrite.conf README NEWS INSTALL Makefile squid.conf.url_rewrite url_rewrite.py
DISTFILES = url_rewrite  $(EXTRA_DIST)

url_rewrite-$(VERSION).tar.gz: $(DISTFILES)
	$(TAR) --transform='s:^:url_rewrite-$(VERSION)/:' --show-transformed-names -czf url_rewrite-$(VERSION).tar.gz $(DISTFILES)

dist: url_rewrite-$(VERSION).tar.gz

release: url_rewrite-$(VERSION).tar.gz

