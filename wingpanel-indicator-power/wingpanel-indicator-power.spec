%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global srcname panel-power
%global appname io.elementary.panel.power

%global commit      f8baf7a1d35d1a18a271dd752acbcbf23657ae8a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate     20260830

Name:           wingpanel-indicator-power
Summary:        Power indicator for wingpanel
Version:        8.0.2^%{gitdate}.git%{shortcommit}
Release:        %autorelease
License:        GPL-2.0-or-later

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

Patch0:         panel-power-gala-backlight-interface.patch

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.57.0
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wingpanel-9)

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}

Recommends:     power-profiles-daemon

%description
A power indicator for wingpanel.


%prep
%autosetup -n %{srcname}-%{commit} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}

# remove the specified stock icon from metainfo (invalid in libappstream-glib)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%files -f %{appname}.lang
%doc README.md
%license COPYING

%{_libdir}/wingpanel-9/libpower.so

%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.metainfo.xml


%changelog
%autochangelog
