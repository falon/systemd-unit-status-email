%global systemd (0%{?fedora} >= 18) || (0%{?rhel} >= 7)
%global upname systemd-unit-status-email

Summary: A tool to send an email with the Systemd status of a service.
Name: systemd-unit-status-email
Version: 0.1.0
Release: 0%{?dist}
Group: System Environment/Base
License: Apache-2.0
URL: https://falon.github.io/%{upname}/
Source0: https://github.com/falon/%{upname}/archive/master.zip
BuildArch:	noarch

# Required for all versions
Requires: systemd

%if %systemd
# Required for systemd
%{?systemd_requires}
BuildRequires: systemd
%endif

%description
%{upname} 
Systemd can send an e-mail when a unit fails, or it stops
or any other event you can imagine.

%clean
rm -rf %{buildroot}/

%prep
%autosetup -n %{upname}-master


%install

%if %systemd
mkdir -p %{buildroot}%{_unitdir}
install -m 0444 LICENSE %{buildroot}
install -m 0644 status-email-sysadmin@.service %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_bindir}
install -m 0755 systemd-email %{buildroot}%{_bindir}
install -D -m0644 systemd-email.conf-default %{buildroot}%{_sysconfdir}/sysconfig/systemd-email.conf
%endif

%files
%{_unitdir}
%{_bindir}/systemd-email
/LICENSE
%license LICENSE
%config(noreplace) %{_sysconfdir}/sysconfig/systemd-email.conf

%changelog
* Thu Apr 05 2018 Marco Favero <marco.favero@csi.it> 0.1.0-0
- Initial release.
