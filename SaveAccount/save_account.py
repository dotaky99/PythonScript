import sqlite3

def DataTxt(fileName, cur):
    print(f'Hi, {fileName}')
    with open(fileName, encoding='utf8') as f:
        for line in f.readlines():
            cur.execute('INSERT INTO account VALUES(?)', [line])

if __name__ == '__main__':
    fileName = str(input("파일을 드래그 앤 드롭하세요: \n"))
    conn = sqlite3.connect("password.db")
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS account(pass TEXT)')

    if fileName.endswith('.txt'):
        DataTxt(fileName, cur)

    conn.commit()
    conn.close()
    input("Press enter to exit ;)")