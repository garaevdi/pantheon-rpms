%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global srcname panel-notifications
%global appname io.elementary.panel.notifications

%global commit      353ef37f429820f3bc9229813b311dd6a9db7ffa
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate     20260906

Name:           wingpanel-indicator-notifications
Summary:        Notifications Indicator for wingpanel
Version:        7.1.1^%{gitdate}.git%{shortcommit}
Release:        %autorelease
License:        LGPL-2.1-or-later AND GPL-3.0-or-later AND GPL-2.0-or-later

URL:            https://github.com/elementary/wingpanel-indicator-notifications
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(wingpanel-9)

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}


%description
A notifications indicator for wingpanel.


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
%license COPYING
%doc README.md

%{_libdir}/wingpanel-9/libnotifications.so

%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.metainfo.xml


%changelog
* Sun Nov 12 2023 Fabio Valentini <decathorpe@gmail.com> - 7.1.0-1
- Initial packaging
