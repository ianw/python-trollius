%global pypiname trollius
Name:           python-trollius
Version:        0.1.5
Release:        2%{?dist}
Summary:        A port of the Tulip asyncio module to Python 2

Group:          Development/Libraries
License:        ASL 2.0
URL:            http://bitbucket.org/enovance/trollius/overview
Source0:        http://pypi.python.org/packages/source/t/%{pypiname}/%{pypiname}-%{version}.tar.gz
#md5=8186f3b1685f79a36c208363fab740f4

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

#  TODO : rhel6 support can't happen until
#         python-futures makes it into EPEL
#         https://bugzilla.redhat.com/show_bug.cgi?id=1066211  
Requires:  python-futures

# required for check
BuildRequires:  python-tox

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
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%check

%if 0%{?fedora}
TOXENV=py27 %{__python} setup.py test
%endif
 
%files
%defattr(-,root,root,-)
%doc README
%{python_sitelib}/asyncio
%{python_sitelib}/%{pypiname}-%{version}-py2.?.egg-info


%changelog
* Tue Feb 20 2014  <iwienand@redhat.com> - 0.1.5-2
- Initial release

