# revision 31532
# category Package
# catalog-ctan /macros/latex/contrib/wsemclassic
# catalog-date 2013-08-27 15:13:32 +0200
# catalog-license bsd
# catalog-version 1.0.1
Name:		texlive-wsemclassic
Version:	1.0.1
Release:	3
Summary:	LaTeX class for Bavarian school w-seminar papers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/wsemclassic
License:	BSD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wsemclassic.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wsemclassic.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wsemclassic.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class is designed either to conform with the
recommendations of the Bavarian Kultusministerium for
typesetting w-seminar papers (strict mode), or to use another
style which should look better. The class is based on the LaTeX
standard report class.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/wsemclassic/wsemclassic.cls
%doc %{_texmfdistdir}/doc/latex/wsemclassic/LICENSE
%doc %{_texmfdistdir}/doc/latex/wsemclassic/Makefile
%doc %{_texmfdistdir}/doc/latex/wsemclassic/README
%doc %{_texmfdistdir}/doc/latex/wsemclassic/test.bib
%doc %{_texmfdistdir}/doc/latex/wsemclassic/user-doc.tex
%doc %{_texmfdistdir}/doc/latex/wsemclassic/wsemclassic-test.pdf
%doc %{_texmfdistdir}/doc/latex/wsemclassic/wsemclassic-test.tex
%doc %{_texmfdistdir}/doc/latex/wsemclassic/wsemclassic.pdf
#- source
%doc %{_texmfdistdir}/source/latex/wsemclassic/wsemclassic.dtx
%doc %{_texmfdistdir}/source/latex/wsemclassic/wsemclassic.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
