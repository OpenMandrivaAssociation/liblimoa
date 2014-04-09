%define	major	0
%define	oname	limoa
%define	libname	%mklibname %{oname} %{major}
%define	devname	%mklibname -d %{oname}

Summary:	LIM OpenMAX Application layer library
Name:		lib%{oname}
Version:	0.1.1
Release:	1
Group:		System/Libraries
License:	LGPLv2.1+
Url:		http://limoa.sourceforge.net/
Source0:	%{name}-%{version}.tar.xz

%description
LIM OpenMAX Application layer library.

%files
%{_bindir}/limox

%libpackage %{oname} %{major}

%package -n	%{devname}
Summary:	Development headers for LIM OpenMAX Application Layer base library
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n	%{devname}
Development headers for LIM OpenMAX Application Layer base library.

%files -n	%{devname}
%doc COPYING ChangeLog
%{_includedir}/OpenMAXAL*.h
%{_libdir}/lib%{oname}.so
%{_libdir}/pkgconfig/lib%{oname}.pc

%prep
%setup -q

%build
%configure2_5x	--enable-limox
%make

%install
%makeinstall_std

%changelog
* Wed Apr 9 2014 Per Øyvind Karlsen <proyvind@moondrake.org> 0.1.1-1
- initial release
