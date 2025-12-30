# This is an slightly changed spec file from fedora 40
%global mutter_api_version 14

Name:           mutter
Summary:        Window and compositing manager based on Clutter
Version:        46.9
Release:        %autorelease
License:        GPLv2+

URL:            https://gitlab.gnome.org/GNOME/mutter
Source0:        http://download.gnome.org/sources/%{name}/46/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  git-core
BuildRequires:  meson
BuildRequires:  python3-dbusmock
BuildRequires:  pam-devel
BuildRequires:  sysprof-devel
BuildRequires:  cvt

BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libgbm-devel

BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(libwacom)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(sysprof-capture-4)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(xkeyboard-config)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(graphene-gobject-1.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(gnome-settings-daemon)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(wayland-eglstream)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(colord)
BuildRequires:  pkgconfig(libei-1.0)
BuildRequires:  pkgconfig(libeis-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(xwayland)

Requires:       control-center-filesystem
Requires:       gsettings-desktop-schemas
Requires:       gnome-settings-daemon
Requires:       gtk4%{?_isa}
Requires:       json-glib%{?_isa}
Requires:       libinput%{?_isa}
Requires:       pipewire
Requires:       startup-notification
Requires:       dbus

Requires:       %{name}-common = %{version}-%{release}

Recommends:     mesa-dri-drivers%{?_isa}

Provides:       bundled(cogl) = 1.22.0
Provides:       bundled(clutter) = 1.26.0

%description
%summary

%package common
Summary: Common files used by %{name} and forks of %{name}
BuildArch: noarch

%description common
$summary

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: mesa-libEGL-devel

%description devel
%summary

%package tests
Summary: Tests for the %{name} package
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gtk3%{?_isa}

%description tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.

%prep
%autosetup -S git -n %{name}-%{version}

%build
%meson -Degl_device=true -Dwayland_eglstream=true
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc NEWS
%{_bindir}/mutter
%{_libdir}/lib*.so.*
%{_libdir}/mutter-%{mutter_api_version}/
%{_libexecdir}/mutter-restart-helper
%{_libexecdir}/mutter-x11-frames
%{_mandir}/man1/mutter.1*

%files common
%{_datadir}/GConf/gsettings/mutter-schemas.convert
%{_datadir}/glib-2.0/schemas/org.gnome.mutter.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.mutter.wayland.gschema.xml
%{_datadir}/gnome-control-center/keybindings/50-mutter-*.xml
%{_udevrulesdir}/61-mutter.rules

%files devel
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*

%files tests
%{_libexecdir}/installed-tests/mutter-%{mutter_api_version}
%{_datadir}/installed-tests/mutter-%{mutter_api_version}
%{_datadir}/mutter-%{mutter_api_version}/tests

%changelog
%autochangelog
