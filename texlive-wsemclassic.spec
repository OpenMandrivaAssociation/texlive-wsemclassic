%global tl_name wsemclassic
%global tl_revision 31532

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.1
Release:	%{tl_revision}.1
Summary:	LaTeX class for Bavarian school w-seminar papers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/wsemclassic
License:	bsd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/wsemclassic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/wsemclassic.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/wsemclassic.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class is designed either to conform with the recommendations of the
Bavarian Kultusministerium for typesetting w-seminar papers (strict
mode), or to use another style which should look better. The class is
based on the LaTeX standard report class.

