#!/usr/bin/env python
import glob
from distutils import sysconfig
from distutils.core import setup, Extension

# TODO improve this code
# * detect platform/compiler
# * have autoconf fill the include dirs
# * set have local define where necessary

module = Extension(
	"pyewf",
	glob.glob("*.c"),
	define_macros = [
		("HAVE_LOCAL_LIBCSTRING", ""),
		("HAVE_LOCAL_LIBCERROR", ""),
		("HAVE_LOCAL_LIBCDATA", ""),
		("HAVE_LOCAL_LIBCLOCALE", ""),
		("HAVE_LOCAL_LIBCSPLIT", ""),
		("HAVE_LOCAL_LIBUNA", ""),
		("HAVE_LOCAL_LIBCFILE", ""),
		("HAVE_LOCAL_LIBCPATH", ""),
		("HAVE_LOCAL_LIBBFIO", ""),
	],
	include_dirs = [
		"..\\common",
		"..\\include",
		"..\\libcstring",
		"..\\libcerror",
		"..\\libcdata",
		"..\\libclocale",
		"..\\libcsplit",
		"..\\libuna",
		"..\\libcfile",
		"..\\libcpath",
		"..\\libbfio",
	],
	libraries = [
		"libcstring",
		"libcerror",
		"libcdata",
		"libclocale",
		"libcsplit",
		"libuna",
		"libcfile",
		"libcpath",
		"libbfio",
		"libewf",
	],
	library_dirs = [
		"..\\msvscpp\\Release",
	],
)

# TODO: what about license, description and platform in egg file
setup(
	name = "pyewf",
	url = "http://code.google.com/p/libewf/",
	version = "20130128",
	description = "Python bindings module for libewf",
	author = "Joachim Metz",
	author_email = "joachim.metz@gmail.com",
	ext_modules = [
		module,
	],
	data_files = [
		(sysconfig.get_python_lib(), [
			"..\\msvscpp\\Release\\libewf.dll",
			"..\\msvscpp\\Release\\zlib.dll",
		]),
	],
)

