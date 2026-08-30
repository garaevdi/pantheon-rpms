%global appname io.elementary.quick-settings
%global srcname quick-settings

%global commit      f999414ae2d18e95617748b848fd8def339aceb7
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate     20260903

Name:           wingpanel-quick-settings
Summary:        Access frequently used settings and system actions
Version:        1.4.0^%{gitdate}.git%{shortcommit}
Release:        %autorelease
License:        GPL-3.0-or-later AND GPL-2.0-or-later

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.32.1

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(packagekit-glib2)
BuildRequires:  pkgconfig(wingpanel-9)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(libportal)

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}

Obsoletes:      wingpanel-indicator-a11y

%description
%{summary}


%prep
%autosetup -n %{srcname}-%{commit} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}

# remove the specified stock icon from appdata (invalid in libappstream-glib)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%files -f %{appname}.lang
%license LICENSE
%doc README.md

%{_libdir}/wingpanel-9/lib%{srcname}.so

%{_datadir}/glib-2.0/schemas/%{srcname}.gschema.xml
%{_datadir}/metainfo/%{appname}.metainfo.xml


%changelog
%autochangelog
