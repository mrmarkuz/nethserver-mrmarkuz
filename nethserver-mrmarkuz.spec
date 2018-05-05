Name: nethserver-mrmarkuz
Version: 0.0.1
Release: 2%{?dist}
Summary: mrmarkuz NethServer repo
License: GPL
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
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


%changelog
* Wed Mar 07 2018 Markus Neuberger <dev@markusneuberger.at> - 0.0.1-1
- First release
