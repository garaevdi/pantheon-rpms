# FIXME: most tests currently fail
%bcond_with tests

%global glib2_version	%(pkg-config --modversion glib-2.0 2>/dev/null || echo "2.44")
%global giturl		https://github.com/ubuntu/lightdm

Name:		lightdm
Summary:	A cross-desktop Display Manager
Version:	1.33.1
Release:	%autorelease
# So the copr version will always be prefered over the fedora one
Epoch:		1

# library/bindings are LGPLv2 or LGPLv3, the rest GPLv3+
License:	(LGPL-2.0-only OR LGPL-3.0-only) AND GPL-3.0-or-later
URL:		https://www.freedesktop.org/wiki/Software/LightDM/
Source0:	%{giturl}/archive/%{version}/lightdm-%{version}.tar.gz

Source10:	lightdm.pam
Source11:	lightdm-autologin.pam
Source12:	lightdm-tmpfiles.conf
Source13:	lightdm.service
Source14:	lightdm.logrotate
Source15:	lightdm.rules
Source16:	lightdm.sysusers


# .conf snippets
Source20:	50-backup-logs.conf
Source21:	50-minimum-vt.conf
Source22:	50-session-wrapper.conf
Source23:	50-user-authority-in-system-dir.conf
Source24:	50-xserver-command.conf
Source25:	50-disable-guest.conf
Source26:	50-run-directory.conf

Patch0:		gcc-10.patch
Patch1:		remove_bin_path.patch
Patch2:		lightdm-1.33-fix_wayland_session.patch

# Pending

# Upstream commits

BuildRequires:	gettext-devel
BuildRequires:	gnome-common
BuildRequires:	gtk-doc itstool
BuildRequires:	intltool
BuildRequires:	libgcrypt-devel
BuildRequires:	pam-devel
BuildRequires:	pkgconfig(audit)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gio-2.0) >= 2.26
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gmodule-export-2.0)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 0.9.5
BuildRequires:	pkgconfig(libxklavier)
BuildRequires:	pkgconfig(Qt5Core) pkgconfig(Qt5DBus) pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt6Core) pkgconfig(Qt6DBus) pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xdmcp)
BuildRequires:	systemd-rpm-macros
BuildRequires:	vala

Requires:	%{name}-gobject%{?_isa} = %{version}-%{release}
Requires:	accountsservice
Requires:	dbus
Requires:	polkit-js-engine
Requires:	/sbin/nologin
Requires:	systemd
Requires:	xorg-x11-server-Xorg
Requires:	xorg-x11-xinit
Requires:   lightdm-greeter = 1.2
Suggests:   slick-greeter
%{?systemd_requires}

Obsoletes: lightdm-qt < %{version}-%{release}
Obsoletes: lightdm-qt-devel < %{version}-%{release}

Requires(post):	psmisc dbus-daemon

# needed for anaconda to boot into runlevel 5 after install
Provides:	service(graphical-login) = lightdm

%description
Lightdm is a display manager that:
* Is cross-desktop - supports different desktops
* Supports different display technologies
* Is lightweight - low memory usage and fast performance


%package gobject
Summary:	LightDM GObject client library
Requires:	%{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	glib2%{?_isa} >= %{glib2_version}
%description gobject
This package contains a GObject based library for LightDM clients to use to
interface with LightDM.


%package gobject-devel
Summary:	Development files for %{name}-gobject
Requires:	%{name}-gobject%{?_isa} = %{epoch}:%{version}-%{release}
%description gobject-devel
%{summary}.


%package qt5
Summary:	LightDM Qt5 client library
Requires:	%{name}%{?_isa} = %{epoch}:%{version}-%{release}


%description qt5
This package contains a Qt5-based library for LightDM clients to use to interface
with LightDM.


%package qt5-devel
Summary:	Development files for %{name}-qt5
Requires:	%{name}-qt5%{?_isa} = %{epoch}:%{version}-%{release}
%description qt5-devel
%{summary}.

%package qt6
Summary:	LightDM Qt6 client library
Requires:	%{name}%{?_isa} = %{epoch}:%{version}-%{release}


%description qt6
This package contains a Qt6-based library for LightDM clients to use to interface
with LightDM.


%package qt6-devel
Summary:	Development files for %{name}-qt6
Requires:	%{name}-qt6%{?_isa} = %{epoch}:%{version}-%{release}
%description qt6-devel
%{summary}.


%prep
%autosetup -p 1


%conf
# Make libtoolize happy.
%{__cat} %{_datadir}/aclocal/intltool.m4 > aclocal.m4
# gettext-0.25 fix
export ACLOCAL_PATH=%{_datadir}/gettext/m4/
# Bootstrap
NOCONFIGURE=1 ./autogen.sh

%configure                      \
	--disable-dmrc              \
	--disable-silent-rules      \
	--disable-static			\
	--enable-gtk-doc			\
	--enable-libaudit			\
	--enable-liblightdm-qt5     \
	--enable-liblightdm-qt6		\
	--enable-introspection      \
%if %{with tests}
	--enable-tests				\
%else
	--disable-tests				\
%endif
	--enable-vala				\
	--with-greeter-user=lightdm \
	--with-greeter-session=lightdm-greeter


%build
%make_build


%install
%make_install

# We need to own these
%{__mkdir_p} %{buildroot}%{_sysconfdir}/lightdm/lightdm.conf.d/		\
		%{buildroot}%{_datadir}/dbus-1/interfaces		\
		%{buildroot}%{_datadir}/dbus-1/system.d			\
		%{buildroot}%{_datadir}/lightdm/lightdm.conf.d/		\
		%{buildroot}%{_datadir}/lightdm/remote-sessions/	\
		%{buildroot}%{_datadir}/xgreeters/			\
		%{buildroot}%{_localstatedir}/cache/lightdm/		\
		%{buildroot}%{_rundir}/lightdm/		\
		%{buildroot}%{_localstatedir}/log/lightdm/		\
		%{buildroot}%{_localstatedir}/lib/lightdm/		\
		%{buildroot}%{_localstatedir}/lib/lightdm-data/

# libtool cruft
rm -fv %{buildroot}%{_libdir}/lib*.la

# We don't ship AppAmor
%{__rm} -rfv %{buildroot}%{_sysconfdir}/apparmor.d/

# omit upstart support
%{__rm} -rfv %{buildroot}%{_sysconfdir}/init

# install pam file
%{__install} -Dpm 0644 %{SOURCE10} %{buildroot}%{_sysconfdir}/pam.d/lightdm
%{__install} -Dpm 0644 %{SOURCE11} %{buildroot}%{_sysconfdir}/pam.d/lightdm-autologin
%{__install} -Dpm 0644 %{SOURCE12} %{buildroot}%{_prefix}/lib/tmpfiles.d/lightdm.conf
%{__install} -Dpm 0644 %{SOURCE13} %{buildroot}%{_unitdir}/lightdm.service
%{__install} -Dpm 0644 %{SOURCE14} %{buildroot}%{_sysconfdir}/logrotate.d/lightdm
%{__install} -Dpm 0644 %{SOURCE15} %{buildroot}%{_datadir}/polkit-1/rules.d/lightdm.rules
%{__install} -Dpm 0644 %{SOURCE16} %{buildroot}%{_sysusersdir}/lightdm.conf
%{__install} -pm 0644 %{SOURCE20} %{SOURCE21} %{SOURCE22} %{SOURCE23}	\
	%{SOURCE24} %{SOURCE25} %{SOURCE26} %{buildroot}%{_datadir}/lightdm/lightdm.conf.d/


%find_lang lightdm --with-gnome


%if %{with tests}
%check
%make_build check ||:
%endif



%post
%systemd_post lightdm.service

%preun
%systemd_preun lightdm.service

%postun
%systemd_postun lightdm.service


%files -f lightdm.lang
%license COPYING.GPL3
%doc NEWS
%dir %{_sysconfdir}/lightdm/
%dir %{_sysconfdir}/lightdm/lightdm.conf.d
%config(noreplace) %{_sysconfdir}/pam.d/lightdm*
%config(noreplace) %{_sysconfdir}/lightdm/keys.conf
%config(noreplace) %{_sysconfdir}/lightdm/lightdm.conf
%config(noreplace) %{_sysconfdir}/lightdm/users.conf
%dir %{_sysconfdir}/logrotate.d/
%{_sysconfdir}/logrotate.d/lightdm
%dir %attr(-,lightdm,lightdm) %{_localstatedir}/cache/lightdm/
%dir %attr(-,lightdm,lightdm) %{_localstatedir}/lib/lightdm/
%dir %attr(-,lightdm,lightdm) %{_localstatedir}/lib/lightdm-data/
%dir %attr(-,lightdm,lightdm) %{_localstatedir}/log/lightdm/
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%dir %{_datadir}/xgreeters/
%ghost %dir %{_rundir}/lightdm
%{_bindir}/dm-tool
%{_sbindir}/lightdm
%{_libexecdir}/lightdm-guest-session
%{_datadir}/lightdm/
%{_libdir}/girepository-1.0/LightDM-1.typelib
%{_mandir}/man1/dm-tool.1*
%{_mandir}/man1/lightdm*
%{_sysusersdir}/lightdm.conf
%{_unitdir}/lightdm.service
%{_datadir}/accountsservice
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/system.d/*.conf
%{_datadir}/polkit-1/rules.d/lightdm.rules
%{_datadir}/polkit-1/actions/org.freedesktop.DisplayManager.AccountsService.policy
%{_datadir}/bash-completion/completions/dm-tool
%{_datadir}/bash-completion/completions/lightdm
%{_prefix}/lib/tmpfiles.d/lightdm.conf

%files gobject
%license COPYING.LGPL2 COPYING.LGPL3
%{_libdir}/liblightdm-gobject-1.so.0*

%files gobject-devel
%doc %{_datadir}/gtk-doc/html/lightdm-gobject-1/
%{_includedir}/lightdm-gobject-1/
%{_libdir}/liblightdm-gobject-1.so
%{_libdir}/pkgconfig/liblightdm-gobject-1.pc
%{_datadir}/gir-1.0/LightDM-1.gir
%{_datadir}/vala/vapi/liblightdm-gobject-1.*

%files qt5
%license COPYING.LGPL2 COPYING.LGPL3
%{_libdir}/liblightdm-qt5-3.so.0*

%files qt5-devel
%{_includedir}/lightdm-qt5-3/
%{_libdir}/liblightdm-qt5-3.so
%{_libdir}/pkgconfig/liblightdm-qt5-3.pc

%files qt6
%license COPYING.LGPL2 COPYING.LGPL3
%{_libdir}/liblightdm-qt6-3.so.0*

%files qt6-devel
%{_includedir}/lightdm-qt6-3/
%{_libdir}/liblightdm-qt6-3.so
%{_libdir}/pkgconfig/liblightdm-qt6-3.pc


%changelog
%autochangelog
