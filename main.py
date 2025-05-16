import qtools.qstr as qstr

version = 1.0
suuid = qstr.generate_short_uuid()
print(f"test, version {version}")
print(f"the suuid is {suuid}")