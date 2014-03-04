%global pypiname trollius
Name:           python-trollius
Version:        0.1.5
Release:        3%{?dist}
Summary:        A port of the Tulip asyncio module to Python 2

Group:          Development/Libraries
License:        ASL 2.0
URL:            http://bitbucket.org/enovance/trollius/overview
Source0:        http://pypi.python.org/packages/source/t/%{pypiname}/%{pypiname}-%{version}.tar.gz
#md5=8186f3b1685f79a36c208363fab740f4

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

# see https://fedoraproject.org/wiki/Packaging:Python#Macros
%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

#  TODO : rhel6 support can't happen until
#         python-futures makes it into EPEL
#         https://bugzilla.redhat.com/show_bug.cgi?id=1066211  
Requires:  python-futures

# required for check
BuildRequires:  python-tox
BuildRequires:  python-futures

%if 0%{?rhel}==6
# things required just by python2.6 on RHEL
Requires:  python-orderddict

# required for check with python2.6 
# TODO : python-argparse required by unittest2, until
#        new unittest2 package with correct deps
#        https://bugzilla.redhat.com/show_bug.cgi?id=1065824
BuildRequires:  python-argparse
BuildRequires:  python-unittest2
%endif

%description

Trollius is a portage of the Tulip project (asyncio module, PEP 3156)
on Python 2. Trollius works on Python 2.6-3.4. It has been tested on
Windows, Linux, Mac OS X, FreeBSD and OpenIndiana.

%prep 
%setup -q -n %{pypiname}-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

%check

%if 0%{?fedora}
TOXENV=py27 %{__python2} setup.py test
%endif
 
%files
%defattr(-,root,root,-)
%doc README
%{python2_sitelib}/asyncio
%{python2_sitelib}/%{pypiname}-%{version}-py2.?.egg-info


%changelog
* Tue Mar  4 2014  <iwienand@redhat.com> - 0.1.5-3
- add python-futures as build-dep
- add __python2* macros; convert to them

* Thu Feb 20 2014  <iwienand@redhat.com> - 0.1.5-2
- change license to ASL 2.0
- add defattr (from rpmlint)
- add group tag (from rpmlint)

* Tue Feb 18 2014  <iwienand@redhat.com> - 0.1.5-1
- Initial release
