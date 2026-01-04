%global srcname session-settings

Name:           pantheon-session-settings
Summary:        Desktop files for pantheon session
Version:        8.1.0
Release:        %autorelease -b2
License:        GPL-3.0

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch0:         remove-unnecessary-stuff.patch

BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  gnome-keyring
BuildRequires:  meson
BuildRequires:  orca
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(gnome-settings-daemon)

Requires:       gnome-settings-daemon
Requires:       gnome-session
Requires:       gnome-desktop3
Requires:       gala
Requires:       gala-wayland
Requires:       elementary-settings-daemon
Requires:       elementary-dock

Recommends:     gnome-keyring
Recommends:     orca

Suggests:       gala-x11

%description
%{summary}


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson -Dfallback-session="gnome"
%meson_build


%install
%meson_install

%files
%license LICENSE
%doc README.md

%{_datadir}/applications/pantheon-mimeapps.list
%{_datadir}/wayland-sessions/pantheon-wayland.desktop
%{_datadir}/xsessions/pantheon.desktop
%{_datadir}/gnome-session/sessions/pantheon.session
%{_datadir}/gnome-session/sessions/pantheon-wayland.session

%{_userunitdir}/gnome-session@pantheon.target.d/session.conf
%{_userunitdir}/gnome-session@pantheon-wayland.target.d/session.conf

%{_sysconfdir}/xdg/autostart/pantheon-*.desktop

%changelog
%autochangelog
