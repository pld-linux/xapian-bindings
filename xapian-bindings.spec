# NOTE: for perl binding, see perl-Search-Xapian.spec
# TODO: python3- after upgrade to 1.3.x/1.4.x
#
# Conditional build:
%bcond_without	dotnet		# C# bindings
%bcond_without	java		# Java bindings
%bcond_without	lua		# Lua bindings
%bcond_without	php		# PHP bindings
%bcond_without	python		# Python bindings
%bcond_without	ruby		# Ruby bindings
%bcond_without	tcl		# Tcl bindings

Summary:	Bindings for Xapian
Summary(pl.UTF-8):	Wiązania do Xapiana
Name:		xapian-bindings
Version:	1.2.21
Release:	3
License:	GPL v2+
Group:		Development/Languages
Source0:	http://oligarchy.co.uk/xapian/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	33c598a26fcf92ab15af6c65475ab8de
Patch0:		python-install.patch
URL:		http://www.xapian.org/
%{?with_java:BuildRequires:	jdk >= 1.2}
%{?with_java:BuildRequires:	jpackage-utils}
%{?with_lua:BuildRequires:	lua51-devel >= 5.1.5-2}
# 2.6.x should be sufficient, but 2.11.1 complaints about write permissions to /usr/share/.mono/keypairs
%{?with_dotnet:BuildRequires:	mono-devel >= 2.11.4}
%{?with_php:BuildRequires:	%{php_name}-devel >= 4:5.0.4}
BuildRequires:	pkgconfig
%{?with_python:BuildRequires:	python-devel >= 1:2.3}
BuildRequires:	python-modules >= 1:2.3
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.665
%{?with_ruby:BuildRequires:	ruby-devel >= 1.8}
%{?with_ruby:BuildRequires:	ruby-modules >= 1.8}
%{?with_ruby:BuildRequires:	rpm-rubyprov}
%{?with_tcl:BuildRequires:	tcl-devel >= 8.1}
BuildRequires:	xapian-core-devel >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xapian is an Open Source Probabilistic Information Retrieval Library.
It offers a highly adaptable toolkit that allows developers to easily
add advanced indexing and search facilities to applications. This
package is a collection of bindings for different programming
languages.

%description -l pl.UTF-8
Xapian to mająca otwarte źródła biblioteka do uzyskiwania informacji
probabilistycznych. Oferuje wysoce adoptowalne narzędzia pozwalające
programistom łatwo dodawać do aplikacji zaawansowane możliwości
indeksowania i wyszukiwania. Ten pakiet zawiera zestaw wiązań dla
różnych języków programowania.

%package -n dotnet-xapian
Summary:	Files needed for developing C# applications which use Xapian
Summary(pl.UTF-8):	Pliki do tworzenia aplikacji C# wykorzystujących Xapiana
Group:		Development/Languages
Requires:	mono >= 2.6.7
Obsoletes:	csharp-xapian

%description -n dotnet-xapian
Xapian is an Open Source Probabilistic Information Retrieval
framework. It offers a highly adaptable toolkit that allows developers
to easily add advanced indexing and search facilities to applications.
This package provides the files needed for developing C# applications
which use Xapian.

%description -n dotnet-xapian -l pl.UTF-8
Xapian to mająca otwarte źródła biblioteka do uzyskiwania informacji
probabilistycznych. Oferuje wysoce adoptowalne narzędzia pozwalające
programistom łatwo dodawać do aplikacji zaawansowane możliwości
indeksowania i wyszukiwania. Ten pakiet zawiera pliki potrzebne przy
tworzeniu aplikacji C# wykorzystujących Xapiana.

%package -n java-xapian
Summary:	Files needed for developing Java applications which use Xapian
Summary(pl.UTF-8):	Pliki do tworzenia aplikacji Javy wykorzystujących Xapiana
Group:		Libraries/Java
Requires:	jpackage-utils
Requires:	jre

%description -n java-xapian
Xapian is an Open Source Probabilistic Information Retrieval
framework. It offers a highly adaptable toolkit that allows developers
to easily add advanced indexing and search facilities to applications.
This package provides the files needed for developing Java
applications which use Xapian.

%description -n java-xapian -l pl.UTF-8
Xapian to mająca otwarte źródła biblioteka do uzyskiwania informacji
probabilistycznych. Oferuje wysoce adoptowalne narzędzia pozwalające
programistom łatwo dodawać do aplikacji zaawansowane możliwości
indeksowania i wyszukiwania. Ten pakiet zawiera pliki potrzebne przy
tworzeniu aplikacji Javy wykorzystujących Xapiana.

%package -n lua-xapian
Summary:	Files needed for developing Lua scripts which use Xapian
Summary(pl.UTF-8):	Pliki do tworzenia skryptów w języku Lua wykorzystujących Xapiana
Group:		Development/Languages
Requires:	lua51-libs

%description -n lua-xapian
Xapian is an Open Source Probabilistic Information Retrieval
framework. It offers a highly adaptable toolkit that allows developers
to easily add advanced indexing and search facilities to applications.
This package provides the files needed for developing Lua scripts
which use Xapian.

%description -n lua-xapian -l pl.UTF-8
Xapian to mająca otwarte źródła biblioteka do uzyskiwania informacji
probabilistycznych. Oferuje wysoce adoptowalne narzędzia pozwalające
programistom łatwo dodawać do aplikacji zaawansowane możliwości
indeksowania i wyszukiwania. Ten pakiet zawiera pliki potrzebne przy
tworzeniu skryptów w języku Lua wykorzystujących Xapiana.

%package -n %{php_name}-xapian
Summary:	Files needed for developing PHP scripts which use Xapian
Summary(pl.UTF-8):	Pliki do tworzenia skryptów w PHP wykorzystujących Xapiana
Group:		Development/Languages/PHP
%{?requires_php_extension}

%description -n %{php_name}-xapian
Xapian is an Open Source Probabilistic Information Retrieval
framework. It offers a highly adaptable toolkit that allows developers
to easily add advanced indexing and search facilities to applications.
This package provides the files needed for developing PHP scripts
which use Xapian.

%description -n %{php_name}-xapian -l pl.UTF-8
Xapian to mająca otwarte źródła biblioteka do uzyskiwania informacji
probabilistycznych. Oferuje wysoce adoptowalne narzędzia pozwalające
programistom łatwo dodawać do aplikacji zaawansowane możliwości
indeksowania i wyszukiwania. Ten pakiet zawiera pliki potrzebne przy
tworzeniu skryptów w PHP wykorzystujących Xapiana.

%package -n python-xapian
Summary:	Files needed for developing Python scripts which use Xapian
Summary(pl.UTF-8):	Pliki do tworzenia skryptów w Pythonie wykorzystujących Xapiana
Group:		Development/Languages/Python
%pyrequires_eq	python-modules

%description -n python-xapian
Xapian is an Open Source Probabilistic Information Retrieval
framework. It offers a highly adaptable toolkit that allows developers
to easily add advanced indexing and search facilities to applications.
This package provides the files needed for developing Python scripts
which use Xapian.

%description -n python-xapian -l pl.UTF-8
Xapian to mająca otwarte źródła biblioteka do uzyskiwania informacji
probabilistycznych. Oferuje wysoce adoptowalne narzędzia pozwalające
programistom łatwo dodawać do aplikacji zaawansowane możliwości
indeksowania i wyszukiwania. Ten pakiet zawiera pliki potrzebne przy
tworzeniu skryptów w Pythonie wykorzystujących Xapiana.

%package -n ruby-xapian
Summary:	Files needed for developing Ruby scripts which use Xapian
Summary(pl.UTF-8):	Pliki do tworzenia skryptów w języku Ruby wykorzystujących Xapiana
Group:		Development/Languages

%description -n ruby-xapian
Xapian is an Open Source Probabilistic Information Retrieval
framework. It offers a highly adaptable toolkit that allows developers
to easily add advanced indexing and search facilities to applications.
This package provides the files needed for developing Ruby scripts
which use Xapian.

%description -n ruby-xapian -l pl.UTF-8
Xapian to mająca otwarte źródła biblioteka do uzyskiwania informacji
probabilistycznych. Oferuje wysoce adoptowalne narzędzia pozwalające
programistom łatwo dodawać do aplikacji zaawansowane możliwości
indeksowania i wyszukiwania. Ten pakiet zawiera pliki potrzebne przy
tworzeniu skryptów w języku Ruby wykorzystujących Xapiana.

%package -n tcl-xapian
Summary:	Files needed for developing Tcl scripts which use Xapian
Summary(pl.UTF-8):	Pliki do tworzenia skryptów w Tcl-u wykorzystujących Xapiana
Group:		Development/Languages/Tcl
Requires:	tcl >= 8.1

%description -n tcl-xapian
Xapian is an Open Source Probabilistic Information Retrieval
framework. It offers a highly adaptable toolkit that allows developers
to easily add advanced indexing and search facilities to applications.
This package provides the files needed for developing TCL scripts
which use Xapian.

%description -n tcl-xapian -l pl.UTF-8
Xapian to mająca otwarte źródła biblioteka do uzyskiwania informacji
probabilistycznych. Oferuje wysoce adoptowalne narzędzia pozwalające
programistom łatwo dodawać do aplikacji zaawansowane możliwości
indeksowania i wyszukiwania. Ten pakiet zawiera pliki potrzebne przy
tworzeniu skryptów w Tcl-u wykorzystujących Xapiana.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
CLASSPATH="." \
RUBY_LIB=%{ruby_vendorlibdir} \
RUBY_LIB_ARCH=%{ruby_vendorarchdir} \
%configure \
	%{?with_lua:LUA=/usr/bin/lua5.1 LUA_INC=/usr/include/lua51} \
	%{?with_dotnet:--with-csharp} \
	%{?with_java:--with-java} \
	%{?with_lua:--with-lua} \
	%{?with_python:--with-python} \
	%{?with_php:--with-php} \
	%{?with_ruby:--with-ruby} \
	%{?with_tcl:--with-tcl}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	jnidir=%{_jnidir} \
	phpincdir=%{php_data_dir}

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%if %{with java}
install -D java/built/xapian_jni.jar $RPM_BUILD_ROOT%{_javadir}/xapian_jni-%{version}.jar
ln -sf xapian_jni-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/xapian_jni.jar
%endif

for binding in %{?with_dotnet:csharp} %{?with_php:php} %{?with_python:python} %{?with_ruby:ruby} %{?with_tcl:tcl8}; do
	install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/$binding
	cp -a $binding/docs/{index.html,examples} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/$binding
done

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README TODO
%{_examplesdir}/%{name}-%{version}

%if %{with dotnet}
%files -n dotnet-xapian
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/_XapianSharp.so
%dir %{_libdir}/mono
%{_libdir}/mono/XapianSharp
%dir %{_libdir}/mono/gac
%{_libdir}/mono/gac/XapianSharp
%endif

%if %{with java}
%files -n java-xapian
%defattr(644,root,root,755)
%attr(755,root,root) %{_jnidir}/libxapian_jni.so
%{_javadir}/xapian_jni-%{version}.jar
%{_javadir}/xapian_jni.jar
%endif

%if %{with lua}
%files -n lua-xapian
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lua/5.1/xapian.so
%endif

%if %{with php}
%files -n %{php_name}-xapian
%defattr(644,root,root,755)
%attr(755,root,root) %{php_extensiondir}/xapian.so
%{php_data_dir}/xapian.php
%endif

%if %{with python}
%files -n python-xapian
%defattr(644,root,root,755)
%dir %{py_sitedir}/xapian
%attr(755,root,root) %{py_sitedir}/xapian/_xapian.so
%{py_sitedir}/xapian/__init__.py[co]
%endif

%if %{with ruby}
%files -n ruby-xapian
%defattr(644,root,root,755)
%attr(755,root,root) %{ruby_vendorarchdir}/_xapian.so
%{ruby_vendorlibdir}/xapian.rb
%endif

%if %{with tcl}
%files -n tcl-xapian
%defattr(644,root,root,755)
%dir %{_libdir}/xapian%{version}
%{_libdir}/xapian%{version}/pkgIndex.tcl
%attr(755,root,root) %{_libdir}/xapian%{version}/xapian.so
%endif
