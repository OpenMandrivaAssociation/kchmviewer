Name:		kchmviewer
Version:	5.2
Release:	%mkrel 1
Summary:	KDE chm viewer
License:	GPLv2+
URL:		http://kchmviewer.sourceforge.net/
Group:		Graphical desktop/KDE
Source:		http://downloads.sourceforge.net/kchmviewer/%{name}-%{version}.tar.gz
Patch0:		kchmviewer-5.2-fix-build.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	kdelibs4-devel
BuildRequires:	chmlib-devel
Requires:	okular

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

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%{_kde_bindir}/kchmviewer
%{_kde_datadir}/applications/kde4/kchmviewer.desktop
%exclude %{_kde_libdir}/kde4/kio_msits.so
%exclude %{_kde_datadir}/kde4/services/msits.protocol

#--------------------------------------------------------------------

%prep
%setup -q -n build-%{version}
%patch0 -p0

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%find_lang %{name}

%clean
rm -rf %{buildroot}
