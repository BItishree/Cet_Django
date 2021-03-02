from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.



def home(request):
    return render(request, 'index.html')
def academics(request):
    return render(request,'Academics.html')
def admissions(request):
    return render(request,'Admissions.html')
def students(request):
    return render(request,'students.html')
def faculty(request):
    return render(request,'faculty.html')


def my_tender(request):
    tenders = tender.objects.all()
    return render(request, 'tender.html', {'tenders': tenders})

def teqip(request):
    return render(request, 'teqip.html')
def gallery(request):
    return render(request,'gallery.html')


def contactus(request):
    return render(request, 'contactus.html')
def careers(request):
    car = careerDB.objects.all()
    return render(request,'careers.html',{'careers':car})
def rti(request):
    return render(request,'RTI.html')
def facilities(request):
    return render(request,'facilities.html')



def Uevents(request):
    events=upcomingeventss.objects.all()
    return render(request,'UpcomingEvents.html',{'events': events})



def my_noticeboard(request):
    posts = noticeboard.objects.all()
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request,'NoticeBoard.html',{'posts': posts})





def departments(request):
    return render(request,'departments.html')

def Architecturesubpage(request):
    return render(request,'Architecturesubpage.html')


def Biotechnologysubpage(request):
    return render(request, 'Biotechnologysubpage.html')


def computer_science_application(request):
    return render(request, 'computer_science_application.html')


def ComputerScienceAndEngineering(request):
    return render(request,'ComputerScienceAndEngineering.html')
def ElectricalEngineering(request):
    return render(request,'ElectricalEngineering.html')


def FashionApparel(request):
    return render(request,'FashionApparel.html')
def InformationTechnology(request):
    return render(request,'InformationTechnology.html')





def InstrumentationElectronicsEngineering(request):
    return render(request, 'InstrumentationElectronicsEngineering.html')


def MechanicalEngineering(request):
    return render(request, 'MechanicalEngineering.html')

def TextileEngineering(request):
    return render(request, 'TextileEngineering.html')

def Mathematics(request):
    return render(request, 'Mathematics.html')


def Physics(request):
    return render(request, 'Physics.html')

def Chemistry(request):
    return render(request, 'Chemistry.html')








def UGsyllabus(request):
    return render(request, 'UGsyllabus.html')

def PGsyllabus(request):
    return render(request, 'PGsyllabus.html')

def AcademicregulationUG(request):
    return render(request, 'AcademicregulationUG.html')

def AcademicregulationPG(request):
    return render(request, 'AcademicregulationPG.html')



def acadcalendarUGPG(request):
    acad= acadcalendar.objects.all()
    return render(request, 'acadcalendarUGPG.html',{'acad': acad})


def resultsautonomous(request):
    res = result.objects.all()
    return render(request, 'resultsautonomous.html',{'res':res})

def examschedule(request):
    sce = scedule.objects.all()
    return render(request, 'examschedule.html',{'scedule': sce})

def phdlinks(request):
    return render(request, 'phdlinks.html')

def BOGgoverningcouncilmin(request):
    return render(request, 'BOGgoverningcouncilmin.html')






#
# def Resultsof2ndsemesterregularIntMSCMSCMTechMPlan(request):
#     return render(request, 'Resultsof2ndsemesterregularIntMSCMSCMTechMPlan.html')
#
#
# def Resultsof4thsemesterBTechBArchMCAIntMscBPlan(request):
#     return render(request, 'Resultsof4thsemesterBTechBArchMCAIntMscBPlan.html')
#
#
# def Resultsof6thsemesterBTechIntMscBPlanBArch(request):
#     return render(request, 'Resultsof6thsemesterBTechIntMscBPlanBArch.html')
#
# def Resultsof2nd4thSemEvenBack(request):
#     return render(request, 'Resultsof2nd4thSemEvenBack.html')
#
#
# def Rechecking_results_of_Odd_Semester(request):
#     return render(request, 'Rechecking_results_of_Odd_Semester.html')
# def BTechBArchBPlan2ndSemester(request):
#     return render(request, 'BTechBArchBPlan2ndSemester.html')
#
# def MScAppliedChemistryPhysicsMathematicandComputingMasterofPlanning4thSemester1(request):
#     return render(request, 'MScAppliedChemistryPhysicsMathematicandComputingMasterofPlanning4thSemester1.html')
#
#
# def MCASEMESTERREGULAR(request):
#     return render(request, 'MCASEMESTERREGULAR.html')
#
# def MTECH4THSEMESTERBACK1(request):
#     return render(request, 'MTECH4THSEMESTERBACK1.html')
#
# def firstSemesterBackPaperResultUG(request):
#     return render(request, 'firstSemesterBackPaperResultUG.html')
#
#
# def firstsSemesterBackPaperResultPG(request):
#     return render(request, 'firstsSemesterBackPaperResultPG.html')
# def thirdSemesterBackPaperResultUG(request):
#     return render(request, 'thirdSemesterBackPaperResultUG.html')
#
# def thirdSemesterBackPaperResultPG(request):
#     return render(request, 'ThirdSemesterBackPaperResultPG.html')
#
#
# def firstSemesterUG(request):
#     return render(request, 'firstSemesterUG.html')
#
# def Resultof1stSemesterAutonomousPG(request):
#     return render(request, 'Resultof1stSemesterAutonomousPG.html')
#
# def Resultof3rdSemesteAutonomousUG(request):
#     return render(request, 'Resultof3rdSemesteAutonomousUG.html')
#
# def Resultof3rSemesteAutonomousPGone(request):
#     return render(request, 'Resultof3rSemesteAutonomousPGone.html')
#
# def Resultsof5thSemAutonomousUG(request):
#     return render(request, 'Resultsof5thSemAutonomousUG.html')
#
# def Resultof5SemesterAutonomoPG(request):
#     return render(request, 'Resultof5SemesterAutonomoPG.html')


