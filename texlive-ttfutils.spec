%global tl_name ttfutils
%global tl_revision 77830

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	convert TrueType to TFM and PK fonts
Group:		Publishing
URL:		https://www.ctan.org/pkg/ttfutils
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ttfutils.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ttfutils.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(ttfutils.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Utilities: ttf2afm ttf2pk ttf2tfm ttfdump. FreeType is the underlying
library.

