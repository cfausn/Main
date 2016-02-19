------------------------------------------------------------------------------------------------------------------------
Names: Daniel Dang, Colin Fausnaught, Raasin Siddiq, William Tarr, Barry Wu
Date: October 4, 2015


Release 1

Welcome to HealthNet! In this file, we will explain how this software works and how helpful it is for hospitals.
This software is meant to facilitate interactions between patients, doctors, nurses, and administrators. With this
software, you can manage your schedule and create appointments with your doctor, as well as edit your personal
information. In this release we emphasized the focus to be on managing your schedule.

------------------------------------------------------------------------------------------------------------------------

How to install:
1.) Take the zip file and extract it to a directory that is easily accessible.
2.) Open Command Prompt
3.) Change directory to the directory of the software i.e. cd ~/[your software location]
4.) Make sure there is a file named manage.py in the directory and type 'python manage.py migrate'
5.) After that 'python manage.py runserver' on the server.
The server should then be running, so you can go to 'http://127.0.0.1:8000' to launch the site.

------------------------------------------------------------------------------------------------------------------------

Navigating the site:
On the splash page, there are two buttons: one to Login and another to Register. You can either login with one of the
prepopulated users below to create your own account. The minimum required fields are Username, Password, Email, First
Name, and Last Name; after filling at least those out, click submit at the bottom to verify your information and if all
the fields have been entered properly, you will be taken to the Profiles Page.
At the profile page, you can view or edit your general information, as well as click a link view your schedule.
In the schedule page, the page is for the current day listed, and from here your can add an appointment for that day.
To navigate to future or past days, you can traverse forward and back by day, week, and year. 

You can also go to 'http://127.0.0.1:8000/admin' to access the Django administrator webpage for the software.

------------------------------------------------------------------------------------------------------------------------

Release 1 Features:
    -Patient Registration
    -View schedule/calendar
    -Create/Update appointments
    -Delete Appointment
    -Administrator Registration
    -Administrator Removal

Missing Features from initial Requirements Document:
    -Admitting and Discharging a patient from a hospital. Talked to Dr. House about this in a previous meeting and we
     decided to postpone this feature for a later release
    -Viewing Activity Log, the actions are being logged but have not been set to be viewed via the web pages. Only
     admin logs are viewable at this point.

------------------------------------------------------------------------------------------------------------------------

Known Bugs and Disclaimers:
    -While creating or editing an appointment, if the user hits cancel they are taken back to the splash screen. This
     will be resolved in the next release.
    -When creating or editing an appointment, the start time and end time fields must be entered as 'YYYY-MM-DD H:MM:SS'
    -Nurses do not have profile pages but they can view other users' pages. Only doctors and patients can view their 
     pages.
    -Nurses' profile pages instead redirect to the Scheduling page where they can create and modify appointments.

------------------------------------------------------------------------------------------------------------------------

Prepopulated users and their respective passwords are listed below:
    User Type: Administrator
    Username: 2BD
    Password: 2BD

    User Type: Doctor
    Username: TestDoctor
    Password: password

    User Type: Nurse
    Username: TestNurse
    Password: password

    User Type: Patient
    Username: Patient0
    Password: password

------------------------------------------------------------------------------------------------------------------------