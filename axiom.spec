#
# Conditional build:
%bcond_with	tests	# perform regression test
#
%define snap 20040509
Summary:	Axiom Computer Algebra System
Summary(pl):	System algebry komputerowej Axiom
Summary(ru_RU.UTF-8):	Система аналитических вычислений Axiom
Name:		axiom
Version:	3.%{snap}
Release:	1
License:	Modified BSD License
Group:		Applications/Science
Source0:	%{name}-cvs-%{snap}.tar.bz2
Source1:	%{name}
Source2:	gcl-2.6.2-%{name}.tar.gz
Patch1:		%{name}-no-test.patch
Patch2:		%{name}-external-gcl.patch
URL:		http://savannah.nongnu.org/projects/axiom/
BuildRequires:	XFree86-devel
BuildRequires:	gawk
BuildRequires:	lynx
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	tcl-devel
BuildRequires:	tetex
BuildRequires:	tetex-dvips
BuildRequires:	tetex-latex
BuildRequires:	texinfo
BuildRequires:	tk-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl
Axiom to system algebry komputerowej og�lnego przeznaczenia. Jest
przydatny przy badaniach i rozwoju algorytm�w matematycznych.
Definiuje silnie typowan�, poprawn� matematycznie hierarchi� typ�w. Ma
j�zyk programowania i wbudowany kompilator.

Axiom jest rozwijany od 1973 i by� sprzedawany jako produkt
komercyjny. Zosta� wypuszczony jako darmowe oprogramowanie.

S� czynione starania rozszerzenia tego oprogramowania, aby: stworzy�
lepszy interfejs u�ytkownika, uczyni� je przydatne jako narz�dzie do
nauczania, stworzy� protok� serwera algebry, zintegrowa� dodatkow�
matematyk�, przebudowa� algebr� w czytelnym stylu programowania,
zintegrowa� programowanie logiczne, stworzy� Axiom Journal.

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
Summary:	Axiom Book and other documentaion
Summary(pl):	Axiom Book i inna dokumentacja
Summary(ru_RU.UTF-8):	Книга и другая документация по Axiom
Group:		Applications/Science

%description doc
Axiom Book and other Documentaion.

%description doc -l pl
Axiom Book i inna dokumentacja.

%description doc -l ru_RU.UTF-8
Книга и другая документация по Axiom.

%prep
%setup -q -n %{name}
%if !%{with tests}
%patch1 -p1
%endif

cp %{SOURCE2} zips/gcl-2.6.2a.tgz

#%patch2 -p1

%build
export AXIOM=%{_builddir}/%{name}/mnt/linux
export PATH=$AXIOM/bin:$PATH

%{__make}
cd mnt/linux/doc
dvips -o book.ps book.dvi
dvips -o Rosetta.ps Rosetta.dvi
dvips -o DeveloperNotes.ps DeveloperNotes.dvi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	INSTALL=$RPM_BUILD_ROOT%{_libdir}/%{name} \
	COMMAND=$RPM_BUILD_ROOT%{_bindir}/%{name}

install -D -m755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%dir%{_libdir}/%{name}
%dir%{_libdir}/%{name}/mnt
%dir%{_libdir}/%{name}/mnt/linux
%{_libdir}/%{name}/mnt/linux/algebra
%{_libdir}/%{name}/mnt/linux/autoload
%{_libdir}/%{name}/mnt/linux/bin
%{_libdir}/%{name}/mnt/linux/input
%{_libdir}/%{name}/mnt/linux/lib
%{_libdir}/%{name}/mnt/linux/src
%{_libdir}/%{name}/mnt/linux/timestamp
%dir%{_libdir}/%{name}/mnt/linux/doc
%{_libdir}/%{name}/mnt/linux/doc/hypertex
%{_libdir}/%{name}/mnt/linux/doc/msgs

%files doc
%defattr(644,root,root,755)
%doc %{_libdir}/%{name}/mnt/linux/doc/*.ps
