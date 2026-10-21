from database import Base, engine, SessionLocal
from models import Usuario, Livro

Base.metadata.create_all(engine)

session = SessionLocal()

maria = Usuario(nome="Maria")
session.add(maria)
session.commit()

livro = Livro(titulo="Dom Casmurro", usuario=maria)
session.add(livro)
session.commit()

print("Usuário:", maria.nome)
print("Livro:", maria.livros[0].titulo)

session.close()