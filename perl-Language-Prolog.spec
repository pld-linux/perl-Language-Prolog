%include	/usr/lib/rpm/macros.perl
%define	pdir	Language
%define	pnam	Prolog
Summary:	Language::Prolog perl modules
Summary(pl):	Modu³y perla Language::Prolog
Name:		perl-Language-Prolog
Version:	alpha
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	'perl(Language::Prolog::Interpreter)'

%description
Language::Prolog perl modules - Prolog interpreter.

%description -l pl
Modu³y perla Language::Prolog - interpreter Prologa.

%package Interpreter
Summary:	Language::Prolog::Interpreter perl module
Summary(pl):	Modu³ perla Language::Prolog::Interpreter
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description Interpreter
Language::Prolog::Interpreter perl module.

%description Interpreter -l pl
Modu³ perla Language::Prolog::Interpreter.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_sitelib}/Language/Prolog

install Language/Prolog.pm $RPM_BUILD_ROOT%{perl_sitelib}/Language
install Language/Prolog/*.pm $RPM_BUILD_ROOT%{perl_sitelib}/Language/Prolog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/Language/Prolog.pm
%dir %{perl_sitelib}/Language/Prolog
%{perl_sitelib}/Language/Prolog/[^I]*.pm
%{perl_sitelib}/Language/Prolog/IndexStack.pm

%files Interpreter
%defattr(644,root,root,755)
%{perl_sitelib}/Language/Prolog/Interpreter.pm
