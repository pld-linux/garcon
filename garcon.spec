#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
%bcond_without	static_libs	# don't build static libraries
#
Summary:	Freedesktop.org compliant menu library for the Xfce desktop environment
Summary(pl.UTF-8):	Biblioteka menu dla środowiska Xfce zgodna z freedesktop.org
Name:		garcon
Version:	0.1.5
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://archive.xfce.org/src/libs/garcon/0.1/%{name}-%{version}.tar.bz2
# Source0-md5:	c4fd42082b4ae157aa4c7abb6d6570aa
URL:		http://archive.xfce.org/src/libs/garcon/
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.14.0
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	intltool
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.8.0
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
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.14.0
Obsoletes:	libxfce4menu-devel

%description devel
Header files for garcon library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki garcon.

%package static
Summary:	Static garcon library
Summary(pl.UTF-8):	Statyczna biblioteka garcon
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libxfce4menu-static

%description static
Static garcon library.

%description static -l pl.UTF-8
Statyczna biblioteka garcon.

%package apidocs
Summary:	garcon API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki garcon
Group:		Documentation
Requires:	gtk-doc-common
Obsoletes:	libxfce4menu-apidocs

%description apidocs
API and internal documentation for garcon library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki garcon.

%prep
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static} \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# pt locale is already installed, so there is no need to rename it
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/pt_PT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README STATUS TODO
%attr(755,root,root) %{_libdir}/libgarcon-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgarcon-1.so.0
%{_sysconfdir}/xdg/menus
%{_datadir}/desktop-directories/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgarcon-1.so
%{_libdir}/libgarcon-1.la
%{_includedir}/garcon-1
%{_pkgconfigdir}/garcon-1.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgarcon-1.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/garcon
%endif