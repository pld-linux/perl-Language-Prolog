%include	/usr/lib/rpm/macros.perl
%define	pdir	Language
%define	pnam	Prolog
Summary:	Language::Prolog perl modules
Summary(pl):	Modu³y perla Language::Prolog
Name:		perl-Language-Prolog
Version:	alpha
Release:	3
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
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

%build
touch Makefile.PL; mkdir lib; mv Language lib
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"Language::Prolog")'
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
