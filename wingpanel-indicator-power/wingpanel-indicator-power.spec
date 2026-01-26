%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global srcname panel-power
%global appname io.elementary.wingpanel.power

Name:           wingpanel-indicator-power
Summary:        Power indicator for wingpanel
Version:        8.0.2
Release:        %autorelease -b2
License:        GPL-2.0-or-later

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.57.0
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 6.0.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wingpanel) >= 3.0.0

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}

Recommends:     power-profiles-daemon

%description
A power indicator for wingpanel.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang power-indicator

# remove the specified stock icon from metainfo (invalid in libappstream-glib)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%files -f power-indicator.lang
%doc README.md
%license COPYING

%{_libdir}/wingpanel/libpower.so

%{_datadir}/glib-2.0/schemas/io.elementary.desktop.wingpanel.power.gschema.xml
%{_datadir}/metainfo/%{appname}.metainfo.xml


%changelog
%autochangelog
