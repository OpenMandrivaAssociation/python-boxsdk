Name:		python-boxsdk
# Before updating to the 10.x+ branch, please make sure
# it doesn't break duplicity.
Version:	10.17.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/b/boxsdk/boxsdk-%{version}.tar.gz
Summary:	Official Box Python SDK
URL:		https://pypi.org/project/boxsdk/
License:	Apache-2.0
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildSystem:	python
BuildArch:	noarch

%patchlist
# Get rid of the dataclasses dependency -- dataclasses are
# supported out of the box in python >= 3.7
# dropped (no longer applies): boxsdk-no-dataclasses-dep.patch

%description
Official Box Python SDK

%files
%{py_sitedir}/box_sdk_gen
%{py_sitedir}/boxsdk-*.*-info
