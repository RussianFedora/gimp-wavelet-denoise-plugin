Name:           gimp-wavelet-denoise-plugin
Version:        0.3.1
Release:        1%{?dist}
Summary:        Gimp wavelet denoise plugin

License:        GPLv2+
URL:            http://registry.gimp.org/node/4235
Source0:        http://registry.gimp.org/files/wavelet-denoise-%{version}.tar.gz

BuildRequires:  gimp-devel >= 2.4.0
BuildRequires:  pkgconfig

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


%build
sed -i 's|gimptool-2.0 --libs)|gimptool-2.0 --libs) -lm|' src/Makefile
sed -i "s|/usr/share/locale|$RPM_BUILD_ROOT/usr/share/locale|" po/Makefile
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
GIMP_PLUGINS_DIR=`gimptool-2.0 --gimpplugindir`
mkdir -p $RPM_BUILD_ROOT$GIMP_PLUGINS_DIR/plug-ins
install src/wavelet-denoise $RPM_BUILD_ROOT$GIMP_PLUGINS_DIR/plug-ins
mkdir -p $RPM_BUILD_ROOT/usr/share/locale/de/LC_MESSAGES
mkdir -p $RPM_BUILD_ROOT/usr/share/locale/ru/LC_MESSAGES
mkdir -p $RPM_BUILD_ROOT/usr/share/locale/it/LC_MESSAGES
mkdir -p $RPM_BUILD_ROOT/usr/share/locale/et/LC_MESSAGES
mkdir -p $RPM_BUILD_ROOT/usr/share/locale/pl/LC_MESSAGES
make install po
%find_lang gimp20-wavelet-denoise-plug-in


%files -f gimp20-wavelet-denoise-plug-in.lang
%doc AUTHORS  ChangeLog  COPYING README
%{_libdir}/gimp/2.0/plug-ins/wavelet-denoise



%changelog
* Wed May 15 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.3.1-1.R
- initial release
