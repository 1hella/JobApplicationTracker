import os
import csv

from JobApplication import JobApplication

# create file
if not os.path.exists("jobs.csv"):
    with open("jobs.csv", "w") as file:
        pass


# todo: replace with db
def load_job_applications():
    with open("jobs.csv", 'r') as file:
        data = list(csv.reader(file))

    if len(data) == 0:
        insert_dummy_data()
        with open("jobs.csv") as file:
            data = list(csv.reader(file))

    print("applications", data)
    applications = []
    for application in data:
        print(application)
        try:
            company_name = application[0]
            position_title = application[1]
            website_link = application[2]
            address = application[3]
            contact_name = application[4]
            phone_number = application[5]
            job_pay = application[6]
            date_applied = application[7]
            interview_1_date = application[8]
            interview_2_date = application[9]
            interview_3_date = application[10]
            notes = application[11]
            applications.append(JobApplication(company_name, position_title, website_link, address, contact_name,
                                           phone_number, job_pay, date_applied, interview_1_date, interview_2_date,
                                           interview_3_date, notes))
        except IndexError:
            print("can't parse line", application)
    return applications


# todo: replace with db
def save_job_applications(job_applications: list[JobApplication]):
    with open("jobs.csv", 'w') as file:
        csv_writer = csv.writer(file)
        for application in job_applications:
            csv_writer.writerow([application.company_name,
                                 application.position_title,
                                 application.website_link,
                                 application.address,
                                 application.contact_name,
                                 application.phone_number,
                                 application.job_pay,
                                 application.date_applied,
                                 application.interview_1_date,
                                 application.interview_2_date,
                                 application.interview_3_date,
                                 application.notes])


def insert_dummy_data():
    dummy_data = [
        JobApplication('Google', 'Software Engineer', 'www.google.com', '1600 Amphitheatre Parkway, Mountain View, CA 94043, USA',
         'John Doe', '123-456-7890', 100000.00, '2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01', 'Good company'),
        JobApplication('Amazon', 'DevOps Engineer', 'www.amazon.com', '410 Terry Ave N, Seattle, WA 98109, USA', 'Jane Doe',
         '987-654-3210', 120000.00, '2022-05-01', '2022-06-01', '2022-07-01', None, 'Good opportunity'),
        JobApplication('Microsoft', 'Data Scientist', 'www.microsoft.com', 'One Microsoft Way, Redmond, WA 98052, USA', 'Jim Smith',
         '456-123-7890', 110000.00, '2022-08-01', '2022-09-01', None, None, 'Interesting projects')]
    save_job_applications(dummy_data)
