%global srcname icons
%global appname io.elementary.icons

Name:           elementary-icon-theme
Summary:        Named, vector icons for elementary OS
Version:        9.0.0
Release:        %autorelease
License:        GPL-3.0-only

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  meson >= 0.61
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  librsvg2-tools
BuildRequires:  xcursorgen

BuildArch:      noarch

Requires:       hicolor-icon-theme

%description
%{summary}


%prep
%autosetup -n %{srcname}-%{version} -p1


%conf
%meson -Dvolume_icons=false


%build
%meson_build


%install
%meson_install


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_metainfodir}/%{appname}.metainfo.xml


%files
%license COPYING
%doc README.md

%{_datadir}/icons/elementary
%{_datadir}/gimp/2.0/palettes/elementary.gpl
%{_datadir}/inkscape/palettes/elementary.gpl
%{_datadir}/metainfo/%{appname}.metainfo.xml

%changelog
%autochangelog
