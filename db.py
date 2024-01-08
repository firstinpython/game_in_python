import sqlite3


class Base:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cur = self.connection.cursor()

    def score(self,score):

        if int(self.cur.execute('SELECT score FROM play').fetchone()[0])< score:
            return 1
        else:
            return 2

    def update_user(self, name):
        with self.connection:
            return self.cur.execute('UPDATE `play`SET name==?', (name,))

    def update_score(self, score):
        with self.connection:
            if self.score(score)==1:
                return self.cur.execute('UPDATE play SET score== ? WHERE name==?', (score, 'player'))

    def money(self, money):
        with self.connection:
            mon = int(self.cur.execute('SELECT money FROM play').fetchone()[0])
            mon += money
            return self.cur.execute('UPDATE play SET money== ? WHERE name==?', (mon, 'player'))

    def buy(self,skin):
        with self.connection:
            if int(self.cur.execute(f'SELECT {skin} FROM play').fetchone()[0]) == 0:
                if int(self.cur.execute('SELECT money FROM play').fetchone()[0]) >= 100:
                    money1 = int(self.cur.execute('SELECT money FROM play').fetchone()[0])
                    money1 -= 100
                    self.cur.execute('UPDATE play SET money== ? WHERE name==?', (money1, 'player'))
                    self.cur.execute(f'UPDATE play SET {skin}== ? WHERE name==?', (1, 'player'))
                    return 1
                else:
                    return 2
            else:
                return 3

    def skins(self,skin,skin1):
        with self.connection:
            if int(self.cur.execute(f'SELECT {skin} FROM play').fetchone()[0]) == 1:
                return [self.cur.execute(f'UPDATE play SET {skin}== ? WHERE name==?', (2, 'player')),self.cur.execute(f'UPDATE play SET {skin1}== ? WHERE name==?', (1, 'player'))]



    def proverka(self,knight_image,knight_image2,knight_image3,knight_image4,knight_image5):
        with self.connection:
            if int(self.cur.execute('SELECT skin_1 FROM play').fetchone()[0]) == 2:
                return 'skin_1',knight_image
            elif int(self.cur.execute('SELECT skin_2 FROM play').fetchone()[0]) == 2:
                return 'skin_2',knight_image2
            elif int(self.cur.execute('SELECT skin_3 FROM play').fetchone()[0]) == 2:
                return 'skin_3',knight_image3
            elif int(self.cur.execute('SELECT skin_4 FROM play').fetchone()[0]) == 2:
                return 'skin_4',knight_image4
            elif int(self.cur.execute('SELECT skin_5 FROM play').fetchone()[0]) == 2:
                return 'skin_5',knight_image5