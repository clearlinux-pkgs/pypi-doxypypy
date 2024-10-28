#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
# autospec version: v20
# autospec commit: e180208
#
Name     : pypi-doxypypy
Version  : 0.8.8.7
Release  : 3
URL      : https://files.pythonhosted.org/packages/f9/d2/8331005fb117a27c0122f714fe3f528d8c5752aa13d11d5cba12d754270b/doxypypy-0.8.8.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/f9/d2/8331005fb117a27c0122f714fe3f528d8c5752aa13d11d5cba12d754270b/doxypypy-0.8.8.7.tar.gz
Summary  : A Doxygen filter for Python
Group    : Development/Tools
License  : GPL-2.0
Requires: pypi-doxypypy-bin = %{version}-%{release}
Requires: pypi-doxypypy-license = %{version}-%{release}
Requires: pypi-doxypypy-python = %{version}-%{release}
Requires: pypi-doxypypy-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(chardet)
BuildRequires : pypi(pytest)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
doxypypy
========
*A more Pythonic version of doxypy, a Doxygen filter for Python.*

%package bin
Summary: bin components for the pypi-doxypypy package.
Group: Binaries
Requires: pypi-doxypypy-license = %{version}-%{release}

%description bin
bin components for the pypi-doxypypy package.


%package license
Summary: license components for the pypi-doxypypy package.
Group: Default

%description license
license components for the pypi-doxypypy package.


%package python
Summary: python components for the pypi-doxypypy package.
Group: Default
Requires: pypi-doxypypy-python3 = %{version}-%{release}

%description python
python components for the pypi-doxypypy package.


%package python3
Summary: python3 components for the pypi-doxypypy package.
Group: Default
Requires: python3-core
Provides: pypi(doxypypy)
Requires: pypi(chardet)

%description python3
python3 components for the pypi-doxypypy package.


%prep
%setup -q -n doxypypy-0.8.8.7
cd %{_builddir}/doxypypy-0.8.8.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1730142615
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-doxypypy
cp %{_builddir}/doxypypy-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-doxypypy/eb80802cb4987788608e666725031238f6e1f0a6 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/doxypypy

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-doxypypy/eb80802cb4987788608e666725031238f6e1f0a6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
