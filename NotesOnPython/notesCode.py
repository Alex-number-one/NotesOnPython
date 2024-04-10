import os
import datetime
class Note:
      def __init__(self, id, header, txt):
         self.id = id
         self.header = header
         self.txt = txt
      def createANote (self):
         f = open ('notes.txt', mode='a', encoding='utf-8')
         f.write(f"{self.id} {datetime.date.today()} {self.header} {self.txt} {'\n'}")
         f.close()
id = input('Write an id')
header = input('Write a header')
text = input('Write a txt')
Note1 = Note(id, header, text)
Note1.createANote()

         