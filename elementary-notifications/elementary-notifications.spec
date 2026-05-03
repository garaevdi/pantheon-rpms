%global srcname notifications
%global appname io.elementary.notifications

Name:           elementary-notifications
Version:        8.1.2
Release:        %autorelease
Summary:        GTK Notifications Server
License:        GPL-3.0-or-later

URL:            https://github.com/elementary/notifications
Source:         %{url}/archive/%{version}/notifications-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(granite-7) >= 7.7.0
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtk4-wayland)
BuildRequires:  pkgconfig(gtk4-x11)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner)

%description
elementary Notifications is a GTK notification server for Pantheon.

%package demo
Summary:        GTK Notifications Server (demo application)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description demo
elementary Notifications is a GTK notification server for Pantheon.

This package contains a demo application.


%prep
%autosetup -n notifications-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

# remove the specified stock icon from appdata (invalid for desktop components)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%files
%license LICENSE
%doc README.md

%{_bindir}/%{appname}

%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.metainfo.xml

%files demo
%{_bindir}/%{appname}.demo

%{_datadir}/applications/%{appname}.demo.desktop


%changelog
%autochangelog
