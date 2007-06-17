%define name kchmviewer
%define version 3.1
%define release %mkrel 1
%define __libtoolize /bin/true
%define __cputoolize /bin/true

%define lib_name_orig %mklibname %name
%define lib_major 0
%define lib_name %lib_name_orig%lib_major

Name:      	%{name}
Version:   	%{version}
Release:   	%{release}
Summary: 	Kchmviewer is a new chm viewer for KDE
License: 	GPL
URL: 		http://kchmviewer.sourceforge.net/
Group: 		Development/KDE and Qt
Source: 	%name-%version-2.tar.gz
Patch1:		kchmviewer-3.1-desktop-file.patch
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	kdelibs-devel >= 3.2
BuildRequires:	chmlib-devel

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
		--with-qt-dir=%{qt3dir} \
		--with-qt-includes=%{qt3include} \
		--with-qt-libraries=%{qt3lib}
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/kde3/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/kde3/*.la

desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
	--vendor="" \
	$RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

%{find_lang} %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/kchmviewer
%{_libdir}/kde3/kio_msits.so
%{_datadir}/applications/kchmviewer.desktop
%{_datadir}/services/msits.protocol
%{_iconsdir}/crystalsvg/*/apps/*

%post
%{update_menus}
%{update_desktop_database}
%{update_icon_cache} crystalsvg

%postun
%{clean_menus}
%{clean_desktop_database}
%{clean_icon_cache} crystalsvg
