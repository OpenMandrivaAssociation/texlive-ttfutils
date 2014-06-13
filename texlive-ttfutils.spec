# revision 31355
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-ttfutils
Version:	20131009
Release:	6
Summary:	TeXLive ttfutils package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ttfutils.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ttfutils.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-ttfutils.bin

%description
TeXLive ttfutils package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/ttf2pk/base/T1-WGL4.enc
%{_texmfdistdir}/fonts/sfd/ttf2pk/Big5.sfd
%{_texmfdistdir}/fonts/sfd/ttf2pk/EUC.sfd
%{_texmfdistdir}/fonts/sfd/ttf2pk/HKSCS.sfd
%{_texmfdistdir}/fonts/sfd/ttf2pk/KS-HLaTeX.sfd
%{_texmfdistdir}/fonts/sfd/ttf2pk/SJIS.sfd
%{_texmfdistdir}/fonts/sfd/ttf2pk/UBg5plus.sfd
%{_texmfdistdir}/fonts/sfd/ttf2pk/UBig5.sfd
%{_texmfdistdir}/fonts/sfd/ttf2pk/UGB.sfd
%{_texmfdistdir}/fonts/sfd/ttf2pk/UGBK.sfd
%{_texmfdistdir}/fonts/sfd/ttf2pk/UJIS.sfd
%{_texmfdistdir}/fonts/sfd/ttf2pk/UKS-HLaTeX.sfd
%{_texmfdistdir}/fonts/sfd/ttf2pk/UKS.sfd
%{_texmfdistdir}/fonts/sfd/ttf2pk/Unicode.sfd
%{_texmfdistdir}/ttf2pk/VPS.rpl
%{_texmfdistdir}/ttf2pk/ttf2pk.cfg
%doc %{_mandir}/man1/ttf2afm.1*
%doc %{_texmfdistdir}/doc/man/man1/ttf2afm.man1.pdf
%doc %{_mandir}/man1/ttf2pk.1*
%doc %{_texmfdistdir}/doc/man/man1/ttf2pk.man1.pdf
%doc %{_mandir}/man1/ttf2tfm.1*
%doc %{_texmfdistdir}/doc/man/man1/ttf2tfm.man1.pdf
%doc %{_mandir}/man1/ttfdump.1*
%doc %{_texmfdistdir}/doc/man/man1/ttfdump.man1.pdf
%doc %{_texmfdistdir}/doc/ttf2pk/ttf2pk.doc
%doc %{_texmfdistdir}/doc/ttf2pk/ttf2pk.txt
%doc %{_texmfdistdir}/doc/ttf2pk/ttf2tfm.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
