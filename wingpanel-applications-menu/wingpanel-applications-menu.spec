%global appname io.elementary.wingpanel.applications-menu
%global srcname applications-menu

%global __provides_exclude_from ^%{_libdir}/(wingpanel|%{appname})/.*\\.so$

%global commit      6729fcd2f8efa8688742221fb2fe9350d52ee946
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate     20260813

Name:           wingpanel-applications-menu
Summary:        Lightweight and stylish app launcher
Version:        8.0.4^%{gitdate}.git%{shortcommit}
Release:        %autorelease
# - GPL-3.0-or-later: applies to most applications-menu sources
# - GPL-2.0-or-later: applies to all files derived from the synapse launcher
License:        GPL-3.0-or-later AND GPL-2.0-or-later

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.32.1

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(switchboard-3)
BuildRequires:  pkgconfig(wingpanel-9)

Requires:       redhat-menus

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}

%description
The lightweight and stylish app launcher from elementary.


%prep
%autosetup -n applications-menu-%{commit} -p1


%build
%meson -Dwith-zeitgeist=false
%meson_build


%install
%meson_install

%find_lang slingshot

# remove the specified stock icon from appdata (invalid in libappstream-glib)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%files -f slingshot.lang
%license COPYING
%doc README.md

%{_libdir}/%{appname}/
%{_libdir}/wingpanel-9/libslingshot.so

%{_datadir}/glib-2.0/schemas/io.elementary.desktop.wingpanel.applications-menu.gschema.xml
%{_datadir}/metainfo/%{appname}.metainfo.xml


%changelog
%autochangelog
