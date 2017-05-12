%define debug_package          %{nil}

Name:		rdup
Summary:	Rdup backup tool
Version:	1.1.15
Release:	2
Source0:	http://github.com/miekg/rdup/releases/rdup-%{version}.tar.gz
URL:		http://github.com/miekg/rdup
License:	GPL
Group:		Archiving/Backup
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pcre-devel
BuildRequires:  libarchive-devel
BuildRequires:	nettle-devel

%description
rdup is a platform for backups. It provides a list of files to backup 
and the necessary mechanisms to process them. It delegates the 
encryption, compression, transfer and packaging to other utilities 
in a true Unix-way.

%prep
%setup -q 
%apply_patches
autoreconf -fiv

%build
%configure2_5x
make GCC='gcc %ldflags'

%install
make install DESTDIR=%buildroot

%files
%doc todo 
%_bindir/rdup
%_bindir/rdup-tr
%_bindir/rdup-up
%_bindir/rdup-simple
%_mandir/man1/*
%_mandir/man7/*

