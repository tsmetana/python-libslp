AM_CFLAGS =\
	$(DEBUG_CFLAGS) \
	-Wall \
	-g \
	-D_GNU_SOURCE \
	-fPIC \
	$(Python_CFLAGS)

noinst_PROGRAMS = slpmodule.so

slpmodule_so_LDFLAGS = -shared -Wl,-Bdynamic \
						-Wl,-soname=slpmodule.so

slpmodule_so_SOURCES = \
	slpmodule.c

slpmodule_so_LDADD = $(Python_LIBS) $(Slp_LIBS)
