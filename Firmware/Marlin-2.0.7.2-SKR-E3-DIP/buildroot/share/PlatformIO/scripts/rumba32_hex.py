from os.path import join
from os.path import expandvars
Import("env", "projenv")

env.AddPostAction(
	join("$BUILD_DIR","${PROGNAME}.elf"),
	env.VerboseAction(" ".join([
		"$OBJCOPY", "-O ihex", "$TARGET", # TARGET=.pio/build/rumba32/firmware.elf
		"\"" + join("$BUILD_DIR","${PROGNAME}.hex") + "\"", # Note: $BUILD_DIR is a full path
	]), "Building $TARGET"))
