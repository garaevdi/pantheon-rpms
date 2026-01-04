%global srcname default-settings

Name:           elementary-settings
Summary:        Default settings for elementary OS
Version:        8.1.0
Release:        %autorelease -b2
License:        GPL-3.0-or-later

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  meson

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(polkit-gobject-1)

BuildArch:      noarch

Recommends:       elementary-icon-theme
Recommends:       elementary-sound-theme
Recommends:       elementary-theme
Recommends:       elementary-wallpapers
Recommends:       google-roboto-mono-fonts
Recommends:       rsms-inter-fonts
Recommends:       open-sans-fonts

%description
%{summary}


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson \
    -Dapparmor-profiles=false \
    -Dgeoclue=false \
    -Dappcenter-flatpak=false
%meson_build


%install
%meson_install

%files
%license LICENSE

%{_datadir}/polkit-1/actions/io.elementary.pantheon.AccountsService.policy
%{_datadir}/dbus-1/interfaces/io.elementary.pantheon.AccountsService.xml
%{_datadir}/accountsservice/interfaces/io.elementary.pantheon.AccountsService.xml
%ghost %{_datadir}/cups/data/default-testpage.pdf
%{_datadir}/applications/sessioninstaller.desktop
%{_datadir}/xdg-desktop-portal/pantheon-portals.conf
%{_datadir}/glib-2.0/schemas/default-settings.gschema.override

%{_sysconfdir}/sudoers.d/pwfeedback
%{_sysconfdir}/gtk-4.0/settings.ini
%{_sysconfdir}/skel/.inputrc
%ghost %{_sysconfdir}/netplan/01-network-manager-all.yml
%ghost %{_sysconfdir}/NetworkManager/conf.d/10-globally-managed-devices.conf

%changelog
* Sun Jan 04 2025 Denis Garaev <garaevdi> - 8.1.0-2
- Add recommended packages

* Sun Jan 04 2025 Denis Garaev <garaevdi> - 8.1.0-1
- Initial build for COPR
