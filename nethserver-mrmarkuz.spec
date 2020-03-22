Name: nethserver-mrmarkuz
Version: 0.0.1
Release: 4%{?dist}
Summary: mrmarkuz NethServer repo
License: GPL
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: https://wiki.nethserver.org/doku.php?id=mrmarkuz_repository
BuildRequires: nethserver-devtools

%description
mrmarkuz NethServer repository installer

%prep
%setup -q

%build
%{makedocs}
perl createlinks

%install
rm -rf %{buildroot}
(cd root ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-%{release}-filelist

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%attr(0755,root,root) %{_sysconfdir}/cron.daily/check4mrmarkuzUpdates


%changelog
* Sun Mar 22 2020 Markus Neuberger <dev@markusneuberger.at> - 0.0.1-4
- Domain change
- Update mail
- Backup
- Metadata signing
- URL Update
* Sun Oct 21 2018 Markus Neuberger <dev@markusneuberger.at> - 0.0.1-3
- Change to mrmarkuz.goip.de
* Wed Mar 07 2018 Markus Neuberger <dev@markusneuberger.at> - 0.0.1-1
- First release
