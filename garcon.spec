#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
%bcond_with	static_libs	# static libraries

Summary:	Freedesktop.org compliant menu library for the Xfce desktop environment
Summary(pl.UTF-8):	Biblioteka menu dla środowiska Xfce zgodna z freedesktop.org
Name:		garcon
Version:	0.7.0
Release:	2
License:	LGPL v2+
Group:		Libraries
Source0:	https://archive.xfce.org/src/xfce/garcon/0.7/%{name}-%{version}.tar.bz2
# Source0-md5:	2964c7a7e5d4aac58b4afef9b8602914
URL:		https://gitlab.xfce.org/xfce/garcon
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.30.0
BuildRequires:	gtk+2-devel >= 2:2.24.0
BuildRequires:	gtk+3-devel >= 3.20.0
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	intltool >= 0.35
BuildRequires:	libxfce4ui-devel >= 4.12.0
BuildRequires:	libxfce4util-devel >= 4.12.0
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.10.0
Requires:	filesystem >= 4.1-15
Requires:	glib2 >= 1:2.30.0
Requires:	libxfce4util >= 4.12.0
Obsoletes:	libxfce4menu
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
garcon is a freedesktop.org compliant menu implementation based on
GLib and GIO. It was started as a complete rewrite of the former Xfce
menu library called libxfce4menu, which, in contrast to garcon, was
lacking menu merging features essential for loading menus modified
with menu editors.

%description -l pl.UTF-8
garcon jest implementacją menu zgodnego z freedesktop.org, bazującą na
GLib i GIO. Została rozpoczęta jako całkowite przepisanie biblioteki
libxfce4menu, której, w odróżnieniu do garcon, brakowało
funkcjonalności łączenia menu, wymaganej w przypadku modyfikowania za
pomocą edytora.

%package devel
Summary:	Header files for garcon library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki garcon
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.30.0
Obsoletes:	libxfce4menu-devel

%description devel
Header files for garcon library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki garcon.

%package static
Summary:	Static garcon library
Summary(pl.UTF-8):	Statyczna biblioteka garcon
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libxfce4menu-static

%description static
Static garcon library.

%description static -l pl.UTF-8
Statyczna biblioteka garcon.

%package gtk2
Summary:	Freedesktop.org compliant menu library - GTK+ 2 support
Summary(pl.UTF-8):	Biblioteka menu zgodnego z Freedesktop.org - obsługa GTK+2
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2 >= 2:2.24.0
Requires:	libxfce4ui >= 4.12.0

%description gtk2
Freedesktop.org compliant menu library - GTK+ 2 support.

%description gtk2 -l pl.UTF-8
Biblioteka menu zgodnego z Freedesktop.org - obsługa GTK+2.

%package gtk2-devel
Summary:	Header files for garcon-gtk2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki garcon-gtk2
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gtk2 = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.24.0
Requires:	libxfce4ui-devel >= 4.12.0

%description gtk2-devel
Header files for garcon-gtk2 library.

%description gtk2-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki garcon-gtk2.

%package gtk2-static
Summary:	Static garcon-gtk2 library
Summary(pl.UTF-8):	Biblioteka statyczna garcon-gtk2
Group:		X11/Development/Libraries
Requires:	%{name}-gtk2-devel = %{version}-%{release}

%description gtk2-static
Static garcon-gtk2 library.

%description gtk2-static -l pl.UTF-8
Biblioteka statyczna garcon-gtk2.

%package gtk3
Summary:	Freedesktop.org compliant menu library - GTK+ 3 support
Summary(pl.UTF-8):	Biblioteka menu zgodnego z Freedesktop.org - obsługa GTK+3
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+3 >= 3.20.0
Requires:	libxfce4ui >= 4.12.0

%description gtk3
Freedesktop.org compliant menu library - GTK+ 3 support.

%description gtk3 -l pl.UTF-8
Biblioteka menu zgodnego z Freedesktop.org - obsługa GTK+3.

%package gtk3-devel
Summary:	Header files for garcon-gtk3 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki garcon-gtk3
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gtk3 = %{version}-%{release}
Requires:	gtk+3-devel >= 3.20.0
Requires:	libxfce4ui-devel >= 4.12.0

%description gtk3-devel
Header files for garcon-gtk3 library.

%description gtk3-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki garcon-gtk3.

%package gtk3-static
Summary:	Static garcon-gtk3 library
Summary(pl.UTF-8):	Biblioteka statyczna garcon-gtk3
Group:		X11/Development/Libraries
Requires:	%{name}-gtk3-devel = %{version}-%{release}

%description gtk3-static
Static garcon-gtk3 library.

%description gtk3-static -l pl.UTF-8
Biblioteka statyczna garcon-gtk3.

%package apidocs
Summary:	garcon API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki garcon
Group:		Documentation
Requires:	gtk-doc-common
Obsoletes:	libxfce4menu-apidocs
%if "%{_rpmversion}" >= "4.6"
BuildArch:	noarch
%endif

%description apidocs
API and internal documentation for garcon library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki garcon.

%prep
%setup -q

%build
%configure \
	--enable-gtk-doc \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static} \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
# duplicate of hy
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/hy_AM
# older version of uz
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/uz@Latn
# not supported by glibc (as of 2.32)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	gtk2 -p /sbin/ldconfig
%postun	gtk2 -p /sbin/ldconfig

%post	gtk3 -p /sbin/ldconfig
%postun	gtk3 -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README STATUS TODO
%attr(755,root,root) %{_libdir}/libgarcon-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgarcon-1.so.0
%{_sysconfdir}/xdg/menus/xfce-applications.menu
%{_datadir}/desktop-directories/xfce-*.directory

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgarcon-1.so
%{_includedir}/garcon-1
%{_pkgconfigdir}/garcon-1.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgarcon-1.a
%endif

%files gtk2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgarcon-gtk2-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgarcon-gtk2-1.so.0

%files gtk2-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgarcon-gtk2-1.so
%{_includedir}/garcon-gtk2-1
%{_pkgconfigdir}/garcon-gtk2-1.pc

%if %{with static_libs}
%files gtk2-static
%defattr(644,root,root,755)
%{_libdir}/libgarcon-gtk2-1.a
%endif

%files gtk3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgarcon-gtk3-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgarcon-gtk3-1.so.0

%files gtk3-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgarcon-gtk3-1.so
%{_includedir}/garcon-gtk3-1
%{_pkgconfigdir}/garcon-gtk3-1.pc

%if %{with static_libs}
%files gtk3-static
%defattr(644,root,root,755)
%{_libdir}/libgarcon-gtk3-1.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/garcon
%endif
