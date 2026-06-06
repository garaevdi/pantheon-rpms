%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname settings-sharing

%global plug_type network
%global plug_name sharing
%global plug_rdnn io.elementary.settings.sharing

Name:           switchboard-plug-sharing
Summary:        Switchboard Sharing Plug
Version:        8.0.3
Release:        %autorelease -b2
License:        GPL-3.0-or-later

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk4) >= 4.10
BuildRequires:  pkgconfig(libadwaita-1) >= 1.4
BuildRequires:  pkgconfig(switchboard-3)

Requires:       rygel
Requires:       elementary-bluetooth-daemon
Requires:       switchboard%{?_isa}

Supplements:    (switchboard%{?_isa} and rygel)

%description
Configure the sharing of system services.


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

%{_libdir}/switchboard-3/%{plug_type}/lib%{plug_rdnn}.so

%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml


%changelog
%autochangelog
