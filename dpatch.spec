Name:		dpatch
Version:	2.0.31
Release:	%mkrel 2
Summary:	Debian dpatch tool
Group:		Development/Other
License:	GPLv2+
URL:		https://alioth.debian.org/projects/dpatch/
Source0:	ftp://ftp.debian.org/debian/pool/main/d/dpatch/%{name}_%{version}.tar.gz
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
