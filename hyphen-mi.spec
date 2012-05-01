Name: hyphen-mi
Summary: Maori hyphenation rules
%define upstreamid 20080630
Version: 0.%{upstreamid}
Release: 3.1%{?dist}
Source: http://packages.papakupu.maori.nz/hunspell-hyphen/hunspell-hyphen-mi-0.1.%{upstreamid}-beta.tar.gz
Group: Applications/Text
URL: http://papakupu.maori.nz/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv3+
BuildArch: noarch

Requires: hyphen

%description
Maori hyphenation rules.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p mi.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_mi_NZ.dic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc mi.LICENSE mi.README
%{_datadir}/hyphen/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20080630-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080630-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080630-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 09 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080630-1
- initial version
