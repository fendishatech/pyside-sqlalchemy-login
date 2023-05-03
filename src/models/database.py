import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .user import Base

appdata_path = os.path.join(os.environ['APPDATA'], 'my_app')
os.makedirs(appdata_path, exist_ok=True)
db_path = os.path.join(appdata_path, 'my_app.db')

engine = create_engine(f'sqlite:///{db_path}')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()