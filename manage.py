from website import db, app
from flask_script import Manager
from website.mod_student.models import Student
from website.mod_professor.models import Professor
from website.mod_course.models import Course, Slide , Term
from website.mod_news.models import Post, Category , Tag
from website.mod_auth.models import User, Authority
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
    student=student,
    verify=True
)

bianca = Professor(
        field_of_study="system reliability",
        degree="PhD",
        level="Associate Professor",
    )

dan = Professor(
        field_of_study="NLP",
        degree="PhD",
        level="Professor",
    )

noam = Professor(
        field_of_study="Compiler",
        degree="PhD",
        level="Professor",
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
        professor=professor,
        verify=True
    )
    u.authorities.append(authorityProfessor)
    db.session.add(u)
    db.session.add(professor)

    u = User(
        first_name="Dan",
        last_name="Jurafsky",
        username="dan.jurafsky",
        img_url="dan_jurafsky.jpg",
        password_hash=generate_password_hash("123456"),
        professor=dan,
        verify=True
    )
    u.authorities.append(authorityProfessor)
    db.session.add(u)
    db.session.add(dan)

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
        professor=professor,
        verify=True
    )
    u.authorities.append(authorityProfessor)
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
        professor=professor,
        verify=True
    )
    u.authorities.append(authorityProfessor)
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
        img_url="Richard_Stallman.jpg",
        verify=True
    )
    db.session.add(u)
    db.session.add(professor)

    u = User(
        first_name="Noam",
        last_name="Chomsky",
        username="noam.chomsky",
        password_hash=generate_password_hash("123456"),
        professor=noam,
        img_url="Noam_Chomsky.jpg",
        verify=True
    )
    u.authorities.append(authorityProfessor)
    db.session.add(noam)
    db.session.add(professor)

    u = User(
        first_name="Bianca",
        last_name="Schroeder",
        username="bianca.schroeder",
        password_hash=generate_password_hash("123456"),
        professor=bianca,
        img_url="bianca_schroeder.jpg",
        verify=True
    )
    u.authorities.append(authorityProfessor)
    db.session.add(bianca)
    db.session.add(professor)

    db.session.commit()


term96 = Term(
        year=1396
    )

term97 = Term(
        year=1397
    )

machineLearning = Course(
    title="Machine Learning",
    minor_title="Build Intelligent Applications. Master machine learning fundamentals in four hands-on courses.",
    about="This Specialization from leading researchers at the University of Washington introduces you to the exciting, high-demand field of Machine Learning. Through a series of practical case studies, you will gain applied experience in major areas of Machine Learning including Prediction, Classification, Clustering, and Information Retrieval. You will learn to analyze large and complex datasets, create systems that adapt and improve over time, and build intelligent applications that can make predictions from data.",
    term=term96,
    video_url="3.webm",
    degree="bachelor",
    homework="Exercise 2",
    resources="Machine Learning from amir",
    syllabus="From molecular genetics to sustainable urban infrastructure – global security in the age of cyber-espionage to music composition, our internationally renowned teachers and researchers are leaders in their fields."
)
machineLearning.teachers.extend([bianca,dan])

def buildCourse():
    db.session.add_all([term96,term97])
    db.session.commit()
    
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
        minor_title="Automata theory is the study of abstract machines and automata, as well as the computational problems that can be solved using them",
        about="<p>We begin with a study of finite automata and the languages they can define (the so-called \"regular languages.\" Topics include deterministic and nondeterministic automata, regular expressions, and the equivalence of these language-defining mechanisms. We also look at closure properties of the regular languages, e.g., the fact that the union of two regular languages is also a regular language. We conssider decision properties of regular languages, e.g., the fact that there is an algorithm to tell whether or not the language defined by two finite automata are the same language. Finally, we see the pumping lemma for regular languages — a way of proving that certain languages are not regular languages.</p><p>Our second topic is context-free grammars and their languages. We learn about parse trees and follow a pattern similar to that for finite automata: closure properties, decision properties, and a pumping lemma for context-free languages. We also introduce the pushdown automaton, whose nondeterministic version is equivalent in language-defining power to context-free grammars.</p><p>Next, we introduce the Turing machine, a kind of automaton that can define all the languages that can reasonably be said to be definable by any sort of computing device (the so-called \"recursively enumerable languages\"). We shall learn how \"problems\" (mathematical questions) can be expressed as languages. That lets us define problems to be \"decidable\" if their language can be defined by a Turing machine and \"undecidable\" if not. We shall see some basic undecidable problems, for example, it is undecidable whether the intersection of two context-free languages is empty.</p><p>Last, we look at the theory of intractable problems. These are problems that, while they are decidable, have almost certainly no algorithm that runs in time less than some exponential function of the size of their input. We meet the NP-complete problems, a large class of intractable problems. This class includes many of the hard combinatorial problems that have been assumed for decades or even centuries to require exponential time, and we learn that either none or all of these problems have polynomial-time algorithms. A common example of an NP-complete problem is SAT, the question of whether a Boolean expression has a truth-assignment to its variables that makes the expression itself true.</p>",
        term=term97,
        degree="bachelor",
        video_url="1.mp4"
    )
    c.teachers.extend([noam])
    db.session.add(c)

    db.session.commit()


def buildPosts():

    it = Category(name="it")
    sport = Category(name="sport")
    science = Category(name="science")
    culture = Category(name="culture")
    course = Category(name="course")

    db.session.add_all([it, sport, culture, science, course])

    ai = Tag(name="ai")
    event = Tag(name="event")
    health = Tag(name="health")
    museum = Tag(name="museum")
    tour = Tag(name="tour")
    exam = Tag(name="exam")

    p = Post(
        title="Panel Discussion on Big Data and Artificial Intelligence in Healthcare",
        user=amir,
        content_mini="For those who register to attend all four Health IT Sessions you may be eligible for a certificate of completion.",
        content="Aaron Berk is a Partner in KPMG’s Digital Health practice. He has 20 years of experience as a clinician, hospital manager and consultant. Aaron has led provincial projects related to Analytics, wait-time management, cancer care, peri-operative practice, critical care, and population health initiatives. Aaron has also provided strategic advice to governments, agencies and health regions on integration of virtual care to improve the integrated delivery of healthcare services. Aaron is a member of the Masters in eHealth program advisory committee for McMaster University and holds an appointment at U of T's institute of Health Policy, Management and Evaluation. He is a Board member for the Ontario Community Support Association and the Information Technology Association of Canada Health Board.",
        date="2017",
        img_url="Events-BANNER-1440x277.png",
        category=it,
    )
    p.tags.extend([ai,event,health])
    db.session.add(p)

    p = Post(
        title="Free museum passes for U of T students",
        user=amir,
        content_mini="For the second year in a row, U of G students can visit select museums and cultural institutions for free, thanks to a U of G Libraries partnership.",
        content="The pass can be used for free admission for two visitors to one of the following venues: The Aga Khan Museum, the Art Gallery of Ontario, the Bata Shoe Museum, Black Creek Pioneer Village, the Royal Ontario Museum, the Textile Museum of Canada and City of Toronto Historic Sites.",
        date="2017",
        img_url="dinosaur-museum.jpg",
        category=culture,
    )
    p.tags.extend([event,museum])
    db.session.add(p)

    p = Post(
        title="The city of Guilan",
        user=amir,
        content_mini="",
        content="visit Guilan",
        date="2017",
        img_url="Shahrdari-1.jpg",
        category=culture,
    )
    p.tags.extend([tour])
    db.session.add(p)

    p = Post(
        title="Basketball Event",
        user=amir,
        content_mini="",
        content="",
        date="2017",
        img_url="filip-mroz-177565.jpg",
        category=sport,
    )

    p.tags.extend([event])
    db.session.add(p)

    p = Post(
        title="Applications now open for Pathways Taster Days",
        user=amir,
        content_mini="These events for Year 10 and Year 12 students at UK state schools provide information, advice and guidance about higher education and Oxford",
        content="",
        date="2017",
        img_url="bcar_pathways.jpg",
        category=science,
    )

    p.tags.extend([event,tour])
    db.session.add(p)

    p = Post(
        title="Machine Learning Exam",
        user=amir,
        content_mini="Machine Learning Exam On Friday",
        content="Machine Learning Exam On Friday , classrom 20",
        date="2017",
        img_url="brain.jpg",
        category=course,
        course=machineLearning,
    )
    p.tags.extend([exam])
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
