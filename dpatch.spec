Name:		dpatch
Version:	2.0.35
Release:	1
Summary:	Debian dpatch tool
Group:		Development/Other
License:	GPLv2+
URL:		https://alioth.debian.org/projects/dpatch/
Source0:	ftp://ftp.debian.org:21/debian/pool/main/d/dpatch/dpatch_2.0.35.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:   	dpkg
Patch1:		dpatch-nawk.patch

%description
Debian dpatch tool.

%prep
%setup -q -n %{name}-%{version}
%patch1 -p1 -b .orig

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/{man1,man7},%{_bindir}}
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc debian/control debian/copyright debian/NEWS README.History
%{_bindir}/*
%{_datadir}/dpatch
%{_mandir}/*/*
%{_sysconfdir}/bash_completion.d/dpatch_edit_patch


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.31-2mdv2011.0
+ Revision: 610271
- rebuild

* Tue Feb 23 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.0.31-1mdv2010.1
+ Revision: 510390
- up to 2.0.31

* Sat Jan 24 2009 Jérôme Soyer <saispo@mandriva.org> 2.0.30-1mdv2009.1
+ Revision: 333151
- import dpatch



