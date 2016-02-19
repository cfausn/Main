------------------------------------------------------------------------------------------------------------------------
Names: Daniel Dang, Colin Fausnaught, Raasin Siddiq, William Tarr, Barry Wu
Date: November 8, 2015


Release 2 Beta

Welcome to HealthNet! In this file, we will explain how this software works and how helpful it is for hospitals.
This software is meant to facilitate interactions between patients, doctors, nurses, and administrators. With this
software, you can manage your schedule and create appointments with your doctor, as well as edit your personal
information. In this release we emphasized the focus to be on managing your schedule.

------------------------------------------------------------------------------------------------------------------------

How to install:
1.) Take the zip file and extract it to a directory that is easily accessible.
2.) Open Command Prompt
3.) Change directory to the directory of the software: i.e. cd ~/[your software location].
4.) Make sure there is a file named manage.py in the directory and type 'python manage.py migrate'
5.) After that 'python manage.py runserver' on the server.
The server should then be running, so you can go to 'http://127.0.0.1:8000' or 'localhost:8000' to launch the site.

------------------------------------------------------------------------------------------------------------------------

Navigating the site:
On the splash page, there are two buttons: one to Login and another to Register. You can either login with one of the
prepopulated users below to create your own account. The required fields are Insurance Company, Insurance Number, Email, 
Password, First Name, and Last Name, and Hospital; after filling at least those out, click submit at the bottom to verify 
your information and if all the fields have been entered properly, you will be taken to the Profiles Page.
At the profile page, you can view or edit your general information and you can view your medical information.
In the schedule page, 

------------------------------------------------------------------------------------------------------------------------

Release 2 Beta Features:
    -Patient Registration
    -View schedule/calendar
    -Create/Update appointments
    -Delete Appointment
    -Update Patient General Information
    -View Prescriptions
    -Patient Transfer
    -Update Patient Medical Info
    -View Patient Medical Info
    -Release Test Results
    -Add/Remove Patient Prescriptions
    -Update Patient Information (as a doctor)
    -View Activity Log
    -Populate Database with CSV file
    -View System Statistics
    -Administrator Registration
    -Administrator Removal
    -Admit/Discharge Patientfrom Hospital
    -Send Private Messages


Missing Features from initial Requirements Document for this Release:
    -Export Information
    -Printable Chart
    -Export schedule to iCal/Google Calendar
    

------------------------------------------------------------------------------------------------------------------------

Known Bugs and Disclaimers:
    -Password verification in registration is minimal. The prompts there are suggestions at this point.
    -Admins can delete their own account.
    -Going to other pages in the navbar from the Schedules index will not work at the moment. Go to their dashboard first and the urls are restored.
    -Hitting cancel when creating a surgery, test result, or prescription will take the user back to the splash screen.
    -As of now, the form for creating a prescription allows for negative doses.
    -The test results created cannot be seen on the profile page because they have not been approved for release by the doctor. At this point, the forms do not allow     -The MyDoctor and MyPatients links on the dashboard do not currently link to any pages, this functionality is missing
    -Support for Nurses and Nurse permissions is very minimal, many Nurse permissions were lumped in with Doctor permissions or excluded altogether
    -The medical informaion is still being linked to on the nav bar despite now being a part of a user's profile, it does not link to anything if you wish to
    view a user's medical info please view their profile
    -After creating an appointment on the appointment page you must refresh the page in order for changes to visibly appear

the doctor to toggle this but they do live in the database.
    -The doses on prescriptions are not shown properly in the patient's profiles page.
    

------------------------------------------------------------------------------------------------------------------------

Prepopulated users and their respective passwords are listed below:
    User Type: Administrator
    Username: 2BD@mail.com
    Password: 2BD

    User Type: Doctor
    Username: TestDoctor@mail.com
    Password: password

    User Type: Nurse
    Username: TestNurse@mail.com
    Password: password

    User Type: Patient
    Username: Patient0@mail.com
    Password: password

------------------------------------------------------------------------------------------------------------------------