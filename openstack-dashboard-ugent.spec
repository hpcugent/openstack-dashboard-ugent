#
# Copyright 2021 Ghent University
#
# This file is part of openstack-dashboard-ugent,
# originally created by the HPC team of the University of Ghent (http://ugent.be/hpc).
#
#
# https://github.com/hpcugent/openstack-dashboard-ugent
#
# openstack-dashboard-ugent is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation v2.
#
# openstack-dashboard-ugent is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with openstack-dashboard-ugent. If not, see <http://www.gnu.org/licenses/>.
##

%{!?_rel:%{expand:%%global _rel 1}}

%define dashboardpath /usr/share/openstack-dashboard/openstack_dashboard/local
%define dashboardconf /etc/openstack-dashboard/local_settings.d
%define ugentpanelpath %{dashboardpath}/ugent
%define localsettings %{dashboardpath}/local_settings.d
%define imagespath /usr/share/openstack-dashboard/openstack_dashboard/themes/default/img

Summary: UGent OpenStack dashboard
Name: openstack-dashboard-ugent
Version: 1.0
Release: 1%{?dist}
License: GPLv2
Group: Applications/System
URL: https://www.ugent.be/
Source: %{name}-%{version}.tar.gz
ExclusiveOS: linux
BuildRoot: %{?_tmppath}%{!?_tmppath:/var/tmp}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: openstack-dashboard

%description
openstack-dashboard-ugent provides the required OpenStack panels
for UGent Cloud.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{ugentpanelpath}
mkdir -p $RPM_BUILD_ROOT%{localsettings}
mkdir -p $RPM_BUILD_ROOT%{imagespath}
mkdir -p $RPM_BUILD_ROOT%{dashboardconf}

install -m 0644 panels/_00_ugent.py $RPM_BUILD_ROOT%{localsettings}/_00_ugent.py
install -m 0644 panels/_12_ugent_theme.py $RPM_BUILD_ROOT%{dashboardconf}/_12_ugent_theme.py
install -m 0644 panels/__init__.py $RPM_BUILD_ROOT%{ugentpanelpath}/__init__.py
install -m 0644 panels/_disabled.py $RPM_BUILD_ROOT%{ugentpanelpath}/_disabled.py
install -m 0644 img/favicon.ico $RPM_BUILD_ROOT%{imagespath}/favicon.ico
install -m 0644 img/logo-splash.svg $RPM_BUILD_ROOT%{imagespath}/logo-splash.svg
install -m 0644 img/logo.svg $RPM_BUILD_ROOT%{imagespath}/logo.svg

# Disabled tabs
ln -s _disabled.py $RPM_BUILD_ROOT%{ugentpanelpath}/_1360_project_volume_groups.py
ln -s _disabled.py $RPM_BUILD_ROOT%{ugentpanelpath}/_1370_project_vg_snapshots.py
ln -s _disabled.py $RPM_BUILD_ROOT%{ugentpanelpath}/_1440_project_routers_panel.py

%post

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)

%{localsettings}/_00_ugent.py
%{dashboardconf}/_12_ugent_theme.py
%{ugentpanelpath}/__init__.py
%{ugentpanelpath}/_disabled.py

%{ugentpanelpath}/_1360_project_volume_groups.py
%{ugentpanelpath}/_1370_project_vg_snapshots.py
%{ugentpanelpath}/_1440_project_routers_panel.py

%{imagespath}/favicon.ico
%{imagespath}/logo-splash.svg
%{imagespath}/logo.svg

%attr(0755, root, root) %dir %{ugentpanelpath}
%attr(0755, root, root) %dir %{imagespath}

%changelog
* Thu Aug 11 2021 Álvaro Simón <Alvaro.SimonGarcia@UGent.be>
- Initial build.

