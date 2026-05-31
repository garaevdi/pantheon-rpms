%global srcname icons

%global commit      366f1963082be26d11da2a333cb21a6c9ea6d2b1
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate     20260530

Name:           elementary-icon-theme
Summary:        Named, vector icons for elementary OS
Version:        8.2.0^%{gitdate}.git%{shortcommit}
Release:        %autorelease
License:        GPL-3.0-only

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz
Patch0:         actions-gtk422.patch
Patch1:         apps-gtk422.patch
Patch2:         categories-gtk422.patch
Patch3:         devices-gtk422.patch
Patch4:         emblems-gtk422.patch
Patch5:         mimes-gtk422.patch

BuildRequires:  meson >= 0.61
BuildRequires:  gettext
BuildRequires:  librsvg2-tools
BuildRequires:  xcursorgen

BuildArch:      noarch

Requires:       hicolor-icon-theme

%description
%{summary}


%prep
%autosetup -n %{srcname}-%{commit} -p1


%build
%meson -Dvolume_icons=false
%meson_build


%install
%meson_install


%files
%license COPYING
%doc README.md

%{_datadir}/icons/elementary
%{_datadir}/gimp/2.0/palettes/elementary.gpl
%{_datadir}/inkscape/palettes/elementary.gpl
%{_datadir}/metainfo/io.elementary.icons.metainfo.xml

%changelog
%autochangelog
