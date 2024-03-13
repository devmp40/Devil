import platform
bit = platform.architecture()[0]
if "32bit" in bit:
  try:
    import devil32
  except Exception as error:
    print(error)
elif "64bit" in bit:
  try:
    import devil64
  except Exception as error:
    print(error)
else:
  print(" Your device can't support this tool ")
