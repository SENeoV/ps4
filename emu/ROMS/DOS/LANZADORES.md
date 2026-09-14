# DOS: lanzadores

Cada juego está descomprimido en su carpeta y se arranca con su `.conf`, que monta la carpeta como `C:` y ejecuta el programa. Los genera `tools/dos.py`, que elige el ejecutable por su nombre. **Sin probar en la consola.**

- `seguro`: un único candidato claro. `dudoso`: hay otros posibles (columna *Alternativas*); si no arranca el bueno, se cambia la última línea del `.conf`.
- `instalar`: el zip solo trae el instalador; el `.conf` deja la consola de DOS en la carpeta para ejecutarlo.
- `disquete`: arranca desde una imagen de disquete.

Resumen: disquete 1, dudoso 254, instalar 11, seguro 690

| Juego | Estado | Arranca con | Alternativas | Notas |
|---|---|---|---|---|
| 1000 Miglia | dudoso | `RUNME.BAT` | 1000\MIGLIA.EXE, 1000\MIDI3DRV.EXE, 1000\EXPLO.EXE, 1000\WRITEAT.EXE, 1000\CHELINGU.EXE |  |
| 3D World Boxing | dudoso | `3DWB.BAT` | 3DBOX\3DWBINST.BAT, 3DBOX\3DWBMIDI.BAT, 3DBOX\BCVGA.EXE, 3DBOX\NEWMIDIL.EXE |  |
| 4x4 Off-Road Racing | dudoso | `4X4.EXE` | 4X4\RUNME.BAT, 4X4\ROAD.EXE, 4X4\FRONT.EXE, 4X4\REPAIR.EXE, 4X4\HALLFAME.EXE |  |
| 7 Cities of Gold | dudoso | `7CITIES.EXE` | 7CITIES\7COG.BAT, 7CITIES\TESTBLAS.EXE |  |
| A320 Airbus | dudoso | `A320.COM` | AIRBUS\A320S.EXE, AIRBUS\A320P.EXE, AIRBUS\A320I.EXE, AIRBUS\A320U.COM |  |
| Abrams Battle Tank | dudoso | `RUNME.BAT` | ABRAMS.COM, START.EXE, BRIEF.EXE, END.EXE, SIM.EXE |  |
| Action Fighter | dudoso | `ACT_EGA.EXE` | ACT_CGA.EXE |  |
| Advanced Civilization | dudoso | `AC_MAIN.EXE` | ADCIVI\AC_START.EXE, ADCIVI\SETSOUND.EXE |  |
| Agent USA | dudoso | `AGENTUSA.EXE` | AGENTUSA\AGENTUSA.COM |  |
| Air Strike USA | dudoso | `USA1.EXE` | USA2.EXE |  |
| Airbucks | instalar | `dir /w` | LHA.EXE, INSTALL.EXE, README.BAT | solo trae el instalador: hay que instalarlo antes (en DOSBox del PC o en la consola) |
| Al Qadim - The Genie's Curse | dudoso | `GENIE.BAT` | AL-QADIM\GENIER.EXE, AL-QADIM\SINSTALL.EXE, AL-QADIM\LOADPATS.EXE, AL-QADIM\SOUND.BAT |  |
| Albion | dudoso | `ALBION.BAT` | ALBION\LAUNCH.EXE, ALBION\MAIN.EXE, ALBION\CD\AUTORUN.EXE, ALBION\DOS4GW.EXE, ALBION\SETUP.EXE |  |
| Alien Incident | dudoso | `GAME.EXE` | AI.COM, SYSTEM.EXE, DOS4GW.EXE, ANIMPLAY.EXE, SETUP.EXE |  |
| Alien Rampage | instalar | `dir /w` | ALIENRAM\INSTALL.EXE | solo trae el instalador: hay que instalarlo antes (en DOSBox del PC o en la consola) |
| All dogs go to Heaven | dudoso | `DOGSC.BAT` | DOGS\DOGSE.BAT, DOGS\DOGST.BAT, DOGS\MRH_DOGE.EXE, DOGS\MRH_DOGC.EXE, DOGS\MRH_DOGT.EXE |  |
| Alone in the Dark 2 | dudoso | `AITD2.BAT` | AITD2.EXE, WINSTALL.EXE, ADLIBM.COM, AITD2CRK.COM, DRV_BZ.COM |  |
| Alter Ego - Female | dudoso | `ALTEREGO.BAT` | ALTERFEM.BAT, AEGV.EXE, AETV.EXE |  |
| Altered Beast | dudoso | `BEAST.BAT` | LOAD.EXE, BEASTY.EXE, FREAKFAC.COM |  |
| Amazing Learning Games With Rayman | dudoso | `RAYDEMO.EXE` | RAYEDU\RUNDEMO.BAT, RAYEDU\SNDDEMO.BAT, DEMO.BAT, RAYEDU\SETSOUND.EXE |  |
| Amulets and Armor | dudoso | `AA.BAT` | AAGRAV.BAT, TESTME.EXE, SERDRV.EXE, DOS4GW.EXE, SETSOUND.EXE |  |
| An American Tail - Fievel goes West | dudoso | `AMTAIL.EXE` | FIEVEL\CAPSTONE.EXE, FIEVEL\PKCONFIG.EXE |  |
| Apollo 18 - Mission to the Moon | dudoso | `APOLLO.EXE` | APOLLO18\RUNME.BAT, APOLLO18\APOLLOHI.EXE |  |
| Archer MacLean's Pool | dudoso | `POOL.EXE` | ARCHER\POOL256.EXE, ARCHER\MUSIC.EXE, ARCHER\CDPATCH.EXE, ARCHER\CDGO.BAT, ARCHER\INSTALL.EXE |  |
| Archon Ultra | dudoso | `ARCHON.EXE` | ORIGINAL\ARCHON.EXE, ARCHON1.EXE, ORIGINAL\AU_V11.EXE, DOS4GW.EXE |  |
| Arctic Adventure | dudoso | `AA1.EXE` | AA2.EXE, AA3.EXE, AA4.EXE, AA-HINT.EXE |  |
| Arctic Fox | dudoso | `AFOX.BAT` | AFOX.EXE, AFOXH.EXE, AFOX16.EXE, CONFIG.EXE |  |
| Arkanoid 2 - Revenge of Doh | dudoso | `ARKANO.EXE` | ARKA2\ARKANOID.BAT, ARKA2\DOH.EXE, ARKA2\INSTALL.BAT, ARKA2\CONFIG.BAT |  |
| Ashes of Empire | dudoso | `ASHES.BAT` | ASHES\GAME.EXE, ASHES\INTRO.EXE, ASHES\INSTALL.EXE |  |
| Asterix - Operation Getafix | seguro | `LOADER.EXE` |  | tiene INTRO.STK: puede que ScummVM lo ejecute |
| Atomino | dudoso | `ATOMINO.EXE` | LOADER.EXE, RUNME.COM, HARD.COM, INSTALL.BAT |  |
| Baal | dudoso | `BAAL.EXE` | BAAL\START.EXE |  |
| Back to the Future III | dudoso | `BF.BAT` | FUTURE\CHAIN.COM, FUTURE\GAME1\GAME1.EXE, FUTURE\GAME3\GAME3.EXE, FUTURE\GAME2\GAME2.EXE, FUTURE\GAMEI\GAMEI.EXE |  |
| Bad Blood | dudoso | `BADB.EXE` | BADBLOOD\GAME.EXE, BADBLOOD\BADBLOOD.EXE, BADBLOOD\MCGA2ALL.EXE, BADBLOOD\TILE2ALL.EXE, BADBLOOD\TANDYPIN.EXE |  |
| Bad Street Brawler | dudoso | `BR.EXE` | BOOT.COM, BOOT2.COM |  |
| Batman - The Caped Crusader | dudoso | `JOKER.EXE` | BATMANC\PENGUIN.EXE, BATMANC\R-BCCJOK.COM, BATMANC\R-BCCPEN.COM |  |
| BattleTech - The Crescent Hawks Inception | dudoso | `BTECH.EXE` | $VERIFY.EXE |  |
| Beyond Zork - The Coconut of Quendor | dudoso | `BZORK.BAT` | BZ\FROTZ.EXE, BZ\BZORK.EXE |  |
| Big Business | dudoso | `BB.BAT` | BIGBIZ\BBIZ.EXE, BIGBIZ\BBCONFIG.COM |  |
| Bio Menace | dudoso | `BMENACE1.EXE` | BMENACE2.EXE, BMENACE3.EXE, BIOPATCH\BIOPATCH.EXE |  |
| Birds of Prey | dudoso | `BIRDS.EXE` | BIRDPREY\START.BAT, BIRDPREY\BOPINC.COM |  |
| Black Sect | dudoso | `SECTE.EXE` | BS.BAT, SECTE1.EXE, PRES.EXE, CFG.EXE, CONFIG.BAT |  |
| Blues Brothers 2 | dudoso | `BLUES.BAT` | BLUES.EXE, BLUES-JA.BAT, BBJBTRNR.COM |  |
| Bobby Fischer teaches Chess | dudoso | `BFTC.EXE` | BFTC\BFTCG.EXE, BFTC\BFTCC.EXE, BFTC\BFTCB.EXE, BFTC\BFTCA.EXE, BFTC\BFTCF.EXE |  |
| Breakers | dudoso | `BREAKERS.BAT` | RUN.EXE, TITLE.EXE |  |
| Brett Hull Hockey '95 | instalar | `dir /w` | TRN-BHH1\INSTALL.EXE, TRN-BHH1\INSTALL2.EXE, TRN-BHH1\LHA.EXE, TRN-BHH1\READ.COM | solo trae el instalador: hay que instalarlo antes (en DOSBox del PC o en la consola) |
| Brimstone | dudoso | `GO.EXE` | BRIMSTNE.BAT, CLEAR.COM |  |
| Cadaver | dudoso | `RUNME.BAT` | CADAVER.COM, CAD.EXE, SETUP.COM, INTRO.EXE |  |
| California Games | dudoso | `CALGAMES.EXE` | SURFING.EXE, BMX.EXE, ROLLER.EXE, HALFPIPE.EXE, FOOTBAG.EXE |  |
| Cannon Fodder | dudoso | `CF_ENG.EXE` | CANNONF\CANNON.BAT, CANNONF\CANINTRO.COM, CANNONF\INSTALL.EXE |  |
| Captain Dynamo | dudoso | `DYNAMO.COM` | CDYNAMO\DYNAMO-T.COM, CDYNAMO\DYN.EXE |  |
| Car & Driver | dudoso | `C&D.EXE` | CAR\MODEM.EXE, CAR\NETB2.EXE, CAR\PART2.BAT, CAR\SETUP.EXE, CAR\COMIO.EXE |  |
| Centurion - Defender of Rome | dudoso | `RUNME.BAT` | CENTURIO.EXE, READ_ME.COM |  |
| Championship Lode Runner | disquete | `boot a:` |  |  |
| Chessmaster 2000 | dudoso | `CM.EXE` | CMASTER.EXE |  |
| Civilization | dudoso | `CIV.EXE` | CIV\EGRAPHIC.EXE, CIV\TGRAPHIC.EXE, CIV\MGRAPHIC.EXE, CIV\MISC.EXE |  |
| Cloud Kingdoms | dudoso | `CKEGA.EXE` | CKCGA.EXE |  |
| Colonization | instalar | `dir /w` | COLONIZE\INSTALL.EXE, COLONIZE\MPSCOPY.EXE, COLONIZE\PKUNZJR.COM | solo trae el instalador: hay que instalarlo antes (en DOSBox del PC o en la consola) |
| Conan the Cimmerian | dudoso | `CONAN.EXE` | CONAN\START.EXE, CONAN\RUNME.COM, CONAN\MUSTREAD.COM, CONAN\RAZOR.COM, CONAN\INSTALL.EXE |  |
| Conqueror | dudoso | `TANKS.BAT` | TANKSTGA.EXE, CDSON.EXE, TANKSEGA.EXE, TANKSCGA.EXE, README.BAT |  |
| Cool Croc Twins | dudoso | `COOL.EXE` | CROC\COOL.COM |  |
| Covert Action | dudoso | `COVERT.BAT` | COVERT.EXE, GAME.EXE, FINAL.EXE, TAC.EXE, BUG.EXE |  |
| Creepers | dudoso | `CREEPERS.EXE` | CREEPE_K.EXE, INSTALL.EXE, SETUP.EXE |  |
| CyClones | dudoso | `CYCLONE.EXE` | CYCLONES\CYCLONES.EXE, CYCLONES\SMKPLAY.EXE, CYCLONES\SVIEW.EXE, CYCLONES\CRACK.COM, CYCLONES\SSETUP.EXE |  |
| Cyber Empires | dudoso | `RUNME.BAT` | CYBER\CYBER.COM, CYBER\KEYINIT.EXE |  |
| CyberRace | dudoso | `CR.BAT` | CYBERRAC\T15.EXE, CYBERRAC\VOXEL4.EXE, CYBERRAC\CRBOOT.BAT, CYBERRAC\CHECK.EXE, CYBERRAC\READ.BAT |  |
| D-Generation | dudoso | `DGEN.EXE` | DGEN\DGENVGA.EXE, DGEN\RST\DGEN.EXE, DGEN\RST\DGENVGA.EXE |  |
| Daemonsgate | dudoso | `DGINST.EXE` | D-GATE.EXE, DGCONFIG.EXE, INSTALL.BAT |  |
| Dalek Attack | dudoso | `DRW.EXE` | DALEK\DRWHO.EXE, DALEK\INST2.BAT, DALEK\INSTALL.BAT |  |
| Dark Castle | dudoso | `DC.EXE` | RUNME.BAT, DCOVL.COM, INSTALL.BAT |  |
| Dark Seed | dudoso | `DS.BAT` | DARKSEED\START.EXE, DARKSEED\TOS.EXE |  |
| Darklands | dudoso | `DARKLAND.EXE` | DARKPOP.COM, MGRAPHIC.EXE, MISC.EXE, XTRACT.EXE, PICS\PICSHOW.EXE |  |
| Defender of the Crown | dudoso | `DOC.EXE` | READTHIS.EXE |  |
| Demon Stalker | dudoso | `DS.BAT` | DSED.BAT, GAME.EXE, ED.EXE |  |
| Descent 2 (Shareware) | dudoso | `D2.BAT` | D2DEMO\D2DEMO.EXE, D2DEMO\EREGCARD.EXE, D2DEMO\PCXVIEW.EXE, D2DEMO\SETUP.EXE |  |
| Disc | dudoso | `DISC.EXE` | DISC\RUNME.BAT, DISC\BBSAHOLC.EXE |  |
| Disciples of Steel | dudoso | `START.BAT` | STEEL.EXE, LOGO.EXE, DCONFIG.EXE, CRACK.COM, STEELDAT\SBFMDRV.COM |  |
| Discworld | instalar | `dir /w` | INSTALL.EXE | solo trae el instalador: hay que instalarlo antes (en DOSBox del PC o en la consola) |
| Doom (Shareware) | instalar | `dir /w` | DEICE.EXE, INSTALL.BAT | solo trae el instalador: hay que instalarlo antes (en DOSBox del PC o en la consola) |
| Double Dribble | dudoso | `RUNME.BAT` | DDRIBBLE\PLAY.EXE |  |
| Dragons of Flame | dudoso | `GAME.EXE` | START.COM, DISKA.BAT, DISKB.BAT, TANDY.COM, CGA.COM |  |
| Dream Zone | dudoso | `DREAM.EXE` | DZ.BAT, META.EXE, INST2.EXE, INSTALL.BAT |  |
| Dstroy | dudoso | `DS.EXE` | DSTROY\JOY2.EXE, DSTROY\README.EXE |  |
| Duke Nukem 3D | dudoso | `DN3DHELP.EXE` | DUKE3D.EXE, SETMAIN.EXE, COMMIT.EXE, SETUP.EXE |  |
| EWJ | dudoso | `EWJ.BAT` | RUNME.BAT, EWJ1.EXE, EWJ2.EXE, DOS4GW.EXE, SETUP.EXE |  |
| Entombed | instalar | `dir /w` | INSTALL.EXE | solo trae el instalador: hay que instalarlo antes (en DOSBox del PC o en la consola) |
| Essex | dudoso | `ESSEX.BAT` | GO.EXE, CLEAR.COM |  |
| Euro Soccer | dudoso | `EURO.EXE` | EURO.COM, SETUP.EXE |  |
| F-15 Strike Eagle II | dudoso | `START.EXE` | F15.COM, F15LOADR.BAT, EGAME.EXE, END.EXE, CGRAPHIC.EXE |  |
| F-15 Strike Eagle III | dudoso | `F15.EXE` | F15-3\PLAY.EXE, F15-3\F15MON.EXE, F15-3\LOAD.EXE, F15-3\F15.COM, F15-3\RAP.EXE |  |
| F-19 - Stealth Fighter | dudoso | `START.EXE` | F19\F19.COM, F19\EGAME.EXE, F19\END.EXE, F19\SU.EXE, F19\CGRAPHIC.EXE |  |
| Fast Break | dudoso | `FB.BAT` | FB-T.EXE, FB-E.EXE, FB-C.EXE, KSEL.EXE, RTLINKST.COM |  |
| Fields of Glory | instalar | `dir /w` | INSTALL.EXE, UNZIP.EXE | solo trae el instalador: hay que instalarlo antes (en DOSBox del PC o en la consola) |
| Final Frontier | dudoso | `FRONTIER.BAT` | FRONTIER\FRONTIER.EXE |  |
| Football Limited | dudoso | `FLI.EXE` | FOOTLI~1\FOOTLI~1\FLTD.EXE, FOOTLI~1\FOOTLI~1\GO.EXE, FOOTLI~1\FOOTLI~1\DOS4GW.EXE, FOOTLI~1\FOOTLI~1\SETUP.EXE |  |
| Football Manager 3 | dudoso | `FM3MM.EXE` | FOOTMAN3\FM3ENV.EXE, FOOTMAN3\FM3VGA.BAT, FOOTMAN3\FM3CGA.BAT, FOOTMAN3\INSTALL.BAT |  |
| Fuzzy's world of Miniature Space Golf | instalar | `dir /w` | INSTALL.EXE | solo trae el instalador: hay que instalarlo antes (en DOSBox del PC o en la consola) |
| Gateway 2 - Homeworld | dudoso | `HOME.EXE` | HOMEMAIN.EXE, RTLINKST.COM |  |
| Gemfire | dudoso | `MAIN.EXE` | GEMFIRE\OPEN.EXE, GEMFIRE\END.EXE, GEMFIRE\FMDRV.COM, GEMFIRE\KOEI.COM |  |
| Ghostbusters 2 | dudoso | `GB.EXE` | GHOSTB2\GB2.BAT, GHOSTB2\SHELL.EXE, GHOSTB2\GB2FIX.EXE, GHOSTB2\LASTSAVE.BAT, GHOSTB2\RECALL.BAT |  |
| Gloriana | dudoso | `GLORIANA.BAT` | GLORI\GLORI_VM.BAT, GLORI\ELISABET\GO.EXE, GLORI\HBDINTRO.EXE, GLORI\DELBLAST.BAT, GLORI\ELISABET\ELLI.EXE |  |
| Gods | dudoso | `GODS.EXE` | GODS\GAME.EXE, GODS\TGA.EXE, GODS\TGAME.EXE, GODS\VGA.EXE, GODS\UNPACK.EXE |  |
| Golden Axe | dudoso | `RUNME.BAT` | GOLD.EXE, HUMBLE!.EXE |  |
| Grand Monster Slam | dudoso | `GMS.BAT` | GMS2.EXE, GMS1.EXE, GMSC.BAT, GMSE.BAT, GMSH.BAT |  |
| Grand Prix Circuit | dudoso | `GPCGA.EXE` | GP.EXE, GPEGA.EXE, GPTDY.EXE |  |
| Gunboat | dudoso | `GB.EXE` | GUNBOAT\ADLIB.COM, GUNBOAT\SETUP.EXE, GUNBOAT\INSTALL.EXE |  |
| Harrier Jump Jet | dudoso | `HARRIER.BAT` | AV8B\GAME.EXE, AV8B\HARR.COM, AV8B\FRONTEND.EXE, AV8B\END.EXE, AV8B\PLAYSCR.EXE |  |
| Heavy Barrel | dudoso | `HB.EXE` | HB_PROG.EXE, CHECKFOR.EXE |  |
| Heimdall | dudoso | `HEIMDALL.EXE` | HEIMDALL\GAME.EXE, HEIMDALL\AXE.EXE, HEIMDALL\PIG.EXE, HEIMDALL\LONGBOAT.EXE, HEIMDALL\ENDSEQ.EXE |  |
| Heirs to the Throne | dudoso | `START.EXE` | HEIRS\START.COM, HEIRS\PSMCFG.EXE, HEIRS\SETUP.EXE |  |
| Hero Quest | dudoso | `HERO.EXE` | QUEST.EXE, MG.BAT, INTRO.EXE, INSTALL.BAT |  |
| Hill Street Blues | dudoso | `HSB.BAT` | HSB_TGA.EXE, HSB_VGA.EXE, HSB_CGA.EXE, INTRO.EXE |  |
| Hocus Pocus | dudoso | `HOCUS.EXE` | HP-HELP.EXE, HOCUSG.BAT, __HPGRVS.EXE, ULTRAMID.EXE, DEALERS.EXE |  |
| Home Alone 2 - Lost in New York | dudoso | `HA2.EXE` | HA2\HA2SETUP.EXE, HA2\CAPSTONE.EXE, HA2\MIDPAK.COM |  |
| Home Alone | dudoso | `HA.EXE` | HACRACK.EXE |  |
| Horror Zombies from the Crypt | dudoso | `HZVGA.EXE` | HORROR\HZEGA.EXE |  |
| Impact! | dudoso | `IMPACTE.EXE` | IMPACTC.EXE |  |
| Impossible Mission 2 | dudoso | `IM2_TAN.EXE` | IM2_EGA.EXE, IM2_MCGA.EXE, IM2_CGA.EXE, BBGAME.EXE, BBPSM.EXE |  |
| Incunabula | dudoso | `SCRIBE.EXE` | BASRUN.EXE, IMPERIUM.EXE, SCRIBE2.EXE, TRADES.EXE, IMPEVAL.EXE |  |
| Infiltrator 2 | dudoso | `IGROUND.EXE` | IBMSIM.EXE, IBMINTRO.EXE, IBMEND.EXE, INF.EXE, AUTOEXEC.BAT |  |
| Infiltrator | dudoso | `IGROUND.EXE` | IBMSIM.EXE, IBMINTRO.EXE, IBMEND.EXE, INF.EXE, FIXIN.BAT |  |
| Innocent Until Caught | dudoso | `INNOCENT.EXE` | IUC\IUC.BAT, IUC\START.BAT, IUC\SET_IUC.EXE, IUC\CRACK.COM, IUC\INNCRK.COM |  |
| International Sports Challenge | dudoso | `CHALL.EXE` | ISC\SPORTS.BAT, ISC\MEN.EXE, ISC\MAR.EXE, ISC\CYC.EXE, ISC\DIV.EXE |  |
| Isle of the Dead | dudoso | `IOD.BAT` | IOD\IODEX1.EXE, IOD\DOSXTEST.EXE, IOD\LHA.EXE, IOD\SETUP.BAT |  |
| Iznogoud | dudoso | `IZN1FHER.EXE` | PROTECT.BAT, TATOU.COM, IZN1FCGA.EXE |  |
| Jagged Alliance | dudoso | `JA.EXE` | JAVM.BAT, DOS4GW.EXE, SETSOUND.EXE, README.BAT |  |
| Jazz Jackrabbit | seguro | `JAZZ.EXE` |  | ejecutable indicado en AUTOBOOT.DBP |
| Jewels of Darkness (Trilogy) | dudoso | `AINT.EXE` | MENU.EXE, CHECKSUM.EXE |  |
| Jurassic Park | dudoso | `JP.EXE` | JP\JP2D.EXE, JP\JP3D.EXE, JP\ICREDS.EXE, JP\OUTRO.EXE, JP\OPTIONS.EXE |  |
| Kick Off 3 - European Challenge | dudoso | `KICK.EXE` | PLAY.BAT, MAIN.EXE, KO3.BAT, DOS4GW.EXE, INTRO.EXE |  |
| Kingdoms of Germany | dudoso | `START.BAT` | KINGOGER\GERMANY.EXE, KINGOGER\KOGCRACK.EXE |  |
| Kings Table - The Legend of Ragnarok | dudoso | `GAME.EXE` | KTLOR\RAGNAROK.BAT, KTLOR\INSTALL.EXE |  |
| Knights of the Sky | dudoso | `START.BAT` | KOTS\GAME.EXE, KOTS\KNIGHTS.COM, KOTS\FLIGHT.EXE, KOTS\TITLE.EXE, KOTS\ID.EXE |  |
| Laser Squad | dudoso | `LSQDBCC.EXE` | LSQUAD\LASER.EXE, LSQUAD\SQUAD.EXE, LSQUAD\LSAVE.COM, LSQUAD\INTRO3.EXE, LSQUAD\INTRO1.EXE |  |
| Legend of the Sword | dudoso | `LEGEND.EXE` | START.BAT, LOADFIX.COM |  |
| Life & Death 2 - The Brain | dudoso | `LD2.EXE` | LAD2\OP.EXE |  |
| Litil Divil | instalar | `dir /w` | ARJ.EXE, INSTALL.EXE, LGC-APPG\APPLY.EXE | solo trae el instalador: hay que instalarlo antes (en DOSBox del PC o en la consola) |
| Locomotion | dudoso | `GAME.EXE` | LOCO.BAT, SOUND.COM |  |
| Lode Runner | dudoso | `LR.COM` | V1\LR.COM, V2\LR.COM |  |
| Lombard RAC Rally | dudoso | `RREGA.EXE` | LOMBARD\RRCGA.EXE, LOMBARD\UNINSTAL.EXE |  |
| Magic Pockets | dudoso | `START.BAT` | MAGICPO\GAME.EXE, MAGICPO\POCKETS.EXE, MAGICPO\TDTINTRO.EXE, MAGICPO\X.COM, MAGICPO\INSTALL.EXE |  |
| Maupiti Island | dudoso | `MAUPAN.EXE` | MAUPITI.BAT, MAUPAN1.EXE, CRACK\MAUPAN.EXE, START.COM, INSTALL.EXE |  |
| Mean 18 | dudoso | `ARCH.EXE` | GOLF.EXE |  |
| Mechwarrior | dudoso | `MW.EXE` | BTECH.EXE, MW_MAIN.EXE, GFAST.EXE, MW_CPICS.EXE, MW_EGA.EXE |  |
| MegaTraveller 2 - Quest for the Ancients | dudoso | `OLD.COM` | MT2\MT2.COM, MT2\SETUP.EXE |  |
| Michael Jordan in Flight | dudoso | `BB.BAT` | JORDAN\BBEXE.EXE, JORDAN\CONFIG.EXE, JORDAN\CONFIG.BAT |  |
| Micro Machines 2 - Turbo Tournament | dudoso | `MM2.BAT` | MM2\MM2.EXE, MM2\NEXT.BAT, MM2\CFG\MM2.BAT, MM2\IL-CRACK.COM, MM2\MAPS\WORDYMAP.EXE |  |
| Micro Machines | dudoso | `MICRO.EXE` | MICRO.COM, SM.EXE, SETUP.EXE, INSTALL.EXE |  |
| Moonstone - A hard days Knight | dudoso | `MAIN.EXE` | MSTONE\INTR.EXE, MSTONE\MS.EXE |  |
| Murders in Venice | dudoso | `VENISE.EXE` | VENICE\EGA_OVL.EXE, VENICE\HERC_OVL.EXE, VENICE\CGA_OVL.EXE, VENICE\COBRA.BAT, VENICE\SELECT.EXE |  |
| Ninja Rabbits | dudoso | `JOY.BAT` | NRABBITS\VGA.EXE, NRABBITS\TGA.EXE, NRABBITS\CBS.EXE, NRABBITS\JOYCALIB.EXE, NRABBITS\EGA.EXE |  |
| Nobunagas Ambition II | dudoso | `MAIN.EXE` | NOBU2\OE.EXE, NOBU2\KOEI.COM |  |
| Nobunagas Ambition | dudoso | `PLAY.BAT` | NOBU1\NOBUNAGA.BAT, NOBU1\MAIN.EXE, NOBU1\CDX.EXE, NOBU1\ODA_A.BAT, NOBU1\ODA_B.BAT |  |
| Ocean Ranger | dudoso | `OCEAN.EXE` | ORANGER\RANGER.BAT, ORANGER\RANGER1.EXE, ORANGER\REPLY.COM |  |
| Omnicron Conspiracy | dudoso | `OMNICRON.EXE` | PLAY.EXE, SCODE.EXE |  |
| On the Ball - World Cup Edition | dudoso | `ANSTWCE.EXE` | ED.EXE, PMINFO.EXE, RMINFO.EXE, PLAY0090.EXE, PLAYINTW.EXE |  |
| Oo-Topos | dudoso | `NOVEL.EXE` | CRACK.COM, IBMDOS.COM, IBMBIO.COM, INSTALL.BAT, AUTOEXEC.BAT |  |
| Operation Europe - Path to Victory 1939-45 | dudoso | `MAIN.EXE` | EUROPE\OPEN.EXE, EUROPE\END.EXE, EUROPE\BOOTHELP.BAT, EUROPE\KOEI.EXE, EUROPE\OPEU.BAT |  |
| Operation Wolf | dudoso | `START.BAT` | WOLF.EXE, SPWOLF.EXE, 1.BAT, 2.BAT, VGA.BAT |  |
| P.H.M. Pegasus | dudoso | `PHM.BAT` | PHMINST.BAT, HF.EXE |  |
| PC-Man | dudoso | `PCMAN (GREG KUPERBERG).V1.1982.COM` | PCMANG~1.COM |  |
| Panzer General | dudoso | `PG.BAT` | PANZERG\EXE\PANZER.EXE, PANZERG\SVIEW.EXE, PANZERG\SOUND.BAT, PANZERG\EXE\SOUND.EXE, PANZERG\EXE\UNIVBE.EXE |  |
| Paperboy | dudoso | `PAPERBOY.EXE` | PAPERCG2.EXE, PAPERCGT.EXE, PAPERBOY.COM, PAPERCGA.EXE |  |
| Pinball Illusions | dudoso | `START.BAT` | ILLUSION\ILLUSION.EXE |  |
| Pinball World | dudoso | `PWPCGAME.EXE` | PBW\PWPCINTR.EXE, PBW\PWORLD.EXE, PBW\PW.COM, PBW\SETSND.EXE, PBW\HYBRID.EXE |  |
| Pirates! Gold | dudoso | `PGJUKE.EXE` | PIRATESG.EXE, PCXDITH.EXE, CHVER.EXE, CONV.BAT, PCXS.BAT |  |
| Pizza Tycoon | dudoso | `PT.EXE` | PIZZA.BAT, C.BAT, MUSIC.COM, SOUNDRV.COM, VECTOR.COM |  |
| Power Dolls | dudoso | `PD.BAT` | PDOLLS\PD.EXE, PDOLLS\PLAY.BAT, PDOLLS\CRACK.EXE, PDOLLS\CHECKEMM.EXE, PDOLLS\XINSTALL.BAT |  |
| Power Drive | dudoso | `PD.BAT` | PDRIVE.EXE, S\PD.BAT, Y\PD.BAT, MEGAEM.EXE, EMUSET.EXE |  |
| Prehistorik | dudoso | `DP.BAT` | HISTORIK.EXE, 2.BAT, 1.BAT, DP30.COM, AT720.COM |  |
| Purple Saturn Day | dudoso | `PURPLE.EXE` | PSD\PURPEDIT.EXE, PSD\PURPHRC.EXE, PSD\PURPEGA.EXE, PSD\PURPTDY.EXE, PSD\PURPCGA.EXE |  |
| Quadralien | dudoso | `START.BAT` | QUAD\QUAD.EXE |  |
| Rags to Riches - The Financial Market Simulation | dudoso | `RAGS.EXE` | RAGS\START.EXE, RAGS\SETUP.EXE |  |
| Rambo III | dudoso | `RAMBO.EXE` | RAMBO3\RAMBO.COM, RAMBO3\GETDRV.EXE |  |
| Rastan | dudoso | `RASTAN.BAT` | RASTAN.EXE, RASTAN.COM, GETDRV.EXE, INSTALL.BAT |  |
| Rendez-Vous with Rama | dudoso | `RDV.EXE` | CRACK.COM |  |
| Renegade | dudoso | `RENEGADE.EXE` | RENEGADE\RENEGADE.COM, RENEGADE\GETDRV.EXE, RENEGADE\INSTALL.BAT |  |
| Return of the Phantom | dudoso | `RETURN.EXE` | PHANTOM\PHANTOM.BAT, PHANTOM\ANIMVIEW.EXE, PHANTOM\BLOODNET.EXE, PHANTOM\DRAGON.EXE, PHANTOM\MAINMENU.EXE |  |
| Rex Nebular and the cosmic Gender-Bender | dudoso | `REX.BAT` | REX\NEBULAR.EXE, REX\ANIMVIEW.EXE, REX\TEXTVIEW.EXE, REX\MAINMENU.EXE, REX\BONUS.EXE |  |
| Rick Dangerous | dudoso | `START.BAT` | RICKD\RICK.COM, RICKD\SIMCGA.COM, RICKD\LOADFIX.COM |  |
| Risky Woods | dudoso | `RISKY.EXE` | RWTRN.COM, LEVEL.COM |  |
| Rollercoaster Rumbler | dudoso | `ROLLER.BAT` | LOADER.EXE, EGA\ROLLER.EXE, CGA\ROLLER.EXE, NEUA.COM |  |
| Romance of the Three Kingdoms | dudoso | `MAIN.EXE` | ROMANCE1\SAN_B.EXE, ROMANCE1\SANGOKU.COM, ROMANCE1\INSTALL.EXE |  |
| S.C. Out | dudoso | `SCOUT.EXE` | GAME.EXE |  |
| Shadow Warrior | dudoso | `SW.EXE` | SWHELP.EXE, SETMAIN.EXE, COMMIT.EXE, SETUP.EXE |  |
| Shadowgate | dudoso | `SGATE.EXE` | SHADOWGT\SETFIXED.BAT, SHADOWGT\FINISH.BAT, SHADOWGT\INSTALL.EXE, SHADOWGT\UNINSTAL.BAT |  |
| Silent Service 2 | dudoso | `SS2.EXE` | SS2\SILENT.BAT, SS2\S.BAT, SS2\MISC.EXE |  |
| Silpheed | dudoso | `S.EXE` | SILPHEED.BAT, SIERRA.EXE, __INSTH.BAT, INSTGAME.BAT, EXISTS.COM |  |
| SimCity 2000 | dudoso | `SC2000.EXE` | SIMC2000\VRF_DLL.EXE, SIMC2000\VDETECT.EXE, SIMC2000\SC2KCHT2.EXE, SIMC2000\ATISET.EXE, SIMC2000\SC2VESA.BAT |  |
| Sinbad and the Throne of the Falcon | dudoso | `SB.EXE` | DBD.EXE, SBCGA.EXE |  |
| Skyrunner | dudoso | `RUNNER.BAT` | SKY1.COM, SKY2.COM |  |
| Slipstream 5000 | dudoso | `SLIP.BAT` | SLIP5000\SLIPSTRM.EXE, SLIP5000\SLIP5000.EXE, SLIP5000\INSTALL.EXE, SLIP5000\LOADPATS.EXE |  |
| Sorcerian | dudoso | `SIERRA.EXE` | JO.EXE, TOWN.EXE, END.EXE, INN.EXE, STAFF.EXE |  |
| Space Crusade | dudoso | `SPACE.EXE` | SPACE\SC.BAT, SPACE\CRUSADE.EXE, SPACE\MOSLO.COM, SPACE\CRACK.COM, SPACE\INTRO.EXE |  |
| Speedball 2 - Brutal Deluxe | dudoso | `GGS.BAT` | SB2.EXE, TANDY.EXE, INTRO.EXE, SETUP.COM |  |
| Speedball | dudoso | `SHOW.EXE` | SB.BAT, EGA.EXE, REPLY.COM, CGA.EXE, TANDY.EXE |  |
| Spellcasting 201 - The Sorcerers Appliance | dudoso | `S201.EXE` | S201\S201MAIN.EXE, S201\RTLINKST.COM |  |
| Spellcasting 301 - Spring Break | dudoso | `S301.EXE` | S301\S301MAIN.EXE, S301\LEGEND.BAT, S301\RTLINKST.COM, S301\INSTALL.EXE |  |
| Spirit of Excalibur | dudoso | `EXCAL.EXE` | SOE\START.EXE, SOE\INSTALL.EXE |  |
| Star Control 2 | dudoso | `STARCON2.EXE` | STARCON2.COM, MELEE.EXE, KEYS.EXE, RESOURCE.BAT, PLAYSC2.BAT |  |
| Star Control | dudoso | `STARCON.EXE` | STARCON.COM, KEYS.EXE, DISKFREE.EXE, EDIT.EXE |  |
| Star Trek - The Next Generation - The Transinium Challenge | dudoso | `TRANS.EXE` | STTNG\TREK.BAT, STTNG\METAWNDO.EXE |  |
| Star Trek V - The Final Frontier | dudoso | `ST5.EXE` | BOPWIRE\BOPWIRE.EXE, KFIGHT\KFIGHT.EXE, CARTOON\CARTOON.EXE, INSTALL.BAT |  |
| Star Wars Dark Forces | dudoso | `DF.EXE` | IMUSE.EXE, KEYCONFI.EXE, BOOTMKR.EXE, DFDEMO.BAT, DOS4GW.EXE |  |
| Starflight 2 - Trade Routes of the Cloud Nebula | dudoso | `STAR2B.COM` | STAR2A.COM, STARFLT2.COM, SF2.BAT, MMAIN.EXE, EPUT.EXE |  |
| Starflight | dudoso | `STARB.COM` | STARA.COM, STARFLT.COM, NAMER.EXE, HDINSTL.BAT, THROWOUT.BAT |  |
| Steel Panthers | dudoso | `START.BAT` | STEELPAN\STEEL.EXE, STEELPAN\START2.BAT, STEELPAN\SETSOUND.EXE, STEELPAN\UNIVBE.EXE, STEELPAN\SOUND.BAT |  |
| Stellar 7 | dudoso | `S7.BAT` | STELLAR7\STELLAR7.EXE, STELLAR7\INSTALL.COM |  |
| Stone Age | dudoso | `SA_V1_00.EXE` | STONE\STONE.BAT, STONE\SCROLLER.EXE, STONE\FXDRIVER.EXE |  |
| Stunt Driver | dudoso | `STUNT.BAT` | STDRIVER\STUNT.EXE, STDRIVER\STUNT_K.EXE, STDRIVER\CFGED.EXE, STDRIVER\INFLATE.EXE, STDRIVER\EGALIB0.EXE |  |
| Stunt Island | dudoso | `SIPLAY.EXE` | STUNTISL\SIPLAYER.EXE, STUNTISL\STUNT.EXE, STUNTISL\SIUP1.EXE, STUNTISL\MAKEONE.EXE, STUNTISL\PLAYONE.EXE |  |
| Summer Challenge | dudoso | `SUMMER.EXE` | SUMMER\RUNME.BAT, SUMMER\SUMCRACK.EXE |  |
| Super Solvers - Operation Neptune | dudoso | `ON.EXE` | ON\OPNEP.BAT, ON\INSTALL.EXE |  |
| Super Street Fighter II Turbo | dudoso | `SF2TURBO.EXE` | 32RTM.EXE, MAKESWP.EXE, SSF2T.BAT, INSTALL.EXE, LOADPATS.EXE |  |
| Superstar Ice Hockey | dudoso | `HOCKEY.EXE` | PLAY.COM, LEAGUE.COM, JOY_CNTL.COM |  |
| Sword of the Samurai | dudoso | `START.EXE` | SWORD\SAMURAI.COM, SWORD\RP.EXE, SWORD\MELEE.EXE, SWORD\BATTLE.EXE, SWORD\DUEL.EXE |  |
| Teenage Mutant Ninja Turtles | dudoso | `GO.BAT` | TMNT\RUNME.BAT, TMNT\TMNTEGA.EXE, TMNT\TMNTCGA.EXE, TMNT\TMNTTDY.EXE, TMNT\MNU.EXE |  |
| Telengard | dudoso | `TELEN.EXE` | TELEQU.EXE, TELMO.EXE |  |
| Tennis Cup 2 | dudoso | `T.EXE` | SWAPAB.COM |  |
| The Beverly Hillbillies | dudoso | `HB.EXE` | HB\MIDPAK.COM, HB\SOUNDRV.COM, HB\CONFIG.EXE |  |
| The Dark Half | dudoso | `DH.BAT` | DARKHALF\DHINTRO.EXE, DARKHALF\DARKHALF.BAT, DARKHALF\DDH.EXE, DARKHALF\MIDPAK.COM, DARKHALF\DRIVERS\SETM.EXE |  |
| The Dark Queen of Krynn | dudoso | `DQK.EXE` | START.BAT, INSTALL.EXE |  |
| The Even More Incredible Machine | seguro | `TIM.EXE` | INSTALL.EXE, INTRO.EXE | tiene RESOURCE.MAP: puede que ScummVM lo ejecute |
| The Final Conflict | dudoso | `E.EXE` | FINALCON\V.EXE, FINALCON\INSTALL.BAT |  |
| The Hunt for Red October | dudoso | `HFRO.EXE` | GAME.EXE, LOADPIC.EXE |  |
| The Incredible Machine | seguro | `RUNME.BAT` | TIM\TIM.EXE, TIM\XRAY.EXE, TIM\TIMCHEAT.COM, TIM\EM-NFO.COM, TIM\INSTALL.COM | tiene RESOURCE.MAP: puede que ScummVM lo ejecute |
| The King of Chicago | dudoso | `KING.BAT` | KOFC\CHICAGO.EXE |  |
| The Lost Dutchman Mine | dudoso | `LDM.EXE` | LDME.EXE, SIMCGA40.COM |  |
| The Patrician | dudoso | `PATR.EXE` | START.BAT, PATRIZ.EXE, SCHLACHT.EXE |  |
| The Pawn | dudoso | `MAGNETIC.EXE` | XTRACT64.EXE |  |
| The Punisher | dudoso | `RUNME.BAT` | GO.EXE, PUNISHER.COM, ADLIB.BAT, SIM.EXE, WAREHSE.EXE |  |
| The Scrabble | dudoso | `SCRABBLC.EXE` | SCRABBLH.EXE, 1.BAT, 2.BAT |  |
| Theatre of Death | dudoso | `TOD.EXE` | TOD\CRACK.COM, TOD\SOUNDS\MEGAEM.EXE, TOD\SOUNDS\EMUSET.EXE, TOD\SOUNDS\GRAVIS.EXE |  |
| Times of Lore | dudoso | `RUNME.BAT` | LORE.EXE |  |
| Top Gun | dudoso | `TOPGUN.EXE` | TOPGUN_.EXE |  |
| Toyota Celica GT Rally | dudoso | `RALLY.EXE` | RUNME.EXE, DB-CALL.COM, INSTALL.EXE |  |
| Traffic Department 2192 | instalar | `dir /w` | INSTALL.EXE | solo trae el instalador: hay que instalarlo antes (en DOSBox del PC o en la consola) |
| Transport Tycoon Deluxe (for Windows) | dudoso | `SPANISH.EXE` | FRENCH.EXE, GERMAN.EXE, ENGLISH.EXE, AMERICAN.EXE, GAMEGFX.EXE |  |
| Treasure Trap | dudoso | `TT.EXE` | RUNME.BAT, DTYPE.EXE, INSTALL.BAT |  |
| Trog! | dudoso | `TROG.BAT` | TROG\RUN.EXE, TROG\CALLER.EXE, TROG\VGASTUFF.EXE, TROG\INSTALL.EXE |  |
| Tubular Worlds | dudoso | `PART2.EXE` | CHECKMS.EXE, PART1.EXE, TUBWORLD.BAT |  |
| Twilight Zone | dudoso | `TZ.BAT` | TZONE\TZONE.EXE, TZONE\TZVGA.BAT, TZONE\TZEGA.BAT, TZONE\TZCGA.BAT, TZONE\TZTANDY.BAT |  |
| Typhoon of Steel | dudoso | `TYPHOONE.EXE` | TYPHOON\TYPHOONC.EXE, TYPHOON\TYPHOO~1.COM |  |
| Tyrian 2000 | dudoso | `TYRIAN2.EXE` | TYRIAN2K.EXE, FILE0001.EXE, SHIPEDIT.EXE, RTM.EXE, SETUP.EXE |  |
| Ultima - Worlds of Adventure 2 - Martian Dreams | dudoso | `GAME.EXE` | MARTIAN\MARTIAN.EXE, MARTIAN\INSTALL.EXE |  |
| Ultima Underworld - The Stygian Abyss | dudoso | `UW.EXE` | UWSOUND.EXE, INSTALL.EXE |  |
| Ultima Underworld 2 - Labyrinth of Worlds | dudoso | `UW2.EXE` | RPGINST.EXE, UINSTALL.EXE, UWSOUND.EXE |  |
| Ultima VI - The False Prophet | dudoso | `GAME.EXE` | ULTIMA6.EXE, ULTIMA6.COM, U.EXE, END.EXE, T2HRC.EXE |  |
| Uncharted Waters 2 - New Horizons | dudoso | `MAIN.EXE` | INSTMAIN.EXE, END.EXE, OPEN.EXE, GRP480C.EXE, GRPDRV.EXE |  |
| Uncharted Waters | dudoso | `MAIN.EXE` | WATERS\OPEN.EXE, WATERS\END.EXE, WATERS\FMDRV.COM, WATERS\KOEI.COM |  |
| Universe 3 | dudoso | `U3.EXE` | RUNME.BAT |  |
| Universe | dudoso | `FLIGHT.EXE` | FLIGHT~1.EXE, STARPORT.EXE, CONSTRUC.EXE |  |
| Up Periscope | dudoso | `SUB.EXE` | EQUUS.BAT |  |
| Vengeance of Excalibur | dudoso | `VEX.EXE` | VOE\GAME.EXE, VOE\FRANCAIS\GAME.EXE, VOE\DEUTSCH\GAME.EXE, VOE\ENGLISH\GAME.EXE, VOE\INSTALL.EXE |  |
| Warcraft II - Tides of Darkness | dudoso | `WAR2.EXE` | WAR2ED95.EXE, UVCONFIG.EXE, SFXED95.EXE, WAR2CRAK.EXE, WAR2EDIT.EXE |  |
| Warcraft | dudoso | `WAR.EXE` | CRACK.EXE, DOS4GW.EXE, SETUP.EXE |  |
| Warlords 2 | dudoso | `START.EXE` | WARLORD2.EXE, ADLIB.COM, IMPORT.EXE, PAUDIO.COM, WAR2.BAT |  |
| Wayne's World | dudoso | `WW.EXE` | WAYNE\WW2.EXE, WAYNE\WWCFG.EXE, WAYNE\KYB.COM, WAYNE\MIDPAK.COM, WAYNE\SBLAST02.COM |  |
| Whale's Voyage | dudoso | `WV.EXE` | WVOYAGE\WVD.EXE, WVOYAGE\WVT.EXE, WVOYAGE\WJUKEBOX.EXE, WVOYAGE\CHRED.EXE, WVOYAGE\CONTROL.EXE |  |
| Where in the World is Carmen Sandiego | dudoso | `CARMEN.BAT` | CARMEN.EXE |  |
| Winter Olympics - Lillehammer '94 | dudoso | `WO94.EXE` | WO94\NOSOUND.EXE, WO94\SOUND.EXE |  |
| Wolf | dudoso | `W.EXE` | WOLF.EXE, SMIDPAK.COM, PAUDIO.COM, SBPRO.COM, ADLIB.COM |  |
| World Class Leader Board | dudoso | `GOLF.EXE` | WCLB\HINSTALL.BAT, WCLB\README.BAT |  |
| World of Xeen | dudoso | `GO.BAT` | XEEN.EXE, XEEN.COM, XEE.EXE, MM5CRACK.COM, INSTALL.EXE |  |
| X-Men Children of the Atom | dudoso | `XMEN.BAT` | XMENPC.EXE, UVCONFIG.EXE, READIFF.EXE, SETSOUND.EXE |  |
| Xiphos | dudoso | `X.EXE` | XIPHOS\RUNME.BAT, XIPHOS\CUR1.EXE, XIPHOS\TUNE.EXE, XIPHOS\STEADY.EXE, XIPHOS\BOARDS.COM |  |
| Zeliard | dudoso | `Z.BAT` | ZELIARD\ZELIARD.EXE, ZELIARD\GAME.BAT, ZELIARD\__INSTH.BAT, ZELIARD\INSTGAME.BAT, ZELIARD\MTINIT.COM |  |
| Zone 66 | dudoso | `GAME.EXE` | ZONE66\ZONE66.EXE, ZONE66\REN-93.EXE, ZONE66\CATALOG.EXE, ZONE66\HELPME.EXE |  |
| Zool | dudoso | `ZOOL.EXE` | START.EXE, FADER.EXE |  |
| Zork Quest - Assault on Egreth Castle | dudoso | `RUNME.BAT` | ZORK.COM, MOSLO.COM |  |

Los 690 juegos `seguro` sin notas no se listan.
