import sqlalchemy as sa
from sqlalchemy.exc import IntegrityError

engine = sa.create_engine("sqlite:///sqlite.db")
metadata = sa.MetaData()


user_table = sa.Table(
    "user", 
    metadata, 
    sa.Column("id", sa.Integer, primary_key=True), 
    sa.Column("username", sa.String), 
    sa.Column("email", sa.String), 
    sa.Column("password", sa.String), 
    sa.Column("sessionid", sa.String, nullable=True, default=None), 
)


def InsertUser(username: str, email: str, password: str) -> None:
    with engine.connect() as connection: 
        try: 
            query = user_table.insert().values(username = username, email= email, password = password)
            connection.execute(query)
            connection.commit()
            return {
            "method": "POST", 
            "status": "Success",
            "message": f"User {username} created successfully!",
            }
                
        except IntegrityError: 
            return {
                "method": "POST",
                "status": "Failed",
                "message": "User already exists!",
            }
            
        except Exception: 
            return{
                "method": "POST", 
                "status": "Failed",
                "message": "Unknown error occured!"
            }
        
     
def SelectUser(email: str) -> tuple | None:
    with engine.connect() as connection:  
        query = sa.select().where(user_table.c.email == email)
        result = connection.execute(query)
        return result.mappings().fetchone()

def CheckUser(email: str) -> tuple |None: 
    with engine.connect() as connection: 
        query = sa.select(sa.exists().where(user_table.c.email == email))   
        result = connection.execute(query).scalar()
        return result

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
    metadata.drop_all(engine) 
    metadata.create_all(engine)
    
    # This is how a user is Inserted: 
    #InsertUser("Rijan", "rijangautam07@gmail.com")
    
    # This select a particular user with their id: 
    #print(SelectUser(1))
    
    # This removes all the users. 
    # for i in range(1,6): 
    #     RemoveUser(i)
        
    # Ths GETs all the users(rows in user_table) in the db
    InsertUser("Rijan", "rijangautam07@gmail.com", "fdadfeisdfn342kfsadfer")
    print(GetAllUsers())
    print(SelectUser("rijangautam07@gmail.com"))
    


if __name__ == "__main__": 
    main()



