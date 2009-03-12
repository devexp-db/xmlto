Summary: A tool for converting XML files to various formats.
Name: xmlto
Version: 0.0.21
Release: 0.1
License: GPLv2
Group: Applications/System
#Older versions up to xmlto-0.0.20
#URL: http://cyberelk.net/tim/xmlto/
#Source0: http://cyberelk.net/tim/data/xmlto/stable/%{name}-%{version}.tar.bz2
URL: https://fedorahosted.org/xmlto/
Source0: http://svn.fedorahosted.org/svn/%{name}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot

BuildRequires: docbook-xsl >= 1.56.0
BuildRequires: libxslt
BuildRequires: util-linux, flex

# We rely entirely on the DocBook XSL stylesheets!
Requires: docbook-xsl >= 1.56.0

# We need one of text-www-browsers(w3m,lynx,elinks) for full functionality
# Chosen w3m, in Fedora there is require for virtual provide 
# text-www-browser instead of it
Requires: w3m

# For full functionality, we need passivetex.
Requires: passivetex >= 1.11
Requires: libxslt
Requires: docbook-dtds
Requires: util-linux, flex

%description
This is a package for converting XML files to various formats using XSL
stylesheets.

%prep
%setup -q

%build
%configure
make
make check

%install
rm -rf %{buildroot}
%makeinstall

[ -d %{buildroot}%{_datadir}/xmlto/xsl ] || \
  mkdir %{buildroot}%{_datadir}/xmlto/xsl

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/*/*
%{_datadir}/xmlto

%changelog
* Fri Jun 20 2008 Ondrej Vasik <ovasik@redhat.com>
- New version 0.0.21
- added dblatex experimental support
- non-mandatory libpaper support
- fixed issue of cp -a option on non-gnu systems

* Tue Jan 15 2008 Ondrej Vasik <ovasik@redhat.com>
- New version 0.0.20
- fop experimental support
- possibility to read stylesheet from STDIN, using 
  recursive cp in docbook formats, preparations
  for other source formats 

* Mon Nov 19 2007 Ondrej Vasik <ovasik@redhat.com>
- New version 0.0.19
- License GPLv2 , changes since last comment in NEWS

* Fri May 23 2003 Tim Waugh <twaugh@redhat.com>
- Be sure to create the xsl directory.
- README.docbook-xsl is no longer shipped.

* Wed Oct  9 2002 Tim Waugh <twaugh@redhat.com>
- Build requires docbook-xsl >= 1.56.0.

* Sun Oct  6 2002 Tim Waugh <twaugh@redhat.com>
- Remove 'BuildArch: noarch' now that we ship a compiled object.
- Run tests.
- Ship xmlif.
- Build requires docbook-xsl >= 1.52.0.

* Fri Aug 30 2002 Tim Waugh <twaugh@redhat.com>
- Bump docbook-xsl requirement to 1.52.0 for manpages.

* Fri Aug  2 2002 Tim Waugh <twaugh@redhat.com>
- The archive is now distributed in .tar.bz2 format.

* Fri Jan 25 2002 Tim Waugh <twaugh@redhat.com>
- Require the DocBook DTDs.

* Fri Jan 18 2002 Tim Waugh <twaugh@redhat.com>
- Ship README.docbook-xsl.

* Fri Nov 23 2001 Tim Waugh <twaugh@redhat.com>
- Initial spec file.