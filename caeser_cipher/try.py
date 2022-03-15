import mysql.connector
import time
import prettytable

class dbOperations():
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",  # password
            database="Dictionary"
        )
        self.myCursor = self.mydb.cursor(buffered=True)


    def ınsertData(self): # for adding new word
        try:
            numbers = [1,2,3,4,5,6,7,8,9,0]
            self.word = input("❓- What is the word?: ")
            self.meaning = input("❓- What is the meaning?: ")
            print("")

            if self.word != "" and self.meaning != "":
                sql = "INSERT INTO wordList (word, meaning) VALUES (%s, %s)"
                value = (self.word, self.meaning)
                self.myCursor.execute(sql, value)
                self.mydb.commit()
                print("✅ The word you requested has been added.")

            elif self.word == "" and self.meaning == "":
                print("     ❗️❗️❗️ Word and Meaning can not be empty.")

            elif self.word == "":
                print("     ❗️❗️❗️ Word can not be empty.")

            elif self.meaning == "":
                print("     ❗️❗️❗️ Meaning can not be empty.")

            elif self.word in numbers:
                print("     ❗️❗️❗️ Word can not be a number.")

        except:
            pass
        


    def deleteData(self): # for deleting word
        try:
            word = input("❓- Which word do you want to delete? just enter word:")
            if  word == "":
                print("❗️❗️❗️ Word can not be empty.")

            else:
                whsql = f"SELECT * FROM wordList WHERE word = '{word}' "
                self.myCursor.execute(whsql)
                myResult = self.myCursor.fetchone()

                if word == myResult[1]:
                    sql = "DELETE FROM wordList WHERE word = %s"
                    value = (word,)
                    self.myCursor.execute(sql, value)
                    self.mydb.commit()
                    print("✅ The word you requested has been deleted.")

        except TypeError:
            print("❗️❗️❗️ Sory!, I didn't found the word in the database. Please check.")
        


    def getDatabase(self): # for getting all words
        try:
            sql = "SELECT * FROM wordList"
            self.myCursor.execute(sql)
            myresult = self.myCursor.fetchall()
            idListe = []
            wordListe = []
            meaningListe = []
            for x in myresult:
                idListe.append(x[0])
                wordListe.append(x[1])
                meaningListe.append(x[2])

            table = prettytable.PrettyTable(["id", "word", "meaning"])
            for i in range(len(idListe)):
                table.add_row([idListe[i], wordListe[i], meaningListe[i]])
            print(table)
        except:
            pass

        

    def updateMeaning(self): # for updating meaning
        try:
            b = False
            while b == False:
                self.meaning = input("❓- Enter the Meaning?: ")

                sql = "SELECT * FROM wordList"
                self.myCursor.execute(sql)
                myresult = self.myCursor.fetchall()
                liste = []
                for x in myresult:
                    liste.append(x[2])

                if self.meaning == "" or self.meaning not in liste:
                    print("❗️❗️❗️ Sorry I didn't found the meaning in the database.")
                    
                if self.meaning != "" or self.meaning  in liste:
                    if self.detectSameMeaning() == 1:
                        self.newMeaning = input("❓- What is the new meaning?: ")
                        if self.newMeaning == "":
                            print("❗️❗️❗️ New meaning can not be empty.")

                        else:
                            sql = f"UPDATE wordList SET meaning = '{self.newMeaning}' WHERE meaning = '{self.meaning}'"
                            self.myCursor.execute(sql)
                            self.mydb.commit()
                            print("✅ The meaning you requested has been updated.")
                            b = True    

                    elif self.detectSameMeaning() > 1:
                        sql = f"SELECT * FROM wordList WHERE meaning = '{self.meaning}'"
                        self.myCursor.execute(sql)
                        myResult = self.myCursor.fetchall()
                        print("❗️❗️❗️ I found several words with the same meaning in the database.")
                        idListe = []
                        wordListe = []
                        meaningListe = []
                        for i in myResult:
                            idListe.append(i[0])
                            wordListe.append(i[1])
                            meaningListe.append(i[2])
                        
                        table = prettytable.PrettyTable(["id", "word", "meaning"])
                        for i in range(len(idListe)):
                            table.add_row([idListe[i], wordListe[i], meaningListe[i]])
                        print(table)
                        time.sleep(0.2)
                        self.arrangeByİdForMeaning()
                        b = True
                    
        except ValueError:
            print("❗️❗️❗️ id can not be empty.")
            
    
    def detectSameMeaning(self): # The function I use in updateMeaning
        # self.meaning = input("❓- Enter the Meaning?: ")
        sql = f"SELECT * FROM wordlist WHERE meaning= '{self.meaning}'"
        self.myCursor.execute(sql)
        self.myResult = self.myCursor.fetchall()
        # # print(len(myResult))
        return len(self.myResult)
        

    def arrangeByİdForMeaning(self): # The function I use in updateMeaning
        self.detectSameMeaning()
        self.iç = [i[0] for i in self.myResult]
     
        a = False
        while a == False:
            self.id = int(input("❓- Which word do you want to update? Please enter id: "))
            if self.id == "":
                print("❗️❗️❗️ İd can not be empty.")

            if self.id != "":

                if self.id in self.iç:
                    id = f"SELECT * FROM wordList WHERE id = '{self.id}'"
                    self.myCursor.execute(id)
                    myResult = self.myCursor.fetchall()
                    for i in myResult:
                        print(i)

                    self.newMeaning = input("❓- Enter the new meaning?: ")

                    if self.newMeaning == "":
                        print("❗️❗️❗️ New meaning can not be empty.")

                    if self.newMeaning != "":
                        sql = f"UPDATE wordList SET meaning = '{self.newMeaning}' WHERE id = '{self.id}'"
                        self.myCursor.execute(sql)
                        self.mydb.commit()
                        print("✅ The meaning you requested has been updated.")
                        a = True

            if not self.id in self.iç:
                print("❗️❗️❗️ The id you entered is not in the database.")



    def updateWord(self): # for updating word
        try:
            b = False
            while b == False:
                self.word = input("❓- Enter the word?: ")

                sql = "SELECT * FROM wordList"
                self.myCursor.execute(sql)
                myresult = self.myCursor.fetchall()
                liste = []
                for x in myresult:
                    liste.append(x[1])


                if self.word == "" or self.word not in liste:
                    print("❗️❗️❗️ word can not be empty and must be in the database.")
                    

                if self.word != "" or self.word in liste:
                    if self.detectSameWord() == 1:
                        self.newWord = input("❓- What is the new word?: ")
                        if self.newWord == "":
                            print("❗️❗️❗️ New word can not be empty.")

                        else:
                            sql = f"UPDATE wordList SET word = '{self.newWord}' WHERE word = '{self.word}'"
                            self.myCursor.execute(sql)
                            self.mydb.commit()
                            print("✅ The word you requested has been updated.")
                            b = True    

                    elif self.detectSameWord() > 1:
                        sql = f"SELECT * FROM wordList WHERE word = '{self.word}'"
                        self.myCursor.execute(sql)
                        myResult = self.myCursor.fetchall()
                        print("❗️❗️❗️ I found several words with the same word in the database.")
                        idListe = []
                        wordListe = []
                        meaningListe = []
                        for i in myResult:
                            idListe.append(i[0])
                            wordListe.append(i[1])
                            meaningListe.append(i[2])
                        
                        table = prettytable.PrettyTable(["id", "word", "meaning"])
                        for i in range(len(idListe)):
                            table.add_row([idListe[i], wordListe[i], meaningListe[i]])
                        print(table)
                        time.sleep(0.2)
                        self.arrangeByİdForWord()
                        b = True






            # idListe = []
            # wordListe = []
            # meaningListe = []
            # for x in myresult:
            #     idListe.append(x[0])
            #     wordListe.append(x[1])
            #     meaningListe.append(x[2])

            # table = prettytable.PrettyTable(["id", "word", "meaning"])
            # for i in range(len(idListe)):
            #     table.add_row([idListe[i], wordListe[i], meaningListe[i]])
            # print(table)
                    
        except ValueError:
            print("❗️❗️❗️ word can not be empty.")




    def detectSameWord(self): # The function I use in updateWord
        # self.word = input("❓- Enter the word?: ")
        sql = f"SELECT * FROM wordlist WHERE word= '{self.word}'"
        self.myCursor.execute(sql)
        self.myResult = self.myCursor.fetchall()
        # # print(len(myResult))
        return len(self.myResult)
        

    def arrangeByİdForWord(self): # The function I use in updateWord
        self.detectSameWord()
        self.iç = [i[0] for i in self.myResult]
     
        a = False
        while a == False:
            self.id = int(input("❓- Which word do you want to update? Please enter id: "))
            if self.id == "":
                print("❗️❗️❗️ İd can not be empty.")

            if self.id != "":

                if self.id in self.iç:
                    id = f"SELECT * FROM wordList WHERE id = '{self.id}'"
                    self.myCursor.execute(id)
                    myResult = self.myCursor.fetchall()
                    for i in myResult:
                        print(i)

                    self.newWord = input("❓- Enter the new word?: ")

                    if self.newWord == "":
                        print("❗️❗️❗️ New word can not be empty.")

                    if self.newWord != "":
                        sql = f"UPDATE wordList SET word = '{self.newWord}' WHERE id = '{self.id}'"
                        self.myCursor.execute(sql)
                        self.mydb.commit()
                        print("✅ The word you requested has been updated.")
                        a = True

            if not self.id in self.iç:
                print("❗️❗️❗️ The id you entered is not in the database.")



    def exit(self): # for exiting the program
        print("Bye!, I hopefully see you again soon.👋")
        self.mydb.close()




print("""
<<< ---- Welcome dictionary V1 ---- >>>

Just enter a number.
⬇             
1 - Show word list
2 - Add word and meaning
3 - Delete data
4 - Update word
5 - Update meaning
6 - exit
""")

while True:
    print("")
    procesChoose = input("?- What is your Choose ↣↣↣ ")
    print(" ")
    # show word list
    if procesChoose == "1":
        print("")
        dbOperations().getDatabase()
        print("")


    #Add word and meaning
    elif procesChoose == "2":
        dbOperations().ınsertData()

    #Delete word
    elif procesChoose == "3":
        dbOperations().deleteData()

    #Update word
    elif procesChoose == "4":
        dbOperations().updateWord()

    #Update meaning
    elif procesChoose == "5":
        dbOperations().updateMeaning()

    elif procesChoose == "6":
        dbOperations().exit()
        break

    else:
        print("❗️❗️❗️ Please enter a number between 1 and 6.")
        
    
 






       
    
    




