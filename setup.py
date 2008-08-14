from numpy.distutils.core import setup, Extension

# --- Configure your environment here ---
include_dirs = ["/usr/include"]
library_dirs = ["/usr/lib/"]
szip_installed = True # Set to False if your library was compiled without
                      # libsz support
compress = True # Set to False if the HDF library reports errors
                # related to SDgetcompress() / SDsetgompress()

# --- End configuration ---

import os.path as path
for p in include_dirs + library_dirs:
    if not path.exists(p):
        raise RuntimeError('Cannot proceed without the HDF4 library.  Please '
                           'edit include paths in "setup.py" and read the '
                           'INSTALL file for further instructions.')

libraries = ["mfhdf", "df", "jpeg", "z"]
if szip_installed:
    extra_compile_args = []
    libraries += ["sz"]
else:
    extra_compile_args = ["-DNOSZIP"]

if not compress:
    extra_compile_args += ["-DNOCOMPRESS"]

_hdfext = Extension('pyhdf._hdfext',
                    sources      = ["pyhdf/hdfext_wrap.c"],
                    include_dirs = include_dirs,
                    extra_compile_args = extra_compile_args,
                    library_dirs = library_dirs,
                    #extra_link_args=["extra stuff passed to the linker"],
                    libraries = libraries,
                    )

setup(name         = 'pyhdf',
      author       = 'Andre Gosselin',
      author_email = 'Andre.Gosselin@dfo-mpo.gc.ca',
      description  = 'Python interface to the NCSA HDF4 library',
      keywords     = ['hdf', 'netcdf', 'numpy', 'python', 'pyhdf', 'parse_odl'],
      license      = 'public',
      long_description = 'The pyhdf package wraps the functionality\n '
                         'of the NCSA HDF version 4 library inside a Python OOP\n '
                         'framework. The SD (scientific dataset), VS\n '
                         '(Vdata) and V (Vgroup) APIs are currently implemented.\n '
                         'SD datasets are read/written\n '
                         'through numpy arrays. netCDF files can also\n '
                         'be read and modified with pyhdf.'
                         '\n'
                         'The function parse_odl is also provided to\n'
                         'deal specifically with data in the ODL\n'
                         '(Object Desdription Language) format.',
      url          = 'www.sourceforge.net/projects/pysclint',
      version      = '0.8-1',
      packages     = ['pyhdf'],
      ext_modules  = [_hdfext]
      )