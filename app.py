import mysql.connector
import webbrowser


conn = mysql.connector.connect(user='visie_user', password='visie_pass',
                              host='db4free.net',database='visie_db')

# Descomenta a linha abaixo para verificar as colunas da tabela
# select_data = "DESCRIBE pessoas"

# Comente da linha 13 à linha 16 para descomentar e verificar a linha 10
select_data = """
    SELECT nome, DATE_FORMAT(data_admissao,'%d/%m/%Y')
    FROM pessoas

"""

cursor = conn.cursor()
cursor.execute(select_data)
result = cursor.fetchall()

p = []

tbl = '''<table>
            <tr>
                <td>Nome</td>
                <td>Admissão</td>
            </tr>
        </table>
'''

for row in result:
    a = "<tr><td>%s</td>"%row[0]
    p.append(a)
    b = "<td>%s <a href= >Remover</a></td>"%row[1]
    p.append(b)
    
contents = '''
<!DOCTYPE html>
<html>
<head>
<meta content="text/html; charset=UTF-8" http-equiv="content-type">
<link rel="stylesheet" href="app.css" type="text/css">
<title>Visie Python</title>
</head>
<body>
<table class="table">
%s
</table>
<div class="form">
<form action="/action_page.php">
  <label for="fname">Nome:</label><br>
  <input type="text" id="fname" name="fname" value="John"><br>
  <label for="lname">RG:</label><br>
  <input type="text" id="lname" name="lname" value="123"><br>
  <label for="lname">CPF:</label><br>
  <input type="text" id="lname" name="lname" value="123456"><br><br>
  <input type="submit" value="Salvar">
</form>
</div>
</body>
</html>
'''%(p)

filename = 'webbrowser.html'

def main(contents, filename):
    output = open(filename,"w")
    output.write(contents)
    output.close()

main(contents, filename)    
webbrowser.open(filename)

if(conn.is_connected()):
    cursor.close()
    conn.close()
    print("MySQL connection is closed.") 