================
Installing pyhdf
================

``pyhdf`` has been successfully installed under Python 2.4 and above on
several platforms, including 

* Windows XP

* Linux 2.4.19

* Tru64 4.0.f

* Solaris 8

* AIX 4

* MacOSX 10.5.

Please open an issue here if you encounter any problems during installation:
https://github.com/fhs/python-hdf4/issues

There are several available options for installing pyhdf:

*  Download and install EPD (Enthought Python Distribution)
   which includes pyhdf 0.8.3 .  This makes sense if Python isn't already
   installed on you computer.
*  Download and install pyhdf 0.8.3 from PyPi / the cheeseshop.
*  Download and install pyhdf 0.8.3 from source


Installing EPD
-----------------

EPD (The Enthought Python Distribution) is a python release which includes
many of the major python packages (such as NumPy, SciPy, etc), along
with pyhdf.  As such, you don't need to worry about install other packages.
The EPD is available at `the Enthought website <http://www.enthought.com>`_.
Follow the instructions on the page.

Please note that the Enthought Python Distribution is a commercial product. If
you have questions about the license, please see `this page 
<http://enthought.com/products/epdlicense.php>`_.

Installing from the Cheeseshop
---------------------------------

**Requirements**:

- `Python 2.5+ <http://www.python.org>`_
- `NumPy 1.0.4+  <http://www.scipy.org>`_
- `Setuptools 0.6c8+ <http://pypi.python.org/pypi/setuptools>`_ (provides easy_install command)

The Python Package Index, also known as the Cheeseshop, is
a site on the web where many open-source python packages are stored. To install
PyHDF v0.8+: open a command prompt in the main python directory and type::

        easy_install pyhdf


Quick install from Source for Windows Users
-------------------------------------------

**Requirements**:

- `Python 2.5+ <http://www.python.org>`_
- `NumPy 1.0.4+  <http://www.scipy.org>`_
- `Mingw32 compiler <http://www.mingw.org>`_ or Visual Studio .NET 2003


1. Download the complete HDF4 binary package from the link given
   below.  These packages include all libraries needed to compile
   pyhdf. There are two binary packages to choose from depending on
   whether or not you want to compile pyhdf with SZIP encoding enabled
   or disabled.  There are different licensing implications for each
   choice (see `the HDF page
   <http://hdfgroup.com/doc_resource/SZIP/>`_ for more details on the
   licensing of SZIP).

   - `HDF4 with encoding enabled <http://pysclint.sourceforge.net/pyhdf/hdf4-all-enc.zip>`_
   - `HDF4 with encoding disabled <http://pysclint.sourceforge.net/pyhdf/hdf4-all-noenc.zip>`_

2. Unzip the selected package into a directory of your choice (e.g. C:\HDF4).  

3. Go to the ``pyhdf`` source directory.

4. Build the package in one of the two following ways:

   * Set the HDF4 environment variable to the directory where you unpacked the binary and (e.g. C:\HDF4). Then run the following::

	python setup.py build

   * Run ``python setup.py build --hdf4 <directory of unzipped package>`` where ``<directory of unzipped package>`` is the location where you unzipped the downloaded HDF4 binary (e.g. C:\HDF4).

   *NOTE*: If you are using the mingw32 compiler and are using the
   standard Python binary distribution, then you need to specify -c
   mingw32 on the command line as well.

5. Install ``pyhdf`` or build a binary distribution (bdist_msi,
   bdist_wininst, bdist_egg, etc.) then run one of the following commands::

	python setup.py install
	python setup.py bdist_msi
	python setup.py bdist_wininst
	python setup.py bdist_egg

Install from Source
----------------------

**Requirements**:

- `Python 2.5+ <http://www.python.org>`_
- `NumPy 1.0.4+  <http://www.scipy.org>`_
- `Compiler suite e.g. <http://gcc.gnu.org>`_
- `HDF4.2r3 libraries <http://hdf.ncsa.uiuc.edu/release4/obtain.html>`_ (to use their HDF4 binaries, you will also need szip, available from the same page)
- `zlib <http://www.zlib.net/>`_
- `libjpeg <http://www.ijg.org/>`_ 

*NOTE*: OS X users can obtain jpeg libraries `here <http://ethan.tira-thompson.com/Mac%20OS%20X%20Ports.html>`_. 
Once the above packages are installed, you are ready to download and install pyhdf.
Binaries and source tarballs can be downloaded from the `SourceForge project page <http://www.sourceforge.net/projects pysclint>`_.

To download pyhdf using Subversion, enter the following at the the command prompt::

    svn checkout https://pysclint.svn.sourceforge.net/svnroot/pysclint/trunk/pyhdf
   

Step-by-step instructions for installing pyhdf
----------------------------------------------

1. Go to the ``pyhdf`` source directory.

2. If your HDF4 libraries or include files reside in directories
   that are not searched by default on your system, the installation script
   will complain about missing files.

   Add to the search path by exporting ``INCLUDE_DIRS`` and
   ``LIBRARY_DIRS``, e.g.::

        export INCLUDE_DIRS=/usr/local/hdf-4.2r3/include
        export LIBRARY_DIRS=/usr/local/hdf-4.2r3/lib

   or on Windows something like (replace with actual location)::

        set INCLUDE_DIRS=C:\hdf4\include
        set LIBRARY_DIRS=C:\hdf4\lib;C:\hdf4\dll;C:\hdf4\jpeg6\lib;C:\hdf4\szip21\lib;C:\hdf4\zlib123\lib

   Note that jpeg, zlib, and (optionally) szip libraries must be found
   as well. If they are not in a standard place for the compiler,
   their location must be specified. On Mac OS X, ``/usr/local/lib``
   and ``/usr/local/include`` may need to be specified if the
   libraries were installed there.  You may need to install the devel
   versions of these packages to get the statically-linked libraries
   if your HDF binary is statically linked.
   
   If you are using the binary HDF4 library available from the HDF4 site, you
   must also have szlib installed. Then, you will also need to set ``SZIP``::

        export SZIP=1

	(or on Windows:  set SZIP=1)

   If you do not wish to use szlib, you will need to compile HDF4 from source.

   If anything goes wrong, read the detailed notes below.
   Warning messages about implicit declarations of some functions
   may be produced.  Those are due to SWIG, and may be safely
   ignored.

3. Install system-wide or locally::

        # sudo python setup.py install
        $ python setup.py install --prefix=/usr/local (or prefix of choice)

   Or, you might prefer to make a package (msi, rpm, egg, etc.) and install the 
   package::

        $ python setup.py bdist_<package>

To make sure everything works as expected, run the ``hdfstruct.py``
script (under ``examples/hdfstruct``) on one of your HDF4 files. The
script should display the file structure. This is a handy tool to have
around when you want to explore the contents of any HDF4 file.


=============
Further notes
=============

External libraries
------------------

HDF4.2 no longer provides its own copies of the jpeg and z libraries.
Those must be installed separately (on Linux, they should be part of
any standard distribution).

The sz library (versions 2.0 or higher) must be installed if the SZIP
compression method is to be used with SDsetcompress(). HDF v4.2 must
also then be compiled with SZIP support.  The binaries available from
NCSA are (at the time of this writing) compiled with SZIP support
(including encoding).  To use these binaries, you *must have SZIP installed*.
The binaries Enthought has produced and which are available in EPD and for 
download from Sourceforge are compiled with SZIP support without encoding
capability.  

Getting an SZIP enabled HDF library may require compiling the library
from source with the "--with-szlib" configuration option.  Note that
you *must* install SZIP in a separate step. For more details, see the
`NCSA hdf site <http://hdf.ncsa.uiuc.edu/doc_resource/SZIP/>`_.
Source code and binaries are `available for download
<ftp://ftp.hdfgroup.org/lib-external/szip/>`_.

In case your HDF library was compiled with SZIP support and you abide by the
szip licensing terms, set the environment variable ``SZIP`` to ``1``.

If you get error messages related to the ``SDgetcompress()`` /
``SDsetcompress()`` functions, e.g. ``"undefined symbol:
SDgetcompress"``, set the environment variable ``NO_COMPRESS`` to "1".
This will transform ``SDgetcompress()`` and ``SDsetcompress()`` into
no-ops, which will immediately raise an exception, and will not be
resolved against the HDF library symbols. This may make it possible to
work with an HDF library earlier than v4.2.

Swig-generated interface files
------------------------------
Interface files ``hdfext.py`` and ``hdfext_wrap.c`` (located under the
``pyhdf`` subdirectory) have been generated using the SWIG tool.
Those two files should be usable as is on most environments.  It could
happen however that, for reasons related to your environment, your C
compiler does not accept the '.c' file and raises a compilation
error. If so, the interface needs to be regenerated.  To do so,
install `SWIG <http://www.swig.org>`_, then run::

  $ cd pyhdf
  $ swig -python hdfext.i

SWIG should silently regenerate the two interface files, after which
installation should proceed correctly.

TRU64 note
----------
The HDF installation creates its libraries as archive (.a) files,
not shareable (.so) ones. On TRU64, the linker by default first looks
for shareable libraries in every directory, then in a second round
for archive files. This means that if there is a libjpeg.so somewhere
on the standard linker search paths, it will be found first, even if
the HDF libjpeg.a file exists in the directory pointed by "library_dirs".
To solve the problem, set the environment variable ``LINK_ARGS``::

  export LINK_ARGS="-oldstyle_liblookup"

This will tell the linker to look for .so then for .a files in each visited
directory.
