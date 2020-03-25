flags = [
    '-x',
    'c',
    '-DDPDK_NETDEV',
    '-L/root/hhb/dpdk-next-net/x86_64-native-linuxapp-gcc/lib',
    '-Wall',
    '-Wextra',
    '-Wno-sign-compare',
    '-Wpointer-arith',
    '-Wformat',
    '-Wformat-security',
    '-Wswitch-enum',
    '-Wunused-parameter',
    '-Wbad-function-cast',
    '-Wcast-align',
    '-Wstrict-prototypes',
    '-Wold-style-definition',
    '-Wmissing-prototypes',
    '-Wmissing-field-initializers',
    '-fno-strict-aliasing',
    '-Wshadow',
    '-I.',
    '-I', './include',
    '-I', './lib',
    '-I', '/root/hhb/dpdk-next-net/x86_64-native-linuxapp-gcc/include',
]

def Settings( **kwargs ):
  return {
    'flags': flags,
  }
