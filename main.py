import PySimpleGUI as sg
import time
import functions

sg.theme("Black")

todays_date = sg.Text(time.strftime("%b %d, %Y"), key="date")
add_button = sg.Button("Add")
remove_button = sg.Button("Delete")
edit_button = sg.Button("Edit")
table_headings = ["Company Name", "Position Title", "Website Link", "Address", "Contact Name", "Phone Number",
                  "Job Pay", "Date Applied", "Interview 1 Date", "Interview 2 Date", "Interview 3 Date",
                  "Days Since Applying", "Days Since Interview 1", "Days Since Interview 2", "Days Since Interview 3",
                  "Notes"]
jobs_table = sg.Table(headings=table_headings, key="jobs_table", values=[application.to_list() for application in functions.load_job_applications()])

layout = [[todays_date], [add_button, remove_button, edit_button], [jobs_table]]

window = sg.Window("Job Application Tracker", layout=layout)

while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "Add":
            job_applications = functions.load_job_applications()
            company_name = sg.Text("Company Name")
            position_title = sg.Text("Position_title")
            website_link = sg.Text("website_link")
            address = sg.Text("address")
            contact_name = sg.Text("contact_name")
            phone_number = sg.Text("phone_number")
            job_pay = sg.Text("job_pay")
            date_applied = sg.Text("date_applied")
            interview_1_date = sg.Text("interview_1_date")
            interview_2_date = sg.Text("interview_2_date")
            interview_3_date = sg.Text("interview_3_date")
            notes = sg.Text("notes")

            company_name_input = sg.Input(key="company_name")
            position_title_input = sg.Input(key="position_title")
            website_link_input = sg.Input(key="website_link")
            address_input = sg.Input(key="address")
            contact_name_input = sg.Input(key="contact_name")
            phone_number_input = sg.Input(key="phone_number")
            job_pay_input = sg.Input(key="job_pay")
            date_applied_input = sg.Input(key="date_applied")
            interview_1_date_input = sg.Input(key="interview_1_date")
            interview_2_date_input = sg.Input(key="interview_2_date")
            interview_3_date_input = sg.Input(key="interview_3_date")
            notes_input = sg.Input(key="notes")

            ok_button = sg.Button("Ok", key="ok")
            cancel_button = sg.Button("Cancel", key="cancel")

            column1 = sg.Column([[company_name],
                                 [position_title],
                                 [website_link],
                                 [address],
                                 [contact_name],
                                 [phone_number],
                                 [job_pay],
                                 [date_applied],
                                 [interview_1_date],
                                 [interview_2_date],
                                 [interview_3_date],
                                 [notes]])
            column2 = sg.Column([[company_name_input],
                                 [position_title_input],
                                 [website_link_input],
                                 [address_input],
                                 [contact_name_input],
                                 [phone_number_input],
                                 [job_pay_input],
                                 [date_applied_input],
                                 [interview_1_date_input],
                                 [interview_2_date_input],
                                 [interview_3_date_input],
                                 [notes_input]])
            add_layout = [[company_name, company_name_input],
                          [position_title, position_title_input],
                          [website_link, website_link_input],
                          [address, address_input],
                          [contact_name, contact_name_input],
                          [phone_number, phone_number_input],
                          [job_pay, job_pay_input],
                          [date_applied, date_applied_input],
                          [interview_1_date, interview_1_date_input],
                          [interview_2_date, interview_2_date_input],
                          [interview_3_date, interview_3_date_input],
                          [notes, notes_input],
                          [ok_button, cancel_button]]
            add_window = sg.Window("Add Job Application", layout=[[column1, column2], [ok_button, cancel_button]])
            while True:
                add_event, add_values = add_window.read()
                print(add_event, add_values)
                match add_event:
                    case "ok":
                        pass
                    case "cancel":
                        add_window.close()
                        break
                    case sg.WIN_CLOSED:
                        break

            pass
        case "Remove":
            pass
        case "Edit":
            pass
        case sg.WIN_CLOSED:
            break
