Name:		kchmviewer
Version:	7.7
Release:	1
Summary:	KDE chm viewer
License:	GPLv2+
URL:		http://kchmviewer.sourceforge.net/
Group:		Graphical desktop/KDE
Source:		http://downloads.sourceforge.net/kchmviewer/%{name}-%{version}.tar.gz
Patch1:		fix-qt5-build.patch
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5WebKit)
BuildRequires:	pkgconfig(Qt5WebKitWidgets) pkgconfig(Qt5Core) pkgconfig(Qt5DBus) pkgconfig(Qt5Gui) pkgconfig(Qt5Network) pkgconfig(Qt5PrintSupport) pkgconfig(Qt5Widgets) pkgconfig(Qt5Xml)
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

%files 
#-f %{name}.lang
%{_bindir}/kchmviewer
%{_datadir}/applications/kchmviewer.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

#--------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%qmake_qt5
%make

%install
#makeinstall_std
make DESTDIR=%{buildroot} install

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48,64x64,128x128}/apps
install -m644 packages/%{name}.png %{buildroot}%{_iconsdir}/hicolor/128x128/apps/

for i in 16x16 32x32 48x48 64x64; do
    convert -scale $i packages/%{name}.png %{buildroot}%{_iconsdir}/hicolor/$i/apps/%{name}.png
done

install -Dm755 bin/%{name} %{buildroot}%{_bindir}/%{name}
#icon/desktop file
install -Dm644 packages/%{name}.desktop %{buildroot}/%{_datadir}/applications/%{name}.desktop

#find_lang %{name}

