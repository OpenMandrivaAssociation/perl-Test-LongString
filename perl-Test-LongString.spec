%define modname	Test-LongString

Summary:	Perl module to test strings for equality
Name:		perl-%{modname}
Version:	0.17
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Test::LongString
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::Builder::Tester)
BuildRequires:	perl-devel

%description
This module provides some drop-in replacements for the string comparison
functions of Test::More, but which are more suitable when you test against long
strings. If you've ever had to search for text in a multi-line string like an
HTML document, or find specific items in binary data, this is the module for
you.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%make_install

%files
%doc Changes README
%{perl_vendorlib}/Test/*
%{_mandir}/man3/*
