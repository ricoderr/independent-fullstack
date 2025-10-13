import sqlalchemy as sa 

engine = sa.create_engine("sqlite:///sqlite.db")
metadata = sa.MetaData()


user_table = sa.Table(
    "user", 
    metadata, 
    sa.Column("id", sa.Integer, primary_key=True), 
    sa.Column("username", sa.String), 
    sa.Column("email", sa.String), 
)


def InsertUser(username: str, email: str) -> None:
    with engine.connect() as connection: 
        query = user_table.insert().values(username = username, email= email)
        connection.execute(query)
        connection.commit()
        
     
def SelectUser(id: int) -> tuple | None:
    with engine.connect() as connection:  
        query = user_table.select().where(user_table.c.id == id)
        result = connection.execute(query)
        return result.mappings().fetchone()
    
    
def GetAllUsers() -> list[dict]:
    with engine.connect() as connection:
        query = user_table.select() 
        result = connection.execute(query)
        return result.mappings().all() 

def RemoveUser(id: int) -> None : 
    with engine.connect() as connection: 
        query = user_table.delete().where(user_table.c.id == id)
        connection.execute(query)
        connection.commit()
    
def main() -> None: 
    # This create the db or updates if it is already present. 
    #------> metadata.create_all(engine)
    
    # This is how a user is Inserted: 
    #------> InsertUser("Rijan", "rijangautam07@gmail.com")
    
    # This select a particular user with their id: 
    #------> print(SelectUser(1))
    
    # Ths GETs all the users(rows in user_table) in the db
    print(GetAllUsers())
    


if __name__ == "__main__": 
    main()



