ipxe-roms-qemu
==============

Enables iPXE client (as opposed to the default and outdated gPXE) for KVM/QEMU.

This is an unofficial package for 64-bit RHEL/CentOS 6 (el6) so I don't have to build from source every time.

Compatibility
-------------

Built and tested on RHEL 6.5, should be compatible with all RHEL 6 and equivalent.

Honestly it probably works everywhere KVM/QEMU is used. It is just a ROM after all.

Installation
------------

This package requires qemu-kvm and libvirt, just so you're not installing this without purpose. If you just want the ROM, build from source.

Download the package then install using ```yum``` not ```rpm```. This ensures RPMDB isn't altered outside of yum and is the recommended way of installing rpms.

```
yum install ipxe-roms-qemu-1.0.0-1.el6.x86_64.rpm
```


History
-------

This is current (1.0.0) as of this writing (Mar 2014).

The source was last updated the day this package was built.

v1.0.0 was released in 2010 with ongoing changes and updates. The version has not changed since.

Features
--------

You should build this from source (it is really easy) if you want to enable or disable features. iPXE has a lot to offer, check out **src/config/general.h** for available features. You can enable them each with #define or disable with #undef. By default (what this package provides) the feature set is pretty extensive. It supports TFTP and HTTP sources, and wireless interfaces.

See the project page for a more comprehensive listing.

Original
--------

Project page: http://ipxe.org/
