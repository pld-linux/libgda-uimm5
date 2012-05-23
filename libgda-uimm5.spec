#
# Conditional build:
%bcond_without	apidocs		# don't generate documentation with doxygen
%bcond_without	static_libs	# don't build static library
#
Summary:	C++ wrapper for libgda-ui 5.x
Summary(pl.UTF-8):	Interfejs C++ dla libgda-ui 5.x
Name:		libgda-uimm5
Version:	4.99.4
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgda-uimm/4.99/libgda-uimm-%{version}.tar.xz
# Source0-md5:	f9e35841c6182d55cdc2b070ad4b15f5
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	gtkmm3-devel >= 3.0.0
BuildRequires:	libgda5-devel >= 4.9.4
BuildRequires:	libgda5-ui-devel >= 4.9.4
BuildRequires:	libgdamm5-devel >= 4.99.4
BuildRequires:	libtool >= 2:1.5
BuildRequires:	mm-common >= 0.9.5
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	gtkmm3 >= 3.0.0
Requires:	libgda5 >= 4.9.4
Requires:	libgda5-ui >= 4.9.4
Requires:	libgdamm5 >= 4.99.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrapper for libgda-ui 5.x.

%description -l pl.UTF-8
terfejs C++ dla libgda-ui 5.x.

%package devel
Summary:	Header files for libgda-uimm 5 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgda-uimm 5
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtkmm3-devel >= 3.0.0
Requires:	libgda5-devel >= 4.9.4
Requires:	libgda5-ui-devel >= 4.9.4
Requires:	libgdamm5-devel >= 4.99.4

%description devel
Header files for libgda-uimm 5 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgda-uimm 5.

%package static
Summary:	Static libgda-uimm 5 library
Summary(pl.UTF-8):	Statyczna biblioteka libgda-uimm 5
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgda-uimm 5 library.

%description static -l pl.UTF-8
Statyczna biblioteka libgda-uimm 5.

%package apidocs
Summary:	libgda-uimm 5 API documentation
Summary(pl.UTF-8):	Dokumentacja API libgda-uimm 5
Group:		Documentation

%description apidocs
libgda-uimm 5 API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libgda-uimm 5.

%prep
%setup -q -n libgda-uimm-%{version}

%build
%{__libtoolize}
%{__aclocal} -I build
%{__autoconf}
%{__automake}
%configure \
	%{!?with_apidocs:--disable-documentation} \
	%{?with_static_libs:--enable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgdauimm-5.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdauimm-5.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdauimm-5.0.so
%{_libdir}/libgda-uimm-5.0
%{_includedir}/libgda-uimm-5.0
%{_includedir}/libgdauimm-5.0
%{_pkgconfigdir}/libgda-uimm-5.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgdauimm-5.0.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_datadir}/devhelp/books/libgda-uimm-5.0
%{_docdir}/libgda-uimm-5.0
%endif
