#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Encode
%define		pnam	HanExtra
Summary:	Encode::HanExtra - Extra sets of Chinese encodings
Summary(pl.UTF-8):	Encode::HanExtra - Dodatkowe zestawy mapowań chińskich
Name:		perl-Encode-HanExtra
Version:	0.23
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Encode/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e1d3bc32c1c8ee304235a06fbcd5d5a4
URL:		http://search.cpan.org/dist/Encode-HanExtra/
BuildRequires:	perl(Encode) >= 2.09
%{?with_tests:BuildRequires:  perl-Module-Signature}
BuildRequires:	perl-devel >= 1:5.7.3
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In the 1950's, the Chinese government simplified over 2000 Chinese
characters. Taiwan and Hong Kong still use the traditional characters.
The simplified characters are hard to read if you only know the
traditional ones, and vice-versa. This module attempts to convert
Chinese text between the two forms, using character-by-character
transliteration.

%description -l pl.UTF-8
W latach 1950-tych rząd chiński uprościł ponad 2000 chińskich
ideogramów. Tajwan i Hong Kong nadal używają ideogramów tradycyjnych.
Ideogramy uproszczone są trudne do odczytania dla znających tylko
tradycyjne i odwrotnie. Moduł próbuje konwertować teksty chińskie
pomiędzy tymi postaciami stosując transliterację znak po znaku.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorarch}/Encode/HanExtra.pm
%dir %{perl_vendorarch}/Encode/TW
%dir %{perl_vendorarch}/Encode/TW/Unisys
%{perl_vendorarch}/Encode/TW/Unisys/*.pm
%dir %{perl_vendorarch}/auto/Encode/HanExtra
%{perl_vendorarch}/auto/Encode/HanExtra/HanExtra.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Encode/HanExtra/HanExtra.so
%{_mandir}/man3/*.3*
