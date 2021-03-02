from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path('academics', views.academics , name='academics'),
    path('admissions', views.admissions , name='admissions'),
    path('students', views.students, name="students"),
    path('faculty', views.faculty, name="faculty"),


    path('tender', views.my_tender, name='tender'),
    path('teqip', views.teqip, name="teqip"),

    path('contactus', views.contactus, name="contactus"),
    path('careers', views.careers, name="careers"),
    path('rti', views.rti, name="rti"),


    path('facilities', views.facilities, name="facilities"),

    path('gallery', views.gallery, name='gallery'),
    path('noticeboard', views.my_noticeboard, name="noticeboard"),

path('events', views.Uevents, name="events"),



    path('departments', views.departments, name='departments'),

    path('Architecturesubpage', views.Architecturesubpage, name="Architecturesubpage"),
    path('Biotechnologysubpage', views.Biotechnologysubpage, name='Biotechnologysubpage'),

    path('computer_science_application', views.computer_science_application, name="computer_science_application"),

    path('ComputerScienceAndEngineering', views.ComputerScienceAndEngineering, name='ComputerScienceAndEngineering'),



    path('ElectricalEngineering', views.ElectricalEngineering, name="ElectricalEngineering"),
    path('FashionApparel', views.FashionApparel, name='FashionApparel'),

    path('InformationTechnology', views.InformationTechnology, name="InformationTechnology"),


    path('InstrumentationElectronicsEngineering', views.InstrumentationElectronicsEngineering, name='InstrumentationElectronicsEngineering'),


    path('MechanicalEngineering', views.MechanicalEngineering, name="MechanicalEngineering"),

    path('TextileEngineering', views.TextileEngineering, name='TextileEngineering'),


    path('Mathematics', views.Mathematics, name="Mathematics"),


    path('Physics', views.Physics, name='Physics'),

    path('Chemistry', views.Chemistry, name="Chemistry"),









    path('UGsyllabus', views.UGsyllabus, name='UGsyllabus'),

    path('PGsyllabus', views.PGsyllabus, name="PGsyllabus"),
    path('AcademicregulationUG', views.AcademicregulationUG, name='AcademicregulationUG'),

    path('AcademicregulationPG', views.AcademicregulationPG, name="AcademicregulationPG"),
    path('acadcalendarUGPG', views.acadcalendarUGPG, name='acadcalendarUGPG'),

    path('resultsautonomous', views.resultsautonomous, name="resultsautonomous"),
    path('examschedule', views.examschedule, name='examschedule'),

    path('phdlinks', views.phdlinks, name="phdlinks"),
    path('BOGgoverningcouncilmin', views.BOGgoverningcouncilmin, name='BOGgoverningcouncilmin'),




















    #
    #
    # path('Resultsof2ndsemesterregularIntMSCMSCMTechMPlan', views.Resultsof2ndsemesterregularIntMSCMSCMTechMPlan, name='Resultsof2ndsemesterregularIntMSCMSCMTechMPlan'),
    # path('Resultsof4thsemesterBTechBArchMCAIntMscBPlan', views.Resultsof4thsemesterBTechBArchMCAIntMscBPlan, name="Resultsof4thsemesterBTechBArchMCAIntMscBPlan"),
    # path('Resultsof6thsemesterBTechIntMscBPlanBArch', views.Resultsof6thsemesterBTechIntMscBPlanBArch, name='Resultsof6thsemesterBTechIntMscBPlanBArch'),
    # path('Resultsof2nd4thSemEvenBack', views.Resultsof2nd4thSemEvenBack, name="Resultsof2nd4thSemEvenBack"),
    # path('Rechecking_results_of_Odd_Semester', views.Rechecking_results_of_Odd_Semester, name='Rechecking_results_of_Odd_Semester'),
    # path('BTechBArchBPlan2ndSemester', views.BTechBArchBPlan2ndSemester, name="BTechBArchBPlan2ndSemester"),
    # path('MScAppliedChemistryPhysicsMathematicandComputingMasterofPlanning4thSemester1', views.MScAppliedChemistryPhysicsMathematicandComputingMasterofPlanning4thSemester1, name='MScAppliedChemistryPhysicsMathematicandComputingMasterofPlanning4thSemester1'),
    # path('MCASEMESTERREGULAR', views.MCASEMESTERREGULAR, name="MCASEMESTERREGULAR"),
    # path('MTECH4THSEMESTERBACK1', views.MTECH4THSEMESTERBACK1, name='MTECH4THSEMESTERBACK1'),
    # path('firstSemesterBackPaperResultUG', views.firstSemesterBackPaperResultUG, name="firstSemesterBackPaperResultUG"),
    # path('firstsSemesterBackPaperResultPG', views.firstsSemesterBackPaperResultPG, name='firstsSemesterBackPaperResultPG'),
    # path('thirdSemesterBackPaperResultUG', views.thirdSemesterBackPaperResultUG, name="thirdSemesterBackPaperResultUG"),
    #
    # path('ThirdSemesterBackPaperResultPG', views.thirdSemesterBackPaperResultPG, name='thirdSemesterBackPaperResultPG'),
    #
    # path('firstSemesterUG', views.firstSemesterUG, name="firstSemesterUG"),
    #
    # path('Resultof1stSemesterAutonomousPG', views.Resultof1stSemesterAutonomousPG, name='Resultof1stSemesterAutonomousPG'),
    #
    # path('Resultof3rdSemesteAutonomousUG', views.Resultof3rdSemesteAutonomousUG, name="Resultof3rdSemesteAutonomousUG"),
    #
    # path('Resultof3rSemesteAutonomousPGone', views.Resultof3rSemesteAutonomousPGone, name='Resultof3rSemesteAutonomousPGone'),
    #
    # path('Resultsof5thSemAutonomousUG', views.Resultsof5thSemAutonomousUG, name="Resultsof5thSemAutonomousUG"),
    #
    # path('Resultof5SemesterAutonomoPG', views.Resultof5SemesterAutonomoPG, name="Resultof5SemesterAutonomoPG"),
























]