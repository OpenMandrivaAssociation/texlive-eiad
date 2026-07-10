%global tl_name eiad
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Traditional style Irish fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/eiad
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eiad.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eiad.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
In both lower and upper case 32 letters are defined (18 'plain' ones, 5
long vowels and 9 aspirated consonants). The ligature 'agus' is also
made available. The remaining characters (digits, punctuation and
accents) are inherited from the Computer Modern family of fonts. The
font definitions use code from the sauter fonts, so those fonts have to
be installed before using eiad. OT1*.fd files are provided for use with
LaTeX.

