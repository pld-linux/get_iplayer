%include	/usr/lib/rpm/macros.perl
Summary:	BBC iPlayer indexing tool and PVR
Summary(pl.UTF-8):	Narzędzie indeksujące i nagrywające dla BBC iPlayera
Name:		get_iplayer
Version:	2.94
Release:	1
License:	GPL v3+
Group:		Applications/Multimedia
Source0:	ftp://ftp.infradead.org/pub/get_iplayer/%{name}-%{version}.tar.gz
# Source0-md5:	180883975710fa3548f1e3359e21d5e2
URL:		https://github.com/dinkypumpkin/get_iplayer/
BuildRequires:	rpm-perlprov
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
get_iplayer lists, searches and records BBC iPlayer TV/Radio, BBC
Podcast programmes. Other 3rd-Party plugins may be available.

%description -l pl.UTF-8
get_iplayer wypisuje, wyszukuje i zapisuje programy BBC iPlayer
TV/Radio oraz BBC Podcast. Dostępne mogą być też inne wtyczki.

%package cgi
Summary:	Web-based PVR manager and streaming proxy for get_iplayer
Summary(pl.UTF-8):	Oparty na WWW zarządca PVR i proxy strumieni dla programu get_iplayer
Group:		Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description cgi
Web-based PVR manager and streaming proxy for get_iplayer.

Warning: it's insecure, never run it in an untrusted environment or
facing the Internet.

%description cgi -l pl.UTF-8
Oparty na WWW zarządca PVR i proxy strumieni dla programu get_iplayer.

Uwaga: ten program nie jest bezpieczny, nigdy nie należy uruchamiać go
w niezaufanym środowisku lub z dostępem z Internetu.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/env perl,/usr/bin/perl,' get_iplayer get_iplayer.cgi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/get_iplayer/plugins,/usr/lib/cgi-bin}

install get_iplayer $RPM_BUILD_ROOT%{_bindir}
install get_iplayer.cgi $RPM_BUILD_ROOT/usr/lib/cgi-bin
cp -p get_iplayer.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -p plugins/*.plugin $RPM_BUILD_ROOT%{_datadir}/get_iplayer/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.txt CONTRIBUTORS README.md html plugins/plugin.template
%attr(755,root,root) %{_bindir}/get_iplayer
%{_datadir}/get_iplayer
%{_mandir}/man1/get_iplayer.1*

%files cgi
%defattr(644,root,root,755)
%doc CHANGELOG-get_iplayer.cgi.txt README-get_iplayer.cgi.txt
%attr(755,root,root) /usr/lib/cgi-bin/get_iplayer.cgi
