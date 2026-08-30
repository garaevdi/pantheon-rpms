%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global srcname panel-bluetooth
%global appname io.elementary.wingpanel.bluetooth

%global commit      e0fe999433f4ccc1a9133016a84155683703dd1f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate     20260912

Name:           wingpanel-indicator-bluetooth
Summary:        Bluetooth Indicator for wingpanel
Version:        8.0.0^%{gitdate}.git%{shortcommit}
Release:        %autorelease
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-2.1-or-later

URL:            https://github.com/elementary/%{name}
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(wingpanel-9)

Requires:       bluez
Requires:       wingpanel%{?_isa}

Supplements:    (wingpanel%{?_isa} and bluez)


%description
A bluetooth indicator for wingpanel.


%prep
%autosetup -n %{srcname}-%{commit} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang io.elementary.panel.bluetooth

# remove the specified stock icon from appdata (invalid in libappstream-glib)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%files -f io.elementary.panel.bluetooth.lang
%license COPYING
%doc README.md

%{_libdir}/wingpanel-9/libbluetooth.so

%{_datadir}/metainfo/%{appname}.metainfo.xml


%changelog
%autochangelog
