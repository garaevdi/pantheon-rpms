%global srcname greeter
%global appname io.elementary.greeter

%global commit      2b47a17ccbb0f6820999ce6139201b28bb11b3bf
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate     20260727

Name:           elementary-greeter
Summary:        LightDM Login Screen for the elementary desktop
Version:        8.1.2^%{gitdate}.git%{shortcommit}
Release:        %autorelease -b2
License:        GPL-3.0-only AND GPL-3.0-or-later AND GPL-2.0-or-later

URL:            https://github.com/elementary/greeter
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch1:         0001-Remove-greeter-compositor.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.58.0
BuildRequires:  vala

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gtk4-wayland)
BuildRequires:  pkgconfig(gtk4-x11)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(liblightdm-gobject-1)

Requires:       lightdm%{?_isa}
Requires:       wingpanel%{?_isa}
Requires:       gala

# requirements for default artwork
Suggests:       elementary-icon-theme
Suggests:       elementary-theme-gtk3
Suggests:       elementary-wallpapers

# requirements for accountsservice extension
Requires:       pantheon-session-settings

# all LightDM greeters provide this
Provides:       lightdm-greeter = 1.2

# alternate descriptive names
Provides:       lightdm-%{name} = %{version}-%{release}
Provides:       lightdm-%{name}%{?_isa} = %{version}-%{release}

%description
The elementary Greeter is a styled Login Screen for LightDM.


%prep
%autosetup -n %{srcname}-%{commit} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%files -f %{appname}.lang
%license LICENSE
%doc README.md

%config(noreplace) %{_sysconfdir}/lightdm/%{appname}.conf

%{_bindir}/%{appname}-session-manager
%{_sbindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}-compositor.gschema.xml
%{_datadir}/lightdm/lightdm.conf.d/40-io.elementary.greeter.conf
%{_datadir}/metainfo/%{appname}.metainfo.xml
%{_datadir}/xgreeters/%{appname}.desktop

%{_iconsdir}/hicolor/*/apps/%{appname}.settings.svg


%changelog
%{autochangelog}
