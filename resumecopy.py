import fontstyle


class EmilyZucker:

    def __init__(self):
        self.name = fontstyle.apply("Emily Zucker", 'underline')
        self.address = 'my address'
        self.email = 'my email'
        self.phone_number = 'my phone number'
        self.linkedin = "my linkedin"

    def __repr__(self):
        return (f"{self.name} -- {self.email}\n"
                f"{self.address} -- {self.phone_number} -- {self.linkedin}\n")


class Education(EmilyZucker):

    def __init__(self):
        EmilyZucker.__init__(self)

    highest_degree = fontstyle.apply("High School Diploma - June 2023", 'Italic')
    high_school = "my high school"
    gpa = "GPA - 5.32 (weighted) - Principal's Honor Roll"

    current_degree = fontstyle.apply("Computer Engineering", 'Italic')
    university = "University of Florida, Gainesville Fl"
    student_status = "Freshman"
    college_gpa = "GPA: N/A"

    def __repr__(self):
        return (f"{self.highest_degree}\n"
                f"\t- {self.high_school}\n"
                f"\t- {self.gpa}\n"
                f"Degree Currently Pursuing: {self.current_degree}\n"
                f"\t- {self.student_status} - {self.university}\n"
                f"\t- {self.college_gpa}\n")


class WorkExperience(EmilyZucker):

    def __init__(self):
        EmilyZucker.__init__(self)

    job_title = fontstyle.apply("Bookseller/Barista", 'Italic')
    date_employed = "October 2021 - August 2023"
    previous_employer = "Barnes and Noble Booksellers, (city I worked in)"
    skills_gained = ["Frequently practiced promoting and increasing local book sales; "
                     "used data entry skills to process various \t  transactions.",
                     "Practiced food-safe procedures and efficiency of service when "
                     "providing customers with their orders.",
                     "Gained experience with teamwork, customer service, monetary processing, "
                     "and flexibility in the workplace."]

    def __repr__(self):
        return (f"{self.job_title}: {self.date_employed}\n"
                f"{self.previous_employer}\n"
                f"\t- {self.skills_gained[0]}\n"
                f"\t- {self.skills_gained[1]}\n"
                f"\t- {self.skills_gained[2]}\n")


class Leadership(EmilyZucker):

    def __init__(self, title, date, location):
        EmilyZucker.__init__(self)
        self.title = fontstyle.apply(title, 'Italic')
        self.leader_date = date
        self.location = location
        self.leadership_skills = ['', '']

    def get_leader_skills(self, index, skill):
        self.leadership_skills[index] = skill

    def __repr__(self):
        return (f"{self.title}: {self.leader_date}\n"
                f"{self.location}\n"
                f"\t- {self.leadership_skills[0]}\n"
                f"\t- {self.leadership_skills[1]}\n")


class Service(EmilyZucker):

    def __init__(self):
        EmilyZucker.__init__(self)

    service_title = fontstyle.apply("Administrative Assistant", 'Italic')
    service_date = "June 2021 - August 2021"
    service_location = "(place I volunteered at), (city I volunteered in)"
    service_skills = ["Assisted with administrative tasks such as file maintenance, using "
                      "Microsoft services such as Excel to \n\t  input data, customer service, "
                      "responding to emails, etc.",
                      "Gained experience working in a professional atmosphere and learned "
                      "to plan and carry out tasks such as data \t  tracking both with and without "
                      "supervision."]

    def __repr__(self):
        return (f"{self.service_title}: {self.service_date}\n"
                f"{self.service_location}\n"
                f"\t- {self.service_skills[0]}\n"
                f"\t- {self.service_skills[1]}\n")


class OnCampusInvolvement(EmilyZucker):

    def __init__(self, name, position, date, location, info):
        EmilyZucker.__init__(self)
        self.club_name = fontstyle.apply(name, 'Italic')
        self.position = position
        self.date_in_club = date
        self.location = location
        self.info = info

    def __repr__(self):
        return (f"{self.club_name} {self.position}: {self.date_in_club}\n"
                f"{self.location}\n"
                f"\t- {self.info}\n")


class CodingExperience(EmilyZucker):

    def __init__(self, name, location, description):
        EmilyZucker.__init__(self)
        self.class_name = name
        self.class_location = location
        self.description = description

    def __repr__(self):
        return (f"{self.class_name} - {self.class_location}\n"
                f"\t-{self.description}\n")


class SkillsAndAwards(EmilyZucker):

    def __init__(self):
        EmilyZucker.__init__(self)
        self.skills = {"Skill1": "Microsoft 2016 Certified",
                       "Skill2": "Bright Futures Scholarship Recipient",
                       "Skill3": "AP Scholar with Distinction in 2023",
                       "Skill4": "Professional: Teamwork, Time Management, Proficiency in Math, "
                                 "Python Programming"}

    def __repr__(self):
        return (f"\t- {self.skills['Skill1']}\n"
                f"\t- {self.skills['Skill2']}\n"
                f"\t- {self.skills['Skill3']}\n"
                f"\t- {self.skills['Skill4']}\n")


me = EmilyZucker()
my_education = Education()
my_work_experience = WorkExperience()
my_leadership_1 = Leadership("Science Honor Society President",
                             "August 2022 - June 2023",
                             "my high school", )
my_leadership_1.get_leader_skills(0, "Served as President for the (my high school) chapter of "
                                     "the Science National Honor Society and \n\t  increased female engagement in "
                                     "the club by over 50%.")
my_leadership_1.get_leader_skills(1, "Led a team that competed in Samsung’s Solve for "
                                     "Tomorrow competition that won on the State level "
                                     "and earned \t  $2,500 for classroom use.")
my_leadership_2 = Leadership("National English Honor Society President",
                             "August 2022 - June 2023",
                             "my high school", )
my_leadership_2.get_leader_skills(0, "Was responsible for keeping track of monetary funds as well as "
                                     "filing project requests, payment requests, \n\t  ordering supplies such as "
                                     "T-shirts, leading meetings, etc.")
my_leadership_2.get_leader_skills(1, "Led workshops such as an SAT reading/grammar workshop and a book drive "
                                     "to stock bookshelves in English \n\t  teacher’s classrooms, increasing total "
                                     "book volume by an estimated 20%.")
my_service = Service()
my_campus_involvement_1 = OnCampusInvolvement("Association of Computing Machinery",
                                              "General Body Member",
                                              "September 2023 - Present",
                                              "University of Florida",
                                              "Club for those pursuing degrees or careers in Computer Science.")
my_campus_involvement_2 = OnCampusInvolvement("Women in Computer Science and Engineering",
                                              "General Body Member",
                                              "September 2023 - Present",
                                              "University of Florida",
                                              "Organization for women to build careers and connections "
                                              "with other women in the field")
my_coding_experience_1 = CodingExperience("Intro to Programming",
                                          "Broward College",
                                          "Developed essential skills in Python programming and "
                                          "learned basics such as data types, iterating over \n\t loops, checking"
                                          " input validity, and created individual projects such as simple "
                                          "calculators, ad-lib games, \n\t Ving-Et-Un, number-guessing games, etc.")
my_coding_experience_2 = CodingExperience("Programming Fundamentals 1",
                                          "University of Florida",
                                          "Built upon and excelled in foundational skills used to develop more "
                                          "complex beginner programs such as a \n\t Blackjack game, scientific "
                                          "calculators, Connect Four, an RLE image encoder/decoder to display pixel "
                                          "images.")
my_skills_and_awards = SkillsAndAwards()


def prof_summ():
    title = fontstyle.apply("** Professional Summary\n", 'bold')
    summary = ("First year pursuant of a Bachelor's Degree is Computer Science/Engineering that is dedicated to "
               "learning about and being immersed in the field of computer science, seeking an internship for "
               "the summer of 2024.\n")
    return title, summary


def main():
    prof_title, prof_sum = prof_summ()

    print(me)
    print('-' * 105, '\n')
    print(prof_title,
          prof_sum,
          fontstyle.apply("\n** Education\n", 'bold'),
          my_education,
          fontstyle.apply("\n** Coding Experience\n", 'bold'),
          my_coding_experience_1,
          my_coding_experience_2,
          fontstyle.apply("\n** Work Experience\n", 'bold'),
          my_work_experience,
          fontstyle.apply("\n** Leadership Experience\n", 'bold'),
          my_leadership_1,
          my_leadership_2,
          fontstyle.apply("\n** Service\n", 'bold'),
          my_service,
          fontstyle.apply("\n** Campus Involvement\n", 'bold'),
          my_campus_involvement_1,
          my_campus_involvement_2,
          fontstyle.apply("\n** Skills & Awards\n", 'bold'),
          my_skills_and_awards, sep='')
    print("Please visit https://github.com/emilyzucker1/resume.2023.git to see this program")


main()
