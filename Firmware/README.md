1. Sometimes an error occurs when compiling this branch for the first time. Please Close vscode and reopen, then compiling will be normal.
2. if you are downloaded from Marlin bugfix-2.0.x Official version. Please modify [here](https://github.com/bigtreetech/BIGTREETECH-SKR-E3-DIP-V1.0/blob/9beb3aea723c1a114d0e5c16ce6d2c37bfbb26c2/Firmware/Marlin-2.0.x-SKR-R3-DIP/platformio.ini#L34) from `TMCStepper@<1.0.0` to `https://github.com/bigtreetech/TMCStepper`. 
This is because the UART of tmc2208/2209 has not yet been merged into the official version, please use this method before merged
3. These firmware are all Ender3 16 microstep. Please download the firmware of the driver you are using, then change the file name to "firmware. bin" and copy it to the TF card to update it.

Note: if you want to design your own version naming rules, folder names must not exceed 64 characters in length, 
marlin 2.0 project files in other folders, folder nesting depth can not exceed 3, 
otherwise, when opening the project compilation project, there will be unexpected compilation errors!
It is recommended that the file name should not be named too long, the shorter the better. 
File nesting depth should not be too much, the less nesting, the better.
