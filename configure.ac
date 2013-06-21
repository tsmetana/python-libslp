AC_INIT(pyslp,0.1,,)
AC_PREREQ(2.57)
AC_CONFIG_HEADERS(config.h)
AC_GNU_SOURCE
AM_INIT_AUTOMAKE
CFLAGS=""
AC_SUBST(CFLAGS)
AC_PROG_CC
AC_PROG_RANLIB
AC_HEADER_STDC

PKG_CHECK_MODULES(Python, python >= 2.7,,)
AC_SUBST(Python_CFLAGS)
AC_SUBST(Python_LIBS)

AC_CHECK_HEADER([slp.h],
	[Slp_LIBS="-lslp"
	AC_SUBST(Slp_LIBS)],
	[echo "OpenSLP header file not found"
	 exit 1],[])

AC_ARG_ENABLE([debug],
	[AC_HELP_STRING([--enable-debug], [enable debugging code @<:@default=no@:>@])],
	[enable_debug=yes],
	[enable_debug=no]
)
if test x$enable_debug = xyes; then
	DEBUG_CFLAGS="-DDEBUG -g -Werror"
	AC_SUBST(DEBUG_CFLAGS)
fi

AC_OUTPUT([
Makefile
src/Makefile
])


