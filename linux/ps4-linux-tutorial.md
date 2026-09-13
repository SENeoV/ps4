# PS4 Linux Tutorial (copia)

> Copia en Markdown de **[dionkill.github.io/ps4-linux-tutorial](https://dionkill.github.io/ps4-linux-tutorial/)** ("A simple guide on how to install Linux on PS4 systems", por DionKill), hecha el 2026-09-13 a partir de la fuente en [GitHub](https://github.com/DionKill/ps4-linux-tutorial) (licencia MIT, último cambio 2026-09-10). Texto original en inglés, sin modificar salvo el formato: los desplegables del sitio son `<details>`, los avisos van como citas y las imágenes apuntan al sitio original. Para la versión al día, ir al enlace.
>
> Contexto para este repo: la PS4 Pro está en 12.52 con GoldHEN y es **Baikal B1**, así que de esta guía aplican el método externo, el kernel 5.4.247 y una distro con Mesa ≤ 25.1. Lo específico de esta consola y el procedimiento elegido, en [`README.md`](README.md); qué aporta Linux aquí (Dolphin, RPCS3), en [`../emu/emuladores-ps4.md`](../emu/emuladores-ps4.md#solo-con-linux--gamecube-wii-ps3-y-ps-vita).

## Índice

- [Key Information](#information)
- [Revisions and Southbridges](#revisions)
- [Setup](#setup)
- [Files](#files)
- [Installation Methods](#installation)
- [Internal Installation](#internal-installation)
- [Scripted External Installation](#external-installation-scripted)
- [Manual External Installation](#external-installation-manual)
- [Ending](#ending)
- [Post install setup](#postinstall)
- [Common issues](#issues)
- [Game compatibility](#game-testing)
- [Distro DIY](#distrodiy)
- [Legacy and preservation](#legacy)

---

## Home

## Before we start
Here are some questions you probably want to know the answer to if you are a novice on this stuff.

<details><summary>What is Linux?</summary>

Linux is a kernel, though nowadays many refer to it as the whole fleet of operating systems using it. In layman's terms, think of it as the core of the OS. Installing Linux refers to installing a Linux distribution to use on your PS4 so that you can turn it into something like a desktop computer.
</details>

<details><summary>Is it reversible? Will it delete all my games and saves?</summary>

All your data will stay intact. Whether you install it on the internal HDD or an external drive, you will keep your data as you first need to exploit your console at every boot.

The internal drive method actually creates a file as big as you want it to be which is going to be mounted whenever you launch Linux as it's own virtual hard disk, so it won't overwrite any data you have on your console.
For the external drive method your HDD isn't even touched at all.

TLDR: yes it is reversible, and no you won't lose any data.
</details>

<details><summary>What are the PS4's specifications?</summary>

- AMD APU
	- 8 cores, x86-64 CPU @1.6GHz (Phat and Slim) or @2.1GHz (Pro) based on the Jaguar architecture
		- In theory, it's two Athlon 5150s duct taped together
		- Performance similar to an i3-2120 in multicore, or a Pentium 4 in single core
	- AMD "Liverpool" (Phat/Slim) or "Gladius" (Pro) GPU
		- Performance is comparable to an AMD HD 7850 or a Nvdia GTX 750 Ti on the Phat/Slim
		- For the Pro, we don't really know. Roughly a GTX 1060
- 8GB of GDDR5 memory
  - Note the G, stands for Graphics. This isn't DDR5 as it wasn't invented in 2013. DDR3 was the only one available.
  - Additional 256MB DDR3 for "Background applications" on Phat/Slim, or 1GB DDR3 on Pro
</details>

<details><summary>What do these specs mean in practice?</summary>

Back in 2013 AMD was nearly about to collapse, because their processors were terrible. It was saved by the PS4's success.

This means that not only was the PS4 lacking a lot of CPU performance at launch, but it is also using GDDR5 memory, of which there's only 8GBs of. GDDR5 is not meant to do anything other than graphic workloads, so while it has a lot of bandwidth (it can move a lot of data at once) it has very high latency (getting to the location in memory takes a long time).
</details>

In practice, the PS4 is totally capable of handling not only modern web browsing, but light PC gaming as well (with limitations of course, especially on the GPU drivers side).

Another thing. We have two methods of installation:
1. Internal HDD of the PS4
2. External Drive via USB

But some consoles don't support internal drives. This will addressed further into the guide.

By the way, if you have any problems, you can make an issue on GitHub. PRs are welcome as well!
## Little bonus
[How it all started](https://www.youtube.com/watch?v=QMiubC6LdTA).

---

<a id="information"></a>

## Key Information

> [!CAUTION] NOTICE
> You will need extensive reading knowledge.
> 
> If you ever ask for help in the communities linked down below, they can't really help you if you don't read the guide.

In this *very professional* tutorial, we'll go over how to install Linux on your PS4.

This guide was originally made because the PS4Linux.com's guide was old, hard to understand, incomplete and with tons of ads. It was updated recently, but the guide section hasn't really changed.

Still, thanks to noob404 for their website, as this is a better-put-together version of their work. This guide wouldn't exist without it.

<details><summary>Is it reversible? Will it delete all my games and saves?</summary>

All your data will stay intact. Whether you install it on the internal HDD or an external drive, you will keep your data as you first need to exploit your console at every boot.

The internal drive method actually creates a file as big as you want it to be which is going to be mounted whenever you launch Linux as it's own virtual hard disk, so it won't overwrite any data you have on your console.
For the external drive method your Internal HDD isn't even touched at all.

TLDR: yes it is reversible, and no you won't lose any data.
</details>

<details><summary>What consoles are compatible? (Up to 13.02)</summary>

All consoles that can run a homebrew enabler (like GoldHEN or ps4hen) are able to run Linux.

*(fragmento `min-firm-ver` no existe en la fuente original)*

However, every console has a different southbridge, and Baikal in particular has many issues. You should be able to get a working installation either way.
</details>

## Video guide (optional)

> [!TIP]
> If you prefer a video guide, I recommend Modded Warfare's on YT.
> 
> As is the nature with videos, it may not be up to date with the content here.

<iframe width="560" height="315" src="https://www.youtube.com/embed/KW_lRyXQcb8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Important places
Here are some links you'll probably find useful. You can come back to them if needed.
1. Discord
	1. [Linux for PS4 Community](https://discord.gg/fZQScGvRQb)
		1. For general help regarding things not working, chatting, and a overall nice community :)
	2. [PS4 Linux Fluxer](https://fluxer.gg/b7fFDGsY)
		1. A Fluxer server, in case Discord were to become unavailable
2. Mental Health Institute of your choice (optional, if you feel overwhelmed)

## Warning before you proceed

> [!CAUTION] 
> Read the guide carefully to avoid any mistakes. It is recommended to read it fully at least once, as it may be a little bit overwhelming at first.
> 
> This guide is offered as is, with no warranty whatsoever. The writers are not responsible if you screw something up.

> [!TIP]
> If you do share this tutorial, remember to mention the source and that things are subject to change.

## To the Revisions and Southbridges section
In the next section, we'll figure out what are the differences between all consoles and southbridges, as well as additional terms for Linux and general computing.

---

<a id="revisions"></a>

## Revisions and Southbridges

We need to clear any confusion for people that are new to this stuff. The PS4 is a relatively quirky console and it can get pretty confusing with the myriad of models there are.

> [!TIP]
> Take notes and remember all you see in this page, as it will interest you during your installation.
## Revisions

The PS4 family of consoles has had 3 revsions in total:
### Phat/Fat
- CUH-1000, CUH-1100 and CUH-1200 series
<img src="https://dionkill.github.io/ps4-linux-tutorial/fat.png" width="50%">

### Slim
- CUH-2000, CUH-2100 and CUH-2200 series
<img src="https://dionkill.github.io/ps4-linux-tutorial/slim.png" width="50%">

### Pro
- CUH-7000, CUH-7100 and CUH-7200 series
<img src="https://dionkill.github.io/ps4-linux-tutorial/pro.png" width="50%">

## Southbridges
A southbridge is a part of a motherboard chipset that connects all the slower parts of a motherboard, like USB, BIOS, ISA, IDE and SATA/PATA, and more, for support for such devices.

The PS4 family is divided into 3 major Southbridges:
### Aeolia
The oldest and very supported for Linux, but is known to have some Wi-Fi or Bluetooth chips that may not work with some kernels.

It's only present on early Phat models.

### Belize
The second gen southbridge, and the one with the most support. Gets kernel updates faster and doesn't have any particular problems.

It can be found on late Phat models, but also on Slims and Pros.

### Baikal
The third and final southbridge, released very late into the console's lifespan, and the one with the least support. It doesn't have support for internal HDD installation, and is known to have issues, especially on PS4 Pros, but you may be able to get a working system.

This is because there are fewer people with Baikal PS4s, so there aren't many developers and testers.

> [!TIP]
> In a nutshell, the list from most to least supported is:
> 1. Belize
> 2. Aeolia
> 3. Baikal
## Other terms
<details><summary>Linux terms</summary>

To be fair, it is expected that you already know some of these, but if not, at least you'll learn something today.
- Root folder or `/` is the the the first folder of the entire OS. It contains all the folders of the system. 
	- `root` is also the user that has access to the entire system.
- Distros or distributions, are operating systems that include the Linux kernel as a common base.
- Mesa: not the biome in Minecraft, but the Mesa Graphics Library. It's essentially a part of the graphics drivers and are necessary for graphics to work properly

</details>
<details><summary>PC terms</summary>

You are also supposed to know what all of these mean, but if not, here's an extremely quick rundown:
- OS: operating system
- CPU: the processor or "brain" of the computer
- GPU: the graphics processor, which handles... graphics
- RAM: the memory of the system, resets when the system is powered off and it's the location on which apps are moved when open
- Storage: the space where you install the OS and apps
- HDD: Hard Disk Drive, it's a type of storage based on a spinning metal disc. Very slow for our purposes.
- SSD: Solid State Drive, it's a type of storage that uses electricity instead of mechanical parts. Much faster than an HDD.

</details>
<details><summary>Other other terms</summary>

For all the other terms that didn't fit anywhere else:
- PS4
	- pfft are you serious?

</details>
## To the setup
Now you've finally become the most powerful human in the world with all these achronyms! You should go to the next step, where you'll set up the console and PC to start the installation.

---

<a id="setup"></a>

## Setup

In order to install Linux on the PS4, a lot of things are needed. You may have to buy some gear to make this work.
## Requirements

In a nutshell, you'll need:
- A PS4 (duh)
	- Extra mouse and keyboard
	- A USB hub to connect all the peripherals is recommended
- A computer
- An internet connection
- (Optional) - one or more USB drives
	- If you want to install to an external drive, you can use a USB pendrive or HDD, but it's recommend to have a SATA SSD and a SATA to USB adapter (preferrably one that supports UAS).
- Ability to read and follow instructions
	- You'll know this if you've read the [Key Information](#information) page.
- Patience
	- Installing Linux on the PS4 (or just, in general...) *can* take a while.
## Storage devices to install to
Before we talk about anything, you must choose now a method of installation.
You will need a device to store Linux, obviously.
1. Internal HDD
	- Baikal still unsupported, veeery slow, needs free space
2. External HDD/SSD
    - External USB Hard Disk Drive or USB Solid State Drive. Use a USB 3.x capable disk and cable for the best performance
	- External SATA-USB or NVMe-USB adapter (if using a SATA/NVMe drive)
	- You can use a pendrive, nobody's stopping you, but it's gonna be painful

## PS4 system
Some configuration is necessary on the PS4's side before we load Linux.

*(fragmento `min-firm-ver` no existe en la fuente original)*

### Things to note down
Note down what you see in "Settings -> System Information":
- System software version
- Southbridge
- Your GoldHEN or ps4hen version

<img src="https://dionkill.github.io/ps4-linux-tutorial/screenshots/system-info.png" width="75%">

### HEN
> [!WARNING]
> You mustn't use GoldHEN v2.4b18.8 as it doesn't boot!
> Always update to the latest version of [GoldHEN](https://ko-fi.com/s/407bb9c94a)!

You need a system that is already jailbroken and has a homebrew enabler (such as GoldHEN or ps4hen) running.

In order to input text on your PS4, you can't use the PS4 built in keyboard, as that is not available on Linux. You must have a keyboard and mouse combo ready to use with your PS4.

#### Payload server settings
Remember to check the GoldHEN "Server" settings (or ps4hen's equivalent if you're using that) so that they are both enabled:

<img src="https://dionkill.github.io/ps4-linux-tutorial/screenshots/payload-server-conf.png" width="75%">

These are required to be able to move files and load Linux later into the guide.

### Settings
These need to be taken as a precaution, not as a necessity, as nowadays they aren't actually needed anymore.
However, as some issues may arise on certain consoles, you should still go and tweak these settings.
#### "Audio and Display" settings
##### Resolution

<img src="https://dionkill.github.io/ps4-linux-tutorial/screenshots/settings-sound-and-screen.png" width="75%">
<img src="https://dionkill.github.io/ps4-linux-tutorial/screenshots/resolution.png" width="75%">

- Set your resolution
	- 720p probably won't work, so on Phat/Slim set 1080p.
	- 4K is only available on PS4 on kernels 6.18 or higher.
	- Not always required? Sometimes Automatic breaks though.

##### RGB Color gamut

<img src="https://dionkill.github.io/ps4-linux-tutorial/screenshots/rgb-range.png" width="75%">

- Set your RGB color gamut
	- It may be automatically set to "Limited" even if your display supports "Full" or viceversa.
	- "Full" may not work on some displays (even new ones). If the image looks really dark, set it to "Limited".
 	- It is assumed that Limited refers to 6 bit colors and Full to 8 bit. Check what your monitor supports.
- Wide color gamut
	- Disable, or you won't have any video output at all!
 	- This refers to outputs higher than 8 bit colors. It isn't currently supported.

#### "System" settings

<img src="https://dionkill.github.io/ps4-linux-tutorial/screenshots/settings-system.png" width="75%">
<img src="https://dionkill.github.io/ps4-linux-tutorial/screenshots/hdcp-and-device-link.png" width="75%">

- Disable "HDCP" and "HDMI device link" is a lie, it works perfectly fine and in fact you should leave them enabled for ease of use with some exploits (notably the BD-JB)
- Check your internet connection
	- Some models have issues if they aren't already connected to internet.
	- Ethernet may not work on PS4 Pro Baikal

## PC
You'll need a way to connect to your PS4 to transfer files. A PC is recommended. You will also need an internet connection.

You'll be accessing your PS4's filesystem from FTP. You can also transfer files with a USB drive if you feel so inclined.

### FTP connections
In order to do that, open up your FTP file manager of choice.

#### Windows
- Windows File Explorer
	- This one likes to crash the desktop if it can't connect, be careful
- WinSCP (recommended, using the simple interface)
- Filezilla

#### Linux
- Built in File explorer, if yours allows it (KDE, Gnome and Cinnamon should)
- Filezilla

> [!warning]
> Dolphin has a weird tendency to break the FTP server.
> You'll need to restart the FTP server from GoldHen Server settings.

#### MacOS
- Filezilla

### Note regarding Filezilla
> [!warning]
> If you use Filezilla, use "binary mode" to transfer files, as the FTP in GoldHen has issues when transferring files!

### Necessary files
In the next step, you also will need to download the following:
- bzImage (the kernel)
- initramfs.cpio.gz (the rescueshell/terminal before the main distro)
- A distro of your choice, already preinstalled and modified to work on the PS4
	- You can also make your own. More on that later.

## To the files section
You can go now go to the files section, where we'll cover how to download the required data.

---

<a id="files"></a>

## Files

## Kernels
Let's start with the kernels: they are very important as they have the software that controls all of the PS4's hardware. This is, by definition, Linux.

This is the section for recommended kernels. There are both vanilla kernels and performance kernels. Ordered by newest to oldest, the top ones are the recommended ones.

[Credits for all of these kernels](#ending).

<details><summary>Read this if you're confused!</summary>

### Do kernel versions matter?
The community has moved on from 6.15 to 7.x kernels on Aeolia and Belize. Baikal has now been ported to 7.0.8 after years of being stuck on 5.4, thanks to rmux.

### What about more performance?
The newest kernels are already built with all the necessary patches to make the console work as good as it can, so there's no need to modify anything anymore.
LTO is a topic of debate, but both ThinLTO and FullLTO are good options.
</details>

<details><summary>(Warning regarding other kernels not on this list)</summary>

Some kernels are to be avoided, specifically the ones "made" by the KHEOPS team, which are stealing work from the PS4 Abuse Club team. You can find more info in the Linux for PS4 Community Discord server, in [this message](https://discord.com/channels/1493663490659975350/1499549352320958514/1530306022508597268), (this is a guide and not a place for drama).

On top of that, there is also a malware problem:
> triki1 is on the same team. He said in writing that they will not publish source code because it is malware. He said it "could set your PlayStation on fire". This is a serious problem. Do not ignore this.

</details>
### Kernel list
These are normal general-use kernels with additional patches to make them work properly on the PS4. Some 

| Kernel Download                                                                                           | Compatible Southbridges | Source Code                                         | Extra info                                                                                                                                              |
| --------------------------------------------------------------------------------------------------------- | ----------------------- | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [7.1.7](https://gitlab.com/rmuxnet/linux/-/releases)<br>*Recommended*                                     | Aeolia, Belize          | [GitLab](https://gitlab.com/rmuxnet/linux)          | All 4 profiles, FullLTO.<br>**General**: desktop/gaming, default.<br>**Server**: headless.<br>**SlopMax**: General + KVM.<br>**Slopium**: Server + KVM. |
| [6.15.4](https://github.com/feeRnt/ps4-linux-12xx/releases/tag/v6.15.4__crashnt-4.7)                      | Aeolia, Belize          | [GitHub](https://github.com/feeRnt/ps4-linux-12xx/) | LTO and other improvements.<br>**ThinLTO** recommended.<br>Some consoles may need `no-builtin-fw`.                                                      |
| [5.15.15](https://github.com/feeRnt/ps4-linux-12xx/releases/tag/v5.15.15__obsidianx-4.0) <br> Belize Ver. | Belize                  | [GitHub](https://github.com/feeRnt/ps4-linux-12xx/) | Same as above. Might provide better performance than 6.15.4.                                                                                            |
| [5.4.247](https://github.com/feeRnt/ps4-linux-12xx/releases/tag/v5.4.247__neocine-1.1)                    | Baikal                  | [GitHub](https://github.com/feeRnt/ps4-linux-12xx/) | Specific for Baikal systems. Don't use on any other console!                                                                                            |

> [!NOTE]
> Some people repackage these kernels into closed-source "packs" and act like they did something, when all they did is apply patches from the internet. Don't fall for it. Real fixes are public, and folks desperate to take credit usually hide the source for a reason.

<details><summary>Server kernels</summary>

### Server kernels
If you are using the PS4 as a server, use these instead of the normal desktop-oriented builds when available.

> [!TIP]
> Pair server kernels with the `128MB` server payload unless you have a specific reason not to.

| Kernel Download                                                                             | Compatible Southbridges                                                                                                      | Source Code                                | Extra info                                                                                      |
| ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| [7.1.7](https://gitlab.com/rmuxnet/linux/-/releases/zaebiz%2F7.1.7-Stable)<br>*Recommended*             | Aeolia, Belize, Baikal                                                                                                      | [GitLab](https://gitlab.com/rmuxnet/linux)         | Use **Server** edition, or **Slopium** if you need VM support.                                      |

</details>

If you have issues, remember to check the [Issues page](#issues). If you want more help, check out [Discord servers](#information).

## Initramfs
This is the rescue shell that boots your Linux installer/installation. Think of it as GRUB, but more basic.

Download [this one](https://github.com/DionKill/ps4-linux-tutorial/blob/main/PS4%20Linux/initramfs.zip). [Source (not really)](https://bitbucket.org/piotrkarbowski/better-initramfs/src/master/).

<details><summary>More details</summary>

There's another in-dev initramfs (probably not working), if you want to check out the source it's [here](https://github.com/ps4gentoo/initramfs).

Also, you may want to read [this post](https://ps4linux.com/forums/d/93-tutorial-for-building-a-custom-initramfs-research-development) on the PS4 Linux forums, it explains what an initramfs is and does in actuality.
</details>
## Distros (that you ACTUALLY wanna use)
Honestly there's a neptillion distros... If you're indecisive, click on all the links and check them out. Either way they are listed from most to least recommended.

<details><summary>Read more here</summary>

Each distro has it's own pros and cons. But most of the difference on PS4 comes down to drivers; each distro requires it's own version of them and it can be a pain in the ass to install.

**Arch based distros are recommended**, but not because you need to be part of the elite. They are the only ones that currently have automatic updates (meaning with the rest of the system) without breaking anything.

You can of course use other distros, but you do run the risk of breaking your distro or having to reinstall everything when something needs updating, unless you know what you are doing.
</details>

> [!TIP]
> Arch based distros are recommended due to ease of update for drivers as the hardware is really peculiar.

> [!NOTE]
> We don't suggest using anything closed-source or bloated (looking at you, Debian, and "MultiBoot" initramfs). Stick to the distros below, they're proven to work without issues by at least 200 people in our own Discord server :)

| Distro Download                                                                                                    | Compatible Southbridge & Mesa     | Port credits                                    | Info                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------ | --------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [CachyOS Light (Mega)](https://mega.nz/file/kS0CwBLJ#I2GtfEZ0HigRyoSoHnBWGH85NqTnNCOUHIBvxlQmUZM)<br>*Recommended* | Aeolia, Belize, Baikal<br>(Mesa 26.0.4) | DionKill                                        | CachyOS, but without it running like crap. Automatic Mesa updates.<br><br><br>[Info on the forums](https://ps4linux.com/forums/d/422-cachyos-light-lxqt-a-light-and-fast-distro) |
| [Arch](https://github.com/ErkkolaMaitohappo/arch-ps4-aur-smth-fork/releases/latest)                                | Aeolia, Belize, Baikal<br>(Mesa 26.0.4) | [Erkkola](https://github.com/ErkkolaMaitohappo) | An Arch install with different desktops: KDE, XFCE or even TempleOS!                                                                                                             |
| [Artix](https://github.com/ErkkolaMaitohappo/ps4-arch-based-distros/releases)                                      | Aeolia, Belize, Baikal<br>(Mesa 26.0.4) | [Erkkola](https://github.com/ErkkolaMaitohappo) | A distro not for noobies.                                                                                                                                                        |
| [CachyOS "Strawberry" Server Edition](https://github.com/sony-jaguar-devs/distros/releases)                        | Aeolia, Belize, Baikal                  | [rmux](https://github.com/rmuxnet/)             | *For server use only*! It doesn't run any DE!                                                                                                                                    |
| [JaguarLinux](https://ps4linux.com/forums/d/265-jaguarlinux-a-ps4-linux-only-distro-beta-release/3)                | Aeolia, Belize, Baikal<br>(Mesa 26-devel) | [TigerClips1](https://github.com/TigerClips1/)  | A distro made from scratch for the PS4! Void-based & in development. Worth a mention.                                                                                            |
<details><summary>More distros</summary>

Here are the distros that we can't recommend anymore, as they have been superseeded, or haven't had any major updates in a while.

It may be useful to you if you want something other than Arch, or if you have a Baikal southbridge.

If you want to take the risk, go to the [legacy page](#legacy).

>[!NOTE]
>Want to add more distros? Make an issue and your wish shall be granted.
>
>Want to make your own? [Check this out!](#distrodiy)

</details>
## To the installation we go
You should go to the next step, where you'll finally complete your installation!

---

<a id="installation"></a>

## Installation Methods

Installing Linux on the PS4 is surprisingly easy, and it helps you free your mind from the hardships of everyday life.

Just kidding, it's fucking terrible.

<details><summary>Internal vs External: The Finale - GOTY Limited Edition (rant)</summary>

As I've mentioned beforehand, you can't install Linux on the internal PS4's HDD on Baikal systems. I know, you're crying your heart out because you wanted to use it, but trust me it's atrocious.
To give you an explanation, it took me 30 MINUTES to update my CachyOS installation (1500MBs) and the system was so unresponsive that I could watch entire anime episodes in between clicks.

Using an external SATA-USB adapter with a Samsung 870 EVO 500GB, the time it took shrinked to less than 5 minutes, same when using it as the internal drive.

Therefore, let's clear some misinformation here:
- The PS4's internal HDD is a repurposed laptop 5400RPM drive. Please, for the love of GOD, do NOT use this. Even the PS4's own menus lag because of how slow it is.
- The PS4 internal drive uses UFS encryption so it slows down significantly, even if you swap in an SSD.
- You CAN clone your PS4 HDD into an SSD, if internal installation is a must for you.
- The PS4 doesn't support TRIM, so a possible internal SSD swap would be a lot slower in writing data (a quality cached SSD with a garbage collector would be a bit better though).
- PS4 Phat and Slim are limited to SATA-II, which is 3Gbps in speed (roughly 375MB/s), which people online say it's not enough (it's enough for a PS4). On the other hand, the PS4 Pro runs at SATA-III, which is 6Gbps (up to 750MB/s), so that can saturate every SATA SSD on the market.
	- External SSD, on my 500GB Samsung 870 EVO, is 350MB/s-ish. So you'd get the same performance as an internal drive (theoretically) even on a Slim/Phat console.
	- Internal SSD performance is similar to external, because both of them use the USB bus (why Sony??), however encryption will slow down I/O access.

An internal SSD is going to be much faster and probably more reliable than a dangling USB drive (which constantly disconnects, too), so it's recommended, just remember to get a good quality one as the PS4 doesn't support TRIM.
</details>

> [!TIP]
> TL;DR:
> 
> Internal HDD is only for Aeolia/Belize, not recommended (unless you have switched to an SSD).
> Every console supports external, which is recommend with an SSD via an adapter.

## Preparing the installation
1. Boot your PS4 and launch GoldHen.
2. Take the initramfs.zip file, open it, and choose your installation method (mind the Southbridge)
	- Put it somewhere like on your desktop as we'll need it
3. Pick your kernel (bzImage), extract the file from the zip and place it somewhere you can remember
4. Choose your distro and and rename it `psxitarch.tar.xz/gz` depending on the original file type

## Choosing a method of installation 
> [!WARNING]
> Choose ONLY ONE method of installation.
> 
> Installing on both the internal and external drives can cause problems! If you did, remove one of the previous installations!

Here you will choose a method of installation.

Again, choose only one method and stick with it, and remember that Baikal can't currently install to internal reliably.

> **Internal Installation**
> This method installs Linux on the internal PS4 HDD, by creating a partition as big as you want. It will not overwrite anything on the drive.
>
> [Internal Installation section.](#internal-installation)

> **External Installation**
> For external installation, there are two methods: the first one involving a script on the PS4 (faster to configure), and another one with manual partitioning (higher success rate).
>
> The manual partitioning method is indeed preferred, but it involves the use of a Linux computer, virtual machine, or specific software on Windows.
> You may choose the scripted method, however if any issues arise, try the other one.
>
> [Scripted External Installation.](#external-installation-scripted)
>
> [Manual External Installation.](#external-installation-manual)

---

<a id="internal-installation"></a>

## Internal Installation

Here you'll setup the internal HDD for installation of a Linux distro.

> [!CAUTION]
> Baikal internal installation is still unstable. Proceed with caution and make backups beforehand.

> [!WARNING]
> This shit is slow on an HDD. Be careful and prepare your balls for imminent explosion.
> 
> However, if you have swapped your internal HDD for an SSD, this doesn't apply.

## Internal HDD setup
Check your PS4 storage, as you'll need to choose the size of the installation. Leave some free space in your console, and remember that the PS4 doesn't report the space taken internally by Linux!

FTP to your PS4. Go to the `/data/` folder, and create the folder `/linux/boot/` and place your bzImage (and bootargs.txt if you have it) and initramfs in there.

> [!NOTE]
> Files sent via FTP can transfer incorrectly, especially if overwritten. In that case, try to move them using a USB drive.

<img src="https://dionkill.github.io/ps4-linux-tutorial/screenshots/internal-drive-conf.png" width="50%">

Then, go to `/user/system/`, create a folder called `boot`, and paste your distro in there. Remember that it needs to be called `psxitarch.tar.gz` or `xz`!

When installed, you can remove your Linux installation by removing the above files, and the "linux.img" found in `/user/home/` folder. Just in case you realize I was correct.

## Launching Linux Rescue Shell
After that, either launch your payload with a payload website to load them, or use "Payload Guest" app if the website doesn't work for you.

> [!TIP]
> Remember that the amount of VRAM you allocate is taken from your system memory!
> For a 2GB of VRAM payload, you'd have 8-2 = 6GB of remaining system RAM!
> You aren't creating memory out of thin air!
> 
> <img src="https://dionkill.github.io/ps4-linux-tutorial/screenshots/trash-statement.png" width="33%">

<details><summary>For servers</summary>

Server payloads are available in `32MB`, `64MB`, and `128MB` VRAM variants.
Use `128MB` by default for server or general headless use, as `32MB` and `64MB` can cause display issues on some setups.
</details>
### Payload website hosts

<details><summary>Firmware (5.05 - 13.02)</summary>

> [!WARNING]
> You MUST use a 1GB VRAM payload for installation and first boot. Afterwards, 2GB is recommended.
> 
> Do not use GoldHEN version v2.4b18.8, [update it](https://ko-fi.com/s/407bb9c94a)!

Follow these steps:
- Go to [http://webkitty.arabpixel.net](http://webkitty.arabpixel.net) on your PS4's browser
- Select Linux tab at the top center
	- Wait for the cache to finish installing!
- Load your desired payload
	- Again, 1GB is necessary for first time installation!
	- If you use the PS4 as a server after installation, switch to one of the server payloads for more system RAM.

<img src="https://dionkill.github.io/ps4-linux-tutorial/screenshots/psfree-payloads.jpg" width="75%">
</details>

<details><summary>Local payloads (if website doesn't work for you)</summary>

If you so desire, or you can't launch it from the web browser for some reason, it's possible to load these payloads locally.

In order to do that, you need to download them [here](https://github.com/ps4-linux/ps4-linux-loader/releases/latest).

#### Local payloads setup
- Install "Payload Guest" or similar app on your PS4 to load the payloads locally
- Extract from the ELF folders, and rename the file to have a `.bin` extension instead of `.elf`, because Payload Loader can't load ELFs
	- Using the `.elf` seems to lead to a higher success rate when launching
	- Enable "see file extensions" on Windows Explorer or what you're using
- Put the files in the `/data/payloads/` directory
- Remember to check here sometimes to see if there's any updates

</details>

## Installation commands
Now that the storage is covered, here comes the moment of truth. You'll be sent to the Rescue Shell, which will look like this:

<img src="https://dionkill.github.io/ps4-linux-tutorial/screenshots/rescue-shell.png" width="80%">

- If you have a disc in your console, remove it by running `eject /dev/sr0` or it'll corrupt the installation
- Type `install-linux-hdd.sh` or `linux-install-hdd.sh`
- Type how much storage you want to use for the installation
	- Check how much free space you have, don't fill up your drive as the PS4 will only report the used amount of space inside the partition, and not the total partition size!
	- If it fails, check your initramfs, or go to the [Installation Issues](#issues)

Hydrate yourself while you wait. It'll take a while.

It should already boot into the desktop. If it doesn't, run:
```bash
resume-boot
```

> [!WARNING]
> Don't run resume-boot more than twice, or it'll crash the system! Do `CTRL+ALT+DELETE` to reboot instead!

## Finale
Go now, conquer the finale. Also, read the post-credit stuff.

---

<a id="external-installation-scripted"></a>

## Scripted External Installation

> [!WARNING]
> Remember we'll format the external drive!
> Back up any existing data you care about.

> [!TIP]
> If you have issues or just want to do manual partitioning (which often works better) try the [alternative installation here](#external-installation-manual).
## Installation scripts
Put the kernel (bzImage, and the bootargs if you need it), initramfs (initramfs.cpio.gz), and your distro `psxitarch.tar.xz/gz` on the root of a FAT32 formatted drive, like so:

<img src="https://dionkill.github.io/ps4-linux-tutorial/screenshots/external-drive-conf.png" width="75%">

### Manual format for big drives
If the drive is larger than 32GB, Windows will dastardly act like it can't format it in FAT32, but only in NTFS or ExFAT, which is just wrong, as FAT32 supports up to 2TB drives.
To fix it, go ahead and download the mythical [Rufus](https://rufus.ie) program.

- Select "List USB Hard Drives"
- Select "Non bootable" as a type of format
- Select "MBR" as partition scheme
- Select "FAT32" as filesystem

Click start and wait.
Once done, place the files on the drive.
Plug your drive on the PS4 and continue.

<img src="https://dionkill.github.io/ps4-linux-tutorial/screenshots/rufus-format.png" width="50%">

## Launching Linux Rescue Shell
After that, either launch your payload with a payload website to load them, or use "Payload Guest" app if the website doesn't work for you.

> [!TIP]
> Remember that the amount of VRAM you allocate is taken from your system memory!
> For a 2GB of VRAM payload, you'd have 8-2 = 6GB of remaining system RAM!
> You aren't creating memory out of thin air!
> 
> <img src="https://dionkill.github.io/ps4-linux-tutorial/screenshots/trash-statement.png" width="33%">

<details><summary>For servers</summary>

Server payloads are available in `32MB`, `64MB`, and `128MB` VRAM variants.
Use `128MB` by default for server or general headless use, as `32MB` and `64MB` can cause display issues on some setups.
</details>
### Payload website hosts

<details><summary>Firmware (5.05 - 13.02)</summary>

> [!WARNING]
> You MUST use a 1GB VRAM payload for installation and first boot. Afterwards, 2GB is recommended.
> 
> Do not use GoldHEN version v2.4b18.8, [update it](https://ko-fi.com/s/407bb9c94a)!

Follow these steps:
- Go to [http://webkitty.arabpixel.net](http://webkitty.arabpixel.net) on your PS4's browser
- Select Linux tab at the top center
	- Wait for the cache to finish installing!
- Load your desired payload
	- Again, 1GB is necessary for first time installation!
	- If you use the PS4 as a server after installation, switch to one of the server payloads for more system RAM.

<img src="https://dionkill.github.io/ps4-linux-tutorial/screenshots/psfree-payloads.jpg" width="75%">
</details>

<details><summary>Local payloads (if website doesn't work for you)</summary>

If you so desire, or you can't launch it from the web browser for some reason, it's possible to load these payloads locally.

In order to do that, you need to download them [here](https://github.com/ps4-linux/ps4-linux-loader/releases/latest).

#### Local payloads setup
- Install "Payload Guest" or similar app on your PS4 to load the payloads locally
- Extract from the ELF folders, and rename the file to have a `.bin` extension instead of `.elf`, because Payload Loader can't load ELFs
	- Using the `.elf` seems to lead to a higher success rate when launching
	- Enable "see file extensions" on Windows Explorer or what you're using
- Put the files in the `/data/payloads/` directory
- Remember to check here sometimes to see if there's any updates

</details>

## Installation commands
Now that the storage is covered, here comes the moment of truth. You'll be sent to the Rescue Shell, which will look like this:

<img src="https://dionkill.github.io/ps4-linux-tutorial/screenshots/rescue-shell.png" width="80%">

- If you have a disc in your console, remove it by running `eject /dev/sr0` or it'll corrupt the installation
- Type `install-psxitarch.sh`
	- If it fails, go to the [Installation Issues](#issues), or use the [alternative method](#external-installation-manual).

Hydrate yourself while you wait. It'll take a while.

After that is done, it should boot into the desktop. If it doesn't, run
```bash
resume-boot
```

> [!WARNING]
> Don't run resume-boot more than twice, or it'll crash the system! Do `CTRL+ALT+DELETE` to reboot instead!

## Finale
Go now, conquer the finale. Also, read the post-credit stuff.

---

<a id="external-installation-manual"></a>

## Manual External Installation

> [!WARNING]
> Remember we'll format the external drive!
> Back up any existing data you care about.

This method involves manual partitioning. It's slower to do, but works flawlessly, therefore it's recommended if you have issues.

Get a Linux PC or VM (even a Live ISO works), or any program that can format drives in Linux's formats.

Then, plug in your drive, and use "GParted", "KDE Partition Manager", or "Aoemi Partition Assistant" on Windows to format your external drive like so:
- 50MB of FAT32 at the start of the drive <u>with an empty label</u>
- And a partition of the remaining space formatted as EXT4 <u>labeled "psxitarch"</u>
	- BTRFS works too, but EXT4 is faster and recommended

Now move your bzImage (and bootargs if you need it) and initramfs to the FAT32 partition.

Then, you will need to untar your distro of choice at the root of the bigger EXT4 partition, using this command:
```bash
sudo tar -xvJpf ps4linux.tar.xz -C /run/media/YOURNAME/psxitarch --numeric-owner
```

> [!NOTE]
> Replace `YOURNAME` and `ps4linux.tar.xz` accordingly.
> Also, you need to check that the drive is actually called psxitarch, it'll be different if you didn't set it.

## Launching Linux Rescue Shell
After that, either launch your payload with a payload website to load them, or use "Payload Guest" app if the website doesn't work for you.

> [!TIP]
> Remember that the amount of VRAM you allocate is taken from your system memory!
> For a 2GB of VRAM payload, you'd have 8-2 = 6GB of remaining system RAM!
> You aren't creating memory out of thin air!
> 
> <img src="https://dionkill.github.io/ps4-linux-tutorial/screenshots/trash-statement.png" width="33%">

<details><summary>For servers</summary>

Server payloads are available in `32MB`, `64MB`, and `128MB` VRAM variants.
Use `128MB` by default for server or general headless use, as `32MB` and `64MB` can cause display issues on some setups.
</details>
### Payload website hosts

<details><summary>Firmware (5.05 - 13.02)</summary>

> [!WARNING]
> You MUST use a 1GB VRAM payload for installation and first boot. Afterwards, 2GB is recommended.
> 
> Do not use GoldHEN version v2.4b18.8, [update it](https://ko-fi.com/s/407bb9c94a)!

Follow these steps:
- Go to [http://webkitty.arabpixel.net](http://webkitty.arabpixel.net) on your PS4's browser
- Select Linux tab at the top center
	- Wait for the cache to finish installing!
- Load your desired payload
	- Again, 1GB is necessary for first time installation!
	- If you use the PS4 as a server after installation, switch to one of the server payloads for more system RAM.

<img src="https://dionkill.github.io/ps4-linux-tutorial/screenshots/psfree-payloads.jpg" width="75%">
</details>

<details><summary>Local payloads (if website doesn't work for you)</summary>

If you so desire, or you can't launch it from the web browser for some reason, it's possible to load these payloads locally.

In order to do that, you need to download them [here](https://github.com/ps4-linux/ps4-linux-loader/releases/latest).

#### Local payloads setup
- Install "Payload Guest" or similar app on your PS4 to load the payloads locally
- Extract from the ELF folders, and rename the file to have a `.bin` extension instead of `.elf`, because Payload Loader can't load ELFs
	- Using the `.elf` seems to lead to a higher success rate when launching
	- Enable "see file extensions" on Windows Explorer or what you're using
- Put the files in the `/data/payloads/` directory
- Remember to check here sometimes to see if there's any updates

</details>

## Booting up
Now that the storage is covered, here comes the moment of truth. It should already boot into the desktop. If it doesn't, and instead shows a Rescue Shell command prompt, type this until the distro starts:
```bash
resume-boot
```

<details><summary>If it doesn't work check this!</summary>

If for some reason it doesn't work for you, run the following commands (thanks @gryoza on Discord and @bene4k on Reddit for this):
```bash
mount /dev/sdb2 /newroot
exec chroot
```
You may need to do this at every reboot.
</details>

> [!WARNING]
> Don't run resume-boot more than twice, or it'll crash the system! Do `CTRL+ALT+DELETE` to reboot instead!

## Finale
Go now, conquer the finale. Also, read the post-credit stuff.

---

<a id="ending"></a>

## Ending

And you're done! If this guide was helpful, you can star it on GitHub and share it!

Now go forth, spread misinformation online.

<img src="https://dionkill.github.io/ps4-linux-tutorial/misinformation.jpg" width="50%">

> [!TIP]
> I highly recommend continuing to the ["Post Installation" setup](#postinstall), to change language and download more RAM!

> [!NOTE]
> For any problems, [check the issues page](#issues)!

## Credits
### Kernel developers
These are the original kernel developers, who did the hard work to port the kernels on which all of the modern kernels are based on. None of this would've been possible without them.
- 4.4  kernel
	- marcan, fail0verflow team
- 4.14 kernel
	- rancido, and psxitateam, eeply, valery for Baikal (based on fail0verflow)
- 4.19 and 5.3 kernel
	- mircoho, (based on fail0verflow, psxitateam, eeply, valeryy)
- 5.15 kernel
	- codedwrench (based on fail0verflow, psxitateam, eeply, valeryy, mircoho)
- 6.15 kernel
	- crashniels with 2 patches from mircoho (fastboot and ethernet kp fixes) (based on fail0verflow - psxitateam  - eeply - valeryy - mircoho - codedwrench)
- 6.18 and 7.x kernel
	- patches from rmux, help from everyone in the ps4 abuse club

If you want, you can check out their repos:
- [marcan (fail0verflow) ](https://github.com/fail0verflow/ps4-linux)
	- Without them nothing would've ever been possible.
- [rancido (psxitateam)](https://github.com/Ps3itaTeam/ps4-linux/)
	- Made the AMDGPU driver work.
- [eeply](https://github.com/eeply/ps4-linux)
	- Brought PS4 Pro to work for video output, in fact now all ps4 with new Panasonic HDMI chip work.
- valeryy (no GitHub, gave the code to rancido)
	- Brought the Baikal Southbridge support.
- [tihmstar](https://github.com/tihmstar/ps4-linux)
	- Brought the Internal SATA driver for PS4 Belize.
- [mircoho](https://github.com/ps4boot/ps4-linux) ([ps4gentoo](https://github.com/ps4gentoo/ps4-linux-5.3.7) and [ps4boot](https://github.com/ps4boot/))
	- Worked on the kernel (especially Gentoo), ported payloads to newer firmwares.
- [codedwrench](https://github.com/codedwrench/ps4-linux)
	- Made kernel patches.
- [crashniels](https://github.com/crashniels/linux)
	- Ported newer kernel versions.
- [feeRnt](https://github.com/feeRnt/ps4-linux-12xx) (Package)
	- Hosts and maintains the PS4 Linux kernel sources on GitHub.
- [rmux](https://github.com/rmuxnet)
	- Kernel 6.18.x and 7.x
- leg
	- Helped with kernel updates, Mesa driver testing, and much more
- bzz
	- Working on updated and fixed Mesa drivers

### Additional credits
- [uar](https://uar.no/ps4/)
	- For their tutorial and fixes for baikal consoles and more.
- [centi07](https://github.com/centi07/)
	- For their help with up-to-date mesa package repos on Arch and more.
- [FlyingPhantom](https://github.com/FlyingPhantom) / z_fentom
	- For their forking this project for new additions. You can find it [here](https://flyingphantom.github.io/ps4-linux-tutorial/).

Thank you all so much for making this possible.

### A quick note
This scene only survives if we keep things **open and clean**. Everything you see here is free, open source, and battle-tested by the community. When you contribute to docs, kernels, distros, tools, keep it that way: public source code, no closed blobs, no bloated gatekeeping. If it's not open, the scene ends up shit, like it always did in the past.

If there is something this guide is missing or got wrong, [open an issue](https://github.com/DionKill/ps4-linux-tutorial/issues) and help make it better!

---

<a id="postinstall"></a>

## Post install setup

Once you've installed Linux and are on the desktop, before rushing to do things, you may want to do a couple of additional steps.

To change some config files (don't worry, it won't hurt), I'll recommend `nano` because it just works. To save a file, use `CTRL+S` and to exit `CTRL+X`.

## Update your system (caution)
Updating your system can be a bit of a pain in the ass, as some of the packages can't be updated because they contain modifications to make them work on the PS4.

> [!CAUTION]
> Arch-based distros have repositories for drivers, other distros might not.

<details><summary>Arch based distros (with driver updates)</summary>

To update the drivers, you need to open the pacman config:
```bash
sudo nano /etc/pacman.conf
```

If you installed an older distro, pacman might refuse to run, citing the following error: `restricting filesystem access failed because Landlock is not supported by the kernel`. If you run into this problem, search for the line containing `DisableSandbox`, and uncomment it by deleting the `#` character from the beginning.

If you installed a distro from the forums, you may have go to the `[Options]` section and delete the lines `IgnorePkg` and `IgnoreGroup`.

Then, under the `REPOSITORIES` section, add this ([GitHub](https://github.com/DionKill/ps4-video-archlinux)):
```bash
[ps4-video]
SigLevel = Optional 
Server = https://dionkill.github.io/ps4-video-archlinux/repo/
```

> [!NOTE]
> This repo will only work as long as the developer is updating it and keeping it online. It may be changed in the future.

Then, `CTRL+S` to save and `CTRL+X` to exit.

Finally, install the driver packages:
```bash
sudo pacman -Syu lib32-mesa-ps4 mesa-ps4 lib32-libdrm-ps4 libdrm-ps4 xf86-video-amdgpu-ps4
```

You should now have up-to-date drivers. If you want to, you can also go to the [DIY section](#distrodiy) and make them from the AUR or from scratch!
</details>

<details><summary>Debian/Ubuntu based distros (WITH Mesa updates, WIP)</summary>

Use uar's script updater:
```bash
wget [https://uar.no/ps4/baikal/mesa-25.sh](https://uar.no/ps4/baikal/mesa-25.sh "https://uar.no/ps4/baikal/mesa-25.sh") && sudo sh mesa-25.sh
```
</details>

<details><summary>Debian/Ubuntu based distros (disabled Mesa updates)</summary>

To make sure that the PS4 packages don't get updated run the command below:
```bash
sudo apt-mark hold lib32-libdrm-git lib32-mesa-git libdrm-git mesa-git lib32-libdrm lib32-mesa libdrm mesa lib32-llvm-libs llvm-libs
```

Then, you should be free to update your system with:
```bash
sudo apt update
sudo apt upgrade
```
</details>

<details><summary>Fedora based distros (untested)</summary>

To make sure that the PS4 packages don't get updated, you need to modify the dnf config:
```bash
sudo nano /etc/dnf/dnf.conf
```

Then, at the line next to the `[main]` section:
```bash
exclude=lib32-libdrm-git lib32-mesa-git libdrm-git mesa-git lib32-libdrm lib32-mesa libdrm mesa lib32-llvm-libs llvm-libs
```

Then, you should be free to update your system with:
```bash
sudo dnf update
```
</details>

Otherwise, you can always update everything but not the driver packages.
## Fix language
Some pre-packaged distros you can download are in foreign languages. Unfortunately changing it from your DE (KDE, Gnome...) doesn't apply system wide. So here's a cheap rundown of all of the commands:

<details><summary>Debian/Ubuntu based distros (thanks triky1)</summary>

```bash
sudo dpkg-reconfigure locales
```
</details>

<details><summary>Fedora based distros (to-do)</summary>

No idea, sorry
</details>

<details><summary>Arch based distros</summary>

You first need to edit your `locale.gen`, to generate your locale settings.

Comment out any language you don't want and uncomment yours:
```bash
sudo nano /etc/locale.gen
```

Now, you can generate your locale with:
```bash
sudo locale-gen
```

And last but not least, to change it system wide, add your language in this file:
```bash
sudo nano /etc/locale.conf
```

If needed, change your language in yout DE (KDE, Gnome...)
</details>

Reboot to apply these changes.

## Change username and password
Honestly? Create a new user. It's faster. Or just keep it.

You can however change the password, by doing:
```bash
sudo passwd
```
And setting a new password.

## Download more RAM?!
No, seriously, we can do such a thing. To do that, we must use Swap and ZRAM.

<details><summary>Enabling Swap</summary>

> [!CAUTION]
> It's ABSOLUTELY NOT recommended to use the internal HDD as swap, you'd just add fuel to the dumpsterfire of slowness that it already is. Disable it and move on.

Swap is storage that you are taking from your drive and allocating as "extra RAM": it works by moving unused software over there if extra main memory needs to be reserved for another program or game. This means we can improve the memory situation a little bit.

We will be using a swap file instead of a swap partition, as it's easier to change in size.
First of all, we need to remove any existing swap:
```bash
sudo swapoff -v /swapfile  
sudo rm /swapfile
```

Then, we need to enable new swap (8GB for this tutorial, you may change it)
```bash
sudo fallocate -l 8G /swapfile 8GB # Allocates 8GBs
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

Finally, go to the `fstab` file, and check if  the line `/swapfile none swap sw 0 0` exists.
If it doesn't, add it by going here and pasting it at the end of the file:
```bash
sudo nano /etc/fstab
```
</details>

<details><summary>Enabling ZRAM</summary>

ZRAM on the other hand, is a part of your memory that you are compressing and allocating as swap. A kernel that supports it is necessary.

This means that we trade some CPU cycles for compressing and decompressing a part of your system memory. If it is enabled by default on Android you can guess how little performance impact there is.

To enable ZRAM, we need to install the `zram-generator` package.
On Arch, we installing using:
```bash
sudo pacman -Syu zram-generator
```

We then create the config file:
```bash
sudo nano /usr/lib/systemd/zram-generator.conf
```

And we paste this inside of it:
```bash
[zram0]
zram-size=ram
compression-algorithm=zstd
swap-priority=60
```
`zram-size` is how much RAM we are allocating for the ZRAM device. Possible values are, for example, `50%`, `2G` (i.e. 2 GB), `ram` or `max` for maximum allocation (all RAM is ZRAM).
Don't change the other values unless you really know what you're doing.

It is also recommended to disable ZSWAP. Some distro already do this, but just in case go to your grub config:
```bash
sudo nano /etc/default/grub
```

And in the `LINUX_CMDLINE_DEFAULT` check that `zswap-enabled=0` is present. If not, add it.

</details>

<details><summary>Disabling ZRAM (if you need to)</summary>

To disable ZRAM, in case of swapping out kernels often for instance, you can simply remove the config file:
```bash
sudo rm /etc/systemd/zram-generator.conf
```

However, if you wish to completely remove it, do the following:
```bash
sudo systemctl disable zram-generator.service # This may not be needed
sudo pacman -Rns zram-generator
```

Also, remove the swap partitions:
```bash
sudo swapoff /dev/zram0
sudo rm /dev/zram0
```

Then reboot the system. It should be gone.

Thanks again to Qba for this [showcase](https://youtu.be/f_kXks8z9dc).
</details>

Oh, and don't worry if you see that your installation is using a lot of memory. It's normal and is meant to happen in order to improve performance. Check this [link](https://linuxatemyram.com) to learn more.

## Get more CPU performance
You may have realized that the PS4's CPU is pretty lacking and is most likely it's biggest disadvantage. But apart from a really optimized kernel (which we already have), what else can you do?

In computing you are always going to gain something and loose something else. Either your time, money, or in this case...

<details><summary>Disengage safety protocols, and run program</summary>

Yes, you can disable some security patches for attacks like Meltdown and Spectre, to gain some CPU performance. It does work and should have a noticeable improvement.

Obviously this is usually not recommended, but if all you want to do is game from your Steam library and occasionally browse the web (which is most of us), you are probably going to be fine. Also remember the console is already jailbroken... Not really going for security with that one.

To do that it's surprisingly simple. Open the `bootargs.txt` file, or create it in the same folder of the kernel if it doesn't exist already, then add this line, save and reboot:
```bash
mitigations=off
```

And there you go! You can change it back anytime of course.
</details>

In the past there were overclocked kernels, but alas they don't make them anymore. This is because overclocked kernels... didn't actually overclock the CPU.

Do not go and download an older kernel to try as they don't work anymore either!
## Install more applications
To play games, these are the recommended softwares:
- Steam
- Heroic Games Launcher (for Epic, GOG and Amazon)
- Lutris (for other PC games not in those launchers)
- Prism Launcher instead of those other shitty Minecraft launchers
	- Minecraft has graphical issues in versions newer than 1.21.5
- And a bunch of emulators!

To do that, if using anything other than Arch based distros, use your Store app from the Start menu and install as a Flatpak. It works well.

If you chose an Arch based distro however, use `pacman` or `yay` to install your packages. All packages you can even think of and more are available.

---

<a id="issues"></a>

## Common issues

During the installation, things can fail. Most of this stuff is undocumented too. There's dozens of posts online where people don't even get a response. We will hopefully fix these problems. If not, write on the forums or on the PS4 Linux Discord.

<details><summary>Root error `The "root" variable is empty, set to false or zero but shouldn't be`</summary>

It shows when booting up before installing, don't worry as it's normal because there is no installed system it can boot. You can proceed with the installation.
</details>

<details><summary>Newroot error - `mount -o ro /newroot failed`</summary>

If this happens, these are possible causes:

1. The initramfs you are using is not the correct one. If you are installing on external, use the one called external, if you are installing for internal check if it's the one for internal, and remember to check for the southbridge.
2. The installer can't find the `psxitarch.tar.xz` or `psxitarch.tar.gz` file. Check that the name and location are correct.
3. You are using different payloads than the one mentioned on the guide. Those will not work on modern distros and are known to have issues, therefore they are incompatible with this guide.

If none of these help you, go to the Linux for PS4 Community Discord server.
</details>

<details><summary>Mounting error - `No valid USB device found`</summary>

If the installer can't find the USB device, you have two options:
1. Try to disconnect everything, and connect the drive first. If that doesn't work, try to reboot but only with the drive connected, only when you get to the rescue shell connect a keyboard and a mouse.
2. If that other method didn't work, you can try to scan for USB storage devices with `fdisk -l` or `lsblk`. It should show all the storage devices.
	- If it shows with the commands, but the installer fails to find it, it's probably because the drive (or adapter if you are using one) doesn't support UAS, which is required in newer kernels. In that case, use the [Method 2](#installation) described.
	- Also, don't use USB hubs, the drive may not show up.

</details>
# Post-install issues
There are a lot of undocumented issues. Or, if they are documented, I couldn't even find them because no search engine indexed those pages or they are in a foreign language.

<details><summary>Black/gray screen or "no signal"</summary>

Since the 6.18 kernels, display issues should mostly be fixed, so if you can use a newer 7.x one instead, please do. Note that monitor hotplugging is not supported anymore.

If you get a black screen right after running the Linux payload, try another TV first. If that doesn't help, try this trick: boot back into the game OS (you'll have to, to run the Linux payload again anyways), run the payload and wait for it to go fully black, then turn your TV or monitor off and back on quickly. You should get a signal in the end.

> [!TIP]
> The rest of this stuff is mostly for safekeeping, but shouldn't be necessary anymore. Keep on readying if you need to!

Once upon a time, these issues were caused by using old kernels that required bootargs, but they are not necessary anymore.

Rarely, a gray image can happen even with fixes like bootargs. Make sure that you try to reboot at least twice.

### Other possible fixes
If booting a display manager or your desktop environment results in a black screen, and the distro is using X11, try Wayland.

To do that, you can try a Wayland based distro, there's plenty out there, or you can also try to change window manager by running:

`dbus-run-session -- startplasma-x11` or `dbus-run-session -- startplasma-wayland` on another TTY (change by doing `CTRL+ALT+F3`).

This is a lot of stuff to cover on the guide so you will need to look it up yourselves.

Thanks to @kalaposfos and @package on Discord for mentioning this fix.
</details>

<details><summary>Stuck on a white LED / instant crash</summary>

Sometimes it fails, try to reboot. It could take you even three or more attempts. Do not leave any apps "suspended" while you launch the exploit.

However, if it keeps happening, and the console gets stuck on a white LED instead of launching Linux, make sure you are following all steps correctly, and that you are using the correct payloads. Also, if you are using FTP, wait for a while or move the data using a USB drive instead.

...If you uploaded the kernel and initramfs using FileZilla, re-upload them with "Binary" mode enabled.
</details>

<details><summary>Wi-Fi and/or Bluetooth don't work (MediaTek modem)</summary>

Again this should be fixed, otherwise keep on reading.

If they don't work, it's because your console is using a Wi-Fi or Bluetooth chip that is made by MediaTek, and unfortunately you will need to find a kernel that includes the fixes for that specific chip. MediaTek does not make open source drivers, so that's the reason it doesn't work normally.

Try feeRnt's kernels, hopefully one of them will work for you.
</details>

<details><summary>Graphical glitches in games</summary>

This is caused by broken Mesa drivers. The community is working hard to fix this, but don't expect it all to work properly!

To solve Vulkan graphical issues you can try:
- Set `RADV_DEBUG=nocompute` in `/etc/environment` (use nano or similar)
- Try `amdgpu.abmlevel=0` with bootargs
- Use WineD3D (terrible performance)
</details>

<details><summary>DS4 must be paired again every time</summary>

This is because we would need to copy the Bluetooth information from the PS4's OS to Linux before booting. It's a known problem and will get fixed at some point.
</details>

<details><summary>Rebooting goes to OrbisOS (the PS4 main menu)</summary>

I mean it was kind of expected. How else are you gonna go back to the main menu?
</details>

# Other issues
<details><summary>The scene is a complete mess</summary>

Previously I used this as a rant to pour all of my stress into figuring how the fuck this shit is supposed to work, but the more I got into it and the more I understood.

In a nutshell, the scene is a mess and a lot of stuff may be shared privately or on Discord servers because:
- It's in testing phase and therefore not public yet (very rare nowadays)
- It's not open sourced because there's a lot of people who steal the developer's work
- It hasn't been merged into main projects because it would be too difficult to maintain thereafter, and would require it to be in a perfect condition (kernel and mesa)

Especially the second reason is why the community is like this. The KHEOPS team has made a mess by stealing, lying and even pointing the finger at other developers claiming the work is all done by them instead. But I'm not gonna go into the details here.

Fortunately, the new ps4 abuse club team has been hard at work fixing this whole endeavour and I thank them for all of their work.
</details>

<details><summary>How can I improve the situation?</summary>

Join the Discord servers, share this tutorial, star it on GitHub (pretty please), also don't forget to like, comment and subscribe!
</details>

---

<a id="game-testing"></a>

## Game compatibility

This page is dedicated to testing and reporting games running on PS4 Linux.

> [!CAUTION]
> Some of these games have worked perfectly fine in the past but could break in the future because of GPU drivers. If you see such an experience, make an issue on GitHub!

## Levels of stability and performance for PC games
There's multiple levels of stability:
- Broken
    - The game doesn't work at all
- Low
    - Major graphical glitches ruin the experience, or it just lags heavily
- Medium
    - Some issues here and there, you can still see frequent glitches
- High
    - Works for the most part, with the only issues being in specific places that don’t really affect the majority of the game
- Perfect
    - It works with no issues

> [!TIP]
> Freeing up as much RAM as possible to make some of these games launch is highly recommended. ZRAM won't help much if you have two browsers open!
> 
> Also, UNREAL ENGINE 5 games are broken. They will not be reported.

<details><summary>PC Games</summary>

| Game                                                         | Stability | Info                                                                        | Online Support Note                                       |
| ------------------------------------------------------------ | --------- | --------------------------------------------------------------------------- | --------------------------------------------------------- |
| Afterfall Insanity Extended Edition                          | Medium    | 30-60 FPS, minor stutters in heavy areas.                                   | Not applicable (single-player).                           |
| Aliens vs Predator 2010                                      | High      | 50-60 FPS, stable.                                                          | Not applicable (single-player).                           |
| Apex Legends                                                 | High      | 40-50 FPS online.                                                           | No longer works on Linux due to anticheat (EA Anticheat). |
| Assetto Corsa                                                | High      | 60 FPS+, stable racing.                                                     | Online play possible but not tested.                      |
| Battlefield 1                                                | Low       | 20-40 FPS, heavy lag in multiplayer.                                        | Online play works but performance-limited.                |
| Battlefield 3                                                | Medium    | 30-50 FPS, frequent glitches in maps.                                       | Online play works.                                        |
| Battlefield 4                                                | Medium    | 30-50 FPS, drops in heavy battles.                                          | Online play works.                                        |
| Battlefield 4 Premium                                        | Medium    | 30-50 FPS, drops in heavy battles.                                          | Online play works.                                        |
| BeamNG.drive                                                 | Medium    | Horrible performance, tweakable for playable framerate.                     | Not applicable (single-player).                           |
| Beyond Enemy Lines Remastered Edition                        | High      | 50-60 FPS, minor issues.                                                    | Not applicable (single-player).                           |
| Black Ops 2 Plutonium                                        | Medium    | 40-60 FPS, stuttering in multiplayer.                                       | Online play works via Plutonium.                          |
| Blacksite Area 51                                            | Low       | 20-40 FPS, major graphical glitches.                                        | Not applicable (single-player).                           |
| Blazblue Cross Tag Battle                                    | Perfect   | 60 FPS, flawless.                                                           | Online play works.                                        |
| Blur                                                         | High      | 50-60 FPS, stable.                                                          | Not applicable (single-player).                           |
| Borderlands 2                                                | High      | 40-60 FPS, minor drops.                                                     | Online co-op works.                                       |
| Borderlands GOTY                                             | High      | 40-60 FPS, minor drops.                                                     | Online co-op works.                                       |
| Brazilian Drug Dealer 3                                      | Perfect   | 60 FPS, very brazil.                                                        | Online play works.                                       |
| Call of Duty 4 Modern Warfare                                | High      | 60 FPS+, stable.                                                            | Online play works.                                        |
| Call of Duty World at War                                    | Medium    | 30-50 FPS, glitches via wine.                                               | Online play not tested.                                   |
| Call of Duty: Black Ops II                                   | Low       | 20-30 FPS, major lag and stuttering.                                        | Online play not tested (likely limited).                  |
| Call of Duty: Black Ops 3                                    | Low       | 20-40 FPS, heavy lag.                                                       | Online play performance-limited.                          |
| Car Mechanic Simulator 2021                                  | Medium    | 30-50 FPS, stutters in menus.                                               | Not applicable (single-player).                           |
| Castlevania: Lords of Shadow                                 | High      | 50-60 FPS, minor issues.                                                    | Not applicable (single-player).                           |
| Castlevania: Lords of Shadow 2                               | High      | 50-60 FPS, minor issues.                                                    | Not applicable (single-player).                           |
| Civilization V                                               | Perfect   | 60 FPS, no issues (native Linux).                                           | Online play works.                                        |
| Command and Conquer 3: Tiberium Wars                         | High      | 50-60 FPS, stable.                                                          | Online play not tested.                                   |
| Command and Conquer Generals: Zero Hour                      | High      | 50-60 FPS, stable.                                                          | Online play not tested.                                   |
| Control                                                      | Low       | 20-40 FPS, major glitches.                                                  | Not applicable (single-player).                           |
| Counter-Strike: Global Offensive                             | High      | 40-50 FPS, native online via Steam.                                         | Online play works via Steam.                              |
| Crusader Kings 2                                             | Perfect   | 60 FPS, no issues.                                                          | Online play works.                                        |
| Dead Cells                                                   | Perfect   | 60 FPS, no issues.                                                          | Not applicable (single-player).                           |
| Dead Island                                                  | High      | 20-60 FPS, minor stutters (native Linux).                                   | Not applicable (single-player).                           |
| Dead Island Riptide                                          | High      | 20-60 FPS, minor stutters/shader issues.                                    | Not applicable (single-player).                           |
| Dead Space                                                   | Medium    | 30-50 FPS, glitches.                                                        | Not applicable (single-player).                           |
| Deadpool 2013                                                | High      | 50-60 FPS, stable.                                                          | Not applicable (single-player).                           |
| Deltarune                                                     | Perfect   | 30 FPS (max fps for this game), no issues.                                 | Not applicable (single-player).                           |
| Detroit Become Human                                         | Low       | 20-40 FPS, crashes via wine.                                                | Not applicable (single-player).                           |
| Diablo III                                                   | Medium    | 30-50 FPS, drops during shader compiling.                                   | Online play works on Linux.                               |
| Diablo IV                                                    | Broken    | Instant crash.                                                              | Not applicable (doesn't launch).                          |
| Doom (2016)                                                  | Low       | 22-32 FPS, lags heavily.                                                    | Not applicable (primarily single-player).                 |
| Doom 3 BFG Edition                                           | High      | 60 FPS, minor issues.                                                       | Not applicable (single-player).                           |
| Driver San Francisco                                         | Medium    | 30-50 FPS, stutters.                                                        | Not applicable (single-player).                           |
| Dying Light                                                  | Low       | 20-40 FPS, heavy lag.                                                       | Online co-op performance-limited.                         |
| Elden Ring                                                   | Low       | 30 FPS in small window, low performance.                                    | Online co-op likely works but performance-limited.        |
| Enter the Gungeon                                            | Perfect   | 60 FPS, no issues.                                                          | Not applicable (single-player).                           |
| F1 Race Stars                                                | High      | 50-60 FPS, stable.                                                          | Not applicable (single-player).                           |
| Fallout (1997)                                               | Perfect   | 60 FPS, no issues.                                                          | Not applicable (single-player).                           |
| Fallout New Vegas                                            | Medium    | Playable with stuttering/freezes, 30 FPS with FSR.                          | Not applicable (single-player).                           |
| Fallout TTW                                                  | Medium    | Similar to Fallout New Vegas, stuttering.                                   | Not applicable (single-player).                           |
| Far Cry 3                                                    | High      | 50-60 FPS, minor drops.                                                     | Not applicable (single-player).                           |
| Fighting EX Layer                                            | Perfect   | 60 FPS, flawless.                                                           | Online play works.                                        |
| GRID 2                                                       | High      | 50-60 FPS, stable.                                                          | Online play not tested.                                   |
| GTA IV                                                       | Broken    | Vulkan errors, unplayable, crashes (PS4 Pro).                               | Not applicable (doesn't launch).                          |
| GTA Online                                                   | Medium    | 30-50 FPS, stutters.                                                        | Online play works but performance-limited.                |
| GTA SA                                                       | Broken    | Doesn't launch.                                                             | Not applicable (single-player).                           |
| GTA V                                                        | Low       | 20-40 FPS, heavy lag.                                                       | Online play performance-limited.                          |
| Garry's Mod                                                  | High      | 60 FPS+, stable.                                                            | Online play works via Steam.                              |
| Half-Life 2                                                  | Perfect   | 60-150 FPS (PS4 Pro, Nobara OS, maxed, 1080p). Minor black shader elements. | Not applicable (single-player).                           |
| Hollow Knight                                                | Perfect   | 60 FPS, no issues.                                                          | Not applicable (single-player).                           |
| Honkai: Star Rail                                            | Broken    | Game breaks the input UI. System requires a reboot after trying loading in. | Online play works with a custom launcher.                 |
| Jurassic Park: The Game                                      | Medium    | 30-50 FPS, glitches.                                                        | Not applicable (single-player).                           |
| Just Cause 2                                                 | High      | 60 FPS pre-OC, 75-80 post-OC in benchmark; 30-60 FPS in-game, minor lag.    | Not applicable (single-player).                           |
| Kerbal Space Program                                         | High      | 50-60 FPS (native Linux).                                                   | Not applicable (single-player).                           |
| King of Fighters XV                                          | Perfect   | 60 FPS online, flawless.                                                    | Online play works on Linux after tweaks.                  |
| Left 4 Dead 2                                                | High      | 50-60 FPS, stable (native Linux).                                           | Online co-op works.                                       |
| Little Nightmares                                            | High      | 50-60 FPS, minor drops.                                                     | Not applicable (single-player).                           |
| MOTOGP 17                                                    | Medium    | 30-50 FPS, stutters.                                                        | Online play not tested.                                   |
| Mad Max                                                      | High      | 20-60 FPS, minor stutters/shader issues.                                    | Not applicable (single-player).                           |
| Mafia 2                                                      | High      | 50-60 FPS, stable.                                                          | Not applicable (single-player).                           |
| Metal Gear Rising: Revengeance                               | Perfect   | 60 FPS, no issues.                                                          | Not applicable (single-player).                           |
| Metro Last Light                                             | Low       | 20-40 FPS, glitches.                                                        | Not applicable (single-player).                           |
| Midnight Driver                                              | Medium    | 30-50 FPS, minor lag.                                                       | Not applicable (single-player).                           |
| Minecraft 1.12.2 (Optifine)                                  | Perfect   | 100-300 FPS vanilla, stable.                                                | Online play supported.                                    |
| Minecraft (Optimization mods)                                | Medium    | 20-100+ FPS, stutters on Slim and Phat. See fix section.                    | Online play supported.                                    |
| Mortal Kombat 9                                              | Medium    | 30-60 FPS, glitches.                                                        | Online play not tested.                                   |
| N64Recomp/rt64                                               | High      | Audio issues on pulseaudio.                                                 | Not applicable (emulation tool).                          |
| Naruto Ultimate Ninja Storm 4                                | Medium    | 30-50 FPS, stutters.                                                        | Online play not tested.                                   |
| Need for Speed Most Wanted 2005                              | High      | 50-60 FPS, stable.                                                          | Not applicable (single-player).                           |
| Need for Speed: Hot Pursuit                                  | High      | 50-60 FPS, stable.                                                          | Online play not tested.                                   |
| Nickelodeon All-Star Brawl                                   | Perfect   | 60 FPS, no issues.                                                          | Online play works.                                        |
| One Armed Cook                                               | Low       | Insane flickering, but still 60 FPS.                                        | Not tested.                                               |
| One Armed Robber                                             | Low       | Insane flickering, but still 60 FPS.                                        | Not tested.                                               |
| OpenRa                                                       | High      | 50-60 FPS, stable.                                                          | Online play works.                                        |
| Orcs Must Die! 2                                             | High      | 50-60 FPS, minor issues.                                                    | Online co-op works.                                       |
| Ori And The Blind Forest                                     | Perfect   | 60 FPS, no issues.                                                          | Not applicable (single-player).                           |
| Outlast                                                      | High      | 30-40 FPS stable (PS4 Pro, Nobara OS, medium, 1080p). Minor drops.          | Not applicable (single-player).                           |
| Overwatch 2                                                  | Medium    | 50 FPS with stuttering.                                                     | No longer works on Linux due to anticheat (BattleEye).    |
| Papers Please                                                | Perfect   | 60 FPS, no issues (native Linux).                                           | Not applicable (single-player).                           |
| Path of Exile                                                | Perfect   | 20-60 FPS, minor stutters/shader issues.                                    | Online play works on Linux.                               |
| Planet Base                                                  | High      | 50-60 FPS, stable.                                                          | Not applicable (single-player).                           |
| Plants vs Zombies Garden Warfare                             | Medium    | 30-50 FPS, glitches.                                                        | Online play performance-limited.                          |
| Portal                                                       | High      | 60 FPS (OpenGL), setting shader to "Very High" has issues.                  | Not applicable (single-player).                           |
| Portal 2                                                     | Perfect   | 60-110 FPS (SteamOS3, OpenGL), no issues.                                   | Online co-op works via Steam.                             |
| Portal 2: Community Edition                                  | Low       | 10-30 FPS, flickering. (tested on Vulkan)                                  | Not applicable (not added yet).                           |
| Puyo Puyo Tetris 2                                           | Perfect   | 60 FPS, no issues.                                                          | Online play works.                                        |
| Resident Evil 0 HD Remaster                                  | Low       | 20-40 FPS, glitches.                                                        | Not applicable (single-player).                           |
| Resident Evil 4 Remake                                       | Low       | 10-20 FPS, freezes on Vulkan.                                               | Not applicable (single-player).                           |
| Resident Evil 5                                              | Low       | Black screen/audio issues, 20-30 FPS, crashes.                              | Not applicable (single-player).                           |
| Resident Evil 7                                              | Low       | 20 FPS, heavy texture anomalies.                                            | Not applicable (single-player).                           |
| Resident Evil HD Remaster                                    | Low       | 20 FPS, texture issues.                                                     | Not applicable (single-player).                           |
| Resident Evil Village                                        | Low       | Low FPS, crashes.                                                           | Not applicable (single-player).                           |
| Resident Evil: Revelations                                   | Low       | 20-30 FPS, crashes.                                                         | Not applicable (single-player).                           |
| Rocket League                                                | High      | 50-60 FPS, stable.                                                          | Online play works.                                        |
| Ruined King: A League of Legends Story                       | High      | 50-60 FPS, minor issues.                                                    | Not applicable (single-player).                           |
| SP Football Life 2023                                        | Medium    | 30-50 FPS, stutters.                                                        | Online play not tested.                                   |
| Saints Row: The Third                                        | Medium    | 30-50 FPS, frequent graphical glitches, playable.                           | Not applicable (single-player).                           |
| Scribblenauts Unlimited                                      | Perfect   | 60 FPS, no issues.                                                          | Not applicable (single-player).                           |
| Shadow of The Tomb Raider                                    | Low       | 20-40 FPS, heavy lag.                                                       | Not applicable (single-player).                           |
| Silent Hill Homecoming                                       | Perfect   | 60 FPS, max settings, no glitches.                                          | Not applicable (single-player).                           |
| Singularity                                                  | Medium    | 30-50 FPS, glitches.                                                        | Not applicable (single-player).                           |
| Skyrim Together Reborn                                       | Medium    | 30-50 FPS, stutters in multiplayer.                                         | Online play works but performance-limited.                |
| Slime Rancher                                                | Perfect   | 60 FPS, no issues.                                                          | Not applicable (single-player).                           |
| Smite                                                        | High      | 50-60 FPS, stable.                                                          | Online play works.                                        |
| Snowrunner                                                   | High      | Stable, no crashes/glitches. 3GB RAM/3GB VRAM, resource-heavy.              | Online co-op works on Linux.                              |
| Sonic Adventure 2 (PC)                                       | High      | 50-60 FPS, minor issues.                                                    | Not applicable (single-player).                           |
| Sonic And Sega All Stars Racing Transformed                  | High      | 50-60 FPS, stable.                                                          | Not applicable (single-player).                           |
| Sonic Roboblast 2                                            | High      | 60 FPS+, stable (native).                                                   | Not applicable (single-player).                           |
| Stalker: Shadow of Chernobyl                                 | Medium    | 30-50 FPS, glitches.                                                        | Not applicable (single-player).                           |
| Star Wars Battlefront II 2005                                | Medium    | 30-50 FPS, stutters.                                                        | Online play not tested.                                   |
| State of Decay 2                                             | Low       | 20-40 FPS, crashes.                                                         | Online co-op performance-limited.                         |
| Stray                                                        | High      | 50-60 FPS, minor drops.                                                     | Not applicable (single-player).                           |
| Street Fighter 3rd Strike & other games offered in Fightcade | Perfect   | 60 FPS, flawless.                                                           | Online play works via Fightcade.                          |
| Street Fighter 5 CE                                          | Perfect   | 60 FPS, no issues.                                                          | Online play works.                                        |
| Street Fighter x Tekken                                      | Perfect   | 60 FPS, no issues.                                                          | Online play works.                                        |
| Superliminal                                                 | Perfect   | 60 FPS, no issues.                                                          | Not applicable (single-player).                           |
| Team Fortress 2                                              | High      | 50-60 FPS, stable.                                                          | Online play works via Steam.                              |
| Teardown                                                     | Medium    | 30-50 FPS, stutters.                                                        | Not applicable (single-player).                           |
| Teenage Mutant Ninja Turtles: 2003                           | High      | 50-60 FPS, stable.                                                          | Not applicable (single-player).                           |
| Teenage Mutant Ninja Turtles: Shredder's Revenge             | High      | 50-60 FPS, stable.                                                          | Online co-op works.                                       |
| Teenage Mutant Ninja Turtles: in Manhattan                   | High      | 50-60 FPS, stable.                                                          | Not applicable (single-player).                           |
| Terrordrome: Rise of the Boogeymen                           | Medium    | 30-50 FPS, glitches.                                                        | Not applicable (single-player).                           |
| Test Drive Unlimited 2                                       | Medium    | 30-50 FPS, stutters (currently testing).                                    | Online play not tested.                                   |
| The Binding of Isaac                                         | Perfect   | 60 FPS, no issues.                                                          | Not applicable (single-player).                           |
| The Escapists 2                                              | High      | 50-60 FPS, minor issues.                                                    | Online co-op works.                                       |
| The Forest                                                   | Low       | 20-40 FPS, heavy lag.                                                       | Online co-op performance-limited.                         |
| The Stanley Parable                                          | Perfect   | 60 FPS, no issues (native Linux).                                           | Not applicable (single-player).                           |
| The Walking Dead Survival Instinct                           | Medium    | 30-50 FPS, glitches.                                                        | Not applicable (single-player).                           |
| There's Poop In My Soup                                      | High      | 50-60 FPS, stable.                                                          | Not applicable (single-player).                           |
| TimeShift                                                    | Medium    | 30-50 FPS, glitches.                                                        | Not applicable (single-player).                           |
| Titans Quest (2006)                                          | High      | 50-60 FPS, stable.                                                          | Online play not tested.                                   |
| Tomb Raider 2013                                             | High      | 50-60 FPS, minor drops.                                                     | Not applicable (single-player).                           |
| Touhou 12.3 Hisoutensoku                                     | Perfect   | 60 FPS, no issues (English translation).                                    | Not applicable (single-player).                           |
| TrackMania Nations Forever                                   | High      | 60 FPS+, stable.                                                            | Online play works.                                        |
| Trackmania (2020)                                            | High      | 50-60 FPS, stable.                                                          | Online play works.                                        |
| Tropico 3 - Steam Special Edition                            | High      | 50-60 FPS, stable.                                                          | Not applicable (single-player).                           |
| Tunic                                                        | Perfect   | 60 FPS, no issues.                                                          | Not applicable (single-player).                           |
| Turok 2008                                                   | Medium    | 30-50 FPS, glitches.                                                        | Not applicable (single-player).                           |
| ULTRAKILL                                                    | Perfect   | 60 FPS, no issues.                                                          | Not applicable (single-player).                           |
| Ultimate Marvel vs Capcom 3                                  | Perfect   | 60 FPS, no issues.                                                          | Online play works.                                        |
| Ultra Street Fighter 4                                       | Perfect   | 60 FPS, no issues.                                                          | Online play works.                                        |
| Vampire Survivors                                            | Perfect   | 60 FPS, no issues.                                                          | Not applicable (single-player).                           |
| Veloren                                                      | High      | 50-60 FPS, minor issues.                                                    | Online play works.                                        |
| Werewolf: The Apocalypse – Earthblood                        | Low       | 20-40 FPS, heavy lag.                                                       | Not applicable (single-player).                           |
| WipeOut Phantom Edition                                      | High      | 50-60 FPS, stable.                                                          | Not applicable (single-player).                           |
| World of Warcraft                                            | Medium    | 30-50 FPS, drops in heavy areas (latest release, 10.0).                     | Online play works but performance-limited.                |

</details>

---

<details><summary>PC Game Fixes and Workarounds (for games that need it)</summary>

| Game                                        | Fixes and Workarounds                                                                                                                                                                                                                                                                  |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Alien Swarm                                 | Use Proton CachyOS/Sarek with `PROTON_USE_WINED3D=1` to avoid black textures. Delete shader cache folder after failed attempts to prevent crashes. Mesa 25.1.0, Arch Linux, 2GB VRAM (PS4 fat). Reduce settings or lock to 30/45 FPS via MangoHUD for stability.                       |
| Apex Legends                                | Precompile shaders to reduce initial stuttering. No fix for anticheat (EA Anticheat) blocking Linux.                                                                                                                                                                                   |
| Call of Duty World at War                   | Use wine tweaks to reduce glitches. No specific fixes reported.                                                                                                                                                                                                                        |
| Counter-Strike: Global Offensive            | Apply performance tweaks (unspecified) for optimal FPS. Native Steam client recommended.                                                                                                                                                                                               |
| Dead Island                                 | Use native Linux version to avoid glitches. No specific fixes reported.                                                                                                                                                                                                                |
| Diablo III                                  | Precompile shaders to minimize FPS drops during gameplay.                                                                                                                                                                                                                              |
| Fallout New Vegas (and other Fallout games) | Use FSR to achieve 30 FPS. No specific fixes for stuttering/freezes.                                                                                                                                                                                                                   |
| King of Fighters XV                         | Set decoder to hardware to ensure flawless performance.                                                                                                                                                                                                                                |
| MOTOGP 17                                   | Lower settings to reduce stutters. No specific fixes reported.                                                                                                                                                                                                                         |
| Metro Last Light                            | No specific fixes reported.                                                                                                                                                                                                                                                            |
| Midnight Driver                             | Lower settings to reduce lag. No specific fixes reported.                                                                                                                                                                                                                              |
| Minecraft                                   | Use Mesa 25.2+ for 1.21.6+ (they started rewriting the OpenGL back-end for deferred rendering).<br>Avoid shaders (broken since 1.12.6). For modded versions, reduce mod count to improve FPS stability.<br>Simply Optimized modpack recommended.<br>Optifine recommended up to 1.12.2. |
| N64Recomp/rt64                              | Export `SDL_AUDIODRIVER=alsa` to fix audio issues on pulseaudio.                                                                                                                                                                                                                       |
| Overwatch 2                                 | Use shader caches to reduce stuttering. No fix for anticheat (BattleEye) blocking Linux.                                                                                                                                                                                               |

</details>

## Levels of stability and performance for emulation
There's multiple levels of stability:
- Broken
    - The game doesn't work at all or GPU acceleration doesn't work
- Low
    - Major graphical glitches ruin the experience, or it just lags heavily
- Medium
    - Some issues here and there, you can still see frequent glitches
- High
    - Works for the most part, with the only issues being in specific places that don’t really affect the majority of the game
- Perfect
    - It works with no issues

---

<details><summary>Emulated Games</summary>

| Game                               | Stability | Info                                                                 | Online Support Note                              |
|------------------------------------|-----------|----------------------------------------------------------------------|--------------------------------------------------|
| Mario Kart 8 Deluxe (Yuzu)         | Low       | 20 FPS, half speed on Vulkan, unstable on OpenGL. Emulator crashes.   | Online play likely limited by performance.       |
| Zelda: Breath of the Wild (Yuzu)   | Low       | 8-14 FPS, heavy lag.                                                 | No online component.                            |
| Kirby and the Forgotten Land (Yuzu)| Low       | 20 FPS, whiteness glitch in stages.                                  | Online play likely limited.                     |
| Pokemon Brilliant Diamond (Yuzu)   | Medium    | 30 FPS, frequent issues but playable.                                | Online play possible but not detailed.          |
| Super Mario 3D World (Cemu)        | High      | 50-55 FPS with Cheat Engine speedhack, tweaks needed.                | Online co-op likely functional.                 |
| General RPCS3/3DS Emu             | Low       | 20-30 FPS max, poor performance.                                     | Online play typically unsupported.              |
| Other (e.g., Yoshi's Crafted World, Xenoblade Chronicles X) | Low/Medium | 18-25 FPS, graphical issues.                        | Online play likely limited.                     |

</details>

---

<details><summary>Emulated Game Fixes and Workarounds</summary>

| Game                               | Fixes and Workarounds                                                                 |
|------------------------------------|--------------------------------------------------------------------------------------|
| Mario Kart 8 Deluxe (Yuzu)         | Use Vulkan for slightly better performance. No specific fixes for emulator crashes. |
| Zelda: Breath of the Wild (Yuzu)   | No specific fixes reported.                                                  |
| Kirby and the Forgotten Land (Yuzu)| No specific fixes reported.                                                  |
| Pokemon Brilliant Diamond (Yuzu)   | Adjust emulator settings to reduce issues. No specific fixes reported. |
| Super Mario 3D World (Cemu)       | Use Cheat Engine speedhack and tweak Cemu settings for better FPS. |
| General RPCS3/3DS Emu             | No specific fixes reported.                                                  |
| Other (e.g., Yoshi's Crafted World, Xenoblade Chronicles X) | No specific fixes reported.                                                  |

</details>

---

<a id="distrodiy"></a>

## Distro DIY

If you don't trust people on the internet (and rightfully so), you may want to port a distro of your liking on the PS4. If everything goes according to plan, you should be able to port your own distro without too many problems.

> [!CAUTION]
> This section is work in progress. For now I haven't figured out how to properly compile the drivers. If anyone is willing to help out, shoot a message at the [tux4orbis'](https://discord.gg/jebUjgBu6T) Discord server; PRs are also welcome.

> [!WARNING]
> This is meant for advanced users ONLY.
> 
> Some things may not work properly. If you encounter issues, chat on the [Discords](#information).

## Preamble - why is this necessary?
The community, as we've established before, is divided: there's the french (that nobody understands), there's people who want to work for real, but in the end none of them work together. So, even after almost 10 years, we still haven't seen these patches merged onto the original projects. Bruh.

## Requirements
In order to port a distro on the PS4, you will need the following:
- A distro of your choice
	- Don't go overboard with the ricing, remember that the GPU doesn't work fully
- A way to install said distro in a VM

### Drivers
To get the drivers, there's a couple of ways:
- On Arch based distros, there are precompiled packages that can be found at this pacman repo, forked and updated to latest stable ([source](https://github.com/DionKill/ps4-video-archlinux)):
```bash
[ps4-video]
SigLevel = Optional 
Server = https://dionkill.github.io/ps4-video-archlinux/repo/
```

- The `mesa-git`, `libdrm`, and `xf86-video-amdgpu` packages compiled with patches for the PS4, or compile them yourself
	- It is necessary to compile mesa in 32 bit too
- You can find patches [here](https://github.com/DionKill/ps4-linux-patches) (forked from FalsePhilosopher) to compile yourself
	- Either build the PKGBUILDS for Arch or straight up take the patches and apply them to Mesa-git
- You will still need to use a kernel of choice, and use the initramfs.

## Porting
> [!TIP]
> From here on out is uncharted territory. Good luck.

Jokes aside, you would need to do something like so:
- Install your distro and possibly configure it to your liking
	- If you want to make it public... Please don't. Leave it with American English and move on. Don't put 90s renders of anime girls, we don't want them...

Uninstall the `mesa-git`, `libdrm`, and `xf86-video-amdgpu` packages, and install the ones that are required by the PS4.
To uninstall the mesa packages, use your package manager instructions. Do not remove the dependencies, as it could break your system. just remove `mesa` and `lib32-mesa`.
- DO NOT USE MESA 22 FFS, IF YOU DO YOU ARE LIKE ACTUALLY A MORON
- The PS4 does NOT support hardware video encoding. It's locked behind DRM.

<details><summary>Package management config (if you don't want to update Mesa)</summary>

After that you need to add these packages to the ignore section so they can't be updated. On Arch based distros, change your pacman config, and add these packages to the ignore section:
```bash
sudo nano /etc/pacman.conf
```

Then, add this inside your pacman config:
```bash
IgnorePkg = lib32-mesa lib32-opencl-mesa ib32-vulkan-asahi lib32-vulkan-dzn lib32-vulkan-freedreno lib32-vulkan-gfxstream lib32-vulkan-intel lib32-vulkan-mesa-device-select lib32-vulkan-mesa-layers lib32-vulkan-nouveau lib32-vulkan-radeon lib32-vulkan-swrast lib32-vulkan-virtio mesa mesa-docs opencl-mesa vulkan-asahi vulkan-dzn vulkan-freedreno vulkan-gfxstream vulkan-intel vulkan-mesa-device-select vulkan-mesa-layers vulkan-nouveau vulkan-radeon vulkan-swrast vulkan-virtio lib32-vulkan-asahi  
IgnoreGroup = mesa
```
</details>

Before compressing the distro and publish it, you can clean your terminal history by running this in Bash:
```bash
history clear
```

Or if you are using Fish as your shell, run this:
```bash
rm ~/.local/share/fish/fish_history
exec fish
```

After that, you can compress your installation and move it over to your PS4 for installation. This next command skips all the useless folders and aims to be relatively fast at compression, using multiple cores. Compression levels higher than 6 are a waste of time.
```bash
cd / && sudo tar \
  --one-file-system \
  --acls \
  --xattrs \
  --numeric-owner \
  --exclude=/proc \
  --exclude=/sys \
  --exclude=/dev \
  --exclude=/run \
  --exclude=/tmp \
  --exclude=/var/tmp \
  --exclude=/var/cache \
  --exclude=/var/log \
  --exclude=/swapfile \
  --exclude=/lost+found \
  --exclude=/mnt \
  --exclude=/media \
  --exclude=/ps4linux.tar.xz \
  -cvpf /ps4linux.tar.xz / -I "xz -T0 -6"
```

Or, if you want a smaller command:
```bash
cd / && sudo tar -cvpf ps4linux.tar.xz --exclude=/ps4linux.tar.xz --exclude=/var/cache/* --one-file-system / -I "xz -T0 -6"
```

Then move the file over to the PS4. And... Follow the guide again...?

## Ending
I know it's a rough tutorial, but I'm lacking time and experience on Linux to be able to write a better one. PRs are welcome.

---

<a id="legacy"></a>

## Legacy and preservation

This page contains content that has been added for preservation's sake, even though most of you aren't ever going to use any of this stuff.

> [!WARNING]
> As this is legacy content, if you use any of these don't expect people to be able to help you.

## Legacy kernels, distros and initramfses
In all honesty: most of these can be found on the PS4Linux.com website, as it hasn't been updated in a long time. Don't use these on modern distros, as they don't boot anymore.
### Kernels
#### Other kernels
These are additional kernels that are kind of up to date but also not really or that do not offer prebuilts, which aren't useful for 99% of people.

| Kernel version | Source and download                           | Compatible Southbridges    | Extra info                          |
| -------------- | --------------------------------------------- | -------------------------- | ----------------------------------- |
| 6.15.y         | [GitHub](https://github.com/crashniels/linux) | All, depends on the branch | No precompiled downloads available. |
#### Kernels to avoid
This list contains kernels that you should be avoiding, with all due respect.

| Kernel version                                                           | Source and download                                                                            | Compatible Southbridges | Extra info                                                                                                              |
| ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| [6.15,<br>5.15 and<br> 5.4](https://www.youtube.com/watch?v=zVzHzJT7dHk) | All                                                                                            | N/A                     | FullLTO, 120Hz support, 4K for PS4 Pro. You need to download the whole archive and pick one for your needs.<br>By saya. |
| [6.15.4](https://mega.nz/folder/N0QjHSBT#609IHevkWEW0vnTCFW-Rhw)         | Aeolia &<br>Belize                                                                             | N/A?                    | ZRAM, CachyOS patches, KVM and more. <br>By triki1.                                                                     |
| 4.4<br>5.x                                                               | Probably no source.<br>[Download](https://ps4linux.com/downloads/#PS4_Linux_Kernel_Downloads). | All                     | The old list from PS4Linux.                                                                                             |

Credits for the kernels can be found [here](#ending).
#### Bootargs
The `bootargs.txt` is not really necessary anymore, unless your "distro + kernel" combo of choice requires it or on certain kernels for Baikal PS4s. Therefore, it has been moved to the legacy section.

This adds certain parameters when launching the kernel to make the GPU work properly.

In order to use it, create a new text file, and input this line inside, then save it as `bootargs.txt`:
```
panic=0 clocksource=tsc consoleblank=0 net.ifnames=0 radeon.dpm=0 amdgpu.dpm=0 drm.debug=0 console=uart8250,mmio32,0xd0340000 console=ttyS0,115200n8 console=tty0 drm.edid_firmware=edid/1920x1080.bin 
```

Remember that this `bootargs.txt` needs to be placed in the same folder as the bzImage.
### Distro
Distros made by other members of the PS4 community that we cannot trust anymore are moved here. They also haven't really been updated in a long time as far as I'm aware.

| Distro                                                                                           | Compatible Southbridge & Mesa          | Port credits                                                              | Info                                                                    |
| ------------------------------------------------------------------------------------------------ | -------------------------------------- | ------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| [CachyOS](https://mega.nz/file/RyUVQARB#HZD49XXac_v2CYKD4Oqa7Tg1aiZ7ltH_cnDxixw9JjY)             | All<br>(Mesa 25.1.0)                   | [Elokuba (Qba)](https://www.youtube.com/channel/UCU-eXjZ7Ud0k2wC_14mqdOw) | "Final Fantasy v2" version. It has nothing to do with FF. Mere fantasy. |
| [EndeavourOS](https://ps4linux.com/forums/d/386-endeavouros-gaming-rebirth)                      | All?<br>(Mesa Version ?)               | [Elokuba (Qba)](https://www.youtube.com/channel/UCU-eXjZ7Ud0k2wC_14mqdOw) | Arch based distro that's nice to use and easy to maintain               |
| [Manjaro](https://ps4linux.com/forums/d/342-manjaro-from-scratch)                                | All?<br>(Mesa Version ?)               | [Elokuba (Qba)](https://www.youtube.com/channel/UCU-eXjZ7Ud0k2wC_14mqdOw) | A Manjaro KDE distro                                                    |
| [Garuda](https://ps4linux.com/forums/d/415-garuda-dr460nized-gaming-v2/2)                        | All?<br>(Mesa Version ?)               | [Elokuba (Qba)](https://www.youtube.com/channel/UCU-eXjZ7Ud0k2wC_14mqdOw) | "Gaming focused" distro (not really)                                    |
| [Fedora 42](https://ps4linux.com/forums/d/399-fedora42-by-qba-triki1kdewayland)                  | Aeolia, Belize<br>(Mesa 26)            | [Elokuba (Qba)](https://www.youtube.com/channel/UCU-eXjZ7Ud0k2wC_14mqdOw) | Normal Fedora running KDE on Wayland                                    |
| [Debian Forky](https://ps4linux.com/forums/d/373-debian-forky-sid/3)                             | Aeolia, Belize<br>(Mesa 25.3+)         | [triki1](https://www.youtube.com/@trakerchris9876)                        | Very new distro. Extremely bleeding edge.                               |
| [Kali Linux](https://ps4linux.com/forums/d/392-debian-forky-kali-linux-edition)                  | All<br>(Mesa 25.0.3-devel+)            | [triki1](https://www.youtube.com/@trakerchris9876)                        | Based on Debian Forky, but with Kali Linux stuff included               |
| [Debian Trixie](https://ps4linux.com/forums/d/369-debien-trixie-full-update-mesa-2520-devel/13)  | Aeolia, Belize<br>(Mesa 25.2.0-devel+) | [triki1](https://www.youtube.com/@trakerchris9876)                        | Latest Debian                                                           |
| [Xubuntu](https://ps4linux.com/forums/d/337-xubuntu-2504-final-release)                          | All<br>(Mesa 25.0.5)                   | [triki1](https://www.youtube.com/@trakerchris9876)                        | Divided into multiple files                                             |
| [Batocera 40](https://ps4linux.com/forums/d/252-batocera-40-for-ps4-installation-setup-tutorial) | All<br>(Mesa 22.1.7)                   | [Noob404](https://www.youtube.com/channel/UC9pY5BDCjDLOC4j-zkHPu8)        | For retrogaming                                                         |

If you are looking for really old distros, check out the downloads from PS4Linux [here](https://ps4linux.com/downloads/#PS4_Linux_Distro_Downloads).

### Initramfs
Old downloads from PS4Linux can be found [here](https://ps4linux.com/downloads/#initramfscpiogz_Downloads).

### Other
Honestly, it's all on the same page as above. [Here you go](https://ps4linux.com/downloads/).

## Legacy configs
More stuff may be moved to here in the future.

### VRAM configs
The `vram.txt` is a file contaning a number, which is your VRAM allocation amount.
You may still be able to use this, but to avoid confusion, it has been moved to the legacy section, as you can just as easily reboot the console and change the payload.

You can create this file yourself. Create an empty text file called `vram.txt`, and in it, input a number between 1 and 3. That's how many GBs will be allocated to your GPU. Remember you are removing that from your system memory!

## Updates
### Arch-based distros (legacy)
To make sure that the PS4 packages don't get updated, you need to modify the pacman config:
```bash
sudo nano /etc/pacman.conf
```

Then, in the `[Options]` section, add this:
```bash
IgnorePkg = lib32-libdrm-git lib32-mesa-git libdrm-git mesa-git lib32-libdrm lib32-mesa libdrm mesa lib32-llvm-libs llvm-libs
IgnoreGroup = mesa
```

Then, you should be free to update your system with:
```bash
sudo pacman -S
```
