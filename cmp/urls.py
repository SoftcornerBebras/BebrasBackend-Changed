from django.contrib import admin
from django.urls import path,re_path
from . import views as cpviews
from rest_framework.schemas import get_schema_view
from .api import *

urlpatterns = [
      path('insertMcqQues/',cpviews.InsertMcqQuestion.as_view()),
     path('insertMcqWithImgsQues/',cpviews.InsertMcqWithImagesQuestion.as_view()),
     path('getCompetition/',cpviews.GetCompetition.as_view()),
     path('getYears/',cpviews.GetDistinctYears.as_view()),
     re_path('getCompetitionSchoolWise/(?P<schoolID>\d+)/$',cpviews.GetCompetitionSchoolWise.as_view()),
     re_path('getNotStartedCmp/(?P<schoolID>\d+)/$',cpviews.GetNotStartedCompetitionSchoolWise.as_view()),
     re_path('getCompetitionYearWise/(?P<year>[\w.@+-]+)/$',cpviews.GetCmpYearWise.as_view()),
     re_path('getAgeGrpCmpWise/(?P<cmpID>\d+)/$',cpviews.GetAgeGrpCmpWise.as_view()),
     re_path('viewSchoolStudentsCmpWise/(?P<schoolID>\d+)&(?P<cmpID>\d+)/$',cpviews.GetSchoolStudentsCmpWise.as_view()),
     re_path('viewSchoolStudentsDetailCmpWise/(?P<schoolID>\d+)&(?P<cmpID>\d+)/$',cpviews.GetSchoolStudentsDetailCmpWise.as_view()),
     re_path('getSchoolStudentsCmpWise/(?P<schoolID>\d+)&(?P<cmpID>\d+)/$',cpviews.DownloadSchoolStudentsCmpWise.as_view()),
     re_path('getTotalMarks/(?P<cmpID>\d+)&(?P<ageID>\d+)/$',cpviews.GetTotalMarks.as_view()),
     re_path('getAllSchoolStudents/(?P<schoolID>\d+)/$', cpviews.GetAllSchoolStudents.as_view()),
     re_path('getCountryWiseStudents/(?P<cmpID>\d+)&(?P<AgeID>\d+)&(?P<countryID>\d+)/$',cpviews.GetCountryWiseStudents.as_view()),
     re_path('getCountryWiseToppers/(?P<cmpID>\d+)&(?P<AgeID>\d+)&(?P<countryID>\d+)/$',cpviews.GetCountryWiseToppers.as_view()),
     re_path('getStateWiseStudents/(?P<cmpID>\d+)&(?P<AgeID>\d+)&(?P<countryID>[\w.@+-]+)&(?P<stateID>\d+)/$',
            cpviews.GetStateWiseStudents.as_view()),
     re_path('getDistrictWiseStudents/(?P<cmpID>\d+)&(?P<AgeID>\d+)&(?P<countryID>\d+)&(?P<stateID>\d+)&(?P<districtID>\d+)/$',
        cpviews.GetDistrictWiseStudents.as_view()),
     re_path('getSchoolGroupWiseStudents/(?P<cmpID>\d+)&(?P<AgeID>\d+)&(?P<codeID>\d+)/$',
        cpviews.GetSchoolGroupWiseStudents.as_view()),
     re_path('getSchoolTypeWiseStudents/(?P<cmpID>\d+)&(?P<AgeID>\d+)&(?P<codeID>\d+)/$',
        cpviews.GetSchoolTypeWiseStudents.as_view()),
     re_path('getAgeGrpWise/(?P<cmpID>\d+)&(?P<AgeID>\d+)&(?P<schoolID>\d+)/$',cpviews.GetStudentsAgeGroupWise.as_view()),
     re_path('getAgeGrpWiseToppers/(?P<cmpID>\d+)&(?P<AgeID>\d+)&(?P<schoolID>\d+)/$',cpviews.GetStudentsAgeGroupWiseToppers.as_view()),
     re_path('getAllStudentsSchoolWise/(?P<schoolID>\d+)/$', cpviews.GetAllStudentsSchoolWise.as_view()),
     re_path('getAllRegisteredStudentsSchoolWise/(?P<schoolID>\d+)/$', cpviews.GetAllRegisteredStudentsSchoolWise.as_view()),
     re_path('updateQuestion/(?P<questionTranslationID>\d+)/$',cpviews.UpdateQuestionView.as_view()),
     path('insertTranslation/',cpviews.InsertTranslation.as_view()),
     re_path('getAgeGroupsPerQues/(?P<questionID>\d+)/$',cpviews.ViewAgeGroupsPerQues.as_view()),
     re_path('getQuesUsage/(?P<quesID>\d+)/$',cpviews.QuesUsage.as_view()),
     re_path('getQuesAge/(?P<AgeID>\d+)&(?P<cmpID>\d+)/$',cpviews.GetquesAge.as_view()),
     re_path('getQuesAgeAll/(?P<AgeID>\d+)/$',cpviews.GetquesAgeAll.as_view()),
     re_path('getCmpQues/(?P<AgeID>\d+)&(?P<cmpID>\d+)/$',cpviews.GetcmpQues.as_view()),
     re_path('getCmpPreview/(?P<AgeID>\d+)&(?P<cmpID>\d+)/$',cpviews.GetcmpPreview.as_view()),
     re_path('getClassAgeWise/(?P<AgeID>\d+)/$',cpviews.GetClassAgeGrpWise.as_view()),
     re_path('getAgeCmpWise/(?P<cmpID>\d+)/$',cpviews.GetAgeGrpCmpWise.as_view()),
     re_path('getClassWiseAgeGroup/(?P<cmpID>\d+)&(?P<Class>\d+)',cpviews.GetClassWiseAgeGroup.as_view()),
     re_path('getMarksAgeCmpWise/(?P<AgeID>\d+)&(?P<cmpID>\d+)/$',cpviews.GetMarksAgeWise.as_view()),
     re_path('getStudentsAgeGrpWise/(?P<AgeID>\d+)&(?P<cmpID>\d+)/$',cpviews.GetAllStudentsAgeGroupWise.as_view()),
     re_path('getStateWiseMean/(?P<AgeID>\d+)&(?P<cmpID>\d+)/$',cpviews.GetStateWiseMean.as_view()),
     re_path('getParticipationCertificates/(?P<cmpID>\d+)&(?P<schoolClassID>\d+)/$',cpviews.GetParticipationCertificates.as_view()),
     re_path('getSchoolTopperCertificates/(?P<cmpID>\d+)&(?P<AgeID>\d+)&(?P<schoolID>\d+)/$',cpviews.GetSchoolToppers.as_view()),
     re_path('getNationalTopperCertificates/(?P<cmpID>\d+)&(?P<AgeID>\d+)&(?P<countryID>\d+)/$',cpviews.GetNationalToppers.as_view()),
     re_path('deleteFiles/(?P<schoolID>\d+)&(?P<class>\d+)&(?P<group>[\w.@+-]+)&(?P<year>[\w.@+-]+)&(?P<CertificateType>[\w.@+-]+)', cpviews.deleteFiles.as_view()),
     path('viewAgeGroup/',cpviews.GetAgeGroups.as_view()),
     path('bulkUploadQuestions/',cpviews.BulkUploadQuestion.as_view()),
     path('insertMarkScheme/',cpviews.InsertMarkingSchemeView.as_view()),
     path('insertAgeGroups/',cpviews.InsertAgeGrpView.as_view()),
     path('insertCmp/',cpviews.InsertCompetition.as_view()),
     path('insertCmpAge/',cpviews.InsertOnlyCmpAge.as_view()),
     path('insertCmpQues/',cpviews.InsertCmpQues.as_view()),
     path('updateCmp/',cpviews.UpdateCmp.as_view()),
     path('deleteCmpQues/',cpviews.DeleteCmpQues.as_view()),
     path('addCmpQues/',cpviews.AddCmpQues.as_view()),
     path('updateAgeGrp/',cpviews.UpdateAgeGrp.as_view()),
     path('checkUpdateAgeGrp/',cpviews.CheckAgeGrp.as_view()),
     path('updateMarks/',cpviews.UpdateMarkingScheme.as_view()),
     path('customizePPT/',cpviews.CustomizePPT.as_view()),
     re_path('getLatestTemplate/(?P<type>[\w.@+-]+)',cpviews.GetLatestTemplate.as_view()),
     path('removeStudents/',cpviews.RemoveParticipants.as_view()),
     path('rollBackQuestion/',cpviews.RollbackQuestion.as_view()),
     path('rollBackQuestionTranslation/',cpviews.RollbackQuestionTranslation.as_view()),
     #userportal
    path('cmpnames', getCompetitionAPI.as_view()),
    path('getcmp', getCmpQuestionAPI.as_view()),
    path('getactivecmpnames', getActiveCompetitionAPI.as_view()),
    path('getcmpResults', getCmpResultsAPI.as_view()),
    path('getcmpnamesResults', getCompetitionsNamesForResultAPI.as_view()),
    path('getcmpnamesAnalysis', getCompetitionsNamesForAnalysisAPI.as_view()),
    path('savedstudentResponse', getAlreadySavedResponse.as_view()),
    path('studentResponseFromExcel', studentResponseFromExcelAPI.as_view()),
    path('validateOfflineUpload', validateOfflineUpload.as_view()),
    path('studentResponse', studentResponseAPI.as_view()),
    path('calcTotalScore', calcTotalScore.as_view()),
    path('getLang', LanguageAPI.as_view()),
    path('GetSchoolClassStudents', GetSchoolClassStudents.as_view()),
    path('GetStudentsAgeGroupWise', GetStudentsAgeGroupWise.as_view()),
    path('SchoolTopperCertificates',GetSchoolToppers.as_view()),
    path('GetParticipationCertificatesforStudentPortal',GetParticipationCertificatesforStudentPortal.as_view()),
    path('GetParticipationCertificatesforSelectedStudents',GetParticipationCertificatesforSelectedStudents.as_view()),
    path('GetAgeGroupToppers',GetAgeGroupToppers.as_view()),
    path('getpracticeChallengeNames', practiceChallengeNames.as_view()),
    path('getPracChallengeQuestionAPI', PracChallengeQuestionAPI.as_view()),
    path('deleteFilesandZip',deleteFiles.as_view()),
    path('ParticipationCertificates',GetParticipationCertificates.as_view()),
]
