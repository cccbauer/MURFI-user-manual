.first {font-weight: bold; margin-left: none; padding-right: 1em;vertical-align: top; }
.second {padding-left: 1em; width: 100%; vertical-align: center; }
.id {font-family: monospace;}
.indented {margin-left: 2em; border-left: dotted thin #dde; padding-bottom: 1em; }
.node {border: solid thin #ffcc66; padding: 1em; background: #ffffcc; }
.node-unclaimed {border: dotted thin #c3c3c3; padding: 1em; background: #fafafa; color: red; }
.node-disabled {border: solid thin #f55; padding: 1em; background: #fee; color: gray; }
rt
id:rt
description: Notebook
product: Oryx Pro (Not Applicable)
vendor: System76
version: oryp5
serial: Not Applicable
width: 64 bits
capabilities: smbios-3.0 dmi-3.0 smp vsyscall32
configuration: administrator_password=disabled boot=normal chassis=notebook family=Not Applicable sku=Not Applicable uuid=000096F0-0000-0010-8000-80FA5B66113E
id:core
description: Motherboard
product: Oryx Pro
vendor: System76
physical id: 0
version: oryp5
serial: Not Applicable
slot: To Be Filled By O.E.M.
id:firmware
description: BIOS
vendor: INSYDE Corp.
physical id: 0
version: 1.07.09
date: 06/13/2019
size: 128KiB
capacity: 10176KiB
capabilities: pci upgrade shadowing bootselect edd int5printscreen int17printer acpi usb biosbootspecification uefi
id:cpu
description: CPU
product: Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
vendor: Intel Corp.
physical id: 4
bus info: cpu@0
version: Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
serial: To Be Filled By O.E.M.
slot: U3E1
size: 2934MHz
capacity: 4100MHz
width: 64 bits
clock: 100MHz
capabilities: x86-64 fpu fpu_exception wp vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb invpcid_single pti ssbd ibrs ibpb stibp tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid mpx rdseed adx smap clflushopt intel_pt xsaveopt xsavec xgetbv1 xsaves dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp md_clear flush_l1d cpufreq
configuration: cores=6 enabledcores=6 threads=12
id:cache:0
description: L1 cache
physical id: 5
slot: L1 Cache
size: 384KiB
capacity: 384KiB
capabilities: synchronous internal write-back unified
configuration: level=1
id:cache:1
description: L2 cache
physical id: 6
slot: L2 Cache
size: 1536KiB
capacity: 1536KiB
capabilities: synchronous internal write-back unified
configuration: level=2
id:cache:2
description: L3 cache
physical id: 7
slot: L3 Cache
size: 9MiB
capacity: 9MiB
capabilities: synchronous internal write-back unified
configuration: level=3
id:memory
description: System Memory
physical id: 1c
slot: System board or motherboard
size: 32GiB
id:bank:0
description: SODIMM DDR4 Synchronous 2667 MHz (0.4 ns)
product: CT16G4SFD8266.C16FD1
vendor: 859B
physical id: 0
serial: E0CB952A
slot: ChannelA-DIMM0
size: 16GiB
width: 64 bits
clock: 2667MHz (0.4ns)
id:bank:1
description: SODIMM DDR4 Synchronous 2667 MHz (0.4 ns)
product: CT16G4SFD8266.C16FD1
vendor: 859B
physical id: 1
serial: E0CB952F
slot: ChannelB-DIMM0
size: 16GiB
width: 64 bits
clock: 2667MHz (0.4ns)
id:pci
description: Host bridge
product: 8th Gen Core Processor Host Bridge/DRAM Registers
vendor: Intel Corporation
physical id: 100
bus info: pci@0000:00:00.0
version: 07
width: 32 bits
clock: 33MHz
configuration: driver=skl_uncore
resources: irq:0
id:pci:0
description: PCI bridge
product: Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor PCIe Controller (x16)
vendor: Intel Corporation
physical id: 1
bus info: pci@0000:00:01.0
version: 07
width: 32 bits
clock: 33MHz
capabilities: pci pm msi pciexpress normal_decode bus_master cap_list
configuration: driver=pcieport
resources: irq:122 ioport:4000(size=4096) memory:a0000000-b40fffff ioport:b4100000(size=1048576)
id:display
description: VGA compatible controller
product: NVIDIA Corporation
vendor: NVIDIA Corporation
physical id: 0
bus info: pci@0000:01:00.0
version: a1
width: 64 bits
clock: 33MHz
capabilities: pm msi pciexpress vga_controller bus_master cap_list rom
configuration: driver=nouveau latency=0
resources: irq:153 memory:b3000000-b3ffffff memory:a0000000-afffffff memory:b0000000-b1ffffff ioport:4000(size=128) memory:b2000000-b207ffff
id:multimedia
description: Audio device
product: NVIDIA Corporation
vendor: NVIDIA Corporation
physical id: 0.1
bus info: pci@0000:01:00.1
version: a1
width: 32 bits
clock: 33MHz
capabilities: pm msi pciexpress bus_master cap_list
configuration: driver=snd_hda_intel latency=0
resources: irq:17 memory:b4000000-b4003fff
id:usb
description: USB controller
product: NVIDIA Corporation
vendor: NVIDIA Corporation
physical id: 0.2
bus info: pci@0000:01:00.2
version: a1
width: 64 bits
clock: 33MHz
capabilities: msi pciexpress pm xhci bus_master cap_list
configuration: driver=xhci_hcd latency=0
resources: irq:128 memory:b4100000-b413ffff memory:b4140000-b414ffff
id:usbhost:0
product: xHCI Host Controller
vendor: Linux 5.4.0-73-generic xhci-hcd
physical id: 0
bus info: usb@3
logical name: usb3
version: 5.04
capabilities: usb-2.00
configuration: driver=hub slots=2 speed=480Mbit/s
id:usbhost:1
product: xHCI Host Controller
vendor: Linux 5.4.0-73-generic xhci-hcd
physical id: 1
bus info: usb@4
logical name: usb4
version: 5.04
capabilities: usb-3.10
configuration: driver=hub slots=4 speed=10000Mbit/s
id:serial
description: Serial bus controller
product: NVIDIA Corporation
vendor: NVIDIA Corporation
physical id: 0.3
bus info: pci@0000:01:00.3
version: a1
width: 32 bits
clock: 33MHz
capabilities: msi pciexpress pm bus_master cap_list
configuration: driver=nvidia-gpu latency=0
resources: irq:129 memory:b4004000-b4004fff
id:display
description: VGA compatible controller
product: Intel Corporation
vendor: Intel Corporation
physical id: 2
bus info: pci@0000:00:02.0
version: 00
width: 64 bits
clock: 33MHz
capabilities: pciexpress msi pm vga_controller bus_master cap_list rom
configuration: driver=i915 latency=0
resources: irq:154 memory:b5000000-b5ffffff memory:90000000-9fffffff ioport:5000(size=64) memory:c0000-dffff
id:generic:0
description: Signal processing controller
product: Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem
vendor: Intel Corporation
physical id: 4
bus info: pci@0000:00:04.0
version: 07
width: 64 bits
clock: 33MHz
capabilities: msi pm bus_master cap_list
configuration: driver=proc_thermal latency=0
resources: irq:16 memory:b4610000-b4617fff
id:generic:1
description: Signal processing controller
product: Cannon Lake PCH Thermal Controller
vendor: Intel Corporation
physical id: 12
bus info: pci@0000:00:12.0
version: 10
width: 64 bits
clock: 33MHz
capabilities: pm msi bus_master cap_list
configuration: driver=intel_pch_thermal latency=0
resources: irq:16 memory:b4624000-b4624fff
id:usb
description: USB controller
product: Cannon Lake PCH USB 3.1 xHCI Host Controller
vendor: Intel Corporation
physical id: 14
bus info: pci@0000:00:14.0
version: 10
width: 64 bits
clock: 33MHz
capabilities: pm msi xhci bus_master cap_list
configuration: driver=xhci_hcd latency=0
resources: irq:127 memory:b4600000-b460ffff
id:usbhost:0
product: xHCI Host Controller
vendor: Linux 5.4.0-73-generic xhci-hcd
physical id: 0
bus info: usb@1
logical name: usb1
version: 5.04
capabilities: usb-2.00
configuration: driver=hub slots=16 speed=480Mbit/s
id:usb:0
description: Video
product: Chicony USB2.0 Camera
vendor: Sonix Technology Co., Ltd.
physical id: 8
bus info: usb@1:8
version: 54.04
capabilities: usb-2.00
configuration: driver=uvcvideo maxpower=500mA speed=480Mbit/s
id:usb:1
description: Generic USB device
vendor: Synaptics, Inc.
physical id: a
bus info: usb@1:a
version: 0.00
serial: 3bd2d88c21e3
capabilities: usb-2.00
configuration: maxpower=100mA speed=12Mbit/s
id:usb:2
description: Bluetooth wireless interface
vendor: Intel Corp.
physical id: e
bus info: usb@1:e
version: 0.02
capabilities: bluetooth usb-2.00
configuration: driver=btusb maxpower=100mA speed=12Mbit/s
id:usbhost:1
product: xHCI Host Controller
vendor: Linux 5.4.0-73-generic xhci-hcd
physical id: 1
bus info: usb@2
logical name: usb2
version: 5.04
capabilities: usb-3.10
configuration: driver=hub slots=8 speed=10000Mbit/s
id:memory
description: RAM memory
product: Cannon Lake PCH Shared SRAM
vendor: Intel Corporation
physical id: 14.2
bus info: pci@0000:00:14.2
version: 10
width: 64 bits
clock: 33MHz (30.3ns)
capabilities: pm bus_master cap_list
configuration: latency=0
resources: memory:b4620000-b4621fff memory:b4625000-b4625fff
id:network
description: Wireless interface
product: Wireless-AC 9560 [Jefferson Peak]
vendor: Intel Corporation
physical id: 14.3
bus info: pci@0000:00:14.3
logical name: wlp0s20f3
version: 10
serial: f4:d1:08:65:af:b8
width: 64 bits
clock: 33MHz
capabilities: pm msi pciexpress msix bus_master cap_list ethernet physical wireless
configuration: broadcast=yes driver=iwlwifi driverversion=5.4.0-73-generic firmware=46.6bf1df06.0 ip=10.105.7.243 latency=0 link=yes multicast=yes wireless=IEEE 802.11
resources: irq:16 memory:b4618000-b461bfff
id:serial:0
description: Serial bus controller
product: Intel Corporation
vendor: Intel Corporation
physical id: 15
bus info: pci@0000:00:15.0
version: 10
width: 64 bits
clock: 33MHz
capabilities: pm bus_master cap_list
configuration: driver=intel-lpss latency=0
resources: irq:16 memory:8d800000-8d800fff
id:serial:1
description: Serial bus controller
product: Intel Corporation
vendor: Intel Corporation
physical id: 15.1
bus info: pci@0000:00:15.1
version: 10
width: 64 bits
clock: 33MHz
capabilities: pm bus_master cap_list
configuration: driver=intel-lpss latency=0
resources: irq:17 memory:8d801000-8d801fff
id:communication
description: Communication controller
product: Cannon Lake PCH HECI Controller
vendor: Intel Corporation
physical id: 16
bus info: pci@0000:00:16.0
version: 10
width: 64 bits
clock: 33MHz
capabilities: pm msi bus_master cap_list
configuration: driver=mei_me latency=0
resources: irq:132 memory:b4628000-b4628fff
id:storage
description: SATA controller
product: Intel Corporation
vendor: Intel Corporation
physical id: 17
bus info: pci@0000:00:17.0
version: 10
width: 32 bits
clock: 66MHz
capabilities: storage msi pm ahci_1.0 bus_master cap_list
configuration: driver=ahci latency=0
resources: irq:130 memory:b4622000-b4623fff memory:b462c000-b462c0ff ioport:5080(size=8) ioport:5088(size=4) ioport:5060(size=32) memory:b462b000-b462b7ff
id:pci:1
description: PCI bridge
product: Cannon Lake PCH PCI Express Root Port 21
vendor: Intel Corporation
physical id: 1b
bus info: pci@0000:00:1b.0
version: f0
width: 32 bits
clock: 33MHz
capabilities: pci pciexpress msi pm normal_decode bus_master cap_list
configuration: driver=pcieport
resources: irq:123
id:pci:2
description: PCI bridge
product: Cannon Lake PCH PCI Express Root Port 9
vendor: Intel Corporation
physical id: 1d
bus info: pci@0000:00:1d.0
version: f0
width: 32 bits
clock: 33MHz
capabilities: pci pciexpress msi pm normal_decode bus_master cap_list
configuration: driver=pcieport
resources: irq:124 memory:b4500000-b45fffff
id:storage
description: Non-Volatile memory controller
product: NVMe SSD Controller SM981/PM981
vendor: Samsung Electronics Co Ltd
physical id: 0
bus info: pci@0000:07:00.0
version: 00
width: 64 bits
clock: 33MHz
capabilities: storage pm msi pciexpress msix nvm_express bus_master cap_list
configuration: driver=nvme latency=0
resources: irq:16 memory:b4500000-b4503fff
id:pci:3
description: PCI bridge
product: Intel Corporation
vendor: Intel Corporation
physical id: 1d.6
bus info: pci@0000:00:1d.6
version: f0
width: 32 bits
clock: 33MHz
capabilities: pci pciexpress msi pm normal_decode bus_master cap_list
configuration: driver=pcieport
resources: irq:125 ioport:3000(size=4096) memory:b4400000-b44fffff
id:network
description: Ethernet interface
product: RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller
vendor: Realtek Semiconductor Co., Ltd.
physical id: 0
bus info: pci@0000:08:00.0
logical name: enp8s0
version: 15
serial: 80:fa:5b:66:11:3e
capacity: 1Gbit/s
width: 64 bits
clock: 33MHz
capabilities: pm msi pciexpress msix bus_master cap_list ethernet physical tp mii 10bt 10bt-fd 100bt 100bt-fd 1000bt-fd autonegotiation
configuration: autonegotiation=on broadcast=yes driver=r8169 firmware=rtl8168h-2_0.0.2 02/26/15 latency=0 link=no multicast=yes port=MII
resources: irq:18 ioport:3000(size=256) memory:b4404000-b4404fff memory:b4400000-b4403fff
id:pci:4
description: PCI bridge
product: Intel Corporation
vendor: Intel Corporation
physical id: 1d.7
bus info: pci@0000:00:1d.7
version: f0
width: 32 bits
clock: 33MHz
capabilities: pci pciexpress msi pm normal_decode bus_master cap_list
configuration: driver=pcieport
resources: irq:126 memory:b4300000-b43fffff
id:generic
description: Unassigned class
product: RTS525A PCI Express Card Reader
vendor: Realtek Semiconductor Co., Ltd.
physical id: 0
bus info: pci@0000:09:00.0
version: 01
width: 32 bits
clock: 33MHz
capabilities: pm msi pciexpress bus_master cap_list
configuration: driver=rtsx_pci latency=0
resources: irq:131 memory:b4300000-b4300fff
id:isa
description: ISA bridge
product: Intel Corporation
vendor: Intel Corporation
physical id: 1f
bus info: pci@0000:00:1f.0
version: 10
width: 32 bits
clock: 33MHz
capabilities: isa bus_master
configuration: latency=0
id:multimedia
description: Audio device
product: Cannon Lake PCH cAVS
vendor: Intel Corporation
physical id: 1f.3
bus info: pci@0000:00:1f.3
version: 10
width: 64 bits
clock: 33MHz
capabilities: pm msi bus_master cap_list
configuration: driver=snd_hda_intel latency=32
resources: irq:134 memory:b461c000-b461ffff memory:b4200000-b42fffff
id:serial:2
description: SMBus
product: Cannon Lake PCH SMBus Controller
vendor: Intel Corporation
physical id: 1f.4
bus info: pci@0000:00:1f.4
version: 10
width: 64 bits
clock: 33MHz
configuration: latency=0
resources: memory:b4629000-b46290ff ioport:5040(size=32)
id:serial:3
description: Serial bus controller
product: Cannon Lake PCH SPI Controller
vendor: Intel Corporation
physical id: 1f.5
bus info: pci@0000:00:1f.5
version: 10
width: 32 bits
clock: 33MHz
capabilities: bus_master
configuration: latency=0
resources: memory:fe010000-fe010fff
id:scsi
physical id: 1
logical name: scsi4
capabilities: emulated
id:disk
description: ATA Disk
product: ST2000LX001-1RG1
vendor: Seagate
physical id: 0.0.0
bus info: scsi@4:0.0.0
logical name: /dev/sda
version: SDM1
serial: ZDZ5L4ES
size: 1863GiB (2TB)
capabilities: gpt-1.00 partitioned partitioned:gpt
configuration: ansiversion=5 guid=c6537684-1d60-4658-9882-1eef43a604a2 logicalsectorsize=512 sectorsize=4096
id:volume:0
description: Windows FAT volume
vendor: mkfs.fat
physical id: 1
bus info: scsi@4:0.0.0,1
logical name: /dev/sda1
version: FAT32
serial: b5e0-93ea
size: 510MiB
capacity: 511MiB
capabilities: boot fat initialized
configuration: FATs=2 filesystem=fat name=EFI System Partition
id:volume:1
description: EXT4 volume
vendor: Linux
physical id: 2
bus info: scsi@4:0.0.0,2
logical name: /dev/sda2
version: 1.0
serial: ae23720b-5246-41f1-be90-f40a1284d1e2
size: 1862GiB
capabilities: journaled extended_attributes large_files huge_files dir_nlink 64bit extents ext4 ext2 initialized
configuration: created=2019-10-22 09:59:58 filesystem=ext4 lastmountpoint=/ modified=2023-05-04 17:25:36 mounted=2023-05-04 17:25:37 state=clean
id:battery
description: Zinc Air Battery
product: CRB Battery 0
vendor: -Virtual Battery 0-
physical id: 1
version: 08/08/2010
serial: Battery 0
slot: Fake
id:power
description: OEM Define 1
product: OEM Define 5
vendor: OEM Define 2
physical id: 2
version: OEM Define 6
serial: OEM Define 3
capacity: 75mWh
id:network
description: Ethernet interface
physical id: 3
logical name: docker0
serial: 02:42:8f:b7:db:d7
capabilities: ethernet physical
configuration: broadcast=yes driver=bridge driverversion=2.3 firmware=N/A ip=172.17.0.1 link=no multicast=yes
