Name:          nexp
Version:       0.2
Release:       %mkrel 1
Summary:       Tool for browsing and monitoring KDE Nepomuk database
Group:         Graphical desktop/KDE
License:       GPLv2+
Url:           http://gitorious.org/nexp/nexp-git 
Source:        122981-%name-%version.tar.gz
Requires:      python-qt4
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:     noarch

%description
NExp is Nepomuk Explorer.
A tool for browsing and monitoring KDE Nepomuk database.

%files 
%defattr(-,root,root)
%_kde_bindir/%name
%_kde_datadir/%name

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
