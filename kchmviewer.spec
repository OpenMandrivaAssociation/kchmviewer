%define         bin_ver  %(echo %{version} | sed -e 's/\\./_/')

Name:		kchmviewer
Version:	8.0
Release:	1
Summary:	KDE chm viewer
License:	GPLv2+
URL:		http://www.ulduzsoft.com/linux/kchmviewer/
Group:		Graphical desktop/KDE
Source:		https://github.com/gyunaev/kchmviewer/archive/refs/tags/RELEASE_%{bin_ver}.tar.gz
Patch1:		fix-no-webkit.patch
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5WebEngine)
BuildRequires:	pkgconfig(Qt5WebEngineWidgets)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	chmlib-devel
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(libzip)
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
%autosetup -p1 -n %{name}-RELEASE_%{bin_ver}

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

