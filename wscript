from os import popen
import sys

srcdir = '.'
blddir = 'build'
VERSION = '0.1.0'

def set_options(opt):
  opt.tool_options('compiler_cxx')

def configure(conf):
  arch_flags = ['-arch', 'x86_64']
  
  conf.check_tool('compiler_cxx')
  conf.check_tool('node_addon')
  
  conf.env.append_value('CXXFLAGS', arch_flags)
  conf.env.append_value('CFLAGS', arch_flags)
  conf.env.append_value('LINKFLAGS', arch_flags)
  
  # conf.check_cfg(package='glew', args=['--cflags', '--libs'])

def build(bld):
  obj = bld.new_task_gen('cxx', 'shlib', 'node_addon')
  obj.target = "webgl"
  obj.cxxflags = ["-g", "-pthread", "-D_FILE_OFFSET_BITS=64", "-D_LARGEFILE_SOURCE","-fPIC", "-arch", "x86_64"]
  
  obj.linkflags = ["-lfreeimage"]
  obj.uselib = ["glew"]
  
  if sys.platform.startswith('darwin'):
    obj.framework = ['OpenGL']
  elif sys.platform.startswith('linux'):
    obj.uselib.append(["GL", "FREEIMAGE"])
    obj.linkflags.append(["-lXrandr","-lX11"])
  else:
    obj.linkflags.append(["-lGLESv2"])
  
  obj.source = bld.path.ant_glob('src/*.cc')
