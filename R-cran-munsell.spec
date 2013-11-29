%define		fversion	%(echo %{version} |tr r -)
%define		modulename	munsell
Summary:	Munsell colour system
Name:		R-cran-%{modulename}
Version:	0.4.2
Release:	1
License:	MIT
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	45561402fe3ffb8e534a1487bb60d938
URL:		http://cran.fhcrc.org/web/packages/munsell/index.html
BuildRequires:	R >= 2.8.1
BuildRequires:	R-cran-colorspace
Requires(post,postun):	R >= 2.8.1
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
Requires:	R
Requires:	R-cran-colorspace
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Functions for exploring and using the Munsell colour system.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library/
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION
%{_libdir}/R/library/%{modulename}
