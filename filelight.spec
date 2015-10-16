%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Graphical disk usage statistics
Name:		filelight
Version:	15.08.2
Release:	1
Group:		Graphical desktop/KDE
License:	LGPLv2
Url:		http://utils.kde.org/projects/filelight/
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(Qt5Script)

%description
Filelight allows you to quickly understand exactly where your
diskspace is being used by graphically representing your file
system as a set of concentric segmented-rings. You can use it
to locate hotspots of disk usage and then manipulate those
areas using a file manager.

%files
%doc %{_docdir}/HTML/en/filelight
%{_sysconfdir}/xdg/*
%{_bindir}/filelight
%{_libdir}/qt5/plugins/filelightpart.so
%{_datadir}/applications/org.kde.filelight.desktop
%{_iconsdir}/*/*/actions/views_filelight.*
%{_iconsdir}/*/*/apps/filelight.*
%{_datadir}/kservices5/filelightpart.desktop
%{_datadir}/kxmlgui5/filelight
%{_datadir}/kxmlgui5/filelightpart

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
