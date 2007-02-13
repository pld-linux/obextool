Summary:	Graphical frontend to communicate with mobiles
Summary(pl.UTF-8):	Graficzny interfejs do komunikacji z urządzeniami przenośnymi
Name:		obextool
Version:	0.33
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/obextool/%{name}-%{version}.tar.gz
# Source0-md5:	bdd4c7e35d353ac6bb5af98c8b6ae5a9
URL:		http://www.tech-edv.co.at/programmierung/en/gplsw.html
Requires:	obexftp
Requires:	tablelist
Requires:	tcl
Requires:	tk-BWidget
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_packagedir	%{_datadir}/%{name}

%description
ObexTool is a graphical frontend to communicate with mobiles and other
devices capable of communicating via Obex Protocol.

%description -l pl.UTF-8
ObexTool to graficzny interfejs do komunikacji z urządzeniami
przenośnymi i innymi urządzeniami potrafiącymi komunikować się za
pomocą protokołu Obex.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/%{name},%{_bindir},%{_packagedir},%{_desktopdir}}

cp -a etc/* $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
cp -a * $RPM_BUILD_ROOT%{_packagedir}
rm -rf $RPM_BUILD_ROOT%{_packagedir}/{etc,doc}

cat > $RPM_BUILD_ROOT%{_bindir}/obextool << 'EOF'
#!/bin/sh
# ObexTool startup shell
#
MODEM="/dev/modem"
[ -n "$1" ] && MODEM="$1"
OBEXDIR=%{_packagedir}
OBEXTOOL_CFG=%{_sysconfdir}/obextool
OBEXTCMD="%{_bindir}/obexftp -t ${MODEM}"
export OBEXDIR OBEXTOOL_CFG OBEXTCMD
#
# Let's start the ObexTool without memory status
# feature (if no Siemens), using Tk version 8.4 and
# a specific configuration directory %{_sysconfdir}/obextool
# and the contributed static compiled obexftp version.
exec %{_bindir}/wish $OBEXDIR/obextool.tk --memstat 0
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/*
%{_packagedir}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/*.???
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/*.sh
