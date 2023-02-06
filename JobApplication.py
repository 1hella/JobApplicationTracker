from datetime import datetime


class JobApplication:
    def __init__(self, company_name, position_title, website_link, address, contact_name, phone_number,
                 job_pay, date_applied, interview_1_date, interview_2_date, interview_3_date,
                 notes):
        self.company_name = company_name
        self.position_title = position_title
        self.website_link = website_link
        self.address = address
        self.contact_name = contact_name
        self.phone_number = phone_number
        self.job_pay = job_pay
        self.date_applied = date_applied
        self.interview_1_date = interview_1_date
        self.interview_2_date = interview_2_date
        self.interview_3_date = interview_3_date
        self.days_since_applying = ""
        self.days_since_interview_1 = ""
        self.days_since_interview_2 = ""
        self.days_since_interview_3 = ""
        try:
            delta = datetime.now() - datetime.strptime(self.date_applied, '%Y-%m-%d')
            self.days_since_applying = delta.days
        except (TypeError, ValueError):
            print("can't parse interview_1_date", self.interview_1_date)
        try:
            delta = datetime.now() - datetime.strptime(self.interview_1_date, '%Y-%m-%d')
            self.days_since_interview_1 = delta.days
        except (TypeError, ValueError):
            print("can't parse interview_1_date", self.interview_1_date)
        try:
            delta = datetime.now() - datetime.strptime(self.interview_2_date, '%Y-%m-%d')
            self.days_since_interview_2 = delta.days
        except (TypeError, ValueError):
            print("Can't parse interview_2_date", self.interview_2_date)
        try:
            delta = datetime.now() - datetime.strptime(self.interview_3_date, '%Y-%m-%d')
            self.days_since_interview_3 = delta.days
        except (TypeError, ValueError):
            print("Can't parse interview_3_date", self.interview_3_date)
        self.notes = notes

    def to_list(self):
        return [self.company_name,
                self.position_title,
                self.website_link,
                self.address,
                self.contact_name,
                self.phone_number,
                self.job_pay,
                self.date_applied,
                self.interview_1_date,
                self.interview_2_date,
                self.interview_3_date,
                self.days_since_applying,
                self.days_since_interview_1,
                self.days_since_interview_2,
                self.days_since_interview_3,
                self.notes]
