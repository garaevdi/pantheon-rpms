%global appname io.elementary.wingpanel
%global glib_version 2.32.0

Name:           wingpanel
Summary:        Stylish top panel
Version:        8.0.4
Release:        %autorelease
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-2.1-or-later

URL:            https://github.com/elementary/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

Patch:          mutter49-wingpanel.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

%if 0%{?fedora} >= 43
BuildRequires:  pkgconfig(libmutter-17)
BuildRequires:  pkgconfig(mutter-clutter-17)
BuildRequires:  pkgconfig(mutter-cogl-17)
BuildRequires:  pkgconfig(mutter-mtk-17)
%endif
%if 0%{?fedora} == 42
BuildRequires:  pkgconfig(libmutter-16)
BuildRequires:  pkgconfig(mutter-clutter-16)
BuildRequires:  pkgconfig(mutter-cogl-16)
BuildRequires:  pkgconfig(mutter-mtk-16)
%endif
%if 0%{?fedora} == 41
BuildRequires:  pkgconfig(libmutter-15)
BuildRequires:  pkgconfig(mutter-clutter-15)
BuildRequires:  pkgconfig(mutter-cogl-15)
BuildRequires:  pkgconfig(mutter-cogl-pango-15)
BuildRequires:  pkgconfig(mutter-mtk-15)
%endif

BuildRequires:  pkgconfig(gala) >= 8.3.0
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(granite) >= 5.4.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10

Requires:       hicolor-icon-theme

%description
%{summary}


%package        devel
Summary:        Stylish top panel (development files)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
%{summary}


%prep
%autosetup -S git -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}

# create plugin directory
mkdir -p %{buildroot}/%{_libdir}/wingpanel

# create settings directory
mkdir -p %{buildroot}/%{_sysconfdir}/wingpanel.d


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%files -f %{appname}.lang
%license COPYING
%doc README.md

%dir %{_sysconfdir}/wingpanel.d
%dir %{_libdir}/wingpanel

%{_bindir}/%{appname}

%{_libdir}/libwingpanel.so.8*
%{_libdir}/gala/plugins/libwingpanel-interface.so

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/io.elementary.desktop.wingpanel.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.metainfo.xml

%files devel
%{_includedir}/wingpanel/

%{_libdir}/libwingpanel.so
%{_libdir}/pkgconfig/wingpanel.pc

%{_datadir}/vala/vapi/wingpanel.deps
%{_datadir}/vala/vapi/wingpanel.vapi

%changelog
%{autochangelog}
