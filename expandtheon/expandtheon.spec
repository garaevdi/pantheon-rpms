%global commit      549fb55a9dec1ed7c6ea58579db21059dcd142c8
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate     20251118

Name:           expandtheon
Summary:        Bringing 3rd-party icon support to Pantheon DE
Version:        1.0.0^%{gitdate}.git%{shortcommit}
Release:        %autorelease
License:        GPL-3.0

URL:            https://github.com/ellie-commons/expandtheon
Source:         %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  meson

BuildArch:      noarch

Requires:       elementary-icon-theme

%description
%summary


%prep
%autosetup -n %{name}-%{commit} -p1


%conf
%meson


%build
%meson_build


%install
%meson_install


%files
%license COPYING
%doc README.md

%{_datadir}/icons/expandtheon

%changelog
%autochangelog
