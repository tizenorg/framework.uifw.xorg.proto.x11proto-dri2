Name:       xorg-x11-proto-dri2proto
Summary:    X.Org X11 Protocol dri2proto
Version:    2.6
Release:    1.8
Group:      Development/System
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/proto/dri2proto-%{version}.tar.gz
Provides:   dri2proto
BuildRequires: pkgconfig(xorg-macros)

%description
Description: %{summary}



%prep
%setup -q -n %{name}-%{version}

%build

%reconfigure --disable-static \
    --libdir=%{_datadir}

# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%clean
rm -rf %{buildroot}






%files
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/dri2proto.h
%{_includedir}/X11/extensions/dri2tokens.h
%{_datadir}/pkgconfig/dri2proto.pc
%exclude %{_datadir}/doc/dri2proto/dri2proto.txt
