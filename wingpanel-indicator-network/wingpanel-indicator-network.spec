%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global srcname panel-network
%global appname io.elementary.panel.network

%global commit      82cdad09cd8f19adbe0097f8c4de8b4bd8f6b4cd
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate     20260828

Name:           wingpanel-indicator-network
Summary:        Network Indicator for wingpanel
Version:        8.0.1^%{gitdate}.git%{shortcommit}
Release:        %autorelease
License:        LGPL-2.1-or-later AND GPL-3.0-or-later AND GPL-2.0-or-later

URL:            https://github.com/elementary/wingpanel-indicator-network
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libnm) >= 1.24
BuildRequires:  pkgconfig(libnma-gtk4)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(wingpanel-9)

Requires:       network-manager-applet%{?_isa}
Requires:       wingpanel%{?_isa}

Supplements:    wingpanel%{?_isa}


%description
A network indicator for wingpanel.


%prep
%autosetup -n %{srcname}-%{commit} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%files -f %{appname}.lang
%license COPYING
%doc README.md

%{_libdir}/wingpanel-9/libnetwork.so

%{_datadir}/metainfo/%{appname}.metainfo.xml
%{_datadir}/polkit-1/actions/%{appname}.policy


%changelog
%autochangelog
