%define betaver beta3
%define rel 1

Name: kchmviewer
Version: 4.0
Release: %mkrel -c %betaver %rel
Summary: KDE chm viewer
License: GPLv2+
URL: http://kchmviewer.sourceforge.net/
Group: Graphical desktop/KDE
Source: %name-%version%betaver.tar.gz
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: kdelibs4-devel
BuildRequires: chmlib-devel

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
%setup -q -n %name-%version%betaver

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
cd build
%makeinstall_std
cd -

%find_lang %name

%clean
rm -rf %buildroot

%files -f %{name}.lang
%defattr(-,root,root)
%{_kde_bindir}/kchmviewer
%{_kde_libdir}/kio_msits.so
%{_kde_datadir}/applications/kde4/kchmviewer.desktop
%{_kde_datadir}/kde4/services/msits.protocol
%{_kde_iconsdir}/crystalsvg/*/apps/*

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

