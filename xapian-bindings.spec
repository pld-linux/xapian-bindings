# Conditional build:
%bcond_with	csharp		# do not build C# bindings
%bcond_without	php			# do not build PHP bindings
%bcond_without	python		# do not build Python bindings
%bcond_without	ruby		# do not build Ruby bindings
%bcond_without	tcl			# do not build TCL bindings
#
Summary:	Bindings for Xapian
Name:		xapian-bindings
Version:	1.0.4
Release:	0.1
License:	GPL
Group:		Development/Languages
URL:		http://www.xapian.org/
Source0:	http://www.oligarchy.co.uk/xapian/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d572e0bec4c4c26f26224e1253c4aa8f
# jdk??
BuildRequires:	jdk
%{?with_csharp:BuildRequires:	mono-devel}
%{?with_php:BuildRequires:	php-devel >= 3:5.0.0}
BuildRequires:	pkgconfig
%{?with_python:BuildRequires:	python-devel}
BuildRequires:	rpmbuild(macros) >= 1.344
%{?with_ruby:BuildRequires:	ruby-devel}
%{?with_tcl:BuildRequires:	tcl-devel}
BuildRequires:	xapian-core-devel = %{version}
Requires:	xapian-core-libs = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xapian is an Open Source Probabilistic Information Retrieval Library.
It offers a highly adaptable toolkit that allows developers to easily
add advanced indexing and search facilities to applications.

%package -n python-xapian
Summary:	Files needed for developing Python scripts which use Xapian
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq	python-modules

%description -n python-xapian
Xapian is an Open Source Probabilistic Information Retrieval
framework. It offers a highly adaptable toolkit that allows developers
to easily add advanced indexing and search facilities to applications.
This package provides the files needed for developing Python scripts
which use Xapian.

%package -n php-xapian
Summary:	Files needed for developing PHP scripts which use Xapian
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4

%description -n php-xapian
Xapian is an Open Source Probabilistic Information Retrieval
framework. It offers a highly adaptable toolkit that allows developers
to easily add advanced indexing and search facilities to applications.
This package provides the files needed for developing PHP scripts
which use Xapian.

%package -n ruby-xapian
Summary:	Files needed for developing Ruby scripts which use Xapian
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
Requires:	ruby

%description -n ruby-xapian
Xapian is an Open Source Probabilistic Information Retrieval
framework. It offers a highly adaptable toolkit that allows developers
to easily add advanced indexing and search facilities to applications.
This package provides the files needed for developing Ruby scripts
which use Xapian.

%package -n tcl-xapian
Summary:	Files needed for developing TCL scripts which use Xapian
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}-%{release}
Requires:	tcl

%description -n tcl-xapian
Xapian is an Open Source Probabilistic Information Retrieval
framework. It offers a highly adaptable toolkit that allows developers
to easily add advanced indexing and search facilities to applications.
This package provides the files needed for developing TCL scripts
which use Xapian.

%package -n csharp-xapian
Summary:	Files needed for developing C# applications which use Xapian
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
Requires:	mono-core

%description -n csharp-xapian
Xapian is an Open Source Probabilistic Information Retrieval
framework. It offers a highly adaptable toolkit that allows developers
to easily add advanced indexing and search facilities to applications.
This package provides the files needed for developing C# applications
which use Xapian.

%prep
%setup -q

%build
%configure \
	--with-swig \
	%{?with_python:--with-python} \
	%{?with_php:--with-php} \
	%{?with_ruby:--with-ruby} \
	%{?with_tcl:--with-tcl} \
	%{?with_csharp:--with-csharp}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

for binding in %{?with_csharp:csharp} %{?with_php:php} %{?with_python:python} %{?with_ruby:ruby} %{?with_tcl:tcl8}; do
	install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/$binding
	cp -a $binding/docs/{index.html,examples} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/$binding
done

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README TODO
%dir %{_examplesdir}/%{name}-%{version}

%if %{with python}
%files -n python-xapian
%defattr(644,root,root,755)
%{py_sitedir}/_xapian.so
%{py_sitedir}/xapian.py[co]
%{_examplesdir}/%{name}-%{version}/python
%endif

%if %{with php}
%files -n php-xapian
%defattr(644,root,root,755)
%{php_extensiondir}/xapian.so
%{php_data_dir}5/xapian.php
%{_examplesdir}/%{name}-%{version}/php
%endif

%if %{with ruby}
%files -n ruby-xapian
%defattr(644,root,root,755)
%attr(755,root,root) %{ruby_sitearchdir}/_xapian.so
%{ruby_sitelibdir}/xapian.rb

%{_examplesdir}/%{name}-%{version}/ruby
%endif

%if %{with tcl}
%files -n tcl-xapian
%defattr(644,root,root,755)
%dir %{_libdir}/xapian%{version}
%{_libdir}/xapian%{version}/pkgIndex.tcl
%attr(755,root,root) %{_libdir}/xapian%{version}/xapian.so
%{_examplesdir}/%{name}-%{version}/tcl8
%endif

%if %{with csharp}
%files -n csharp-xapian
%defattr(644,root,root,755)
%{_libdir}/XapianSharp.la
%{_libdir}/XapianSharp.so
%dir %{_libdir}/mono
%{_libdir}/mono/XapianSharp
%dir %{_libdir}/mono/gac
%{_libdir}/mono/gac/XapianSharp
%{_examplesdir}/%{name}-%{version}/csharp
%endif
