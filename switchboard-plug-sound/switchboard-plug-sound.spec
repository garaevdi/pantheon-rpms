%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname settings-sound

%global plug_type system
%global plug_name sound
%global plug_rdnn io.elementary.settings.sound

Name:           switchboard-plug-sound
Summary:        Switchboard Sound Plug
Version:        8.0.2
Release:        %autorelease
License:        LGPL-2.0-or-later

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.58.0
BuildRequires:  vala

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(switchboard-3)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}

%description
A sound plug for Switchboard.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{plug_rdnn}

# remove the specified stock icon from appdata (invalid in libappstream-glib)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml


%files -f %{plug_rdnn}.lang
%license COPYING
%doc README.md

%{_libdir}/switchboard-3/%{plug_type}/lib%{plug_rdnn}.so

%{_datadir}/glib-2.0/schemas/%{plug_name}.gschema.xml
%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml


%changelog
* Wed Jan 07 2026 Denis Garaev <garaevdi@yandex.ru> - 8.0.2-1
- Update to version 8.0.2

* Thu Nov 16 2023 Fabio Valentini <decathorpe@gmail.com> - 2.3.3-1
- Initial packaging

