%global glib_version 2.74.0

Name:           gala
Summary:        Gala Window Manager for elementary OS and Pantheon
Version:        8.4.0
Release:        %autorelease
License:        GPL-3.0-or-later

URL:            https://github.com/elementary/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

Patch1:         mutter49.patch
Patch2:         libmutter15.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  meson >= 0.59
BuildRequires:  systemd-rpm-macros
BuildRequires:  vala >= 0.46
BuildRequires:  wayland-devel

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

BuildRequires:  pkgconfig(atk-bridge-2.0)
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(gio-unix-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(glib-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pkgconfig(gobject-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(xext)

# gala's multitasking view is activated via dbus
Requires:       dbus

# GTK-based notifications use this new notifications server
Requires:       elementary-notifications

# For some reason gala can't run without this
Requires:       elementary-icon-theme

Provides:       firstboot(windowmanager) = gala

%description
%{summary}

%package        x11
Summary:        Gala window manager X11 support
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}
Requires:       gnome-session
Requires:       xorg-x11-server-Xorg

%description        x11
Gala is Pantheon's Window Manager, part of the elementary project

This package contains the support files for running gala on X11

%package        wayland
Summary:        Gala window manager Wayland support
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}
Requires:       gnome-session
Requires:       xorg-x11-server-Xwayland

%description    wayland
Gala is Pantheon's Window Manager, part of the elementary project

This package contains the support files for running gala on Wayland

%package        devel
Summary:        Gala window manager development files

Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Gala is Pantheon's Window Manager, part of the elementary project

This package contains the development headers


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang gala

# remove the specified stock icon from appdata (invalid in libappstream-glib)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{name}.metainfo.xml

# drop strange file from /etc/xdg
rm %{buildroot}/%{_sysconfdir}/xdg/io.elementary.desktop.wm.shell


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/gala*.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{name}.metainfo.xml


%post x11
%systemd_user_post io.elementary.gala@x11.service

%post wayland
%systemd_user_post io.elementary.gala@wayland.service

%preun x11
%systemd_user_preun io.elementary.gala@x11.service

%preun wayland
%systemd_user_preun io.elementary.gala@wayland.service

%postun x11
%systemd_user_postun io.elementary.gala@x11.service

%postun wayland
%systemd_user_postun io.elementary.gala@wayland.service


%files -f %{name}.lang
%license COPYING
%doc AUTHORS
%doc HACKING
%doc README.md

%{_bindir}/%{name}
%{_bindir}/%{name}-daemon
%{_bindir}/%{name}-daemon-gtk3

%{_libdir}/gala/
%{_libdir}/libgala.so.0*

%{_datadir}/applications/%{name}*.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.desktop.gala.gschema.xml
%{_datadir}/glib-2.0/schemas/20_elementary.pantheon.wm.gschema.override
%{_datadir}/metainfo/%{name}.metainfo.xml

%{_userunitdir}/io.elementary.gala.target

%files x11
%{_userunitdir}/io.elementary.gala@x11.service

%files wayland
%{_userunitdir}/io.elementary.gala@wayland.service

%files devel
%{_includedir}/gala/

%{_libdir}/libgala.so
%{_libdir}/pkgconfig/gala.pc

%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gala.deps
%{_datadir}/vala/vapi/gala.vapi

%changelog
%autochangelog
