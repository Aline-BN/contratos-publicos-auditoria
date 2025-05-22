import interface
import db

if __name__ == "__main__":
    try:
        interface.iniciar_interface()
    finally:
        db.fechar_conexao()