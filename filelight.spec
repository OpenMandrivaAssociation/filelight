%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Graphical disk usage statistics
Name:		filelight
Version:	15.04.0
Release:	1
Group:		Graphical desktop/KDE
License:	LGPLv2
Url:		http://utils.kde.org/projects/filelight/
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz

%description
Filelight allows you to quickly understand exactly where your
diskspace is being used by graphically representing your file
system as a set of concentric segmented-rings. You can use it
to locate hotspots of disk usage and then manipulate those
areas using a file manager.

%files
%doc %{_docdir}/HTML/en/filelight
%{_sysconfdir}/xdg/*
%{_libdir}/plugins/filelightpart.so
%{_bindir}/filelight
%{_datadir}/applications/org.kde.filelight.desktop
%{_iconsdir}/*/*/actions/views_filelight.*
%{_iconsdir}/*/*/apps/filelight.*
%{_datadir}/kservices5/filelightpart.desktop
%{_datadir}/kxmlgui5/filelight
%{_datadir}/kxmlgui5/filelightpart

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake -G Ninja
ninja

%install
DESTDIR="%{buildroot}" ninja -C build install
