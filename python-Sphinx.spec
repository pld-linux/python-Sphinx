Summary:	Sphinx - Python documentation builder
Summary(pl.UTF-8):	Sphinx - narzędzie do tworzenia dokumentacji dla Pythona
Name:		python-Sphinx
Version:	1.0.6
Release:	1
License:	BSD (Sphinx itself, SmartyPants), PSF v2 (pgen2), MIT (ElementTree, JQuery)
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/S/Sphinx/Sphinx-%{version}.tar.gz
# Source0-md5:	4cdb86c7bb7fa2498ac12db844784769
URL:		http://sphinx.pocoo.org/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sphinx is a tool that translates a set of reStructuredText_ source
files into various output formats, automatically producing
cross-references, indices etc. That is, if you have a directory
containing a bunch of reST-formatted documents (and possibly
subdirectories of docs in there as well), Sphinx can generate a
nicely-organized arrangement of HTML files (in some other directory)
for easy browsing and navigation. But from the same source, it can
also generate a LaTeX file that you can compile into a PDF version of
the documents, or a PDF file directly using rst2pdf
(<http://rst2pdf.googlecode.com>).

%description -l pl.UTF-8
Sphinx to narzędzie tłumaczące zbiór plików źródłowych zawierających
reStructuredText_ na różne formaty wyjściowe z automatycznym
tworzeniem wzajemnych odniesień, indeksów itp. Oznacza to, że mając
katalog zawierający zbiór dokumentów w formacie reST (i być może
dalsze podkatalogi dokumentacji) przy użyciu Sphinksa można
wygenerować ładnie zorganizowane pliki HTML (w jakimś innym katalogu)
pozwalające na łatwe przeglądanie i nawigowanie. Z tych samych źródeł
można też wygenerować plik LaTeXa, który można następnie skompilować
do wersji PDF albo wygenerować plik PDF bezpośrednio przy użyciu
narzędzia rst2pdf (<http://rst2pdf.googlecode.com>).

%prep
%setup -q -n Sphinx-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES EXAMPLES LICENSE README TODO
%attr(755,root,root) %{_bindir}/sphinx-autogen
%attr(755,root,root) %{_bindir}/sphinx-build
%attr(755,root,root) %{_bindir}/sphinx-quickstart
%{py_sitescriptdir}/sphinx
%{py_sitescriptdir}/Sphinx-%{version}-py*.egg-info
