# revision 23089
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-ttfutils
Version:	20111104
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXLive ttfutils package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
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
%{_texmfdir}/fonts/enc/ttf2pk/base/T1-WGL4.enc
%{_texmfdir}/ttf2pk/VPS.rpl
%{_texmfdir}/ttf2pk/ttf2pk.cfg
%doc %{_mandir}/man1/ttf2afm.1*
%doc %{_texmfdir}/doc/man/man1/ttf2afm.man1.pdf
%doc %{_mandir}/man1/ttf2pk.1*
%doc %{_texmfdir}/doc/man/man1/ttf2pk.man1.pdf
%doc %{_mandir}/man1/ttf2tfm.1*
%doc %{_texmfdir}/doc/man/man1/ttf2tfm.man1.pdf
%doc %{_mandir}/man1/ttfdump.1*
%doc %{_texmfdir}/doc/man/man1/ttfdump.man1.pdf
%doc %{_texmfdir}/doc/ttf2pk/ttf2pk.doc
%doc %{_texmfdir}/doc/ttf2pk/ttf2pk.txt
%doc %{_texmfdir}/doc/ttf2pk/ttf2tfm.txt
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
