#
# Conditional build:
%bcond_with		csharp		# C# bindings
%bcond_without	php			# PHP bindings
%bcond_without	python		# Python bindings
%bcond_without	ruby		# Ruby bindings
%bcond_without	tcl			# TCL bindings
%bcond_with		java		# Java bindings

Summary:	Bindings for Xapian
Name:		xapian-bindings
Version:	1.0.16
Release:	2
License:	GPL v2+
Group:		Development/Languages
URL:		http://www.xapian.org/
Source0:	http://www.oligarchy.co.uk/xapian/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c330b2ccc451c890916c44446e148f07
%{?with_java:BuildRequires:	jdk}
%{?with_csharp:BuildRequires:	mono-devel}
%{?with_php:BuildRequires:	php-devel >= 4:5.0.4}
BuildRequires:	pkgconfig
%{?with_python:BuildRequires:	python-devel}
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.484
%{?with_ruby:BuildRequires:	ruby-devel}
%{?with_ruby:BuildRequires:	ruby-modules}
%{?with_tcl:BuildRequires:	tcl-devel}
BuildRequires:	xapian-core-devel >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xapian is an Open Source Probabilistic Information Retrieval Library.
It offers a highly adaptable toolkit that allows developers to easily
add advanced indexing and search facilities to applications.

%package -n python-xapian
Summary:	Files needed for developing Python scripts which use Xapian
Group:		Development/Languages/Python
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
%{?requires_php_extension}

%description -n php-xapian
Xapian is an Open Source Probabilistic Information Retrieval
framework. It offers a highly adaptable toolkit that allows developers
to easily add advanced indexing and search facilities to applications.
This package provides the files needed for developing PHP scripts
which use Xapian.

%package -n ruby-xapian
Summary:	Files needed for developing Ruby scripts which use Xapian
Group:		Development/Languages
%{?ruby_mod_ver_requires_eq}

%description -n ruby-xapian
Xapian is an Open Source Probabilistic Information Retrieval
framework. It offers a highly adaptable toolkit that allows developers
to easily add advanced indexing and search facilities to applications.
This package provides the files needed for developing Ruby scripts
which use Xapian.

%package -n tcl-xapian
Summary:	Files needed for developing TCL scripts which use Xapian
Group:		Development/Languages/Tcl
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
	%{?with_java:--with-java} \
	%{?with_python:--with-python} \
	%{?with_php:--with-php} \
	%{?with_ruby:--with-ruby} \
	%{?with_tcl:--with-tcl} \
	%{?with_csharp:--with-csharp}

# PATH=. hack needed:
# /bin/sh ../libtool  --config > libtoolconfig.tmp
# . libtoolconfig.tmp; cp $objdir/_xapian.so .
# /bin/sh: .: libtoolconfig.tmp: not found
PATH=$PATH:. %{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	phpincdir=%{php_data_dir} \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

for binding in %{?with_csharp:csharp} %{?with_php:php} %{?with_python:python} %{?with_ruby:ruby} %{?with_tcl:tcl8}; do
	install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/$binding
	cp -a $binding/docs/{index.html,examples} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/$binding
done

rm -f $RPM_BUILD_ROOT%{_libdir}/XapianSharp.la

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README TODO
%{_examplesdir}/%{name}-%{version}

%if %{with python}
%files -n python-xapian
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_xapian.so
%{py_sitedir}/xapian.py[co]
%endif

%if %{with php}
%files -n php-xapian
%defattr(644,root,root,755)
%attr(755,root,root) %{php_extensiondir}/xapian.so
%{php_data_dir}/xapian.php
%endif

%if %{with ruby}
%files -n ruby-xapian
%defattr(644,root,root,755)
%attr(755,root,root) %{ruby_sitearchdir}/_xapian.so
%{ruby_sitelibdir}/xapian.rb
%endif

%if %{with tcl}
%files -n tcl-xapian
%defattr(644,root,root,755)
%dir %{_libdir}/xapian%{version}
%{_libdir}/xapian%{version}/pkgIndex.tcl
%attr(755,root,root) %{_libdir}/xapian%{version}/xapian.so
%endif

%if %{with csharp}
%files -n csharp-xapian
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/XapianSharp.so
%dir %{_libdir}/mono
%{_libdir}/mono/XapianSharp
%dir %{_libdir}/mono/gac
%{_libdir}/mono/gac/XapianSharp
%endif
