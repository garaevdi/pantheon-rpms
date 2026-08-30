%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global srcname panel-sound
%global appname io.elementary.panel.sound

%global commit      e6e33d9c68d3268ee8507ecfe5c2935872f736a4
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate     20260902

Name:           wingpanel-indicator-sound
Summary:        Sound Indicator for wingpanel
Version:        8.0.3^%{gitdate}.git%{shortcommit}
Release:        %autorelease
License:        GPL-3.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libcanberra-gtk)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(wingpanel-9)

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}

%description
A sound indicator for wingpanel.


%prep
%autosetup -n %{srcname}-%{commit} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}

# remove the specified stock icon from appdata (invalid in libappstream-glib)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/io.elementary.wingpanel.sound.metainfo.xml


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/io.elementary.wingpanel.sound.metainfo.xml


%files -f %{appname}.lang
%license COPYING
%doc README.md

%{_libdir}/wingpanel-9/libsound.so

%{_datadir}/glib-2.0/schemas/io.elementary.desktop.wingpanel.sound.gschema.xml
%{_datadir}/metainfo/io.elementary.wingpanel.sound.metainfo.xml


%changelog
%autochangelog
