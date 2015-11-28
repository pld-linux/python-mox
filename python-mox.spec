Summary:	Mox - mock object framework for Python
Summary(pl.UTF-8):	Mox - szkielet obiektów-atrap dla Pythona
Name:		python-mox
Version:	0.5.3
Release:	3
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
Obsoletes:	python-pymox
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mox is a mock object framework for Python based on the Java mock
object framework EasyMock.

Mox will make mock objects for you, so you don't have to create your
own! It mocks the public/protected interfaces of Python objects. You
set up your mock objects expected behavior using a domain specific
language (DSL), which makes it easy to use, understand, and refactor!

%description -l pl.UTF-8
Mox to szkielet obiektów-atrap dla Pythona, oparty na szkielecie
EasyMock dla Javy.

Mox tworzy okienty-atrapy za programistę, dzięki czemu nie musi on
tworzyć własnych. Imituje interfejsy publiczne i chronione obiektów
pythonowych. Można konfigurować oczekiwane zachowanie własnych
obiektów-atrap przy użyciu specjalizowanego języka (DSL), który jest
łatwy w użyciu, rozumieniu i refaktoryzacji.

%prep
%setup -q -n mox-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

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
