%global appname io.elementary.quick-settings
%global srcname quick-settings

Name:           wingpanel-quick-settings
Summary:        Access frequently used settings and system actions
Version:        1.4.0
Release:        %autorelease
License:        GPL-3.0-or-later AND GPL-2.0-or-later

URL:            https://github.com/elementary/%{srcname}
Source:         %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.32.1

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(gdk-wayland-3.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 6.0.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libhandy-1) >= 1.0
BuildRequires:  pkgconfig(packagekit-glib2)
BuildRequires:  pkgconfig(wingpanel)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(libportal)

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}

%description
%{summary}


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}

# remove the specified stock icon from appdata (invalid in libappstream-glib)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%files -f %{appname}.lang
%license LICENSE
%doc README.md

%{_libdir}/wingpanel/lib%{srcname}.so

%{_datadir}/glib-2.0/schemas/%{srcname}.gschema.xml
%{_datadir}/metainfo/%{appname}.metainfo.xml


%changelog
%autochangelog
