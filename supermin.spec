Name: supermin
Version: 5.1.20
Release: 1
Source0: http://download.libguestfs.org/supermin/supermin-%{version}.tar.gz
Patch0: supermin-5.1.20-clang.patch
Patch1: supermin-5.1.20-openmandriva.patch
Summary: Tool for creating and building supermin appliances
URL: http://libguestfs.org/
License: GPL
BuildRequires: ocaml ocaml-findlib perl(Pod::Html)
BuildRequires: make
BuildRequires: pkgconfig(rpm)
# Just so autoconf can see what we are
BuildRequires: rpm dnf cpio tar e2fsprogs xz

%description
Supermin is a tool for building supermin appliances.
These are tiny appliances (similar to virtual machines),
usually around 100KB in size, which get fully instantiated
on-the-fly in a fraction of a second when you need to boot
one of them.

%prep
%autosetup -p1
%configure

%build
%make

%install
%make_install

%files
%{_bindir}/supermin
%{_mandir}/man1/supermin.1*
