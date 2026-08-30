%global appname io.elementary.wingpanel
%global glib_version 2.32.0

%global commit      9eda202f268adb70e89376063974a3f7895e095c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate     20260902

Name:           wingpanel
Summary:        Stylish top panel
Version:        8.0.4^%{gitdate}.git%{shortcommit}
Release:        %autorelease
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-2.1-or-later

URL:            https://github.com/elementary/%{name}
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch0:         0002-mutter51-wingpanel.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

%if 0%{?fedora} >= 45
BuildRequires:  pkgconfig(libmutter-51)
BuildRequires:  pkgconfig(mutter-clutter-51)
BuildRequires:  pkgconfig(mutter-cogl-51)
BuildRequires:  pkgconfig(mutter-mtk-51)
%endif
%if 0%{?fedora} == 44
BuildRequires:  pkgconfig(libmutter-18)
BuildRequires:  pkgconfig(mutter-clutter-18)
BuildRequires:  pkgconfig(mutter-cogl-18)
BuildRequires:  pkgconfig(mutter-mtk-18)
%endif
%if 0%{?fedora} == 43
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
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk4)

Requires:       hicolor-icon-theme

%description
%{summary}


%package        devel
Summary:        Stylish top panel (development files)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
%{summary}


%prep
%autosetup -n %{name}-%{commit} -p1


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

%{_libdir}/libwingpanel-9.so.*
%{_libdir}/gala/plugins/libwingpanel-interface.so

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/io.elementary.desktop.wingpanel.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.metainfo.xml

%files devel
%{_includedir}/wingpanel-9/

%{_libdir}/libwingpanel-9.so
%{_libdir}/pkgconfig/wingpanel-9.pc

%{_datadir}/vala/vapi/wingpanel-9.deps
%{_datadir}/vala/vapi/wingpanel-9.vapi

%changelog
%{autochangelog}
