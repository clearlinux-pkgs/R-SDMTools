#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-SDMTools
Version  : 1.1.221
Release  : 2
URL      : https://cran.r-project.org/src/contrib/SDMTools_1.1-221.tar.gz
Source0  : https://cran.r-project.org/src/contrib/SDMTools_1.1-221.tar.gz
Summary  : Species Distribution Modelling Tools: Tools for processing data
Group    : Development/Tools
License  : GPL-3.0
Requires: R-SDMTools-lib
Requires: R-R.utils
BuildRequires : R-R.utils
BuildRequires : clr-R-helpers

%description
outcomes of species distribution modeling exercises. It includes novel
    methods for comparing models and tracking changes in distributions through
    time. It further includes methods for visualizing outcomes, selecting
    thresholds, calculating measures of accuracy and landscape fragmentation
    statistics, etc.. This package was made possible in part by financial
    support from the Australian Research Council & ARC Research Network for
    Earth System Science.

%package lib
Summary: lib components for the R-SDMTools package.
Group: Libraries

%description lib
lib components for the R-SDMTools package.


%prep
%setup -q -c -n SDMTools

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521242771

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521242771
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library SDMTools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library SDMTools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library SDMTools
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library SDMTools|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/SDMTools/DESCRIPTION
/usr/lib64/R/library/SDMTools/INDEX
/usr/lib64/R/library/SDMTools/Meta/Rd.rds
/usr/lib64/R/library/SDMTools/Meta/features.rds
/usr/lib64/R/library/SDMTools/Meta/hsearch.rds
/usr/lib64/R/library/SDMTools/Meta/links.rds
/usr/lib64/R/library/SDMTools/Meta/nsInfo.rds
/usr/lib64/R/library/SDMTools/Meta/package.rds
/usr/lib64/R/library/SDMTools/NAMESPACE
/usr/lib64/R/library/SDMTools/R/SDMTools
/usr/lib64/R/library/SDMTools/R/SDMTools.rdb
/usr/lib64/R/library/SDMTools/R/SDMTools.rdx
/usr/lib64/R/library/SDMTools/help/AnIndex
/usr/lib64/R/library/SDMTools/help/SDMTools.rdb
/usr/lib64/R/library/SDMTools/help/SDMTools.rdx
/usr/lib64/R/library/SDMTools/help/aliases.rds
/usr/lib64/R/library/SDMTools/help/paths.rds
/usr/lib64/R/library/SDMTools/html/00Index.html
/usr/lib64/R/library/SDMTools/html/R.css
/usr/lib64/R/library/SDMTools/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/SDMTools/libs/SDMTools.so
/usr/lib64/R/library/SDMTools/libs/SDMTools.so.avx2
/usr/lib64/R/library/SDMTools/libs/SDMTools.so.avx512
