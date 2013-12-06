%define modname	Test-LongString
%define modver	0.15

Summary:	Perl module to test strings for equality
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	8
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/%{modname}-%{modver}.tar.gz
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
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Test/*
%{_mandir}/man3/*

