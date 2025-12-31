%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname settings-bluetooth

%global plug_type network
%global plug_name bluetooth
%global plug_rdnn io.elementary.settings.bluetooth

Name:           switchboard-plug-bluetooth
Summary:        Switchboard Bluetooth plug
Version:        8.0.2
Release:        %autorelease
License:        GPL-3.0-or-later

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(switchboard-3)

Requires:       bluez
Requires:       switchboard%{?_isa}

Supplements:    (switchboard%{?_isa} and bluez)

%description
The Bluetooth plug is a section in the Switchboard (System Settings)
that allows the user to manage bluetooth settings and connected
devices.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{plug_rdnn}

# remove the specified stock icon from metainof (invalid in libappstream-glib)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml


%files -f %{plug_rdnn}.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard-3/%{plug_type}/lib%{plug_name}.so

%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml


%changelog
%autochangelog
