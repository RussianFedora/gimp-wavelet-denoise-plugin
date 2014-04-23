Name:           gimp-wavelet-denoise-plugin
Version:        0.3.1
Release:        3%{?dist}
Summary:        Gimp wavelet denoise plugin

License:        GPLv2+
URL:            http://registry.gimp.org/node/4235
Source0:        http://registry.gimp.org/files/wavelet-denoise-%{version}.tar.gz

BuildRequires:  gimp-devel >= 2.4.0
BuildRequires:  pkgconfig
BuildRequires:  gettext

Requires:       gimp >= 2.4

%description
The wavelet denoise plugin is a tool to reduce noise in each channel of an
image separately. The default colour space to do denoising is YCbCr which
has the advantage that chroma noise can be reduced without affecting image
details. Denoising in CIELAB (L*a*b*) or RGB is available as an option.
The user interface allows colour mode and preview channel selection.
The denoising threshold can be set for each colour channel independently.

%prep
%setup -q -n wavelet-denoise-%{version}
sed -i -e 's/CFLAGS.*/& $(shell echo $$CFLAGS)/' src/Makefile
sed -i 's|gimptool-2.0 --libs)|gimptool-2.0 --libs) -lm|' src/Makefile
echo '#!/bin/bash' > configure
chmod +x configure


%build
%configure
make %{?_smp_mflags}


%install
GIMP_PLUGINS_DIR=`gimptool-2.0 --gimpplugindir`
sed -i "s|/usr/share/locale|%{buildroot}%{_datadir}/locale|" po/Makefile
mkdir -p %{buildroot}$GIMP_PLUGINS_DIR/plug-ins
install -m 0644 -p src/wavelet-denoise %{buildroot}$GIMP_PLUGINS_DIR/plug-ins
mkdir -p %{buildroot}%{_datadir}/locale/de/LC_MESSAGES
mkdir -p %{buildroot}%{_datadir}/locale/ru/LC_MESSAGES
mkdir -p %{buildroot}%{_datadir}/locale/it/LC_MESSAGES
mkdir -p %{buildroot}%{_datadir}/locale/et/LC_MESSAGES
mkdir -p %{buildroot}%{_datadir}/locale/pl/LC_MESSAGES
make install po
%find_lang gimp20-wavelet-denoise-plug-in


%files -f gimp20-wavelet-denoise-plug-in.lang
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/gimp/2.0/plug-ins/wavelet-denoise



%changelog
* Wed Apr 23 2014 Vasiliy N. Glazov <vascom2@gmail.com> - 0.3.1-3
- Correct install parameters

* Mon Mar 31 2014 Vasiliy N. Glazov <vascom2@gmail.com> - 0.3.1-2
- Correct CFLAGS

* Tue May 15 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.3.1-1
- initial release
