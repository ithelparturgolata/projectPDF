# import os
# import glob
#
# # path
# path = r'/Users/arturgolata/Desktop/Programowanie/pythonProjects/projectPDF/Output'
# path_name = r'Users/arturgolata/Desktop/Programowanie/pythonProjects/projectPDF/Output/*.pdf'
# # set counter
# counter = 1
#
# for f in glob.glob(path_name, recursive=True):
# 	# print(f)
# 	new = "2316_" + str(counter).zfill(5) + ".pdf"
# 	dst = os.path.join(path, new)
# 	os.rename(f, dst)
# 	counter += 1

import os
from glob import glob

os.chdir('/Users/arturgolata/Desktop/Programowanie/pythonProjects/projectPDF/Output')
print(os.getcwd())

for count, f in enumerate(os.listdir()):
	f_name, f_ext = os.path.splitext(f)
	f_name = "2316" + str(count).zfill(5)

	new_name = f'{f_name}{f_ext}'
	os.rename(f, new_name)