Summary:	FrameBuffer Viewer
Name:		fbv
Version:	1.0b
Release:	2
License:	GPL
Group:		Applications/Graphics
Source0:	http://s-tech.elsat.net.pl/fbv/%{name}-%{version}.tar.gz
# Source0-md5:	3e466375b930ec22be44f1041e77b55d
Patch0:		%{name}-nocenter.patch
Patch1:		%{name}-libpng15.patch
Patch2:		%{name}-giflib.patch
URL:		http://s-tech.elsat.net.pl/
BuildRequires:	giflib-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	util-linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple program to view pictures on a framebuffer console. It
supports PNG, JPEG, GIF and BMP files.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
./configure \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--mandir=%{_mandir}

%{__make} \
	CC="%{__cc} %{rpmcflags}" \
	LIBS="-lpng -ljpeg -lgif"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

