%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname settings-network

%global plug_type network
%global plug_name network
%global plug_rdnn io.elementary.settings.network

Name:           switchboard-plug-network
Summary:        Switchboard Network plug
Version:        8.2.0
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
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libnma-gtk4)
BuildRequires:  pkgconfig(switchboard-3)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}
Suggests:       nm-connection-editor

%description
A switchboard plug to configure network settings.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{plug_rdnn}


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml


%files -f %{plug_rdnn}.lang
%license COPYING
%doc README.md

%{_libdir}/switchboard-3/%{plug_type}/lib%{plug_name}.so

%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml


%changelog
%autochangelog
