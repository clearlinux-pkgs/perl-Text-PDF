#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Text-PDF
Version  : 0.31
Release  : 8
URL      : https://cpan.metacpan.org/authors/id/B/BH/BHALLISSY/Text-PDF-0.31.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BH/BHALLISSY/Text-PDF-0.31.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtext-pdf-perl/libtext-pdf-perl_0.31-1.debian.tar.xz
Summary  : 'PDF Manipulation and generation'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Text-PDF-bin = %{version}-%{release}
Requires: perl-Text-PDF-license = %{version}-%{release}
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

%description dev
dev components for the perl-Text-PDF package.


%package license
Summary: license components for the perl-Text-PDF package.
Group: Default

%description license
license components for the perl-Text-PDF package.


%prep
%setup -q -n Text-PDF-0.31
cd ..
%setup -q -T -D -n Text-PDF-0.31 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Text-PDF-0.31/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Text-PDF
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Text-PDF/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Text-PDF/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.2/Text/PDF.pm
/usr/lib/perl5/vendor_perl/5.28.2/Text/PDF/Array.pm
/usr/lib/perl5/vendor_perl/5.28.2/Text/PDF/Bool.pm
/usr/lib/perl5/vendor_perl/5.28.2/Text/PDF/Dict.pm
/usr/lib/perl5/vendor_perl/5.28.2/Text/PDF/File.pm
/usr/lib/perl5/vendor_perl/5.28.2/Text/PDF/Filter.pm
/usr/lib/perl5/vendor_perl/5.28.2/Text/PDF/Name.pm
/usr/lib/perl5/vendor_perl/5.28.2/Text/PDF/Null.pm
/usr/lib/perl5/vendor_perl/5.28.2/Text/PDF/Number.pm
/usr/lib/perl5/vendor_perl/5.28.2/Text/PDF/Objind.pm
/usr/lib/perl5/vendor_perl/5.28.2/Text/PDF/Page.pm
/usr/lib/perl5/vendor_perl/5.28.2/Text/PDF/Pages.pm
/usr/lib/perl5/vendor_perl/5.28.2/Text/PDF/SFont.pm
/usr/lib/perl5/vendor_perl/5.28.2/Text/PDF/String.pm
/usr/lib/perl5/vendor_perl/5.28.2/Text/PDF/TTFont.pm
/usr/lib/perl5/vendor_perl/5.28.2/Text/PDF/TTFont0.pm
/usr/lib/perl5/vendor_perl/5.28.2/Text/PDF/Utils.pm

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
/usr/share/package-licenses/perl-Text-PDF/LICENSE
/usr/share/package-licenses/perl-Text-PDF/deblicense_copyright
