%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global srcname panel-nightlight
%global appname io.elementary.panel.nightlight

%global commit      bcf0b10f1692daa11e2b327e55aeb2d7aa1cbaca
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate     20260901

Name:           wingpanel-indicator-nightlight
Summary:        Night Light Indicator for wingpanel
Version:        2.1.3^%{gitdate}.git%{shortcommit}
Release:        %autorelease
License:        GPL-2.0-or-later

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(wingpanel-9)

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}


%description
A wingpanel indicator for Night Light.


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

%{_libdir}/wingpanel-9/libnightlight.so

%{_datadir}/metainfo/%{appname}.metainfo.xml


%changelog
%autochangelog
