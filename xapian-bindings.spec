#
# Conditional build:
%bcond_without	dotnet		# C# bindings
%bcond_without	java		# Java bindings
%bcond_without	lua		# Lua bindings
%bcond_without	perl		# Perl bindings
%bcond_with	php		# PHP bindings
%bcond_without	python2		# Python 2 bindings
%bcond_without	python3		# Python 3 bindings
%bcond_without	ruby		# Ruby bindings
%bcond_without	tcl		# Tcl bindings

%ifarch x32
%undefine	with_dotnet
%endif

%{?with_java:%{?use_default_jdk}}

Summary:	Bindings for Xapian
Summary(pl.UTF-8):	Wiązania do Xapiana
Name:		xapian-bindings
Version:	1.4.18
Release:	7
License:	GPL v2+
Group:		Development/Languages
Source0:	https://oligarchy.co.uk/xapian/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	b9e5abec087824ede77a885d0bafd6af
Patch0:		python-install.patch
URL:		https://xapian.org/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.12.2
%{?with_java:%buildrequires_jdk}
%{?with_java:BuildRequires:	jpackage-utils}
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtool >= 2:2.2.6
%{?with_lua:BuildRequires:	lua51-devel >= 5.1.5-7}
# 2.6.x should be sufficient, but 2.11.1 complaints about write permissions to /usr/share/.mono/keypairs
%{?with_dotnet:BuildRequires:	mono-devel >= 2.11.4}
%{?with_perl:BuildRequires:	perl-devel >= 1:5.8.0}
%{?with_php:BuildRequires:	%{php_name}-devel >= 4:5.0.4}
BuildRequires:	pkgconfig
%{?with_python2:BuildRequires:	python-Sphinx}
%{?with_python2:BuildRequires:	python-devel >= 1:2.6}
%{?with_python3:BuildRequires:	python3-Sphinx}
%{?with_python3:BuildRequires:	python3-devel >= 1:3.2}
BuildRequires:	python-modules >= 1:2.3
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.021
%{?with_ruby:BuildRequires:	rpm-rubyprov}
%{?with_ruby:BuildRequires:	ruby-devel >= 1.8}
%{?with_ruby:BuildRequires:	ruby-modules >= 1.8}
%{?with_tcl:BuildRequires:	tcl-devel >= 8.1}
BuildRequires:	xapian-core-devel >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if %{with php}
%if "%{php_major_version}" >= "7"
%define		phpbindname	php7
%else
%define		phpbindname	php
%endif
%endif

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
Requires:	xapian-core-libs >= %{version}
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
Requires:	xapian-core-libs >= %{version}

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
Requires:	xapian-core-libs >= %{version}

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

%package -n perl-Xapian
Summary:	Xapian - Perl XS frontend to the Xapian C++ search library
Summary(pl.UTF-8):	Xapian - interfejs Perlowy XS do biblioteki wyszukiwania Xapian
Group:		Development/Languages/Perl
Requires:	xapian-core-libs >= %{version}

%description -n perl-Xapian
This module wraps most methods of most Xapian classes. The missing
classes and methods should be added in the future. It also provides a
simplified, more 'perlish' interface to some common operations.

%description -n perl-Xapian -l pl.UTF-8
Ten moduł obudowuje większość metod z większości klas Xapiana.
Brakujące klasy i metody powinny być dodane w przyszłości. Moduł
udostępnia także uproszczony, bardziej perlowy interfejs do niektórych
popularnych operacji.

%package -n %{php_name}-xapian
Summary:	Files needed for developing PHP scripts which use Xapian
Summary(pl.UTF-8):	Pliki do tworzenia skryptów w PHP wykorzystujących Xapiana
Group:		Development/Languages/PHP
Requires:	xapian-core-libs >= %{version}
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
Summary:	Files needed for developing Python 2 scripts which use Xapian
Summary(pl.UTF-8):	Pliki do tworzenia skryptów w Pythonie 2 wykorzystujących Xapiana
Group:		Development/Languages/Python
Requires:	python-modules >= 1:2.6
Requires:	xapian-core-libs >= %{version}

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

%package -n python3-xapian
Summary:	Files needed for developing Python 3 scripts which use Xapian
Summary(pl.UTF-8):	Pliki do tworzenia skryptów w Pythonie 3 wykorzystujących Xapiana
Group:		Development/Languages/Python
Requires:	python3-modules >= 1:3.2
Requires:	xapian-core-libs >= %{version}

%description -n python3-xapian
Xapian is an Open Source Probabilistic Information Retrieval
framework. It offers a highly adaptable toolkit that allows developers
to easily add advanced indexing and search facilities to applications.
This package provides the files needed for developing Python scripts
which use Xapian.

%description -n python3-xapian -l pl.UTF-8
Xapian to mająca otwarte źródła biblioteka do uzyskiwania informacji
probabilistycznych. Oferuje wysoce adoptowalne narzędzia pozwalające
programistom łatwo dodawać do aplikacji zaawansowane możliwości
indeksowania i wyszukiwania. Ten pakiet zawiera pliki potrzebne przy
tworzeniu skryptów w Pythonie wykorzystujących Xapiana.

%package -n ruby-xapian
Summary:	Files needed for developing Ruby scripts which use Xapian
Summary(pl.UTF-8):	Pliki do tworzenia skryptów w języku Ruby wykorzystujących Xapiana
Group:		Development/Languages
Requires:	xapian-core-libs >= %{version}

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
Requires:	xapian-core-libs >= %{version}

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

%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+python(\s|$),#!%{__python}\1,' -e '1s,#!\s*/usr/bin/python(\s|$),#!%{__python}\1,' \
      python/docs/examples/*.py

%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+python(\s|$),#!%{__python3}\1,' -e '1s,#!\s*/usr/bin/python(\s|$),#!%{__python3}\1,' \
      python3/docs/examples/*.py

%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+ruby(\s|$),#!%{__ruby}\1,' \
      ruby/docs/examples/*.rb

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
CLASSPATH="." \
%{?with_java:export JAVA_HOME="%{java_home}"}
%configure \
	PERL_ARCH=%{perl_vendorarch} \
	PERL_LIB=%{perl_vendorlib} \
	RUBY_LIB=%{ruby_vendorlibdir} \
	RUBY_LIB_ARCH=%{ruby_vendorarchdir} \
	%{?with_lua:LUA=/usr/bin/lua5.1 LUA_INC=/usr/include/lua5.1} \
	%{?with_dotnet:--with-csharp} \
	%{?with_java:--with-java} \
	%{?with_lua:--with-lua} \
	%{?with_perl:--with-perl} \
	%{?with_python2:--with-python} \
	%{?with_python3:--with-python3} \
	%{?with_php:--with-%{phpbindname}} \
	%{?with_ruby:--with-ruby} \
	%{?with_tcl:--with-tcl}

%{__make} \
	%{?with_java:JAVA_CPPFLAGS="-I%{java_home}/include -I%{java_home}/include/linux"}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	jnidir=%{_jnidir} \
	phpincdir=%{php_data_dir}

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%if %{with java}
install -D java/built/xapian.jar $RPM_BUILD_ROOT%{_javadir}/xapian-%{version}.jar
ln -sf xapian-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/xapian.jar
%endif

for binding in %{?with_dotnet:csharp} %{?with_perl:perl} %{?with_php:%{phpbindname}} %{?with_python2:python} %{?with_python3:python3} %{?with_ruby:ruby} %{?with_tcl:tcl8}; do
	install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/$binding
	[ ! -f $binding/docs/index.html ] || cp -p $binding/docs/index.html $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/$binding
	cp -pr $binding/docs/examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/$binding
done

%if %{with python2}
%py_postclean
%endif
%if %{with python3}
install -d $RPM_BUILD_ROOT%{py3_sitedir}/xapian/__pycache__
%{__mv} $RPM_BUILD_ROOT%{py3_sitedir}/xapian/*.py[co] $RPM_BUILD_ROOT%{py3_sitedir}/xapian/__pycache__
%endif

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
%{_javadir}/xapian-%{version}.jar
%{_javadir}/xapian.jar
%endif

%if %{with lua}
%files -n lua-xapian
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lua/5.1/xapian.so
%endif

%if %{with perl}
%files -n perl-Xapian
%defattr(644,root,root,755)
%{perl_vendorlib}/Xapian.pm
%dir %{perl_vendorlib}/Xapian
%{perl_vendorlib}/Xapian/*.pm
%dir %{perl_vendorarch}/auto/Xapian
%attr(755,root,root) %{perl_vendorarch}/auto/Xapian/Xapian.so
%endif

%if %{with php}
%files -n %{php_name}-xapian
%defattr(644,root,root,755)
%attr(755,root,root) %{php_extensiondir}/xapian.so
%{php_data_dir}/xapian.php
%endif

%if %{with python2}
%files -n python-xapian
%defattr(644,root,root,755)
%dir %{py_sitedir}/xapian
%attr(755,root,root) %{py_sitedir}/xapian/_xapian.so
%{py_sitedir}/xapian/__init__.py[co]
%endif

%if %{with python3}
%files -n python3-xapian
%defattr(644,root,root,755)
%dir %{py3_sitedir}/xapian
%attr(755,root,root) %{py3_sitedir}/xapian/_xapian.cpython-*.so
%{py3_sitedir}/xapian/__init__.py
%{py3_sitedir}/xapian/__pycache__
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
