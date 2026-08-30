%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global srcname panel-keyboard
%global appname io.elementary.panel.keyboard

%global commit      a1c6bed89e9e7f5a94b4a0d877e42eb512871b1f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate     20260729

Name:           wingpanel-indicator-keyboard
Summary:        Keyboard Indicator for wingpanel
Version:        2.4.2^%{gitdate}.git%{shortcommit}
Release:        %autorelease
License:        LGPL-2.1-or-later AND GPL-2.0-or-later

URL:            https://github.com/elementary/%{name}
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(ibus-1.0) >= 1.5.19
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(wingpanel-9)
BuildRequires:  pkgconfig(xkeyboard-config)

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}


%description
A keyboard indicator for wingpanel.


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

%{_libdir}/wingpanel-9/libkeyboard.so

%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.metainfo.xml


%changelog
%autochangelog
