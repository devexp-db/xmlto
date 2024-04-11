# xmlto

Utility `xmlto` is a simple shell script for converting XML files to various formats.
It serves as an easy-to-use command-line frontend to make fine output without
remembering many long options and searching for the syntax of the backends.

Currently, it supports conversion from `docbook`, `xhtml1`, and `fo` format to
various output formats (`awt`, `fo`, `htmlhelp`, `javahelp`, `mif`, `pdf`, `svg`,
`xhtml`, `dvi`, `html`, `html-nochunks`, `man`, `pcl`, `ps`, `txt`, `xhtml-nochunks`).
Some output formats may be unavailable if you don't have all prerequisites installed,
as xmlto uses backends (`xsltproc`, `passivetex/fop/dblatex`) for processing.

You could check and generate the offline version of documentation with xmlto from
`doc/xmlif.xml` sources. However, if you received the xmlif as a part of the distribution,
you should already have the `xmlif(1)` manpage on your machine.

If you received xmlto as a part of the distribution, you should already have
the `xmlto(1)` manpage on your machine.

# xmlif

`xmlif` utility filters XML according to conditionalizing markup. This can be useful
for formatting one of several versions of an XML document depending on conditions
passed to the command.

You could check and generate the offline version of documentation with xmlto from
`doc/xmlif.xml` sources. However, if you received xmlif as a part of distribution,
you should already have `xmlif(1)` manpage on your machine.

# How to contact authors

Since xmlto 0.19, xmlto is maintained by Ondřej Vašík (`ovasik@redhat.com`) and
since 0.29 co-maintained by Ondřej Sloup (`osloup@redhat.com`).

You can contact me directly via email or leave a issue on the project's Pagure
instance at [https://pagure.io/xmlto/new_issue](https://pagure.io/xmlto/new_issue).
A registered fedoraproject.org account is required for this.
