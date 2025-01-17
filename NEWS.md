# XMLTO News

- 0.0.29 (stable)

  - Rename variable BASH to XMLTO_BASH_PATH (#8)
  - Regenerate xmlif to use new version of gcc
  - Rename and format markdown files
  - Update Fedora spec file generation according to Fedora package repo
  - Convert output path to unix on cygwin/msys
  - Add .gitignore
  - Skip validating xmlto man page during build

- 0.0.28 (stable)

  - fix broken temp files removal (introduced in 0.0.27)
  - links detection changed to elinks (new links options
    not compatible)

- 0.0.27 (stable)

  - remove several bashisms from scripts
  - add new option `--profile` for preprocessing documents
    with profiling stylesheet
  - fix several potential crashes in xmlif (found by static
    analysis)

- 0.0.26 (stable)

  - `--searchpath` option no longer produces warning
    about local builtin used outside the function
    (debian #652974)
  - fix build with automake 1.13+
  - fix noextensions option recognition
  - handle used css list in epub format

- 0.0.25 (stable)

  - prevent possible collisions in manpage generation
  - fix broken `fop/fop1` extensions
  - fix handling of external data objects with fop
    (debian #568894)

- 0.0.24 (stable)

  - README file was improved to provide better guidance
    for users
  - show the text-web-browser converting command in
    verbose mode for better debugging
  - workaround passivetex limitation for chapters
    titles starting with L
  - use passivetex/fop extensions by default, provide
    --noextensions option to disable them
  - basic experimental support for conversion from docbook
    to epub

- 0.0.23 (stable)

  - add support for detection of tail and gnu cp, do
    not hardcode `/bin/bash` initial value
  - use those detected binaries instead of previously
    hardcoded ones
  - use `type -t` bash shell builtin instead of `which`
    utility for detection of file availability
  - new option `--noautosize` to prevent overriding of
    user-defined paper sizes

- 0.0.22 (stable)

  - added experimental support for xhtml1 source format
    (output formats are awt, dvi, fo, mif, pcl, pdf, ps,
    svg, txt)
  - create tex and xhtml subpackage in spec file to reduce
    requirements for main package
  - automated detection of programs path in configure,
    program/utility path could be passed to configure by
    variable, allowed selection of default backend and
    default webbrowser (just for requirements at the moment)
  - check for missing tools/programs, fail if tool is not
    available
  - fixed libpaper cleaning up(debian #491390)
  - xmllint validity check now with noent option(debian
    #516253)
  - fixed `--stringparam` option
  - added some messages to easier detection of troubles,
    used different error codes for various situations(see
    docs)
  - fixed FSF addresses, xmlif now licensed under GPLv2+
    (was GPL+, various indentation fixes, fixed documentation
    compilation warnings)

- 0.0.21 (stable)

  - added experimental support for dblatex (needs installed
    dblatex package)
  - fixed issue with `cp -a` option on non-gnu systems
    non-mandatory support for libpaper

- 0.0.20 (stable)

  - added experimental fop support(needs installed fop package)
    possibility to read a stylesheet from STDIN
  - some small fixes/changes in docbook formats and xmlto script

- 0.0.19 (stable)

  - added supported for basename with spaces
  - stringparam option for passing argument to stylesheet
  - bash no longer hardcoded
  - added option for not cleaning temp files for diagnostics

- 0.0.18 (stable)

  - A portability problem was fixed, and the xmlif syntax was modified.

- 0.0.17 (stable)

  - The exit code when validation fails was fixed. w3m is used for text output.

- 0.0.16 (stable)

  - Minor bug-fixes.

- 0.0.15 (stable)

  - Some format script fixes.

- 0.0.14 (stable)

  - The db2man fixes are no longer needed.

- 0.0.13 (stable)

  - Several minor bugs were fixed.

- 0.0.12 (stable)

  - Validation is now working, and output encoding is
    determined from the environment.

- 0.0.11 (stable)

  - The db2man stylesheet is no longer shipped,
    since it now comes with docbook-xsl.
  - A new tool, xmlif, is included.
  - Several bugs were fixed.

- 0.0.10 (stable)

  - A small bug was fixed in the PS and DVI format scripts,
    and the db2man code has been synchronised to CVS.

- 0.0.9 (stable)

  - There were some further improvements made to db2man.

- 0.0.8 (stable)

  - There were assorted fixes, and some further db2man improvements.

- 0.0.7 (stable)

  - Some portability fixes were made and
    there were some more db2man improvements.

- 0.0.6 (stable)

  - Some db2man improvements were made, some minor script bugs
    were fixed, and automatic paper size handling was added.

- 0.0.5 (stable)

  - Some db2man bugs were fixed.

- 0.0.4 (stable)

  - The option handling was improved.

- 0.0.3 (stable)

  - The db2man stylesheet was further improved.

- 0.0.2 (stable)

  - More format scripts were added, and the db2man stylesheet was
    further improved.

- 0.0.1 (stable)

  - Made the format script interface definition a bit clearer.

- 0.0.0 (stable)

  - Initial release.
