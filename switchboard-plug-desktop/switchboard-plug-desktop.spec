%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname settings-desktop

%global plug_type personal
%global plug_name desktop
%global plug_rdnn io.elementary.settings.desktop

Name:           switchboard-plug-desktop
Summary:        Switchboard Pantheon Shell plug
Version:        8.2.1
Release:        %autorelease
License:        GPL-3.0

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gexiv2)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite-7) >= 7.7.0
BuildRequires:  pkgconfig(gtk4) >= 4.10
BuildRequires:  pkgconfig(switchboard-3)

Requires:       gala
Requires:       tumbler
Requires:       wingpanel

Requires:       switchboard%{?_isa}
Supplements:    (switchboard%{?_isa} and gala and wingpanel)

%description
The desktop plug is a section in Switchboard, the elementary System
Settings app, where users can configure the wallpaper, dock, and
hotcorners. In the future the desktop plug might also handle other
desktop settings such as the panel, app launcher, and window manager.


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
