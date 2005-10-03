Summary:	Graphical frontend to communicate with mobiles
Summary(pl):	Graficzny interfejs do komunikacji z urz±dzeniami przeno¶nymi
Name:		obextool
Version:	0.33
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://www.tech-edv.co.at/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	99f8e26f882e95399322e75ad777eacf
#Source1:	%{name}.desktop
URL:		http://www.tech-edv.co.at/programmierung/en/gplsw.html
Requires:	tablelist
Requires:	tcl
Requires:	tk-BWidget
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_packagedir	%{_datadir}/%{name}

%description
ObexTool is a graphical frontend to communicate with mobiles and other
devices capable of communicating via Obex Protocol.

%description -l pl
ObexTool to graficzny interfejs do komunikacji z urz±dzeniami
przeno¶nymi i innymi urz±dzeniami potrafi±cymi komunikowaæ siê za
pomoc± protoko³u Obex.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_packagedir},%{_desktopdir}}

#install src/bin/secpanel $RPM_BUILD_ROOT%{_bindir}
#cp -r src/lib/secpanel/* $RPM_BUILD_ROOT%{_packagedir}
#install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc README CHANGES
#%attr(755,root,root) %{_bindir}/*
#%dir %{_libdir}/secpanel
#%attr(755,root,root) %{_libdir}/secpanel/listserver.tcl
#%attr(755,root,root) %{_libdir}/secpanel/secpanel*
#%{_libdir}/secpanel/convert_history.tcl
#%{_libdir}/secpanel/gui.tcl
#%{_libdir}/secpanel/default*
#%{_libdir}/secpanel/images
#%{_desktopdir}/*.desktop
