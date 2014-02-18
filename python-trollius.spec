# Tests requiring Internet connections are disabled by default
# pass --with internet to run them (e.g. when doing a local rebuild
# for sanity checks before committing)
%bcond_with internet

%global pypiname trollius
Name:           python-trollius
Version:        0.1.5
Release:        1%{?dist}
Summary:        Trollius is a portage of the Tulip project (asyncio module, PEP 3156) on Python 2

License:        Apache License 2.0
URL:            http://bitbucket.org/enovance/trollius/overview
Source0:        http://pypi.python.org/packages/source/t/%{pypiname}/%{pypiname}-%{version}.tar.gz
#md5=8186f3b1685f79a36c208363fab740f4

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

Requires:  python-futures
# required for check
BuildRequires:  python-tox

%if 0%{?rhel}==6
# things required just by python2.6 on RHEL
Requires:  python-orderddict
# for check
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
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# if internet connection available, run tests
%if %{with internet}
%check

%if 0%{?rhel}==6
TOXENV=py26 %{__python} setup.py test
%endif

%if 0%{?fedora}
TOXENV=py27 %{__python} setup.py test
%endif
%endif
 
%files
%doc README
%{python_sitelib}/asyncio
%{python_sitelib}/%{pypiname}-%{version}-py2.?.egg-info


%changelog
* Tue Feb 18 2014  <iwienand@redhat.com> - 0.1.5-1
- Initial release

