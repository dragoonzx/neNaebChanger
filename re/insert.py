import sqlite3
import time


db = sqlite3.connect('db/main.db')

with db:
	db.execute("INSERT INTO reviews (id, name, cont, time) VALUES (26, 'Имран', 'Нашёл этот обменник, так как тут была самая низкая коммисия. Обменял, перевели не так уж быстро, всё заняло часа два.', (?))", (time.time(),))
	db.execute("INSERT INTO reviews (id, name, cont, time) VALUES (27, 'олололл', 'Обменяли норм', (?))", (time.time(),))
	db.execute("INSERT INTO reviews (id, name, cont, time) VALUES (28, 'александр', 'можно было бы и побыстрее', (?))", (time.time(),))

# db.execute("INSERT INTO news (id, cont, time) VALUES (28, 'Александр', 'Заебись обменник', (?))", (time.time(),)c