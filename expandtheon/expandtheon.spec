%global commit      db5b468209fe0212b2baea2a18633607b719d53e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate     20260307

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
