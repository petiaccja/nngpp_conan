from conans import ConanFile, CMake, tools
import os

class NngppConan(ConanFile):
    name = "nngpp"
    license = "MIT"
    author = "Chris Welshman"
    url = "https://github.com/cwzx/nngpp"
    description = "C++ wrapper around the nanomsg NNG API."
    version = "1.3.0"
    requires = [ "nng/1.3.2" ]

    def source(self):
        self.run("git clone https://github.com/cwzx/nngpp.git")

    def package(self):
        print(os.getcwd())
        self.copy("*", dst="include/nngpp", src="nngpp/include/nngpp")