Summary:	Mox - mock object framework for Python
Summary(pl.UTF-8):	Mox - szkielet obiektów-atrap dla Pythona
Name:		python-mox
Version:	0.5.3
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: http://code.google.com/p/pymox/downloads/list
Source0:	http://pymox.googlecode.com/files/mox-%{version}.tar.gz
# Source0-md5:	2c43da56ed1bbbbf7805e81c76a924cc
URL:		http://code.google.com/p/pymox/
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules >= 1:2.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mox is a mock object framework for Python based on the Java mock
object framework EasyMock.

%description -l pl.UTF-8
Mox to szkielet obiektów-atrap dla Pythona, oparty na szkielecie
EasyMock dla Javy.

%prep
%setup -q -n mox-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--skip-build \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/mox.py[co]
%{py_sitescriptdir}/stubout.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/mox-%{version}-py*.egg-info
%endif
