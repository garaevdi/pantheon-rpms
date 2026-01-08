Name:           live-chart
Summary:        A real-time charting library for GTK4
Version:        2.0.0
Release:        %autorelease
License:        MIT

URL:            https://github.com/elementary/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  xorg-x11-server-Xvfb

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)

%description
A real-time charting library for Vala and GTK4 based on Cairo


%package        devel
Summary:        A real-time charting library for GTK4 (development files)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
%{summary}


%prep
%autosetup -p1


%build
%meson
%meson_build

%install
%meson_install


%files
%doc README.md
%license LICENSE
%{_libdir}/liblivechart-2.so.2*


%files devel
%{_includedir}/livechart-2.h

%{_libdir}/liblivechart-2.so
%{_libdir}/pkgconfig/livechart-2.pc

%{_datadir}/vala/vapi/livechart-2.vapi


%changelog
%autochangelog
