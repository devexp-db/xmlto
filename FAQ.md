Q: I'm trying to build xmlto, but it doesn't work.

A: If you get `Attempt to load network entity` errors when building
xmlto, your system does not have the required support for XML
Catalogs (http://www.oasis-open.org/committees/entity/spec-2001-08-06.html).
Try to reinstall your docbook(xhtml1) dtds or fix your catalogs
manually. Verbose mode might help to analyze a problem.

Q: How can I check out the latest sources of XMLTO?

A: Original sources are under svn revision control on fedorahosted.org
server. If you want to check out the latest version, use command

```bash
svn co http://svn.fedorahosted.org/svn/xmlto
```

Autotools helper scripts are not under revision control, so please
run `automake --add-missing` to make these files available.
