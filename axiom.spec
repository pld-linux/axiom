%define NO_REGRESSION_TEST 1

%define snap 20040509

Name:		axiom
Version:	3.%axiom_cvs_date
Release:	alt1
Summary:	Axiom Computer Algebra System
Summary(ru_RU.UTF-8):Система аналитических вычислений Axiom
License:	Modified BSD License
Group:		Applications/Science
Url:		http://savannah.nongnu.org/projects/axiom
Source0:	%{name}-cvs-%{snap}.tar.bz2
Source1:	%{name}
Source2:	gcl-2.6.2-%{name}.tar.gz
Patch1:		%{name}-no-test.patch
Patch2:		%{name}-external-gcl.patch
BuildRequires:	libreadline-devel libncurses-devel tcl-devel tk-devel libiberty-devel libbfd-devel-static xpm-devel XFree86-devel
BuildRequires:	tetex tetex-latex tetex-dvips texinfo lynx sed gawk coreutils diffutils

%description
Axiom is a general purpose Computer Algebra system. It is useful for
research and development of mathematical algorithms. It defines a
strongly typed, mathematically correct type hierarchy. It has a
programming language and a built-in compiler.

Axiom has been in development since 1973 and was sold as a commercial
product. It has been released as free software.

Efforts are underway to extend this software to (a) develop a better
user interface (b) make it useful as a teaching tool (c) develop an
algebra server protocol (d) integrate additional mathematics (e)
rebuild the algebra in a literate programming style (f) integrate
logic programming (g) develop an Axiom Journal with refereed
submissions.

%description -l ru_RU.UTF-8
Axiom является универсальной системой
аналитических вычислений и может
использоваться для научных
исследований и развития
математических алгоритмов. Axiom
является строго типизированной
системой с математически корректной
иерархией типов. Система имеет
собственный язык программирования и
встроенный компилятор.

Axiom развивается с 1973 года и ранее
распространялась как коммерческий
продукт. Сейчас система выпущена под
свободной програмной лицензией.

%package doc
Summary:	Axiom Book and other Documentaion
Summary (ru_RU.UTF-8):Книга и другая документация по Axiom
Group:		Applications/Science

%description doc
Axiom Book and other Documentaion.

%description doc -l ru_RU.UTF-8
Книга и другая документация по Axiom.

%prep
%setup -q -n %name

%if %NO_REGRESSION_TEST
%patch1 -p1
%endif

cp %SOURCE2 zips/gcl-2.6.2a.tgz

#%patch2 -p1

%build
export AXIOM=%_builddir/%name/mnt/linux
export PATH=$AXIOM/bin:$PATH

%{__make}
cd mnt/linux/doc
dvips -o book.ps book.dvi
dvips -o Rosetta.ps Rosetta.dvi
dvips -o DeveloperNotes.ps DeveloperNotes.dvi
cd ../../..

%install
rm -rf $RPM_BUILD_ROOT
install -d %buildroot%_bindir

%{__make} INSTALL=%buildroot%_libdir/%name COMMAND=%buildroot%_bindir/%name install

install -D -m755 %SOURCE1 %buildroot%_bindir/%name

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
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
%defattr(644,root,root,755)
%doc %_libdir/%name/mnt/linux/doc/*.ps
