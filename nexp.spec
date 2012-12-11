Name:          nexp 
Version:       0.2
Release:       %mkrel 2
Summary:       Tool for browsing and monitoring KDE Nepomuk database
Group:         Graphical desktop/KDE
License:       GPLv3
Url:           http://gitorious.org/nexp/nexp-git 
Source:        122981-%name-%version.tar.gz
BuildRequires: kde4-macros
Requires:      python-qt4
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:     noarch

%description
NExp is Nepomuk Explorer.
A tool for browsing and monitoring KDE Nepomuk database.

%files 
%defattr(-,root,root)
%_kde_bindir/%name
%attr(755,root,root) %_kde_datadir/%name

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version

%build

%install
rm -rf %{buildroot}

%__mkdir -p %buildroot%_kde_datadir/%name
%__mkdir -p %buildroot%_kde_bindir/
cp -frv * %buildroot%_kde_datadir/%name/

pushd %buildroot%_prefix
ln -s %_kde_datadir/%name/main.py bin/%name
popd

%clean
rm -rf %{buildroot}


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2-2mdv2011.0
+ Revision: 613039
- the mass rebuild of 2010.1 packages

* Mon Apr 26 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.2-1mdv2010.1
+ Revision: 538873
- Fix perms
  CCBUG: 58898
- Add kde4-macros as BuildRequires:
  CCBUG: 58898
- Fix spec file
  CCBUG: 58898
- Fix licence
  CCBUG:58898
- import nexp


