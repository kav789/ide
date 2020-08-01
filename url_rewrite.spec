%global debug_package %{nil}

%define	name	url_rewrite
%define	version	0.0.1
%define	release	1

Summary:	url rewrite programm for squid.
Name:		%{name}
Version:	%{version}
Release:	%{release}
Prefix:		%{prefix}
License:	Public Domain
Source:		%{name}-%{version}.tar.gz
Requires:	squid  >= 3.5.27
Requires:	python >= 3.6.1
BuildRoot: %{_tmppath}/%{name}-root

%description
simple url rewrite programm for squid

%prep
%setup -q

%build
make

%install
[ "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf "$RPM_BUILD_ROOT"
mkdir -p "$RPM_BUILD_ROOT"/usr/bin
mkdir -p "$RPM_BUILD_ROOT"/etc/squid
cp url_rewrite "$RPM_BUILD_ROOT"/usr/bin
cp url_rewrite.conf "$RPM_BUILD_ROOT"/etc/squid
cp squid.conf.url_rewrite "$RPM_BUILD_ROOT"/etc/squid

%clean
[ "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf "$RPM_BUILD_ROOT"





%files
%defattr(-,root,root,-)
%doc INSTALL NEWS README
%{_bindir}/url_rewrite
/etc/squid/squid.conf.url_rewrite
%config /etc/squid/url_rewrite.conf

%changelog
* Fri Jul 31 2020 kav789 <kav789@gmail.com> 0.0.1
- create




