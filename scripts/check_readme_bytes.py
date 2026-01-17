b = open('README.md','rb').read()
print('len', len(b))
print('has_nul', b.find(b'\x00') != -1)
print('repr tail:', repr(b[-256:]))
# print individual last bytes for quick inspection
print('last bytes:', list(b[-64:]))
