%global appname io.elementary.appcenter

Name:           appcenter
Version:        8.3.1
Release:        %autorelease
Summary:        Pay-what-you-can app store
License:        GPL-3.0

URL:            https://github.com/elementary/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  sassc

BuildRequires:  pkgconfig(appstream)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(flatpak)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite-7) >= 7.6.0
BuildRequires:  pkgconfig(gtk4) >= 4.10
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.4
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(libportal-gtk4)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(polkit-gobject-1)

%description
%{summary}


%prep
%autosetup -p1


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
%{_datadir}/dbus-1/services/%{appname}.service
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/gnome-shell/search-providers/%{appname}.search-provider.ini
%{_datadir}/icons/hicolor/*/apps/%{appname}*.svg
%{_datadir}/metainfo/%{appname}.metainfo.xml
%{_datadir}/polkit-1/actions/%{appname}.policy

%dir %{_sysconfdir}/%{appname}
%{_sysconfdir}/%{appname}/*

%changelog
%autochangelog
