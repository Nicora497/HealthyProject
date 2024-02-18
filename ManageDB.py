import sqlite3

#データベースを操作する関数をまとめたもの
class ManageDB():
    
    def __init__(self):
        self.__cleate_date_tabel()
    
    def __cleate_date_tabel(self):
        try:
            DatabaseConnection = sqlite3.connect('Health.db')
            Database = DatabaseConnection.cursor()
            Database.execute(f'''CREATE TABLE Stetus (
                                Date TEXT, 
                                Sleep_time INTEGER, 
                                Body_temp REAL, 
                                Exer_kind TEXT, 
                                Exer_time INTEGER,
                                Wight REAL,
                                BP_max INTEGER,
                                BP_min INTEGER)''')
            # Date : 日付 text
            # sleep_time : 睡眠時間 int
            # body_temp : 体温 float
            # exer_time : 運動時間 int
            # exer_kind : 運動の種類 text
            # wight : 体重 float
            # BP_max : 最高血圧 int
            # BP_min : 最低血圧 int
            DatabaseConnection.commit()
            DatabaseConnection.close()
        except sqlite3.OperationalError as e:
            print(e)
            
    def insert_or_updata_data(self, date,sleep_time, body_temp, exer_kind, exer_time, wight, BP_max, BP_min):
        #
        # データの追加と更新
        #
        # Date : (text) 日付
        # sleep_time : (int) 睡眠時間
        # body_temp : (float) 体温
        # exer_time : (int) 運動時間
        # exer_kind : (text) 運動の種類
        # wight : (float) 体重
        # BP_max : (int) 最高血圧 
        # BP_min : (int) 最低血圧 
        #

        try:
            DatabaseConnection = sqlite3.connect('Health.db')
            Database = DatabaseConnection.cursor()

            check = self.query_data(date)
            if len(check) == 0:
                print("new")
                #データを追加
                data = [(date,sleep_time, body_temp, exer_kind, exer_time, wight, BP_max, BP_min)]
            
                Database.executemany("INSERT INTO Stetus VALUES (?,?,?,?,?,?,?,?)",data)
                DatabaseConnection.commit()
                DatabaseConnection.close()
            else:
                print("re")
                #存在した場合データを更新
                data = [(sleep_time, body_temp, exer_kind, exer_time, wight, BP_max, BP_min,date)]
            
                Database.executemany('''UPDATE Stetus set 
                                     Sleep_time=?, 
                                     Body_temp=?, 
                                     Exer_kind=?, 
                                     Exer_time=?, 
                                     Wight=?, 
                                     BP_max=?, 
                                     BP_min=? 
                                     WHERE Date=?''',data)
                DatabaseConnection.commit()
                DatabaseConnection.close()
                
        except Exception as e:
            print("##########")
            print("place:insert_or_updata_data")
            print(type(e))
            print(e)
            print("##########")
            DatabaseConnection.close()
    
    def query_data(self, date, op=None):
        #
        # 日付を入れたらその日付のデータがすべて出てくる
        #
        # date : (str) 日付 "year/month/day"
        # query : (str) クエリ ""
        #
        try:
            DatabaseConnection = sqlite3.connect('Health.db')
            Database = DatabaseConnection.cursor()
            if op == None:
                Database.execute('''SELECT * FROM Stetus WHERE Date=?''',(date,))
            else :
                Database.execute(f"SELECT {op} FROM Stetus WHERE Date=?",(date,))
            # Database.execute('''SELECT * FROM Stetus''')
            
            data = Database.fetchall()
            
            DatabaseConnection.close()
            
            return data
        except Exception as e:
            print("##########")
            print("place:query_data")
            print(type(e))
            print(e)
            print("##########")
            DatabaseConnection.close()
            return []
        
        
if __name__ == '__main__':  
    manage = ManageDB()
    manage.insert_or_updata_data("2024/2/14", 15, 15.0, "mauru", 12, 15.0, 12, 40)
    data = manage.query_data("2024/2/14",op = "Sleep_time")
    print(data)