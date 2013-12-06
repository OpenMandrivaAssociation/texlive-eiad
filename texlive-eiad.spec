# revision 15878
# category Package
# catalog-ctan /fonts/eiad
# catalog-date 2008-12-05 21:50:47 +0100
# catalog-license noinfo
# catalog-version undef
Name:		texlive-eiad
Version:	20081205
Release:	4
Summary:	Traditional style Irish fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/eiad
License:	NOINFO
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eiad.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eiad.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
In both lower and upper case 32 letters are defined (18 'plain'
ones, 5 long vowels and 9 aspirated consonants). The ligature
'agus' is also made available. The remaining characters
(digits, punctuation and accents) are inherited from the
Computer Modern family of fonts. The font definitions use code
from the sauter fonts, so those fonts have to be installed
before using eiad. OT1*.fd files are provided for use with
LaTeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/eiad/eiadb10.mf
%{_texmfdistdir}/fonts/source/public/eiad/eiadbx10.mf
%{_texmfdistdir}/fonts/source/public/eiad/eiadbxi10.mf
%{_texmfdistdir}/fonts/source/public/eiad/eiadbxsl10.mf
%{_texmfdistdir}/fonts/source/public/eiad/eiadccsc10.mf
%{_texmfdistdir}/fonts/source/public/eiad/eiadci10.mf
%{_texmfdistdir}/fonts/source/public/eiad/eiadcr10.mf
%{_texmfdistdir}/fonts/source/public/eiad/eiadcsc10.mf
%{_texmfdistdir}/fonts/source/public/eiad/eiadcsl10.mf
%{_texmfdistdir}/fonts/source/public/eiad/eiadcslc9.mf
%{_texmfdistdir}/fonts/source/public/eiad/eiaddunh10.mf
%{_texmfdistdir}/fonts/source/public/eiad/eiadff10.mf
%{_texmfdistdir}/fonts/source/public/eiad/eiadfi10.mf
%{_texmfdistdir}/fonts/source/public/eiad/eiadfib8.mf
%{_texmfdistdir}/fonts/source/public/eiad/eiadi10.mf
%{_texmfdistdir}/fonts/source/public/eiad/eiaditt10.mf
%{_texmfdistdir}/fonts/source/public/eiad/eiadr10.mf
%{_texmfdistdir}/fonts/source/public/eiad/eiadr12.mf
%{_texmfdistdir}/fonts/source/public/eiad/eiadr17.mf
%{_texmfdistdir}/fonts/source/public/eiad/eiadsl10.mf
%{_texmfdistdir}/fonts/source/public/eiad/eiadsltt10.mf
%{_texmfdistdir}/fonts/source/public/eiad/eiadss10.mf
%{_texmfdistdir}/fonts/source/public/eiad/eiadssbx10.mf
%{_texmfdistdir}/fonts/source/public/eiad/eiadssdc10.mf
%{_texmfdistdir}/fonts/source/public/eiad/eiadssi10.mf
%{_texmfdistdir}/fonts/source/public/eiad/eiadssq8.mf
%{_texmfdistdir}/fonts/source/public/eiad/eiadssqi8.mf
%{_texmfdistdir}/fonts/source/public/eiad/eiadtcsc10.mf
%{_texmfdistdir}/fonts/source/public/eiad/eiadtt10.mf
%{_texmfdistdir}/fonts/source/public/eiad/eiadvtt10.mf
%{_texmfdistdir}/fonts/source/public/eiad/eira.mf
%{_texmfdistdir}/fonts/source/public/eiad/eirl.mf
%{_texmfdistdir}/fonts/source/public/eiad/eiru.mf
%{_texmfdistdir}/fonts/source/public/eiad/gaec7cb.mf
%{_texmfdistdir}/fonts/source/public/eiad/gaelach.mf
%{_texmfdistdir}/fonts/tfm/public/eiad/eiadb10.tfm
%{_texmfdistdir}/fonts/tfm/public/eiad/eiadbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/eiad/eiadbxi10.tfm
%{_texmfdistdir}/fonts/tfm/public/eiad/eiadbxsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/eiad/eiadccsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/eiad/eiadci10.tfm
%{_texmfdistdir}/fonts/tfm/public/eiad/eiadcr10.tfm
%{_texmfdistdir}/fonts/tfm/public/eiad/eiadcsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/eiad/eiadcsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/eiad/eiadcslc9.tfm
%{_texmfdistdir}/fonts/tfm/public/eiad/eiaddunh10.tfm
%{_texmfdistdir}/fonts/tfm/public/eiad/eiadff10.tfm
%{_texmfdistdir}/fonts/tfm/public/eiad/eiadfi10.tfm
%{_texmfdistdir}/fonts/tfm/public/eiad/eiadfib8.tfm
%{_texmfdistdir}/fonts/tfm/public/eiad/eiadi10.tfm
%{_texmfdistdir}/fonts/tfm/public/eiad/eiaditt10.tfm
%{_texmfdistdir}/fonts/tfm/public/eiad/eiadr10.tfm
%{_texmfdistdir}/fonts/tfm/public/eiad/eiadr12.tfm
%{_texmfdistdir}/fonts/tfm/public/eiad/eiadr17.tfm
%{_texmfdistdir}/fonts/tfm/public/eiad/eiadsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/eiad/eiadsltt10.tfm
%{_texmfdistdir}/fonts/tfm/public/eiad/eiadss10.tfm
%{_texmfdistdir}/fonts/tfm/public/eiad/eiadssbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/eiad/eiadssdc10.tfm
%{_texmfdistdir}/fonts/tfm/public/eiad/eiadssi10.tfm
%{_texmfdistdir}/fonts/tfm/public/eiad/eiadssq8.tfm
%{_texmfdistdir}/fonts/tfm/public/eiad/eiadssqi8.tfm
%{_texmfdistdir}/fonts/tfm/public/eiad/eiadtcsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/eiad/eiadtt10.tfm
%{_texmfdistdir}/fonts/tfm/public/eiad/eiadvtt10.tfm
%{_texmfdistdir}/tex/latex/eiad/OT1eiad.fd
%{_texmfdistdir}/tex/latex/eiad/OT1eiadcc.fd
%{_texmfdistdir}/tex/latex/eiad/OT1eiadss.fd
%{_texmfdistdir}/tex/latex/eiad/OT1eiadtt.fd
%doc %{_texmfdistdir}/doc/fonts/eiad/Leigh_me.txt
%doc %{_texmfdistdir}/doc/fonts/eiad/amhrawn.pdf
%doc %{_texmfdistdir}/doc/fonts/eiad/amhrawn.tex
%doc %{_texmfdistdir}/doc/fonts/eiad/evening.pdf
%doc %{_texmfdistdir}/doc/fonts/eiad/evening.tex
%doc %{_texmfdistdir}/doc/fonts/eiad/micheal.ps
%doc %{_texmfdistdir}/doc/fonts/eiad/micheal.tex
%doc %{_texmfdistdir}/doc/fonts/eiad/recreat.pdf
%doc %{_texmfdistdir}/doc/fonts/eiad/recreat.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20081205-2
+ Revision: 751369
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20081205-1
+ Revision: 718314
- texlive-eiad
- texlive-eiad
- texlive-eiad
- texlive-eiad

