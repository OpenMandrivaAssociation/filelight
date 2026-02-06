#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Graphical disk usage statistics
Name:		filelight
Version:	25.12.2
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	LGPLv2
Url:		https://utils.kde.org/projects/filelight/
%if 0%{?git:1}
Source0:	https://invent.kde.org/utilities/filelight/-/archive/%{gitbranch}/filelight-%{gitbranchd}.tar.bz2#/filelight-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/filelight-%{version}.tar.xz
%endif
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
Requires:	kf6-qqc2-desktop-style

%rename plasma6-filelight

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

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
%{_datadir}/kio/servicemenus/filelight.desktop
