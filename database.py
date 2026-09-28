from os import makedirs
from sqlite3 import connect
from model import AppItemResponse
from typing import Generator

class Database:
    __table_name = 'apps'
    __item_id = 'item_id'
    __name = 'name'
    __icon_url = 'icon_url'
    __direct_url = 'direct_url'
    __description = 'description'
    def __init__(self):
        makedirs('db',exist_ok=True)
        self.db_path = 'db/more-apps.db'
        self.create_table()
    def create_table(self):
        conn = connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(f'''
        create table if not exists {self.__table_name}(
        {self.__item_id} integer primary key autoincrement,
        {self.__name} text not null,
        {self.__icon_url} text not null,
        {self.__direct_url} text not null,
        {self.__description} text)''')
        conn.commit()
        conn.close()
    def insert_app(self, name: str, icon_url: str, direct_url: str, description: str):
        conn = connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(f'''
        insert into {self.__table_name} 
        ({self.__name}, {self.__icon_url}, {self.__direct_url}, {self.__description}) values (?,?,?,?)''',
                       (name, icon_url, direct_url, description))
        conn.commit()
        conn.close()
    def update_app(self, item_id: int, name: str, icon_url: str, direct_url: str, description: str):
        conn = connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(f'''
        update {self.__table_name} 
        set {self.__name} = ?, {self.__icon_url} = ?, {self.__direct_url} = ?, {self.__description} = ? where {self.__item_id} = ?''',
                       (name, icon_url, direct_url, description, item_id))
        conn.commit()
        conn.close()
    def delete_app(self, item_id: int):
        conn = connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(f'''
        delete from {self.__table_name} where {self.__item_id} = ?''',(item_id,))
        conn.commit()
        conn.close()
    def get_apps(self) -> Generator[AppItemResponse, None, None]:
        conn = connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(f'''select * from {self.__table_name}''')
        for row in cursor:
            yield AppItemResponse(*row)
        conn.close()