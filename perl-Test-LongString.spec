%define upstream_name	 Test-LongString
%define upstream_version 0.15

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Perl module to test strings for equality
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Test::Builder::Tester)
BuildRequires:	perl-devel

BuildArch:	noarch

%description
This module provides some drop-in replacements for the string comparison
functions of Test::More, but which are more suitable when you test against long
strings. If you've ever had to search for text in a multi-line string like an
HTML document, or find specific items in binary data, this is the module for
you.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Test/*
%{_mandir}/*/*

%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.150.0-4mdv2012.0
+ Revision: 765684
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.150.0-3
+ Revision: 764234
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.150.0-2
+ Revision: 667326
- mass rebuild

* Tue Feb 08 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.150.0-1
+ Revision: 636802
- update to new version 0.15

* Thu Nov 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.140.0-1mdv2011.0
+ Revision: 596037
- update to new version 0.14

* Mon Feb 01 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.130.0-1mdv2011.0
+ Revision: 498986
- update to 0.13

* Tue Jan 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.120.0-1mdv2010.1
+ Revision: 490069
- update to 0.12

* Fri Jul 24 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.110.0-1mdv2010.0
+ Revision: 399256
- rebuild
- using %%perl_convert_version
- fixed license field

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.11-3mdv2009.0
+ Revision: 241982
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu May 03 2007 Olivier Thauvin <nanardon@mandriva.org> 0.11-1mdv2008.0
+ Revision: 22108
- 0.11


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.09-2mdk
- Fix SPEC according to Perl Policy
	- Source URL
- use mkrel

* Thu Oct 06 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.09-1mdk
- 0.09

* Tue Aug 16 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.08-1mdk
- 0.08

* Tue Dec 14 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.07-1mdk
- 0.07

* Thu Dec 09 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.05-1mdk
- Initial MDK release.

