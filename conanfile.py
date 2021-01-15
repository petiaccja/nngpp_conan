from conans import ConanFile, CMake, tools

class NngppConan(ConanFile):
    name = "nngpp"
    license = "MIT"
    author = "Chris Welshman"
    url = "https://github.com/cwzx/nngpp"
    description = "C++ wrapper around the nanomsg NNG API."
    version = "1.3.0"
    requires = [ "nng/1.3.2" ]

    def source(self):
        file_name = "nng-v" + self.version + ".tar.gz"
        tools.get("https://github.com/cwzx/nngpp/archive/" + file_name)

    def package(self):
        folder_name = "nngpp-nng-v" + self.version
        self.copy("*", dst="include/nngpp", src=folder_name + "/include/nngpp")