%define		_class		UDDI
%define		upstream_name	%{_class}

Name:		php-pear-%{upstream_name}
Version:	0.2.4
Release:	6
Summary:	API for PHP
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/UDDI/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Implementation of Universal Description, Discovery and Integration API
for locating and publishing Web Services in a UBR (UDDI Business
Registry).

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/examples
%{_datadir}/pear/%{_class}/*.php
%{_datadir}/pear/packages/%{upstream_name}.xml




%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.4-5mdv2012.0
+ Revision: 742296
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.4-4
+ Revision: 679600
- mass rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - spec cleanup
    - use pear installer
    - don't ship tests, even in documentation
    - own all directories
    - use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.2.4-2mdv2010.0
+ Revision: 441664
- rebuild

* Mon Apr 20 2009 Raphaël Gertz <rapsys@mandriva.org> 0.2.4-1mdv2009.1
+ Revision: 368274
- Update php pear UDDI to 0.2.4 version

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.2.3-3mdv2009.1
+ Revision: 322728
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2.3-2mdv2009.0
+ Revision: 237156
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 0.2.3-1mdv2008.0
+ Revision: 15756
- 0.2.3


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.2.2-1mdv2007.0
+ Revision: 82792
- Import php-pear-UDDI

* Sat May 20 2006 Oden Eriksson <oeriksson@mandriva.com> 0.2.2-1mdk
- 0.2.2

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-1mdk
- 0.2.1
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-1mdk
- initial Mandriva package (PLD import)

