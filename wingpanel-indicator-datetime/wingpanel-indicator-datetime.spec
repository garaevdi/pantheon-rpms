%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global srcname panel-datetime
%global appname io.elementary.panel.datetime

%global commit      32fb1d9b28e10475ba7ad41415c01fcdee385be4
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate     20260822

Name:           wingpanel-indicator-datetime
Summary:        Datetime Indicator for wingpanel
Version:        2.4.2^%{gitdate}.git%{shortcommit}
Release:        %autorelease
License:        GPL-3.0-or-later AND GPL-2.0-or-later

URL:            https://github.com/elementary/wingpanel-indicator-datetime
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libecal-2.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libical-glib)
BuildRequires:  pkgconfig(wingpanel-9)

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}


%description
A datetime indicator for wingpanel.


%prep
%autosetup -n %{srcname}-%{commit} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}

# remove the specified stock icon from appdata (invalid in libappstream-glib)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%files -f %{appname}.lang
%license COPYING
%doc README.md

%{_libdir}/wingpanel-9/libdatetime.so

%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.metainfo.xml


%changelog
%autochangelog
