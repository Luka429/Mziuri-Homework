#სავარჯიშო 1

class People:
    def __init__(self,fistname,lastname):
        self.firstname = fistname
        self.lastname = lastname

    def get_email(self):
        return f'{self.firstname}.{self.lastname}.uni@btu.edu.ge'

class Student(People):
    def __init__(self,firstname,lastname,courses):
        super().__init__(firstname,lastname)
        self.courses = courses

    def get_email(self):
        return f'{self.firstname}.{self.lastname}.1@btu.edu.ge'

class Lecturer(People):
    def __init__(self, firstname, lastname, salary):
        super().__init__(firstname, lastname)
        self.salary = salary

    def get_email(self):
        return f'{self.firstname}.{self.lastname}@btu.edu.ge'

person1 = People('dimitri','mcariashvili')
print(person1.get_email())

person2 = Lecturer('zura','white',60000)
print(person2.get_email())

person3 = Student('givi','xmaladze','python')
print(person3.get_email())


#სავარჯიშო 2


class LibraryItem:
    def __init__(self,title,subject,status):
        self.title = title
        self.subject = subject
        self.status = status

    def booking(self):
        if self.status == 'Available':
            self.status = 'Occupied'
            return 'You have booked a Library item'
        else:
            return 'The Library item is currently occupied'

class Book(LibraryItem):
    def __init__(self,title,subject,status,ISBN,authors):
        super().__init__(title,subject,status)
        self.ISBN = ISBN
        self.authors = authors

    def booking(self):
        if self.status == 'Available':
            self.status = 'Occupied'
            return 'You have booked a book'
        else:
            return 'The book is currently occupied'

class Magazine(LibraryItem):
    def __init__(self,JournalName,volume,status):
        super().__init__(None,None,status)
        self.JournalName = JournalName
        self.status = status

    def booking(self):
        if self.status == 'Available':
            self.status = 'Occupied'
            return 'You have booked a magazine'
        else:
            return 'The magazine is currently occupied'

class CD(LibraryItem):
    def __init__(self,title,status):
        super().__init__(title,None,status)
    def booking(self):
        return "it's not possible to book a CD"

#სავარჯიშო 3

class Contacts:
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone

class MailSender:
    def send_mail(self):
        return "თქვენი მეილი გაიგზავნა ამ მისამართზე:giorgi.giorgadze@gmail.com."


class Friend(Contacts,MailSender):
    def __init__(self,name,phone,email):
        super().__init__(name,phone)
        self.email = email

class Family(Contacts,MailSender):
    def __init__(self,name,phone,email,birthday):
        super().__init__(name,phone)
        self.email = email
        self.birthday = birthday

#სავარჯიშო 4

class Doctoral_Student(Student,Lecturer):
    def __init__(self,firstname,lastname,courses,salary):
        self.firstname = firstname
        self.lastname = lastname
        self.courses = courses
        self.salary = salary


    def get_email(self):
        return f'student mail -> {self.firstname}.{self.lastname}.1@btu.edu.ge', f'lector mail ->{self.firstname}.{self.lastname}@btu.edu.ge'

p1 = Doctoral_Student("giorgi","oqtagonashvili",10000,'c++')
print(p1.get_email())


















