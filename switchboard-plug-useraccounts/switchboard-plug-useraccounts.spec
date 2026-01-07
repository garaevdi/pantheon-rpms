%global __provides_exclude_from ^%{_libdir}/switchboard-3/.*\\.so$
%global debug_package %{nil}

%global srcname settings-useraccounts

%global plug_type system
%global plug_name useraccounts
%global plug_rdnn io.elementary.settings.useraccounts

Name:           switchboard-plug-useraccounts
Summary:        Switchboard User Accounts Plug
Version:        8.0.1
Release:        %autorelease
License:        LGPL-3.0-or-later

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pkgconfig(granite-7) >= 7.4.0
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  pkgconfig(switchboard-3)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}

%description
This switchboard plug allows to manipulate users


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
%{_libdir}/switchboard-3/%{plug_type}/%{plug_name}/guest-session-toggle

%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml
%{_datadir}/polkit-1/actions/%{plug_rdnn}.policy


%changelog
%autochangelog
