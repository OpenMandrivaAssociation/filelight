Name:    filelight
Summary: Graphical disk usage statistics
Version: 4.7.90
Release: 1
Group: Graphical desktop/KDE
License: LGPLv2
URL:     http://utils.kde.org/projects/filelight/
Source:  ftp://ftp.kde.org/pub/kde/stable/%version/src/%{name}-%version.tar.bz2

BuildRequires: kdelibs4-devel >= 2:%{version}

%description
Filelight allows you to quickly understand exactly where your
diskspace is being used by graphically representing your file
system as a set of concentric segmented-rings. You can use it
to locate hotspots of disk usage and then manipulate those
areas using a file manager.

%files
%_kde_bindir/filelight
%_kde_libdir/kde4/filelightpart.so
%_kde_applicationsdir/filelight.desktop
%_kde_appsdir/filelight
%_kde_appsdir/filelightpart
%_kde_iconsdir/*/*/actions/view_filelight.*
%_kde_iconsdir/*/*/apps/filelight.*
%_kde_configdir/filelightrc
%_kde_services/filelightpart.desktop
%doc %_kde_docdir/HTML/en/filelight

#----------------------------------------------------------------------

%prep
%setup -q 

%build
%cmake_kde4
	
%make

%install
%makeinstall_std -C build

