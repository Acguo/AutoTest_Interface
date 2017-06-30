import re
import config
# ss = 'E:/OtherFile/AG_SlotFRU_501(101).png'
# s = picname = re.findall('E:/OtherFile/(.*)', ss, re.S)
# print(s[0])

src = config.get_config("upload", "src")
savefile = config.get_config("upload", "savefile")
savename = re.findall('E:/OtherFile/(.*)', src, re.S)[0]
idfile = savefile + savename + '.csv'


print(idfile)