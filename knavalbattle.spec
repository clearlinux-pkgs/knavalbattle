#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : knavalbattle
Version  : 19.12.2
Release  : 16
URL      : https://download.kde.org/stable/release-service/19.12.2/src/knavalbattle-19.12.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/19.12.2/src/knavalbattle-19.12.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/19.12.2/src/knavalbattle-19.12.2.tar.xz.sig
Summary  : A ship sinking game
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: knavalbattle-bin = %{version}-%{release}
Requires: knavalbattle-data = %{version}-%{release}
Requires: knavalbattle-license = %{version}-%{release}
Requires: knavalbattle-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kdnssd-dev
BuildRequires : libkdegames-dev
BuildRequires : qtbase-dev mesa-dev

%description
EXTENDED

%package bin
Summary: bin components for the knavalbattle package.
Group: Binaries
Requires: knavalbattle-data = %{version}-%{release}
Requires: knavalbattle-license = %{version}-%{release}

%description bin
bin components for the knavalbattle package.


%package data
Summary: data components for the knavalbattle package.
Group: Data

%description data
data components for the knavalbattle package.


%package doc
Summary: doc components for the knavalbattle package.
Group: Documentation

%description doc
doc components for the knavalbattle package.


%package license
Summary: license components for the knavalbattle package.
Group: Default

%description license
license components for the knavalbattle package.


%package locales
Summary: locales components for the knavalbattle package.
Group: Default

%description locales
locales components for the knavalbattle package.


%prep
%setup -q -n knavalbattle-19.12.2
cd %{_builddir}/knavalbattle-19.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1581027247
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1581027247
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/knavalbattle
cp %{_builddir}/knavalbattle-19.12.2/COPYING %{buildroot}/usr/share/package-licenses/knavalbattle/fafaf6b2753f82aa8df1d206d6b76c2241c2dfa8
cp %{_builddir}/knavalbattle-19.12.2/COPYING.DOC %{buildroot}/usr/share/package-licenses/knavalbattle/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
pushd clr-build
%make_install
popd
%find_lang knavalbattle

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/knavalbattle

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.knavalbattle.desktop
/usr/share/icons/hicolor/128x128/apps/knavalbattle.png
/usr/share/icons/hicolor/16x16/apps/knavalbattle.png
/usr/share/icons/hicolor/22x22/apps/knavalbattle.png
/usr/share/icons/hicolor/32x32/apps/knavalbattle.png
/usr/share/icons/hicolor/48x48/apps/knavalbattle.png
/usr/share/icons/hicolor/64x64/apps/knavalbattle.png
/usr/share/kconf_update/knavalbattle.upd
/usr/share/knavalbattle/pictures/default.desktop
/usr/share/knavalbattle/pictures/default_theme.svgz
/usr/share/knavalbattle/sounds/ship-player-shoot-water.ogg
/usr/share/knavalbattle/sounds/ship-player1-shoot.ogg
/usr/share/knavalbattle/sounds/ship-player2-shoot.ogg
/usr/share/knavalbattle/sounds/ship-sink.ogg
/usr/share/kservices5/knavalbattle.protocol
/usr/share/kxmlgui5/knavalbattle/knavalbattleui.rc
/usr/share/metainfo/org.kde.knavalbattle.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/de/knavalbattle/index.cache.bz2
/usr/share/doc/HTML/de/knavalbattle/index.docbook
/usr/share/doc/HTML/en/knavalbattle/gameboard.png
/usr/share/doc/HTML/en/knavalbattle/index.cache.bz2
/usr/share/doc/HTML/en/knavalbattle/index.docbook
/usr/share/doc/HTML/es/knavalbattle/index.cache.bz2
/usr/share/doc/HTML/es/knavalbattle/index.docbook
/usr/share/doc/HTML/et/knavalbattle/index.cache.bz2
/usr/share/doc/HTML/et/knavalbattle/index.docbook
/usr/share/doc/HTML/fr/knavalbattle/index.cache.bz2
/usr/share/doc/HTML/fr/knavalbattle/index.docbook
/usr/share/doc/HTML/gl/knavalbattle/index.cache.bz2
/usr/share/doc/HTML/gl/knavalbattle/index.docbook
/usr/share/doc/HTML/it/knavalbattle/index.cache.bz2
/usr/share/doc/HTML/it/knavalbattle/index.docbook
/usr/share/doc/HTML/nl/knavalbattle/index.cache.bz2
/usr/share/doc/HTML/nl/knavalbattle/index.docbook
/usr/share/doc/HTML/pl/knavalbattle/index.cache.bz2
/usr/share/doc/HTML/pl/knavalbattle/index.docbook
/usr/share/doc/HTML/pt/knavalbattle/index.cache.bz2
/usr/share/doc/HTML/pt/knavalbattle/index.docbook
/usr/share/doc/HTML/pt_BR/knavalbattle/index.cache.bz2
/usr/share/doc/HTML/pt_BR/knavalbattle/index.docbook
/usr/share/doc/HTML/ru/knavalbattle/index.cache.bz2
/usr/share/doc/HTML/ru/knavalbattle/index.docbook
/usr/share/doc/HTML/sv/knavalbattle/index.cache.bz2
/usr/share/doc/HTML/sv/knavalbattle/index.docbook
/usr/share/doc/HTML/uk/knavalbattle/gameboard.png
/usr/share/doc/HTML/uk/knavalbattle/index.cache.bz2
/usr/share/doc/HTML/uk/knavalbattle/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/knavalbattle/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
/usr/share/package-licenses/knavalbattle/fafaf6b2753f82aa8df1d206d6b76c2241c2dfa8

%files locales -f knavalbattle.lang
%defattr(-,root,root,-)

