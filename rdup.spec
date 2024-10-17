%define debug_package          %{nil}

Name:		rdup
Summary:	Rdup backup tool
Version:	1.1.15
Release:	8
Source0:	http://github.com/miekg/rdup/releases/rdup-%{version}.tar.gz
Patch1:		f08178e5de0d31cbd9bf17ab541a621a6f1f93fc.patch
# limit to aes256 
Patch2:		rdup-nettle3.5.patch
Patch3:		rdup-1.1.5-pcre2.patch
Patch4:		rdup-1.1.5-install.patch
URL:		https://github.com/miekg/rdup
License:	GPL
Group:		Archiving/Backup
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:	pkgconfig(nettle)

%description
rdup is a platform for backups. It provides a list of files to backup 
and the necessary mechanisms to process them. It delegates the 
encryption, compression, transfer and packaging to other utilities 
in a true Unix-way.

%prep
%autosetup -p1
autoreconf -fiv

%build
%configure
%make_build

%install
%make_install

%files
%doc todo 
%_bindir/rdup
%_bindir/rdup-tr
%_bindir/rdup-up
%_bindir/rdup-simple
%_mandir/man1/*
%_mandir/man7/*
