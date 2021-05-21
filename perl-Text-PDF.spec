#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Text-PDF
Version  : 0.31
Release  : 13
URL      : https://cpan.metacpan.org/authors/id/B/BH/BHALLISSY/Text-PDF-0.31.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BH/BHALLISSY/Text-PDF-0.31.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtext-pdf-perl/libtext-pdf-perl_0.31-1.debian.tar.xz
Summary  : 'PDF Manipulation and generation'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Text-PDF-bin = %{version}-%{release}
Requires: perl-Text-PDF-license = %{version}-%{release}
Requires: perl-Text-PDF-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Text::PDF
There seem to be a growing plethora of Perl modules for creating and
manipulating PDF files. This module is no exception. Beyond the standard
features you would expect from a PDF manipulation module there are:

%package bin
Summary: bin components for the perl-Text-PDF package.
Group: Binaries
Requires: perl-Text-PDF-license = %{version}-%{release}

%description bin
bin components for the perl-Text-PDF package.


%package dev
Summary: dev components for the perl-Text-PDF package.
Group: Development
Requires: perl-Text-PDF-bin = %{version}-%{release}
Provides: perl-Text-PDF-devel = %{version}-%{release}
Requires: perl-Text-PDF = %{version}-%{release}

%description dev
dev components for the perl-Text-PDF package.


%package license
Summary: license components for the perl-Text-PDF package.
Group: Default

%description license
license components for the perl-Text-PDF package.


%package perl
Summary: perl components for the perl-Text-PDF package.
Group: Default
Requires: perl-Text-PDF = %{version}-%{release}

%description perl
perl components for the perl-Text-PDF package.


%prep
%setup -q -n Text-PDF-0.31
cd %{_builddir}
tar xf %{_sourcedir}/libtext-pdf-perl_0.31-1.debian.tar.xz
cd %{_builddir}/Text-PDF-0.31
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Text-PDF-0.31/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Text-PDF
cp %{_builddir}/Text-PDF-0.31/LICENSE %{buildroot}/usr/share/package-licenses/perl-Text-PDF/09aa60e68ba922665fa60c4169d550aa34a94c2e
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Text-PDF/ee54a13446ab9316d82df3cc0b153c362030e1b4
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pdfbklt
/usr/bin/pdfrevert
/usr/bin/pdfstamp

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Text::PDF.3
/usr/share/man/man3/Text::PDF::Array.3
/usr/share/man/man3/Text::PDF::Bool.3
/usr/share/man/man3/Text::PDF::Dict.3
/usr/share/man/man3/Text::PDF::File.3
/usr/share/man/man3/Text::PDF::Filter.3
/usr/share/man/man3/Text::PDF::Name.3
/usr/share/man/man3/Text::PDF::Null.3
/usr/share/man/man3/Text::PDF::Number.3
/usr/share/man/man3/Text::PDF::Objind.3
/usr/share/man/man3/Text::PDF::Page.3
/usr/share/man/man3/Text::PDF::Pages.3
/usr/share/man/man3/Text::PDF::SFont.3
/usr/share/man/man3/Text::PDF::String.3
/usr/share/man/man3/Text::PDF::TTFont.3
/usr/share/man/man3/Text::PDF::TTFont0.3
/usr/share/man/man3/Text::PDF::Utils.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Text-PDF/09aa60e68ba922665fa60c4169d550aa34a94c2e
/usr/share/package-licenses/perl-Text-PDF/ee54a13446ab9316d82df3cc0b153c362030e1b4

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Text/PDF.pm
/usr/lib/perl5/vendor_perl/5.34.0/Text/PDF/Array.pm
/usr/lib/perl5/vendor_perl/5.34.0/Text/PDF/Bool.pm
/usr/lib/perl5/vendor_perl/5.34.0/Text/PDF/Dict.pm
/usr/lib/perl5/vendor_perl/5.34.0/Text/PDF/File.pm
/usr/lib/perl5/vendor_perl/5.34.0/Text/PDF/Filter.pm
/usr/lib/perl5/vendor_perl/5.34.0/Text/PDF/Name.pm
/usr/lib/perl5/vendor_perl/5.34.0/Text/PDF/Null.pm
/usr/lib/perl5/vendor_perl/5.34.0/Text/PDF/Number.pm
/usr/lib/perl5/vendor_perl/5.34.0/Text/PDF/Objind.pm
/usr/lib/perl5/vendor_perl/5.34.0/Text/PDF/Page.pm
/usr/lib/perl5/vendor_perl/5.34.0/Text/PDF/Pages.pm
/usr/lib/perl5/vendor_perl/5.34.0/Text/PDF/SFont.pm
/usr/lib/perl5/vendor_perl/5.34.0/Text/PDF/String.pm
/usr/lib/perl5/vendor_perl/5.34.0/Text/PDF/TTFont.pm
/usr/lib/perl5/vendor_perl/5.34.0/Text/PDF/TTFont0.pm
/usr/lib/perl5/vendor_perl/5.34.0/Text/PDF/Utils.pm
