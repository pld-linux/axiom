%define NO_REGRESSION_TEST 1

%define axiom_cvs_date 20040509

Name: axiom
Version: 3.%axiom_cvs_date
Release: alt1
Summary: Axiom Computer Algebra System
Summary (ru_RU.UTF-8): Система аналитических вычислений Axiom
License: Modified BSD License
Group: Sciences/Mathematics
Url: http://savannah.nongnu.org/projects/axiom
Packager: Vadim V. Zhytnikov <vvzhy@altlinux.ru>

Source0: axiom-cvs-%axiom_cvs_date.tar.bz2
Source1: axiom
Source2: gcl-2.6.2-axiom.tar.gz

Patch1: axiom-no-test.patch
Patch2: axiom-external-gcl.patch

BuildRequires: libreadline-devel libncurses-devel tcl-devel tk-devel libiberty-devel libbfd-devel-static xpm-devel XFree86-devel
BuildRequires: tetex tetex-latex tetex-dvips texinfo lynx sed gawk coreutils diffutils

%description
Axiom is a general purpose Computer Algebra system. It is useful for
research and development of mathematical algorithms. It defines a 
strongly typed, mathematically correct type hierarchy. It has a 
programming language and a built-in compiler. 
 
Axiom has been in development since 1973 and was sold as a 
commercial product. It has been released as free software. 
 
Efforts are underway to extend this software to (a) develop a 
better user interface (b) make it useful as a teaching tool 
(c) develop an algebra server protocol (d) integrate additional 
mathematics (e) rebuild the algebra in a literate programming style 
(f) integrate logic programming (g) develop an Axiom Journal with 
refereed submissions.

%description -l ru_RU.UTF-8
Axiom является универсальной системой аналитических вычислений
и может использоваться для научных исследований и развития
математических алгоритмов.  Axiom является строго типизированной
системой с математически корректной иерархией типов.  Система 
имеет собственный язык программирования и встроенный компилятор.

Axiom развивается с 1973 года и ранее распространялась как 
коммерческий продукт.  Сейчас система выпущена под свободной
програмной лицензией.

%package doc
Summary: Axiom Book and other Documentaion
Summary (ru_RU.UTF-8): Книга и другая документация по Axiom
Group: Sciences/Mathematics

%description doc
Axiom Book and other Documentaion.

%description doc -l ru_RU.UTF-8
Книга и другая документация по Axiom.

%prep 
%setup -q -n%name

%if %NO_REGRESSION_TEST
%patch1 -p1
%endif

cp %SOURCE2 zips/gcl-2.6.2a.tgz

#%patch2 -p1


%build

export AXIOM=%_builddir/%name/mnt/linux
export PATH=$AXIOM/bin:$PATH

make
cd mnt/linux/doc
dvips -o book.ps book.dvi
dvips -o Rosetta.ps Rosetta.dvi
dvips -o DeveloperNotes.ps DeveloperNotes.dvi
cd ../../..

%install

install -d %buildroot%_bindir

make INSTALL=%buildroot%_libdir/%name COMMAND=%buildroot%_bindir/%name install

install -D -m755 %SOURCE1 %buildroot%_bindir/%name


%files
%_bindir/%name
%_libdir/%name/mnt/linux/algebra
%_libdir/%name/mnt/linux/autoload
%_libdir/%name/mnt/linux/bin
%_libdir/%name/mnt/linux/input
%_libdir/%name/mnt/linux/lib
%_libdir/%name/mnt/linux/src
%_libdir/%name/mnt/linux/timestamp
%_libdir/%name/mnt/linux/doc/hypertex
%_libdir/%name/mnt/linux/doc/msgs

%files doc
%doc %_libdir/%name/mnt/linux/doc/*.ps


%changelog
* Sun May 09 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 3.20040509-alt1
- Axiom book.

* Tue Apr 13 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 3.20040228-alt3
- New GCL 2.6.2 CVS 13.04.2003 pre release - 25% buld speed-up.

* Mon Mar 01 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 3.20040228-alt2
- BuildRequires fix. 

* Sat Feb 28 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 3.20040228-alt1
- Build with our own GCL 2.6.2 pre release (not external GCL yet).

* Fri Dec 19 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 3.0-alt0.03
- Build option to disable regression test.

* Thu Dec 11 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 3.0-alt0.02
- Fix spadroot path problem (export AXIOM=/usr/lib/axiom/mnt/linux).

* Sun Nov 30 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 3.0-alt0.01
- Initial ALT Linux release.
