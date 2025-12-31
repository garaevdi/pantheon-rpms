%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname settings-locale

%global plug_type personal
%global plug_name locale
%global plug_rdnn io.elementary.settings.locale

Name:           switchboard-plug-locale
Summary:        Switchboard locale plug
Version:        8.0.3
Release:        %autorelease
License:        GPL-3.0-or-later

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(switchboard-3)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}

%description
This switchboard plug locale settings.


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

%{_libdir}/switchboard-3/%{plug_type}/lib%{plug_rdnn}.so
%{_libdir}/switchboard-3/%{plug_type}/pantheon-locale/*

%{_datadir}/glib-2.0/schemas/%{plug_rdnn}.gschema.xml
%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml
%{_datadir}/polkit-1/actions/%{plug_rdnn}.policy


%changelog
%autochangelog
