AM_CFLAGS =\
	$(DEBUG_CFLAGS) \
	-Wall \
	-g \
	-D_GNU_SOURCE \
	-fPIC \
	$(Python_CFLAGS)

noinst_PROGRAMS = slp.so

slp_so_LDFLAGS = -shared -Wl,-Bdynamic \
						-Wl,-soname=slp.so

slp_so_SOURCES = \
	slpmodule.c

slp_so_LDADD = $(Python_LIBS) $(Slp_LIBS)
