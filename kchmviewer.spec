Name:		kchmviewer
Version:	6.0
Release:	2
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



%changelog
* Wed Mar 28 2012 Andrey Bondrov <abondrov@mandriva.org> 6.0-1mdv2012.0
+ Revision: 787927
- New version 6.0

* Fri Jan 14 2011 Funda Wang <fwang@mandriva.org> 5.3-1
+ Revision: 631063
- new version 5.3

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Thu Apr 29 2010 Funda Wang <fwang@mandriva.org> 5.2-1mdv2010.1
+ Revision: 540901
- New version 5.2

* Sat Feb 27 2010 Ahmad Samir <ahmadsamir@mandriva.org> 5.1-1mdv2010.1
+ Revision: 512197
- new release 5.1
- clean spec formatting

* Wed Dec 16 2009 Funda Wang <fwang@mandriva.org> 5.0-1mdv2010.1
+ Revision: 479496
- new version 5.0

* Mon Nov 09 2009 Funda Wang <fwang@mandriva.org> 4.2-1mdv2010.1
+ Revision: 463296
- new version 4.2

* Thu Jul 30 2009 Frederik Himpe <fhimpe@mandriva.org> 4.1-1mdv2010.0
+ Revision: 404728
- update to new version 4.1

* Tue Dec 02 2008 Funda Wang <fwang@mandriva.org> 4.0-1mdv2009.1
+ Revision: 308981
- 4.0 final
- requires okular for msits protocol

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Use KDE packaging layout
      Use %%exlude instead of rm -fr

* Wed Aug 13 2008 Funda Wang <fwang@mandriva.org> 4.0-0.beta3.2mdv2009.0
+ Revision: 271365
- fix conflicts with okular

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue Jun 10 2008 Funda Wang <fwang@mandriva.org> 4.0-0.beta3.1mdv2009.0
+ Revision: 217343
- New version 4.0beta3

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 3.1-4mdv2008.1
+ Revision: 170915
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Nov 05 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.1-3mdv2008.1
+ Revision: 106169
- Rebuild to fix bug #35325

* Thu Aug 30 2007 Helio Chissini de Castro <helio@mandriva.com> 3.1-3mdv2008.0
+ Revision: 75130
- Recompile against new library

* Sun Jun 17 2007 Helio Chissini de Castro <helio@mandriva.com> 3.1-2mdv2008.0
+ Revision: 40524
- Fix build for x86_64
- Remove invalid %%post and %%postun
- Remove wrong menu install
- Bring back .la file to enable proper load module

* Sun Jun 17 2007 Funda Wang <fwang@mandriva.org> 3.1-1mdv2008.0
+ Revision: 40499
- New version
- kill old menu

* Tue May 01 2007 Funda Wang <fwang@mandriva.org> 3.0-1mdv2008.0
+ Revision: 19881
- BuildRequires chmlib-devel
- use qt3 macros
- added missing locale fiiles.
- New upstream version 3.0


* Thu Dec 07 2006 Lenny Cartier <lenny@mandriva.com> 2.7-1mdv2007.0
+ Revision: 92104
- Update to 2.7
- Import kchmviewer

