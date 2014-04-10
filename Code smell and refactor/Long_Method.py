# This is another kind of code smell: long method
# If we have something that needs many lines of code, break it into
# various functions

class MakeDualBootWindowsMac(self):
	def prepare_install_media(some_arguments):
		usb1 = toolbox.get_mass_storage_usb(sizeGB=8)
		usb2 = toolbox.get_mass_storage_usb(sizeGB=4)

		windows_pc = desktop.getPC()
		macbook = desktop.getMac()

		# These are procedures to prepare install media for Windows and Mac
		# It should be broken into 2 functions

		win81_iso = windows_pc.tools.downloader("MDSN/technet/win81_iso.iso")

		windows_pc.tools.disk.format(usb2.partition(0), fat32)
		windows_pc.tools.archive.extract(win81_iso, usb2.partition(0).contentFolder("/"))
		windows_pc.tools.disk.writeMBR(usb2.MBR(), usb_hddplus)
		windows_pc.tools.disk.writePBR(usb2.partition(0).PBR, bootmgr)
		windows_pc.tools.boot.make_boot(usb2.partition(0), usb2.partition(0).contentFolder("/Windows/"))


		osx_1092_installer = macbook.apps.AppStore.download("com.apple.osx1092")

		bootloader = macbook.tools.downloader("/site/bootloader/")
		macbook.tools.disk.clean(usb2, MBR)
		macbook.tools.disk.create_partition(esp, 200, fat32)
		macbook.tools.disk.create_partition(data, 5000, hfs_plus_journaled)
		bootloader.install(usb2.partition(0))
		osx_1092_installer.createinstallmedia(usb2.partition(1))

	def install_systems():
		# ..................................