import mysql.connector

# Initialisation de la connexion
cnx = mysql.connector.connect(user=' ', password=' ', host=' ', database=' ')
cursor = cnx.cursor()

# Insertion
cmd = ("INSERT .....")
cursor.execute(cmd)
cnx.commit()

# Sélection
cmd = ("SELECT attribut1, .....")
cursor.execute(cmd)
for (attribut1, ....) in cursor:
    print attribut1

# Fermeture de la connexion
cursor.close()
cnx.close()



# see :
# https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
# https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html
# API : https://dev.mysql.com/doc/connector-python/en/connector-python-reference.html

# projet d'API pour cluster trouvée sur github : https://github.com/Pyplate/db-cluster-utils
# on peut trouver des idées là-dessus
