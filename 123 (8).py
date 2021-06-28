from googletrans import Translator
import time

trans = Translator()
n = 0


En_f = open('movie_lines.txt', 'r')
Ru_f = open('RU_dialog.txt', 'a', encoding='utf-8')

for line in En_f:

	count = 0
	l1 = ""
	l = line.split()
	l.reverse()

	for i in l:
		if i != "+++$+++":
			l1 = i + ' ' + l1
			count += 1
		else: break

	l.reverse()

	for i in range(count):
		l.pop()

	print(n, l1)

	flag = False

	while not flag:
		try:
			t = trans.translate(l1, src = 'auto', dest = 'ru')
			flag = True
		except AttributeError:
			time.sleep(1)
			flag = False
		except TypeError:
			break

	Ru_f.write(' '.join(l) + " " + t.text + '\n')
	n += 1

print("finish")

#539, 5637

#### 3872 4006 ####
