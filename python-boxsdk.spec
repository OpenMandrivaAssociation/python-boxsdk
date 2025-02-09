Name:		python-boxsdk
Version:	3.13.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/b/boxsdk/boxsdk-%{version}.tar.gz
Summary:	Official Box Python SDK
URL:		https://pypi.org/project/boxsdk/
License:	Apache Software License, Version 2.0, http://www.apache.org/licenses/LICENSE-2.0
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Official Box Python SDK

%prep
%autosetup -p1 -n boxsdk-%{version}

%files
%{py_sitedir}/boxsdk
%{py_sitedir}/boxsdk-*.*-info
