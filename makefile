CLASS_DRIVER_BUILD_DIR = lufa-lib/tags/LUFA-120730/Demos/Device/ClassDriver/TemperatureSensor

build: lufa-lib lufa-classdriver.build
	rm -rf $(CLASS_DRIVER_BUILD_DIR)
	cp -rf lufa-classdriver $(CLASS_DRIVER_BUILD_DIR)
	make -C $(CLASS_DRIVER_BUILD_DIR)

lufa-lib:
	git clone git@github.com:abcminiuser/lufa-lib.git

lufa-classdriver.build:
	ln -sf $(CLASS_DRIVER_BUILD_DIR) lufa-classdriver.build

program:
	avrdude -p m32u4 -c usbtiny -U flash:w:lufa-classdriver.build/TemperatureSensor.hex

clean:
	rm -rf lufa-lib lufa-classdriver.build

.PHONY: build program clean
