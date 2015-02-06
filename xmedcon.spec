%define major		2
%define libname		%mklibname mdc %{major}
%define develname	%mklibname mdc -d
%define staticname	%mklibname mdc -d -s

Name:		xmedcon
Version:	0.11.0
Release:	2
Summary:	An open source toolkit for medical image conversion
Group:		Graphics
License:	GPLv2
URL:		http://xmedcon.sourceforge.net
Source0:	http://downloads.sourceforge.net/project/xmedcon/XMedCon-Source/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	gtk+2-devel

%description
This project stands for Medical Image Conversion and is released under the
GNU's (L)GPL license. It bundles the C source code, a library, a flexible
command-line utility and a graphical front-end based on the amazing Gtk+
toolkit.

Its main purpose is image conversion while preserving valuable medical
study information. The currently supported formats are: Acr/Nema 2.0,
Analyze (SPM), Concorde/uPET, DICOM 3.0, CTI ECAT 6/7, InterFile 3.3
and PNG or Gif87a/89a towards desktop applications.

%package -n %{libname}
Summary: Libraries for (X)MedCon
Group: System/Libraries

%description -n %{libname}

This package contains (X)MedCon shared library (libmdc).

%package -n %{develname}
Summary: Header files for (X)MedCon development
Group: Development/C
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{EVRD}

%description -n %{develname}

The xmedcon-devel package contains the header files necessary for developing
programs that make use of the (X)MedCon library (libmdc).

%package -n %{staticname}
Summary: Static libraries for (X)MedCon development
Group: Development/C
Requires: %{develname} = %{version}
Provides: %{name}-devel-static = %{EVRD}

%description -n %{staticname}

The xmedcon-devel package contains the header files necessary for developing
programs that make use of the (X)MedCon library (libmdc).

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

rm -rf %{buildroot}%{_libdir}/*.la

%files
%defattr(-, root, root)
%doc ChangeLog COPYING COPYING.LIB README REMARKS AUTHORS
%{_bindir}/*
%{_sysconfdir}/*
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/*so.%{major}*

%files -n %{develname}
%doc README COPYING COPYING.LIB
%defattr(-,root,root)
%{_mandir}/man3/*
%{_mandir}/man4/*
%{_includedir}/*
%{_libdir}/*.so
%{_datadir}/aclocal/*

%files -n %{staticname}
%doc README COPYING COPYING.LIB
%{_libdir}/*.a


%changelog
* Thu Jun 28 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.11.0-1
+ Revision: 807336
+ rebuild (emptylog)

* Wed Jun 27 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.11.0-1
+ Revision: 807219
- update to 0.11.0

* Mon Dec 26 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.10.7-1
+ Revision: 745411
- imported package xmedcon

