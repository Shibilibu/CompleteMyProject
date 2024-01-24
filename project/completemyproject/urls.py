"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from completemyproject import views

urlpatterns = [
    path('', views.Login_),
    path('Login_post', views.Login_post),
    ######################Admin########################################################################################
    path('AdminHomepage',views.AdminHomepage),
    path('AddGuide', views.AddGuide),
    path('AddGuide_post', views.AddGuide_post),
    path('ViewGuide', views.ViewGuide),
    path('EditGuide/<eid>',views.EditGuide),
    path('EditGuide_post/<eid>',views.EditGuide_post),
    path('DeleteGuide/<did>',views.DeleteGuide),
    path('AddExternal',views.AddExternal),
    path('AddExternal_post',views.AddExternal_post),
    path('ViewExternal',views.ViewExternal),
    path('EditExternal/<edid>',views.EditExternal),
    path('EditExternal_post/<edid>',views.EditExternal_post),
    path('DeleteExternal/<deid>',views.DeleteExternal),
    path('AddStudent',views.AddStudent),
    path('AddStudent_post',views.AddStudent_post),
    path('ViewStudent',views.ViewStudent),
    path('EditStudent/<stid>',views.EditStudent),
    path('EditStudent_post/<stid>',views.EditStudent_post),
    path('DeleteStudent/<sdid>',views.DeleteStudent),
    path('Batch_student',views.Batch_student),
    path('Batch_student_post',views.Batch_student_post),
    path('AddGroup',views.AddGroup),
    path('AddGroup_post',views.AddGroup_post),
    path('ViewGroup',views.ViewGroup),
    path('EditGroup/<gid>',views.EditGroup),
    path('EditGroup_post/<gid>',views.EditGroup_post),
    path('DeleteGroup/<did>',views.DeleteGroup),
    path('AddMembers/<gid>',views.AddMembers),
    path('AddMembers_post/<gid>',views.AddMembers_post),
    path('AllocationExternal/<aid>',views.AllocationExternal),
    path('Allocation_post/<aid>',views.Allocation_post),
    path('ViewAttendance',views.ViewAttendance),
    path('group/<gpid>',views.group),
    path('attendanceadmin',views.attendanceadmin),
    path('ViewProgress',views.ViewProgress),
    path('progresslist/<pid>',views.progresslist),
    path('adminprogress_post',views.adminprogress_post),
    path('AddScheduleSubmission',views.AddScheduleSubmission),
    path('AddScheduleSubmisssion_post',views.AddScheduleSubmisssion_post),
    path('ViewScheduleSubmission',views.ViewScheduleSubmission),
    path('EditScheduleSubmission/<edid>',views.EditScheduleSubmission),
    path('EditScheduleSubmission_post/<edid>',views.EditScheduleSubmission_post),
    path('DeleteSchedule/<did>',views.DeleteSchedule),
    # path('remark/<rid>',views.remark),
    # path('remark_post/<rid>',views.remark_post),
    # path('progressremarks/<prid>',views.progressremarks),
    # path('progressremarks_post/<prid>',views.progressremarks_post),
#######################################Internal Guide##########################################################################

    path('InternalHomepage',views.InternalHomepage),
    path('ViewAssignedGrp',views.ViewAssignedGrp),
    path('ViewExternalOrg',views.ViewExternalOrg),
    path('Assign_groupsto_external/<gpid>',views.Assign_groupsto_external),
    path('Assign_groupsto_external_post/<gpid>',views.Assign_groupsto_external_post),
    path('ViewAttendanceInternal',views.ViewAttendanceInternal),
    path('ViewProgressInternal',views.ViewProgressInternal),
    path('ViewSchedule',views.ViewSchedule),
    path('send',views.send),
    path('Sendmessage',views.Sendmessage),
    path('viewGroup/<gid>',views.viewGroup),
    path('attendance',views.attendance),
    path('Viewprogressgroup/<vid>',views.Viewprogressgroup),
    path('viewprogress_post',views.viewprogress_post),
    path('internal_attendanceremarks/<aid>',views.internal_attendanceremarks),
    path('internal_attendanceremarks_post/<aid>',views.internal_attendanceremarks_post),
    path('remarks_progressInternal/<rid>',views.remarks_progressInternal),
    path('remarks_progressInternal_post/<rid>',views.remarks_progressInternal_post),
    # path('AttendanceSearch',views.AttendanceSearch),
    # path('AttendanceSearch_post',views.AttendanceSearch_post),


######################################External Organization########################################################

    path('ExternalHomePage', views.ExternalHomePage),
    path('ViewGroups',views.ViewGroups),
    path('AttendenceUpdate/<aid>',views.AttendenceUpdate),
    path('AttendenceUpdate_post/<aid>',views.AttendenceUpdate_post),
    path('Workprogress/<wid>',views.Workprogress),
    path('Workprogress_post/<wid>',views.Workprogress_post),
    path('ProjectSchedule', views.ProjectSchedule),
    path('ShareFiles',views.ShareFiles),
    path('ChatwithInternals/<cid>',views.ChatwithInternals),
    path('ChatwithInternals_post/<cid>',views.ChatwithInternals_post),
##################################Group###########################################################################3
    path('GroupHomepage',views.GroupHomepage),
    path('ViewInternals',views.ViewInternals),
    path('ViewProjectSchedule',views.ViewProjectSchedule),





#######################Public###########################################################################
    path('ListOfProjects',views.ListOfProjects),


    #########################Android####################################################
    path('And_login',views.And_login),
    path('View_projectSchedule',views.View_projectSchedule),
    # path('View_Schedule',views.View_Schedule),
    path('View_Internal',views.View_Internal),
    path('View_allProjects',views.View_allProjects),
    path('View_AllSchedule',views.View_AllSchedule),
    # path('check',views.check),
    path('connect', views.connect),
    # path('log',views.log)


]



