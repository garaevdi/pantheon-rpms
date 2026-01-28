%global srcname settings-daemon
%global appname io.elementary.settings-daemon
%global iface   io.elementary.SettingsDaemon.AccountsService

Name:           elementary-settings-daemon
Version:        8.5.0
Release:        %autorelease
Summary:        Settings Daemon and Portal for Pantheon
# GPL-3.0-or-later except settings-portal/* which is LGPL-2.0-or-later
License:        GPL-3.0-or-later AND LGPL-2.0-or-later

URL:            https://github.com/elementary/settings-daemon
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.59.0
BuildRequires:  systemd-rpm-macros
BuildRequires:  vala

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fwupd)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gexiv2)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 5.3.0
BuildRequires:  pkgconfig(libgeoclue-2.0)
BuildRequires:  pkgconfig(packagekit-glib2)
BuildRequires:  pkgconfig(systemd)

Requires:       accountsservice
Requires:       dbus-common
Requires:       xdg-desktop-portal

Recommends:     PackageKit

%description
%{summary}.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson -Dubuntu_drivers=false
%meson_build


%install
%meson_install
%find_lang %{appname}


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%post
%systemd_post %{appname}.check-for-firmware-updates.timer
%systemd_user_post %{appname}.xdg-desktop-portal.service
%systemd_user_post %{appname}.system-update.timer
%systemd_user_post %{appname}.service

%preun
%systemd_preun %{appname}.check-for-firmware-updates.timer
%systemd_user_preun %{appname}.xdg-desktop-portal.service
%systemd_user_preun %{appname}.system-update.timer
%systemd_user_preun %{appname}.service

%postun
%systemd_postun_with_restart %{appname}.check-for-firmware-updates.timer
%systemd_user_postun_with_restart %{appname}.xdg-desktop-portal.service
%systemd_user_postun_with_restart %{appname}.system-update.timer
%systemd_user_postun_with_restart %{appname}.service


%files -f %{appname}.lang
%license LICENSE
%doc README.md

%{_bindir}/%{appname}

%{_libexecdir}/%{appname}.xdg-desktop-portal

%{_datadir}/accountsservice/interfaces/%{iface}.xml
%{_datadir}/dbus-1/interfaces/%{iface}.xml
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.elementary.settings-daemon.service
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.metainfo.xml
%{_datadir}/xdg-desktop-portal/portals/%{appname}.portal

%{_unitdir}/%{appname}.check-for-firmware-updates.service
%{_unitdir}/%{appname}.check-for-firmware-updates.timer
%{_userunitdir}/%{appname}.system-update.service
%{_userunitdir}/%{appname}.system-update.timer
%{_userunitdir}/%{appname}.xdg-desktop-portal.service
%{_userunitdir}/%{appname}.service


%changelog
%autochangelog
