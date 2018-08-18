from conans import ConanFile, tools

class CcsConan(ConanFile):
    name = "ccs"
    version = "0.9.13"
    settings = "os", "compiler", "build_type", "arch"
    generators = "compiler_args"
    default_options="boost:shared=True"
    scm = {
            "type": "git",
            "subfolder": "ccs",
            "url": "https://github.com/hellige/ccs-cpp.git",
            "revision" : version
            }
    requires = "boost/1.67.0@conan/stable"
    build_requires = "gtest/1.8.0@bincrafters/stable"
    exports = 'conanbuild.patch'

    def source(self):
        tools.patch(base_path='ccs', patch_file='conanbuild.patch')

    def package(self):
        self.copy("*", src='ccs/dist')

    def package_info(self):
        self.cpp_info.libs = self.collect_libs()

    def build(self):
        conanflags=open('conanbuildinfo.args').read()
        self.run("make CONANFLAGS='{}' -j{}".format(conanflags, tools.cpu_count()), cwd='ccs')
