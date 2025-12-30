%global srcname icons

Name:           elementary-icon-theme
Summary:        Named, vector icons for elementary OS
Version:        8.2.0
Release:        %autorelease
License:        GPL-3.0-only

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  meson >= 0.61
BuildRequires:  gettext
BuildRequires:  librsvg2-tools
BuildRequires:  xcursorgen

BuildArch:      noarch

Requires:       hicolor-icon-theme

%description
%{summary}


%prep
%autosetup -n %{srcname}-%{version}


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
