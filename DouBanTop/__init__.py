# import sqlite3
#
# # 数据持久化-数据库初始化
# con = sqlite3.connect('.\Data\DouBan.db')
# cursor = con.cursor()
# cursor.execute('create table DouBanInfo(id  INTEGER PRIMARY KEY AUTOINCREMENT,MovieName varchar(50),MovieInfo varchar(255) ,Star varchar(8),Quote varchar(200))')
# cursor.close()