from fasthtml.common import *

app,rt = fast_app(hdrs=[Link(rel="icon", type="image/png", href="/favicon.png")])

def Job(employer: str, title: str, location: str, startDate: str, endDate: str, bullets: List[str]):
    return Li(
        H3(employer + " - " + title),
        H4(location),
        H5(startDate + " - " + endDate),
        Ul(*[Li(bullet) for bullet in bullets]),
        style="list-style: none;"
    )

jobs = [
    Job("Erthos", "Senior Software Engineer", "Chandler, AZ", "Feb 2024", "Present", [
        "Developed a comprehensive fleet management tool using React.js and Express.js, integrating authentication and feature flag functionalities to enhance user experience and system security.", 
        "Designed and implemented Azure pipelines for building autonomous bot software, creating deployment jobs via the fleet manager to ensure seamless updates across the entire fleet and improving deployment times by 900%.", 
        "Spearheaded the deployment of a time series database, facilitating historical data collection, issue tracking, and metric dashboards, using Grafana, to improve field debugging and operational efficiency.", 
        "Established a scheduling system for regular bot deployment with specified missions, optimizing field operations and ensuring consistent performance."
        ]),
    Job("Arizona State University", "Software Engineer", "Tempe, AZ", "Sep 2023", "Jan 2024", [
        "Implemented a 9 page, 62 story app re-write of the New Student Orientation Experience application porting from Angular to React and improving page load times by 100-150%.",
        "Developed AWS Lambda endpoints using node.js and UI's using React for the Degree Audit Administration Application allowing for easier assignment of user roles and environment parameters.",
        "Assigned to 2 high priority projects, Orientations and Smart DART, on discovery of my ability as a developer by portfolio managers."
        ]),
    Job("Transact Campus", "Senior Software Engineer", "Phoenix, AZ", "Oct 2022", "Sep 2023", [
        "Utilized C# .NET Core, Azure Table Storage, Cosmos DB, and Azure Service Bus to build robust microservices that offered secure and reliable access to our mobile credential solution.",
        "Developed unit and integration tests using XUnit and Postman to thoroughly validate code and achieve high code coverage on all pull requests, ensuring that the codebase is of high quality.",
        "Leveraged Power BI to create comprehensive reports that highlighted key metrics on the health, performance, and usage of our credentials, providing valuable insights to stakeholders."
        ]),
    Job("Bluetail", "Consulting Senior Developer", "Phoenix, AZ", "Oct 2021", "Sep 2022", [
        "My focus was on the administrative site (working in Express.js, Postgres, and React) to improve performance and give suggestions on better coding practices and provided support on integrating new partner applications in order to improve the value of the app to customers.",
        "I improved pages that were taking seconds or minutes to load data down to milliseconds by optimizing the sql queries being made and improving the code.",
        "Created a PEVN stack application (working in Express.js, Postgres, and Vue) to improve the processing and uploading of bulk raw documents with customers. The tool included blank page detection and automatic page rotation using OCR (tesseract)."
        ]),
    Job("SAP", "Senior Software Developer", "Tempe, AZ", "Dec 2016", "May 2021", [
        "Experience Creating UI's from scratch (Manage Planning Configuration Sets, Manage Option Plans, Manage Category Assortments) and working with UIs of existing applications (Manage Promotional Offers, Manage Offer Content) using the SAPUI5/OpenUI5 framework.",
        "Experience using the SAPUI5 framework to create custom controls such as an image carousel dialog and a pseudo-pivot table.",
        "Developed oData services using CDS views (Preview Events, Manage Category Assortments) and ABAP (Manage Offer Content).",
        "One of ~50 early talents from the global early talent pool selected for the second ever cohort of the SAP Academy for Engineering.",
        "Credited as one of three inventors for 2 patents created for work done with the Manage Option Plans application."
        ]),
]

educations = [
    Job("Arizona State University", "GPA: 4.16 (4.33 Scale)", "Tempe, AZ", "Aug 2013", "May 2017", [
        "Some of the classes I have taken include Data Structures and Algorithms, Operating Systems, Computer Networks, Network Security, Intro to Theoretical Computer Science, Intro to Data Mining, Software Testing and QA, Database Management, and Principles of Programming Languages (all of which I received A's in).",
        ]),
]



def JobsSection():
    return Section(H2("Jobs"), Ul(*[job for job in jobs], ), id="jobs")

def EducationSection():
    return Section(H2("Education"), Ul(*[education for education in educations]), id="education")

@rt("/")
def get(): 
    return Title("Jacob Stovall - Software Engineer"), Main(Nav(Ul(Li(H1("Jacob Stovall - Software Engineer"))), Ul(Li(H2(A("Jobs", href="#jobs"))), Li(H2(A("Education", href="#education"))),)), JobsSection(), EducationSection(), cls="container main")

@rt("/favicon.png")
def get():
    return FileResponse(f"favicon.png")

serve()
