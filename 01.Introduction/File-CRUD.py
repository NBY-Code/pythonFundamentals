#exam_grades.txt dosyasını yaratın
def create_exam_grades()->None:
    file=open(file='exam_grades.txt',mode='w',encoding='utf-8')
    file.close()


#Kullanıcıdan first_name, last_name,midterm,final homework bilgilerini alarak Exam_grades Doayasına yazalım
#aşağıdaki farmatta yazalım
#ad soyad:not1,not2,not3
#ilgili dosyayı withopen() kullanarak açalım

def take_information(first_name:str,last_name:str,midterm:float,final:float,homework:float):
    with open('exam_grades.txt', mode='a', encoding='utf-8') as file:
        file.write(f'{first_name} {last_name} : {midterm},{final},{homework}\n')



# row example => ad soyad : 30:30:30
#harf notunu hesapla ve return ett
def calculate_grade(row:str)->str:
    values=row.split(':')
    full_name=values[0]
    grades_list=values[1].split(',')
    ort=float(grades_list[0])*0.3+float(grades_list[1])*0.6+float(grades_list[2])*0.1
    if 90 <= ort <= 100:
        return f'{full_name}: AA'
    elif 85 <= ort <= 89:
        return f'{full_name}: BA'
    elif 80 <= ort <= 84:
        return f'{full_name}: BB'
    elif 75 <= ort <= 79:
        return f'{full_name}: CB'
    elif 70 <= ort <= 74:
        return f'{full_name}: CC'
    elif 65 <= ort <= 69:
        return f'{full_name}: CD'
    elif 60 <= ort <= 64:
        return f'{full_name}: DD'
    elif 55 <= ort <= 59:
        return f'{full_name}: DC'
    elif 50 <= ort <= 54:
        return f'{full_name}: FD'
    else:
        return f'{full_name}: FF'



#exam_grade.txt dosyasından verileri satır satır okuyalım
#harf notlarını hesaplatalım ve bir listeye ekleyelim
#ilgili listeyi return
def read_exam_grades()->list:
    lst=[]
    with open('exam_grades.txt', mode='r', encoding='utf-8') as file:
        for row in file:
            grade=calculate_grade(row)
            lst.append(grade)
    return lst


#result.txt isimli dosyaya öğrencilerin isim soyisim : harf notunu yazdıralım
def register_grade(grades_list:list)->None:
    with open(file='result.txt',mode='w',encoding='utf-8')as file:
        for item in grades_list:
            file.write(item + "\n")


#result.txt dosyasını verilerini ekrana yaz
def read_result():
    with open(file='result.txt',mode='r',encoding='utf-8')as file:
        for row in file:
            print(row)

def menu():
    print(f"""
    Menu
    ------------
    Read Grades         ==> 1
    Enter Grades        ==> 2
    Calculate Result    ==> 3
    Display Grades         ==> 4
    """)
def main():
    menu()
    while True:
        process = input("Please choose a transaction : ")
        match process:
            case '1':
                read_exam_grades()
                print('Grades hass been read')
            case '2':
                take_information(
                    input('First Name :'),
                    input('Last Name :'),
                    float(input('Midterm :')),
                    float(input('Final :')),
                    float(input('Homeword :'))

                )
                print("Grades hass benn created")
            case '3':
                result=read_exam_grades()
                register_grade(result)
                print('Grades have ben calculated and stored .. ')
            case '4':
                read_result()
            case 'e':
                print('Application hass been closing..!')
            case _:
                print('Please choose a valid tansaction no..!')
                pass
main()