%define getmail_home /var/lib/getmail

Name:		nethserver-getmail
Version:	0.0.1
Release:	1%{?dist}
Summary:	NethServer getmail
Group:		Networking/Daemons
License:	GPLv2
Source0:	%{name}-%{version}.tar.gz
BuildArch: 	noarch
URL: %{url_prefix}/%{name} 

BuildRequires:	nethserver-devtools
Requires:	nethserver-mail-server, nethserver-spamd, nethserver-mail-filter
Requires:	getmail

%description
Getmail add-on for NethServer

%prep
%setup

%build
%{makedocs}
perl createlinks

%install
rm -rf %{buildroot}
(cd root   ; find . -depth -not -name '*.orig' -print  | cpio -dump %{buildroot})
mkdir -p %{buildroot}/%{getmail_home}
%{genfilelist} %{buildroot} \
    --dir '%{getmail_home}' 'attr(0750,vmail,vmail)' \
    > %{name}-%{version}-%{release}-filelist

%clean 
rm -rf %{buildroot}

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%doc COPYING

%changelog
