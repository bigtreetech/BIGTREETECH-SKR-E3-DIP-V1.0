There are two options for compiling and flashing Marlin 2.0 firmware:

1. Use the pre-compiled firmware.bin files:
	a. Identify the stepper motor drivers you have installed on your mainboard (A4988, DRV8825, LV8729, TMC2130, TMC2208, TMC2209, or TMC5160).
	b. Download the "firmware-[stepper driver].bin" of the driver you're using, and rename it to "firmware.bin."
	c. Copy the file to your SD/TF Card and turn on the printer. The firmware will take about 10 seconds to flash.

2. Use Marlin source-code to compile custom firmware (allows you to modify configurations/change settings):
	a. Begin either with the "Marlin-2.0.5_SKR-E3-DIP" uncompiled firmware on this repository, or download the latest Marlin 2.0 firmware files from https://marlinfw.org/.
	b. Download Visual Studio Code, and install the PlatformIO extension.
	c. Open the firmware folder in Visual Studio Code and modify the configuration.h and configuration_adv.h files to customize the settings. Note that if you use the files from "Marlin-2.0.5_SKR-E3-DIP," the basic settings to get the firmware to work with the SKR E3-DIP and Ender-3 are already configured, but if you download the latest official Marlin files you will have to modify the serial ports, boards, printer size, and other settings appropriately. 
	d. Change the "default_envs" in platformio.ini to "STM32F103RC_btt." Note, some SKR E3-DIP boards ship with different chips (RCT6 or RET6), so other options include "STM32F103RE_btt" or "STM32F103RC_btt_512K" based on the board you have. For USB support, add "_USB" to the end.
	e. Click the checkmark in the bottom left of VS Code, or use the Auto Build Marlin extension to compile the firmware. 
	f. Copy the resulting "firmware.bin" file from your project folder to the SD card and boot the printer to flash.

For additional directions on how to flash a custom firmware, here is a list of additional resources: 
1) Teaching Tech "SKR Mini E3 - the best Ender-3 upgrade from stock?" - https://youtu.be/-XUQKQnUNig 
2) Teaching Tech "Marlin firmware explained" - https://youtu.be/U8_ldMckGDE
3) The First Layer "How to install the SKR E3 DIP" - https://youtu.be/CmBhIaEwhaI
4) 3D MakeIt "SKR 1.3 and Mini E3 (DIP) configuration" - https://youtu.be/q_lVkC4V8ps
5) Official Marlin website and Github repository - https://marlinfw.org/ and https://github.com/MarlinFirmware
6) Configuration guides for similar boards such as the SKR Mini E3 - https://www.reddit.com/r/ender3/comments/e894j7/marlin_20x_guide_for_ender_3_using_skr_mini_e3_v12/
7) ANTCLABS BLTouch manuals - https://www.antclabs.com/manual
8) Teaching Tech "DIY filament runout sensor" - https://youtu.be/gwHpXaj_6xE


Troubleshooting:
- Sometimes an error occurs when compiling for the first time. Please close VS Code and reopen, then compiling will be normal.
- Marlin 2.0 project folders must not exceed 64 characters in length, and folder nesting depth can not exceed 3, otherwise, when opening the compiling the project, there will be unexpected errors.
- Homing/limit switches often do not work with TMC2209 drivers. Cut/bend the DIAG pin as outlined in the TMC2209 repository (https://github.com/bigtreetech/BIGTREETECH-TMC2209-V1.2).
- If you get an EEPROM version error/mismatch, try to clear/reset EEPROM settings using "Init EEPROM" from the control menu, or by sending M502 and M500 to the board via USB.
- If you get a "TMC Connection Error" verify that you have set up the jumpers correctly for UART, STEP/DIR, etc.