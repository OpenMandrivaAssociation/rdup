%define	name	rdup
%define	version	0.6.5
%define	release	%mkrel 1
%define	summary Rdup backup tool

Name:		%{name}
Summary:	%{summary}
Version:	%{version}
Release:	%{release}
Source0:	http://www.miek.nl/projects/rdup/rdup-%{version}.tar.bz2
URL:		http://www.miek.nl/blog/articles/rdup/index.html
License:	GPL
Group:		Archiving/Backup
BuildRoot:	 %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	glib2-devel 
BuildRequires:	pcre-devel
BuildRequires:  libarchive-devel

%description
rdup is a platform for backups. It provides a list of files to backup 
and the necessary mechanisms to process them. It delegates the 
encryption, compression, transfer and packaging to other utilities 
in a true Unix-way.

%prep
%setup -q 

%build
%configure
%make

%install
rm -rf %{buildroot}

%makeinstall

%clean
rm -rf %{buildroot}

%files
%doc todo 
%_bindir/rdup
%_bindir/rdup-tr
%_bindir/rdup-up
%dir %_libdir/rdup/
%_libdir/rdup/*
%_mandir/man1/*
%_mandir/man7/*

