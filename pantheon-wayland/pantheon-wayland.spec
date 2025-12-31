Name:           pantheon-wayland
Summary:        Wayland integration library to the Pantheon Desktop
Version:        1.1.0
Release:        %autorelease
License:        LGPL-3.0

URL:            https://github.com/elementary/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  gobject-introspection-devel

BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)

%description
%{summary}


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing application that use %{name}


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install


%files
%license COPYING
%doc README.md
%{_libdir}/libpantheon-wayland.so.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/PantheonWayland-1.typelib


%files devel
%{_includedir}/pantheon-wayland-1
%{_libdir}/libpantheon-wayland.so
%{_libdir}/pkgconfig/pantheon-wayland-1.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/PantheonWayland-1.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/pantheon-wayland-1.vapi
%{_datadir}/vala/vapi/pantheon-wayland-1.deps


%changelog
%autochangelog
