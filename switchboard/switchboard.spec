%global srcname settings
%global appname io.elementary.settings

Name:           switchboard
Version:        8.0.3
Release:        %autorelease
Summary:        Modular Desktop Settings Hub
# - LGPL-2.1-or-later: everything except src/Widgets/*.vala
# - GPL-2.0-or-later: src/Widgets/*.vala
License:        LGPL-2.1-or-later and GPL-2.0-or-later

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  sassc

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.76
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.4

Requires:       hicolor-icon-theme

%description
Extensible System Settings application.


%package        devel
Summary:        Modular Desktop Settings Hub (development files)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Extensible System Settings application.

This package contains the files required for developing plugs for
switchboard.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}

# create plug directories
mkdir -p %{buildroot}/%{_libdir}/%{name}-3

mkdir -p %{buildroot}/%{_libdir}/%{name}-3/hardware
mkdir -p %{buildroot}/%{_libdir}/%{name}-3/network
mkdir -p %{buildroot}/%{_libdir}/%{name}-3/personal
mkdir -p %{buildroot}/%{_libdir}/%{name}-3/system


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%license COPYING
%doc README.md

%{_bindir}/%{appname}

%dir %{_libdir}/%{name}-3
%dir %{_libdir}/%{name}-3/*

%{_libdir}/libswitchboard-3.so.0
%{_libdir}/libswitchboard-3.so.2.0

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/dbus-1/services/%{appname}.service
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.appdata.xml

%files devel
%{_includedir}/switchboard-3/

%{_libdir}/libswitchboard-3.so
%{_libdir}/pkgconfig/switchboard-3.pc

%{_datadir}/vala/vapi/switchboard-3.deps
%{_datadir}/vala/vapi/switchboard-3.vapi


%changelog
%autochangelog
