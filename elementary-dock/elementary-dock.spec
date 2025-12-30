%global srcname dock
%global appname io.elementary.dock
# https://github.com/elementary/dock/issues/418
%global build_type_safety_c 1

Name:           elementary-dock
Summary:        A quick app launcher and window switcher for Pantheon and elementary OS
Version:        8.3.1
Release:        %autorelease
License:        GPL-3.0

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(wayland-scanner)

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

%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.metainfo.xml

%changelog
%autochangelog
