%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global srcname monitor
%global appname io.elementary.monitor

Name:           elementary-monitor
Summary:        Manage processes and monitor system resources
Version:        8.0.1
Release:        %autorelease
License:        GPL-3.0

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  libXNVCtrl-devel
BuildRequires:  meson
BuildRequires:  sassc
BuildRequires:  vala >= 0.40.0

BuildRequires:  pkgconfig(flatpak)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(livechart-2)
BuildRequires:  pkgconfig(udisks2)
BuildRequires:  pkgconfig(wingpanel) >= 2.1.0

%description
%{summary}


%package -n     wingpanel-indicator-monitor
Summary:        System resources Indicator for wingpanel

Requires:       elementary-monitor%{?_isa}
Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}

%description -n wingpanel-indicator-monitor
%{summary}


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson -Dindicator-wingpanel=enabled
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
%doc README.md
%license LICENSE

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.metainfo.xml
%{_datadir}/%{appname}/*

%files -n wingpanel-indicator-monitor
%{_libdir}/wingpanel/lib%{srcname}.so

%changelog
%autochangelog
