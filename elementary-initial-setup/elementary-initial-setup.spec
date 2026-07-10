%global srcname initial-setup
%global appname io.elementary.initial-setup

Name:           elementary-initial-setup
Summary:        Initial setup app to create new users
Version:        8.0.1
Release:        %autorelease
License:        GPL-3.0-or-later

URL:            https://github.com/elementary/initial-setup
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.74.0
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite-7) >= 7.4.0
BuildRequires:  pkgconfig(gtk4) >= 4.14.0
BuildRequires:  pkgconfig(gtk4-wayland)
BuildRequires:  pkgconfig(gtk4-x11)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.4.0
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(pantheon-wayland-1)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  pkgconfig(xkbregistry)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(iso-codes)

Requires:       hicolor-icon-theme

%description
New user setup app designed for elementary OS


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%files -f %{appname}.lang
%license COPYING
%doc README.md

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/metainfo/%{appname}.metainfo.xml
%{_datadir}/polkit-1/rules.d/%{appname}.rules
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg


%changelog
%autochangelog
