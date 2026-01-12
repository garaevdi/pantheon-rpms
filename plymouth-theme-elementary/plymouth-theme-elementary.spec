%global srcname plymouth-theme

%global commit      cc7199569f22fad9d3b6ed20a2dc3c41bcf1e29a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate     20250422

Name:           plymouth-theme-elementary
Summary:        Elementary plymouth theme
Version:        6.0.0^%{gitdate}.git%{shortcommit}
Release:        %autorelease
License:        NO-LICENSE

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz

BuildArch:      noarch

BuildRequires:  meson >= 1.3.0

Requires:       plymouth-theme-spinner

%description
%summary


%prep
%autosetup -n %{srcname}-%{commit} -p1


%build
%meson
%meson_build


%install
%meson_install


%files
%doc README.md

%{_datadir}/plymouth/themes/elementary/*


%changelog
%autochangelog
