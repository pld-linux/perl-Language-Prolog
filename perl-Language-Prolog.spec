%define		pdir	Language
%define		pnam	Prolog
Summary:	Language::Prolog perl modules
Summary(pl.UTF-8):	Moduły perla Language::Prolog
Name:		perl-Language-Prolog
Version:	alpha
Release:	5
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	5711cc77c433e5943f61b7557dd11c05
URL:		http://search.cpan.org/dist/Language-Prolog/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	'perl(Language::Prolog::Interpreter)'

%description
Language::Prolog perl modules - Prolog interpreter.

%description -l pl.UTF-8
Moduły perla Language::Prolog - interpreter Prologa.

%package Interpreter
Summary:	Language::Prolog::Interpreter perl module
Summary(pl.UTF-8):	Moduł perla Language::Prolog::Interpreter
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description Interpreter
Language::Prolog::Interpreter perl module.

%description Interpreter -l pl.UTF-8
Moduł perla Language::Prolog::Interpreter.

%prep
%setup -q -c

%build
touch Makefile.PL; mkdir lib; mv Language lib
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"Language::Prolog")' \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Language/Prolog.pm
%dir %{perl_vendorlib}/Language/Prolog
%{perl_vendorlib}/Language/Prolog/[^I]*.pm
%{perl_vendorlib}/Language/Prolog/IndexStack.pm

%files Interpreter
%defattr(644,root,root,755)
%{perl_vendorlib}/Language/Prolog/Interpreter.pm
