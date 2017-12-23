from website import db, app
from flask_script import Manager
from website.models import Post

manager = Manager(app)


def buildPosts():

    p = Post(
        title="Panel Discussion on Big Data and Artificial Intelligence in Healthcare",
        author="Amir Deljuyi",
        content_mini="For those who register to attend all four Health IT Sessions you may be eligible for a certificate of completion.",
        content="Aaron Berk is a Partner in KPMG’s Digital Health practice. He has 20 years of experience as a clinician, hospital manager and consultant. Aaron has led provincial projects related to Analytics, wait-time management, cancer care, peri-operative practice, critical care, and population health initiatives. Aaron has also provided strategic advice to governments, agencies and health regions on integration of virtual care to improve the integrated delivery of healthcare services. Aaron is a member of the Masters in eHealth program advisory committee for McMaster University and holds an appointment at U of T's institute of Health Policy, Management and Evaluation. He is a Board member for the Ontario Community Support Association and the Information Technology Association of Canada Health Board.",
        date="2017",
        img_url="Events-BANNER-1440x277.png",
        category="it",
        tags="ai,event,health"
        )

    db.session.add(p)
    
    p = Post(
        title="Free museum passes for U of T students",
        author="Amir Deljuyi",
        content_mini="For the second year in a row, U of G students can visit select museums and cultural institutions for free, thanks to a U of G Libraries partnership.",
        content="The pass can be used for free admission for two visitors to one of the following venues: The Aga Khan Museum, the Art Gallery of Ontario, the Bata Shoe Museum, Black Creek Pioneer Village, the Royal Ontario Museum, the Textile Museum of Canada and City of Toronto Historic Sites.",
        date="2017",
        img_url="dinosaur-museum.jpg",
        category="culture",
        tags="event,musem"
        )
    db.session.add(p)
    
    p = Post(
        title="The city of Guilan",
        author="Amir Deljuyi",
        content_mini="",
        content="visit Guilan",
        date="2017",
        img_url="Shahrdari-1.jpg",
        category="culture",
        tags="tour"
        )
    
    db.session.add(p)
    
    p = Post(
        title="Basketball Event",
        author="Amir Deljuyi",
        content_mini="",
        content="",
        date="2017",
        img_url="filip-mroz-177565.jpg",
        category="sport",
        tags="event"
        )    

    db.session.add(p)

    p = Post(
        title="Applications now open for Pathways Taster Days",
        author="Amir Deljuyi",
        content_mini="These events for Year 10 and Year 12 students at UK state schools provide information, advice and guidance about higher education and Oxford",
        content="",
        date="2017",
        img_url="bcar_pathways.jpg",
        category="science",
        tags="event,tour"
        )

    db.session.add(p)

    db.session.commit()

@manager.command
def initdb():
    """ Create database """
    db.create_all()
    buildPosts()
    #posts = buildPosts()
    print('Successful')

@manager.command
def dropall():
    """ Drop database """
    db.drop_all()
    print('Successful')

if __name__ == '__main__':
    manager.run()