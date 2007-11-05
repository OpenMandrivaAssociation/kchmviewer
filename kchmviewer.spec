%define name kchmviewer
%define version 3.1
%define release %mkrel 2
%define __libtoolize /bin/true
%define __cputoolize /bin/true

%define lib_name_orig %mklibname %name
%define lib_major 0
%define lib_name %lib_name_orig%lib_major

Name: kchmviewer
Version: 3.1
Release: %mkrel 3
Summary:	Kchmviewer is a KDE chm viewer
License:	GPL
URL: http://kchmviewer.sourceforge.net/
Group: Graphical desktop/KDE
Source: %name-%version-2.tar.gz
Patch1: kchmviewer-3.1-desktop-file.patch
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: kdelibs-devel >= 3.2
BuildRequires: kchm-devel

Requires(post):    desktop-file-utils
Requires(postun): desktop-file-utils

%description
KchmViewer is a chm (MS HTML help file format) viewer, written in C++. 
Unlike most existing CHM viewers for Unix, it uses Trolltech Qt widget 
library, and does not depend on KDE or Gnome. However, 
it may be compiled with full KDE support, including KDE widgets and KIO/KHTML.
The main advantage of KchmViewer is non-English language support. 
Unlike others, KchmViewer in most cases correctly detects help file encoding, 
correctly shows tables of context of Russian, Korean, Chinese and Japanese help
files, and correctly searches in non-English help files 
(search for MBCS languages - ja/ko/ch is still in progress).

%prep

%setup -q
%patch1 -p0

%build
%configure2_5x \
	--disable-rpath \
	--with-xinerama \
	--with-kde \
	%if "%{_lib}" != "lib"
	--enable-libsuffix="%(A=%{_lib}; echo ${A/lib/})" \
	%endif
	--disable-static

%make

%install
rm -rf %buildroot
%makeinstall_std

%find_lang %name

# Remove static ( there's a problem on buildsystem )
rm -f %buildroot%_libdir/*.a

%clean
rm -rf %buildroot

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/kchmviewer
%{_libdir}/kde3/*
%{_datadir}/applications/kchmviewer.desktop
%{_datadir}/services/msits.protocol
%{_iconsdir}/crystalsvg/*/apps/*

%post
%update_menus

%postun
%clean_menus

