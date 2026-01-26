%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname settings-power

%global plug_type hardware
%global plug_name power
%global plug_rdnn io.elementary.settings.power

Name:           switchboard-plug-power
Summary:        Switchboard Power plug
Version:        8.1.0
Release:        %autorelease -b2
License:        GPL-3.0-or-later

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(switchboard-3)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}

Recommends:     power-profiles-daemon

%description
This switchboard plug shows power settings.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{plug_rdnn}

# remove the specified stock icon from metainfo (invalid in libappstream-glib)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml


%files -f %{plug_rdnn}.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard-3/%{plug_type}/lib%{plug_name}.so
%{_libexecdir}/io.elementary.logind.helper

%{_datadir}/dbus-1/system-services/io.elementary.logind.helper.service
%{_datadir}/dbus-1/system.d/io.elementary.logind.helper.conf
%{_datadir}/polkit-1/actions/%{plug_rdnn}.policy
%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml


%changelog
%autochangelog
