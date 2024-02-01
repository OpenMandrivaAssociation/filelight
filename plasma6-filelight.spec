%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Graphical disk usage statistics
Name:		plasma6-filelight
Version:	24.01.95
Release:	1
Group:		Graphical desktop/KDE
License:	LGPLv2
Url:		http://utils.kde.org/projects/filelight/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/filelight-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6Solid)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6KirigamiAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(KF6QQC2DesktopStyle)
BuildRequires:	qml(org.kde.kirigami)
BuildRequires:	qml(org.kde.quickcharts)
Requires:	qml(org.kde.kirigami)
Requires:	qml(org.kde.quickcharts)
Requires:	qqc2-desktop-style

%description
Filelight allows you to quickly understand exactly where your
diskspace is being used by graphically representing your file
system as a set of concentric segmented-rings. You can use it
to locate hotspots of disk usage and then manipulate those
areas using a file manager.

%files -f filelight.lang
%config %{_sysconfdir}/xdg/filelightrc
%{_datadir}/qlogging-categories6/*
%{_bindir}/filelight
%{_datadir}/applications/org.kde.filelight.desktop
%{_iconsdir}/*/*/apps/filelight.*
%{_datadir}/metainfo/org.kde.filelight.appdata.xml

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n filelight-%{version}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang filelight --with-html
