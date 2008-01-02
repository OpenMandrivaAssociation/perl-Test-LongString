%define module	Test-LongString
%define name	perl-%{module}
%define version	0.11
%define	release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl module to test strings for equality
License:	GPL or Artistic
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/%{module}-%{version}.tar.gz
Url:		http://search.cpan.org/dist/%{module}
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel 
BuildRequires:  perl(Test::Builder::Tester)

%description
This module provides some drop-in replacements for the string comparison
functions of Test::More, but which are more suitable when you test against long
strings. If you've ever had to search for text in a multi-line string like an
HTML document, or find specific items in binary data, this is the module for
you.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Test/*
%{_mandir}/*/*

