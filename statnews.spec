%include	/usr/lib/rpm/macros.perl
Summary:	Extracts some useful statistics out of a newsgroup
Summary(pl):	Generator statystyk grup newsowych
Name:		statnews
Version:	2.3
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://ftp.debian.org/debian/pool/main/s/statnews/%{name}_%{version}.tar.gz
# Source0-md5:	f8aba0c65c8b806cf4803943e4b2d0d5
URL:		http://packages.qa.debian.org/s/statnews.html
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Extracts some useful statistics out of a newsgroup. This program may
be useful to analyze newsgroups with respect to authors, messages
length and frequency, and so on.

%description -l pl
Wyci±ga ró¿ne interesuj±ce informacje z grup newsowych. Ten program
mo¿e byæ u¿yteczny do analizowania grup newsowych pod wzglêdem
autorów, d³ugo¶ci wiadomo¶ci, czêstotliwo¶ci itp.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -D %{name}.pl $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
