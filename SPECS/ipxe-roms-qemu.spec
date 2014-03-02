Name:		ipxe-roms-qemu
Version:	1.0.0
Release:	1%{?dist}
Summary:	Open source boot firmware. Full PXE implementation enhanced with additional features.

License:	GPLv2+
URL:		http://ipxe.org
Source:		git://git.ipxe.org/ipxe.git
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	git, make
Requires:	qemu-kvm >= 0.12.1.2, libvirt >= 0.10.2

%description
iPXE is the leading open source network boot firmware. It provides a full PXE implementation enhanced with additional features such as:

  - boot from a web server via HTTP
  - boot from an iSCSI SAN
  - boot from a Fibre Channel SAN via FCoE
  - boot from an AoE SAN
  - boot from a wireless network
  - boot from a wide-area network
  - boot from an Infiniband network
  - control the boot process with a script

This package is built using the default options. More are available if you compile it from source and #define/#undef whatever you want in src/config/general.h

%prep
# make a backup of the current rom, if it exists. suppress all errors
# note: this doesn't actually work...
#cp /usr/share/gpxe/virtio-net.{rom,orig} 2>/dev/null || :
[ ! -d ipxe ] && git clone git://git.ipxe.org/ipxe.git

%build
cd ipxe/src/
make bin/virtio-net.rom

%install
mkdir -p %{buildroot}/usr/share/gpxe/
cp %{_builddir}/ipxe/src/bin/virtio-net.rom %{buildroot}/usr/share/gpxe/virtio-net.rom

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/share/gpxe/virtio-net.rom

%changelog
* Tue Mar 4 2014 Vlad Ionescu <vlad@vladionescu.com> - 1.0.0-1el6
- Built for qemu-kvm 0.12.1.2, libvirt 0.10.2 on RHEL 6.5
