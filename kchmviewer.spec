Name:		kchmviewer
Version:	6.0
Release:	%mkrel 1
Summary:	KDE chm viewer
License:	GPLv2+
URL:		http://kchmviewer.sourceforge.net/
Group:		Graphical desktop/KDE
Source:		http://downloads.sourceforge.net/kchmviewer/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(QtWebKit)
BuildRequires:	kdelibs4-devel
BuildRequires:	chmlib-devel
BuildRequires:	imagemagick
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

%files -f %{name}.lang
%{_kde_bindir}/kchmviewer
%{_kde_datadir}/applications/kde4/kchmviewer.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std -C build

%__rm -f %{buildroot}%{_kde_libdir}/kde4/kio_msits.so
%__rm -f %{buildroot}%{_kde_datadir}/kde4/services/msits.protocol
%__mkdir_p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48,64x64,128x128}/apps
%__install -m644 packages/%{name}.png %{buildroot}%{_iconsdir}/hicolor/128x128/apps/

for i in 16x16 32x32 48x48 64x64; do
    convert -scale $i packages/%{name}.png %{buildroot}%{_iconsdir}/hicolor/$i/apps/%{name}.png
done

%find_lang %{name}

%clean
%__rm -rf %{buildroot}

