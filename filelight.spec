%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Graphical disk usage statistics
Name:		filelight
Version:	17.04.3
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

%files -f %{name}.lang
%{_sysconfdir}/xdg/*
%{_bindir}/filelight
%{_libdir}/qt5/plugins/filelightpart.so
%{_datadir}/applications/org.kde.filelight.desktop
%{_iconsdir}/*/*/actions/views_filelight.*
%{_iconsdir}/*/*/apps/filelight.*
%{_datadir}/kservices5/filelightpart.desktop
%{_datadir}/kxmlgui5/filelight
%{_datadir}/kxmlgui5/filelightpart
%doc %{_docdir}/HTML/en/filelight
%lang(de) %doc %{_docdir}/HTML/de/filelight
%lang(es) %doc %{_docdir}/HTML/es/filelight
%lang(et) %doc %{_docdir}/HTML/et/filelight
%lang(fr) %doc %{_docdir}/HTML/fr/filelight
%lang(it) %doc %{_docdir}/HTML/it/filelight
%lang(nl) %doc %{_docdir}/HTML/nl/filelight
%lang(pt) %doc %{_docdir}/HTML/pt/filelight
%lang(pt_BR) %doc %{_docdir}/HTML/pt_BR/filelight
%lang(sv) %doc %{_docdir}/HTML/sv/filelight
%lang(uk) %doc %{_docdir}/HTML/uk/filelight

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name}
