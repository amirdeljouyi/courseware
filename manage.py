from website import db, app
from flask_script import Manager
from website.models import Student, Professor
from website.mod_course.models import Course, Slide
from website.mod_news.models import Post, Category 
from website.mod_auth.models import User, Authority , authorities_users
from werkzeug.security import check_password_hash, generate_password_hash

manager = Manager(app)
student = Student(
    year_of_enter=1393,
    field_of_study="Software Engineering",
    degree="undergraduate"
)
amir = User(
    first_name="amir",
    last_name="deljouyi",
    username="amir.deljouyi",
    password_hash=generate_password_hash("123456"),
    img_url="avatar.jpg",
    student=student
)


def buildUsers():
    authorityProfessor = Authority(
        name="Professor"
    )
    authorityStudent = Authority(
        name="Student"
    )
    authorityAdmin = Authority(
        name="Admin"
    )
    amir.authorities.append(authorityAdmin)
    amir.authorities.append(authorityStudent)
    db.session.add(amir)
    db.session.add(student)

    professor = Professor(
        field_of_study="network",
        degree="PhD",
        level="professor",
    )
    u = User(
        first_name="Andrew",
        last_name="Tanenbaum",
        username="andrew.tanenbuam",
        img_url="Andrew_S._Tanenbaum.jpg",
        password_hash=generate_password_hash("123456"),
        professor=professor
    )
    db.session.add(u)
    db.session.add(professor)

    professor = Professor(
        field_of_study="NLP",
        degree="PhD",
        level="Professor",
    )
    u = User(
        first_name="Dan",
        last_name="Jurafsky",
        username="dan.jurafsky",
        img_url="dan_jurafsky.jpg",
        password_hash=generate_password_hash("123456"),
        professor=professor
    )
    db.session.add(u)
    db.session.add(professor)

    professor = Professor(
        field_of_study="Security",
        degree="Bachelor"
    )
    u = User(
        first_name="Edward",
        last_name="Snowden",
        username="edward.snowden",
        password_hash=generate_password_hash("123456"),
        img_url="Edward_Snowden.jpg",
        professor=professor
    )
    db.session.add(u)
    db.session.add(professor)

    professor = Professor(
        field_of_study="Operating Systems",
    )
    u = User(
        first_name="Linus",
        last_name="Torvalds",
        username="linus.torvalds",
        password_hash=generate_password_hash("123456"),
        img_url="Linus_Torvalds.jpg",
        professor=professor
    )
    db.session.add(u)
    db.session.add(professor)

    professor = Professor(
        field_of_study="Opensource"
    )
    u = User(
        first_name="Richard",
        last_name="Stallman",
        username="richard.stallman",
        password_hash=generate_password_hash("123456"),
        professor=professor,
        img_url="Richard_Stallman.jpg"
    )
    db.session.add(u)
    db.session.add(professor)

    professor = Professor(
        field_of_study="Compiler",
        degree="PhD",
        level="Professor",
    )
    u = User(
        first_name="noam",
        last_name="Chomsky",
        username="noam.chomsky",
        password_hash=generate_password_hash("123456"),
        professor=professor,
        img_url="Noam_Chomsky.jpg"
    )
    db.session.add(u)
    db.session.add(professor)

    professor = Professor(
        field_of_study="system reliability",
        degree="PhD",
        level="Associate Professor",
    )
    u = User(
        first_name="Bianca",
        last_name="Schroeder",
        username="bianca.schroeder",
        password_hash=generate_password_hash("123456"),
        professor=professor,
        img_url="bianca_schroeder.jpg"
    )
    db.session.add(u)
    db.session.add(professor)

    db.session.commit()


machineLearning = Course(
        title="Machine Learning",
        about="Learn Evoloution Algoritms , Genetic and more",
        degree="bachelor",
        homework="Exercise 2",
        resources="Machine Learning from amir",
        syllabus="From molecular genetics to sustainable urban infrastructure – global security in the age of cyber-espionage to music composition, our internationally renowned teachers and researchers are leaders in their fields."
    )

def buildCourse():
    sOne = Slide(
        name="Quantum algorithms for supervised and unsupervised machine learning",
        url="1307.0411.pdf",
        course=machineLearning
    )

    sTwo = Slide(
        name="Pattern Recognition",
        url="Pattern Recognition.pdf",
        course=machineLearning
    )

    db.session.add_all([sOne, sTwo])
    db.session.add(machineLearning)

    c = Course(
        title="Automata theory",
        about="Automata theory is the study of abstract machines and automata, as well as the computational problems that can be solved using them",
        degree="bachelor"
    )

    db.session.add(c)
    db.session.commit()


def buildPosts():

    it = Category(
        name="it"
    )

    sport = Category(
        name="sport"
    )

    science = Category(
        name="science"
    )

    culture = Category(
        name="culture"
    )

    course = Category(
        name="course"
    )

    db.session.add_all([it, sport, culture, science,course])

    p = Post(
        title="Panel Discussion on Big Data and Artificial Intelligence in Healthcare",
        user=amir,
        content_mini="For those who register to attend all four Health IT Sessions you may be eligible for a certificate of completion.",
        content="Aaron Berk is a Partner in KPMG’s Digital Health practice. He has 20 years of experience as a clinician, hospital manager and consultant. Aaron has led provincial projects related to Analytics, wait-time management, cancer care, peri-operative practice, critical care, and population health initiatives. Aaron has also provided strategic advice to governments, agencies and health regions on integration of virtual care to improve the integrated delivery of healthcare services. Aaron is a member of the Masters in eHealth program advisory committee for McMaster University and holds an appointment at U of T's institute of Health Policy, Management and Evaluation. He is a Board member for the Ontario Community Support Association and the Information Technology Association of Canada Health Board.",
        date="2017",
        img_url="Events-BANNER-1440x277.png",
        category=it,
        tags="ai,event,health"
    )

    db.session.add(p)

    p = Post(
        title="Free museum passes for U of T students",
        user=amir,
        content_mini="For the second year in a row, U of G students can visit select museums and cultural institutions for free, thanks to a U of G Libraries partnership.",
        content="The pass can be used for free admission for two visitors to one of the following venues: The Aga Khan Museum, the Art Gallery of Ontario, the Bata Shoe Museum, Black Creek Pioneer Village, the Royal Ontario Museum, the Textile Museum of Canada and City of Toronto Historic Sites.",
        date="2017",
        img_url="dinosaur-museum.jpg",
        category=culture,
        tags="event,musem"
    )
    db.session.add(p)

    p = Post(
        title="The city of Guilan",
        user=amir,
        content_mini="",
        content="visit Guilan",
        date="2017",
        img_url="Shahrdari-1.jpg",
        category=culture,
        tags="tour"
    )

    db.session.add(p)

    p = Post(
        title="Basketball Event",
        user=amir,
        content_mini="",
        content="",
        date="2017",
        img_url="filip-mroz-177565.jpg",
        category=sport,
        tags="event"
    )

    db.session.add(p)

    p = Post(
        title="Applications now open for Pathways Taster Days",
        user=amir,
        content_mini="These events for Year 10 and Year 12 students at UK state schools provide information, advice and guidance about higher education and Oxford",
        content="",
        date="2017",
        img_url="bcar_pathways.jpg",
        category=science,
        tags="event,tour"
    )

    p = Post(
        title="Machine Learning Exam",
        user=amir,
        content_mini="Machine Learning Exam On Friday",
        content="Machine Learning Exam On Friday , classrom 20",
        date="2017",
        img_url="brain.jpg",
        category=course,
        course=machineLearning,
        tags="exam"
    )

    db.session.add(p)

    db.session.commit()


@manager.command
def initdb():
    """ Create database """
    db.create_all()
    buildPosts()
    buildCourse()
    buildUsers()
    print('Successful')


@manager.command
def dropall():
    """ Drop database """
    db.drop_all()
    print('Successful')


if __name__ == '__main__':
    manager.run()
