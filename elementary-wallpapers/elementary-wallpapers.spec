%global srcname wallpapers
%global appname io.elementary.wallpapers

Name:           elementary-wallpapers
Summary:        Collection of wallpapers from the elementary project
Version:        8.0.0
Release:        %autorelease

# License breakdown is available in debian/copyright
License:        Public Domain

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  meson
BuildRequires:  gettext

BuildArch:      noarch

Provides:       pandora-wallpapers = %{version}-%{release}
Obsoletes:      pandora-wallpapers < 0.1.8-2


%description
This is the official collection of wallpapers from the elementary
project.


%prep
%autosetup -n %{srcname}-%{version}


%build
%meson
%meson_build


%install
%meson_install


%files
%license LICENSE.md
%doc README.md

%{_datadir}/backgrounds/*
%{_datadir}/metainfo/%{appname}.metainfo.xml


%changelog
%autochangelog
