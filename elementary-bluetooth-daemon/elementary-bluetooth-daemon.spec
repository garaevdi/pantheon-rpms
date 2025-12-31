%global srcname bluetooth-daemon
%global appname io.elementary.bluetooth

Name:           elementary-bluetooth-daemon
Summary:        Send and receive files via Bluetooth
Version:        1.1.0
Release:        %autorelease
License:        GPL-3.0

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 6.0
BuildRequires:  pkgconfig(gtk+-3.0)

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


%files -f %{appname}.lang
%license LICENSE
%doc README.md

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*
%{_datadir}/metainfo/%{appname}.metainfo.xml

%{_sysconfdir}/xdg/autostart/%{appname}.desktop


%changelog
%autochangelog
