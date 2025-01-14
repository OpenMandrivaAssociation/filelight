%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Graphical disk usage statistics
Name:		filelight
Version:	23.08.5
Release:	1
Group:		Graphical desktop/KDE
License:	LGPLv2
Url:		https://utils.kde.org/projects/filelight/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(Qt5Script)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(KF5QQC2DesktopStyle)
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

%files -f %{name}.lang
%config %{_sysconfdir}/xdg/filelightrc
%{_datadir}/qlogging-categories5/*
%{_bindir}/filelight
%{_datadir}/applications/org.kde.filelight.desktop
%{_iconsdir}/*/*/apps/filelight.*
%{_datadir}/kxmlgui5/filelight
%{_datadir}/metainfo/org.kde.filelight.appdata.xml

#----------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-html
