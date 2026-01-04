%global appname io.elementary.desktop.agent-polkit

Name:           pantheon-agent-polkit
Summary:        Pantheon Polkit Agent
Version:        8.0.2
Release:        %autorelease
License:        LGPL-2.0-or-later

URL:            https://github.com/elementary/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.34.1

BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(pantheon-wayland-1)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(polkit-gobject-1)

%description
An agent for Polkit authorization designed for Pantheon.


%prep
%autosetup -n %{name}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_sysconfdir}/xdg/autostart/%{appname}.desktop

desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%files -f %{appname}.lang
%license COPYING
%doc README.md

%config(noreplace) %{_sysconfdir}/xdg/autostart/%{appname}.desktop

%{_libexecdir}/policykit-1-pantheon/

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/metainfo/%{appname}.metainfo.xml


%changelog
%autochangelog
