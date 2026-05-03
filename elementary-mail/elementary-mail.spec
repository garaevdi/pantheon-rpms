%global srcname mail
%global appname io.elementary.mail

%global __provides_exclude_from ^%{_libdir}/%{appname}/webkit2/.*\\.so$

Name:           elementary-mail
Summary:        Mail app designed for elementary
Version:        8.0.1
Release:        %autorelease
License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-2.1-only

URL:            https://github.com/elementary/mail
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

Patch:          0001-libcamel-3.57.1.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(camel-1.2) >= 3.28
BuildRequires:  pkgconfig(folks)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 6.0.0
BuildRequires:  pkgconfig(libedataserver-1.2) >= 3.28
BuildRequires:  pkgconfig(libedataserverui-1.2) >= 3.45.1
BuildRequires:  pkgconfig(libhandy-1) >= 1.1.90
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(libportal-gtk3)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  pkgconfig(webkit2gtk-web-extension-4.1)

Requires:       hicolor-icon-theme

%description
%{summary}.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}

# drop unused AppArmor settings
rm -r %{buildroot}/%{_sysconfdir}/apparmor.d


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%files -f %{appname}.lang
%license COPYING
%doc README.md

%{_bindir}/%{appname}

%{_libdir}/%{appname}/

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.metainfo.xml


%changelog
%autochangelog
