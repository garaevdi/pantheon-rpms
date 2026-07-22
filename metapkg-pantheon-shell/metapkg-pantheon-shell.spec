Name:           metapkg-pantheon-shell
Summary:        Pantheon desktop metapackage
Version:        1.2
Release:        %autorelease
License:        NO-LICENSE

BuildArch:      noarch

Requires:       elementary-dock
Requires:       elementary-greeter
Requires:       elementary-settings
Requires:       elementary-settings-daemon
Requires:       elementary-wallpapers
Requires:       gala
Requires:       gala-wayland
Requires:       pantheon-agent-polkit
Requires:       wingpanel
Requires:       xdg-desktop-portal-pantheon

Suggests:       elementary-screenshot
Suggests:       elementary-sound-theme

%description
%{summary}

%files

%changelog
%autochangelog
