from datetime import time, datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, request, JsonResponse
from django.shortcuts import render, redirect

from completemyproject.models import Login, InternGuide, ExternalGuide, Students, Batch, Group, GroupMember, Attendance, \
    GroupProgress, Schedule, Chat


def Login_(request):
    return render(request,'Mainpage/index.html')

def Login_post(request):
    un=request.POST['Username']
    ps=request.POST['pass']
    data=Login.objects.filter(UserName=un,Password=ps)
    if data.exists():
        data = data[0]
        if data.UserType == 'Admin':
                return redirect('/AdminHomepage')
        if data.UserType == 'Internal':
                request.session['lid'] = data.id
                return redirect('/InternalHomepage')

        if data.UserType == 'External':
                request.session['lid'] = data.id
                return redirect('/ExternalHomePage')

        if data.UserType == 'Group' :
                request.session['lid'] = data.id
                return  redirect('/GroupHomepage')


        return HttpResponse("<script>alert('Successfully LoggedIn');window.location='/'</script>")

    else:

        return HttpResponse("<script>alert('Invalid User');window.location='/'</script>")

##################################Admin#########################################################################################

def AdminHomepage(request):
    return render(request,'Admin/AdminHome.html')

def AddGuide(request):
    return render(request,'Admin/AddingGuide.html')

def AddGuide_post(request):
    nm=request.POST['name']
    gn=request.POST['Gender']
    pos=request.POST['position']
    pas=request.POST['Pass']
    em=request.POST['email']
    mob=request.POST['mobile']


    obj1=Login()
    obj1.UserName=em
    obj1.Password=pas
    obj1.UserType='pending'
    obj1.save()

    obj=InternGuide()
    obj.Name=nm
    obj.Gender=gn
    obj.Position=pos
    obj.Email=em
    obj.Mobile=mob

    obj.save()

    return HttpResponse("<script>alert('Successfully Added');window.location='/AddGuide'</script>")

def ViewGuide(request):
    view=InternGuide.objects.all()
    return render(request,'Admin/ViewInternal_Guide.html',{'view':view})

def EditGuide(request,eid):
    edit=InternGuide.objects.get(id=eid)
    return render(request,'Admin/EditGuide.html',{'edit':edit})

def EditGuide_post(request,eid):
    nm = request.POST['name']
    gn = request.POST['gender']
    pos = request.POST['position']
    pas = request.POST['Pass']
    em = request.POST['email']
    mob = request.POST['mobile']
    InternGuide.objects.filter(id=eid).update(Name=nm,Gender=gn,Position=pos,Password=pas,Email=em,Mobile=mob)
    return HttpResponse ("<script>alert('Edited Successfully');window.location='/ViewGuide'</script>")

def DeleteGuide(request,did):
    InternGuide.objects.get(id=did).delete()
    return HttpResponse ("<script>alert('Deleted Successfully');window.location='/ViewGuide'</script>")

def AddExternal(request):
    return render(request,'Admin/AddingOrganization.html')

def AddExternal_post(request):
    nam=request.POST['name']
    gen=request.POST['Gender']
    post=request.POST['position']
    cn=request.POST['Cnm']
    plc=request.POST['place']
    pst=request.POST['Post']
    pn=request.POST['pin']
    pasw=request.POST['Pass']
    eml=request.POST['email']
    mobl=request.POST['mobile']
    obj=Login()
    obj.UserName=eml
    obj.Password=pasw
    obj.UserType='pending'
    obj.save()

    obj2=ExternalGuide()
    obj2.Name=nam
    obj2.Gender=gen
    obj2.Position=post
    obj2.CompanyName=cn
    obj2.Place=plc
    obj2.Post=pst
    obj2.Pin=pn
    obj2.Email=eml
    obj2.Mobile=mobl
    obj2.Login = obj
    obj2.save()

    return HttpResponse("<script>alert('Added Successfully');window.location='/AddExternal'</script>")

def ViewExternal(request):
    external=ExternalGuide.objects.all()
    return render(request,'Admin/ViewExternal.html',{'external':external})

def EditExternal(request,edid):
    edit=ExternalGuide.objects.get(id=edid)
    return render(request,'Admin/EditExternal.html',{'edit':edit})

def EditExternal_post(request,edid):
    nam = request.POST['name']
    gen = request.POST['Gender']
    post = request.POST['position']
    cn = request.POST['Cnm']
    plc = request.POST['place']
    pst = request.POST['Post']
    pn = request.POST['pin']
    pasw = request.POST['Pass']
    eml = request.POST['email']
    mobl = request.POST['mobile']

    ExternalGuide.objects.filter(id=edid).update(Name=nam,Gender=gen,Position=post,CompanyName=cn,Place=plc,Post=pst,Pin=pn,Password=pasw,Email=eml,Mobile=mobl)
    return HttpResponse("<script>alert('Edited Successfully');window.location='/ViewExternal'</script>")

def DeleteExternal(request,deid):
    ExternalGuide.objects.get(id=deid).delete()
    return HttpResponse("<script>alert('Deleted Successfully');window.location='/ViewExternal'</script>")

def Batch_student(request):
    return render(request,'Admin/Batch.html')

def Batch_student_post(request):
    btch=request.POST['btch']
    obj=Batch()
    obj.Batch=btch
    obj.save()
    return HttpResponse("<script>alert('Batch Added Successfully');window.location='/Batch_student'</script>")




def AddStudent(request):
    data=Batch.objects.all()
    return render(request,'Admin/AddStudents.html',{'data':data})

def AddStudent_post(request):
    nme=request.POST['name']
    gend=request.POST['Gender']
    dob=request.POST['DOB']
    btch=request.POST['Batch']
    ed=request.POST['Education']
    email=request.POST['email']
    Pas=request.POST['Pass']
    Mob=request.POST['mobile']

    obj3=Login()
    obj3.UserName=email
    obj3.Password=Pas
    obj3.UserType='Pending'
    obj3.save()

    obj2=Batch()
    obj2.Batch=btch


    obj=Students()
    obj.Name=nme
    obj.Gender=gend
    obj.DOB=dob
    obj.Education=ed
    obj.Email=email
    obj.Mobile=Mob
    obj.Login = obj3
    obj.save()
    return HttpResponse("<script>alert('Added Successfully');window.location='/AddStudent'</script>")


def ViewStudent(request):
    students=Students.objects.all()
    return render(request,'Admin/ViewStudent.html',{'students':students})

def EditStudent(request,stid):
    data=Students.objects.get(id=stid)
    data1 = Batch.objects.all()
    return render(request,'Admin/EditStudent.html',{'data':data,'data1':data1})

def EditStudent_post(request,stid):
    me = request.POST['name']
    gend = request.POST['Gender']
    dob = request.POST['DOB']
    btch = request.POST['Batch']
    ed = request.POST['Education']
    email = request.POST['email']
    Mob = request.POST['mobile']

    Students.objects.filter(id=stid).update(Name=me,Gender=gend,DOB=dob,Batch=btch,Education=ed,Email=email,Mobile=Mob)
    return HttpResponse("<script>alert('Edited Successfully');window.location='/ViewStudent'</script>")


def DeleteStudent(request,sdid):
    Students.objects.get(id=sdid).delete()
    return HttpResponse("<script>alert('Deleted Successfully');window.location='/ViewStudent'</script>")

def AddGroup(request):
    data=InternGuide.objects.all()
    # data1=ExternalGuide.objects.all()
    data1=Batch.objects.all()

    return render(request,'Admin/AddGroup.html',{'data':data,'data1':data1})


def AddGroup_post(request):
    grp=request.POST['Number']
    tn=request.POST['topic']
    eml=request.POST['Email']
    pas=request.POST['Pass']
    bt=request.POST['Batch']
    obj2=Batch()
    obj2.Batch=bt

    obj1=Login()
    obj1.UserName=eml
    obj1.Password=pas
    obj1.UserType='Pending'
    obj1.save()

    obj=Group()
    obj.GroupNumber=grp
    obj.TopicName=tn
    obj.Email=eml
    obj.save()
    return HttpResponse("<script>alert('Added Successfully');window.location='/AddGroup'</script>")

def ViewGroup(request):
    group=Group.objects.all()
    return render(request,'Admin/ViewGroup.html',{'group':group})


def EditGroup(request,gid):
    edit=Group.objects.get(id=gid)
    return render(request,'Admin/EditGroup.html',{'edit':edit,'gid':gid})

def EditGroup_post(request,gid):
    grp = request.POST['Number']
    tn = request.POST['topic']
    eml = request.POST['Email']

    Group.objects.filter(id=gid).update(GroupNumber=grp,TopicName=tn,Email=eml)
    return HttpResponse("<script>alert('Edited Successfully');window.location='/ViewGroup'</script>")


def DeleteGroup(request,did):
    Group.objects.get(id=did).delete()
    return HttpResponse("<script>alert('Deleted Successfully');window.location='/ViewGroup'</script>")


def AddMembers(request,gid):
    member=Students.objects.all()
    return render(request,'Admin/Addmembers.html',{'member':member,"gid":gid})

def AddMembers_post(request,gid):
    mb=request.POST['member']
    c=GroupMember.objects.filter(Groupid = gid)
    print(c.count())
    if c.count() <=3:
        obj = GroupMember()
        obj.Studid = Students.objects.get(id=mb)
        obj.Groupid = Group.objects.get(id=gid)
        obj.save()
        return HttpResponse("<script>alert('Added Successfully');window.location='/ViewGroup'</script>")

    else:
        return HttpResponse("<script>alert(' Already Add Maximum ,You cant proceed');window.location='/ViewGroup'</script>")

def AllocationExternal(request,aid):
    allo=ExternalGuide.objects.all()
    return render(request,'Admin/ExternalGuideAllocation.html',{'data':allo,'id':aid})

def Allocation_post(request,aid):
    res=request.POST['External']
    Group.objects.filter(id=aid).update(Grp_External_id=res,Status='Allocated')


    return HttpResponse("<script>alert('Added Successfully');window.location='/ViewGroup'</script>")





def ViewAttendance(request):
    bat=Batch.objects.all()
    return render(request,'Admin/ViewAttendance.html',{'bat':bat})

def attendanceadmin(request):
    grp=request.POST['GRP']
    att=Attendance.objects.filter(AGroupid=grp)
    print(att)
    return render(request,'Admin/ViewAttendance.html',{'att':att})

def group(request,gpid):
    gp=Group.objects.filter(id=gpid)
    return render(request,'Admin/group.html',{'gp':gp})

# def remark(request,rid):
#     return render(request,'Admin/remarks.html',{'rid':rid})
#
# def remark_post(request,rid):
#     rm=request.POST['rem']
#     Attendance.objects.filter(id=rid).update(Remarks=rm)
#     return HttpResponse("<script>alert('Successfully added remark');windows.location ='/attendanceadmin'</script>")




def ViewProgress(request):
    pr=Batch.objects.all()
    return render(request,'Admin/ViewProgress.html',{'pr':pr})

def adminprogress_post(request):
    fl = request.POST['GRP']
    data = GroupProgress.objects.filter(PGroupid=fl)
    return render(request, 'Admin/ViewProgress.html', {'data': data})


def progresslist(request,pid):
    data=Group.objects.filter(id=pid)
    return render(request,'Admin/progresslist.html',{'data':data})

# def progressremarks(request,prid):
#     return render(request,'Admin/ProgressRemarks.html',{'prid':prid})
#
# def progressremarks_post(request,prid):
#     prm=request.POST['re']
#     GroupProgress.objects.filter(id=prid).update(GrRemarks=prm)
#     return HttpResponse("<script>alert('Successfully added remark');windows.location ='/ViewProgress'</script>")


def AddScheduleSubmission(request):
    batch=Batch.objects.all()
    return render(request,'Admin/AddSubmissionSchedule.html',{'batch':batch})

def AddScheduleSubmisssion_post(request):
    sub=request.POST['Subject']
    dt=request.POST['date']
    tim=request.POST['time']
    bt = request.POST['Batch']

    obj2=Batch()
    obj2.Batch=bt
    obj2.save()

    obj=Schedule()
    obj.Subject=sub
    obj.Date=dt
    obj.time=tim
    obj.Batchid_id=bt
    obj.save()
    return HttpResponse("<script>alert('Added Successfully');window.location='/AddScheduleSubmission'</script>")


def ViewScheduleSubmission(request):
    ViewShedule=Schedule.objects.all()
    return render(request,'Admin/ViewSubmissionSchedule.html',{'ViewShedule':ViewShedule})


def EditScheduleSubmission(request,edid):
    edit=Schedule.objects.get(id=edid)
    return render(request,'Admin/EditSubmissionSchedule.html',{'edit':edit,'edid':edid})

def EditScheduleSubmission_post(request,edid):
    sub = request.POST['Subject']
    dt = request.POST['date']
    Schedule.objects.filter(id=edid).update(Subject=sub,Date=dt)
    return HttpResponse("<script>alert('Edited Successfully');window.location='/ViewScheduleSubmission'</script>")

def DeleteSchedule(request,did):
    Schedule.objects.get(id=did).delete()
    return HttpResponse("<script>alert('Deleted Successfully');window.location='/ViewScheduleSubmission'</script>")
####################################Internal Guide#############################################################################

def InternalHomepage(request):
    return render(request,'Guide/InternalsHome.html')

def ViewAssignedGrp(request):
    # viewassigned=InternGuide.objects.get(Login=request.session['lid'])
    v=InternGuide.objects.get(Login=request.session['lid'])
    print(v,"iiiiiiiii")

    view=Group.objects.filter(Grp_Internal_id=v)
    return render(request,'Guide/ViewAssignedGroup.html',{'view':view})

def ViewExternalOrg(request):
    externalorg=ExternalGuide.objects.all()
    return render(request,'Guide/ViewExtorg.html',{'externalorg':externalorg})

def Assign_groupsto_external(request,gpid):
    assign=Group.objects.all()
    return render(request,'Guide/AssignGroup.html',{'assign':assign,'gpid':gpid})

def Assign_groupsto_external_post(request,gpid):
    grp = request.POST['Number']
    tn = request.POST['topic']
    eml = request.POST['Email']
    ExternalGuide.objects.filter(Login=request.session['lid'])
    Group.objects.filter(id=gpid).update(GroupNumber=grp,TopicName=tn,Email=eml)
    return HttpResponse("<script>alert('Added Successfully');window.location='/ViewExternalOrg'</script>")



def ViewAttendanceInternal(request):
    btch= Batch.objects.all()
    return render(request,'Guide/ViewAttendanceIntrernal.html',{'btch':btch})

def attendance(request):
    grp=request.POST['GRPs']
    att=Attendance.objects.filter(AGroupid=grp)
    print(att)
    return render(request,'Guide/ViewAttendanceIntrernal.html',{'att':att})

def viewGroup(request,gid):
    grps=Group.objects.filter(id=gid)
    return render(request,'Guide/grouplist.html',{'grps':grps})

def internal_attendanceremarks(request,aid):
    return render(request,'Guide/remarksinternal.html',{'aid':aid})

def internal_attendanceremarks_post(request,aid):
    rm=request.POST['rem']
    Attendance.objects.filter(id=aid).update(Remarks=rm)
    return HttpResponse("<script>alert('Successfully Added Remarks');window.location='/ViewAttendanceInternal'<script>")

def ViewProgressInternal(request):
    bt=Batch.objects.all()
    return render(request,'Guide/ProgressViewIntern.html',{'bt':bt})

def Viewprogressgroup(request,vid):
    data=Group.objects.filter(id=vid)
    return render(request,'Guide/progressgrouplist.html',{'data':data})

def viewprogress_post(request):
    gr=request.POST['GRP']
    pr=GroupProgress.objects.filter(PGroupid=gr)
    return render(request,'Guide/ProgressViewIntern.html',{'pr':pr})

def remarks_progressInternal(request,rid):
    return render(request,'Guide/InternalProgressRemarks.html',{'rid':rid})

def remarks_progressInternal_post(request,rid):
    rms=request.POST['re']
    GroupProgress.objects.filter(id=rid).update(GrRemarks=rms)
    return HttpResponse("<script>alert('Successfully Added Remarks');window.location='/ProgressViewIntern'<script>")

def ViewSchedule(request):
    schedule=Schedule.objects.all()
    return render(request,'Guide/ViewProjectSchedule.html',{'schedule':schedule})

def send(request):
    data=Chat.objects.all()
    return render(request,'Guide/Chat.html',{'data':data})

def Sendmessage(request):
    msg=request.POST['msge']
    import datetime
    dt = datetime.datetime.now().strftime("%Y-%m-%d")
    obj=Chat()
    obj.Message=msg
    obj.Date=dt
    obj.SendType='Internal'
    obj.save()
    return redirect('/send')


##################################################ExternalOrganization########################################################


def ExternalHomePage(request):
    return render(request,'Organization/ExtetrnalHome.html')


def ViewGroups(request):
    group=Group.objects.all()
    return render(request,'Organization/ViewGroupExternals.html',{'group':group})


def AttendenceUpdate(request,aid):
    Group.objects.get(id=aid)
    return render(request,'Organization/UpdateAttendanceExternals.html',{'aid':aid})

def AttendenceUpdate_post(request,aid):
    fl=request.FILES['Attandence']
    fs = FileSystemStorage()
    import datetime
    d = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    fs.save(r"C:\Users\shibil\PycharmProjects\project\completemyproject\static\Files\\" + d + '.pdf', fl)
    filefolder = "/static/Files/" + d + '.pdf'
    res=Group.objects.get(id=aid)
    dt = datetime.datetime.now().strftime("%Y-%m-%d")
    obj=Attendance()
    obj.Date=dt
    obj.File=filefolder
    obj.AGroupid=res
    obj.save()

    return HttpResponse("<script>alert('File Added Successfully');window.location='/ViewGroups'</script>")


def Workprogress(request,wid):
    Group.objects.get(id=wid)
    return render(request,'Organization/WorkProgress.html',{'wid':wid})

def Workprogress_post(request,wid):
    pr=request.FILES['progress']
    fs = FileSystemStorage()
    import datetime
    d = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    fs.save(r"C:\Users\shibil\PycharmProjects\project\completemyproject\static\Files\\" + d + '.pdf', pr)
    ProgressFile = "/static/Files/" + d + '.pdf'
    prgr=Group.objects.get(id=wid)
    dt = datetime.datetime.now().strftime("%Y-%m-%d")
    obj=GroupProgress()
    obj.PDate=dt
    obj.Prgrs=ProgressFile
    obj.PGroupid=prgr
    obj.save()
    return HttpResponse("<script>alert('File Added Successfully');window.location='/ViewGroups'</script>")

def ProjectSchedule(request):
    schedule=Schedule.objects.all()
    return  render(request,'Organization/ViewProjectScheduleExternal.html',{'schedule':schedule})

def ShareFiles(request):
    data=Attendance.objects.all()
    data1=GroupProgress.objects.all()
    return render(request,'Organization/ShareFiles.html',{'data':data,'data1':data1})

def ShareFiles_post(request):
    atd=request.POST['Atnd']
    prgs=request.POST['Progress']
    obj=Attendance()
    obj.File=atd
    obj.save()
    obj1=GroupProgress()
    obj1.Prgrs=prgs
    obj1.save()

def ChatwithInternals(request,cid):
    msg=Chat.objects.filter(Fromid=InternGuide.objects.get(id = cid),Toid=ExternalGuide.objects.get(Login=Login.objects.get(id = request.session['lid'])))
    return render(request,'Organization/ChatwithInternal.html',{'data':msg,"cid":cid})

def ChatwithInternals_post(request,cid):
    ms = request.POST['msg']
    import datetime
    dt = datetime.datetime.now().strftime("%Y-%m-%d")
    obj = Chat()
    obj.Fromid=InternGuide.objects.get(id = cid)
    obj.Date = dt
    obj.Message = ms
    obj.SendType = 'External'
    obj.Toid=ExternalGuide.objects.get(Login=request.session['lid'])
    obj.save()
    return redirect('/ChatwithInternals/'+cid)


#################################Group####################################################################################


def GroupHomepage(request):
    return render(request,'Group/GroupHome.html')


def ViewInternals(request):
    intern=InternGuide.objects.all()
    return render(request,'Group/ViewInternalGuideGrp.html',{'intern':intern})

def ViewProjectSchedule(request):
    project=Schedule.objects.all()
    return render(request,'Group/GroupViewProject.html',{'project':project})



################################Public###############################################################

def ListOfProjects(request):
    projects=Group.objects.all()
    return render(request,'Public/ListOfProjects.html',{'projects':projects})




###################################Android############################################################

def And_login(request):
    usn=request.POST['uname']
    pswd=request.POST['pswd']

    data=Login.objects.filter(UserName=usn,Password=pswd)

    if data.exists():
        data=data[0]
        data1 = Group.objects.get(Login=data.id)
        return JsonResponse({"status": "ok","type":"Group",'lid':data.id,'names':data1.TopicName,'emails':data1.Email})
    else:
        return JsonResponse({"status":"no"})


##############################Group################################################################

def View_projectSchedule(request):
    ed = request.POST['id']
    qry=Group.objects.get(Login=ed)
    ig=Schedule.objects.filter(Batchid=qry.GrpBatchid)
    ar=[]
    for i in ig:
        ar.append({
            'id':i.id,
            'Date':i.Date,
            'Subject':i.Subject,

        })

    return JsonResponse({"status": "ok",'data':ar})




def View_Internal(request):
    lg=request.POST['id']
    print(lg)
    # qry=Group.objects.get(Login=lg)
    gd=Group.objects.get(Login=lg)
    data = {'lid':gd.Grp_Internal_id.id,'Name':gd.Grp_Internal_id.Name,'Gender':gd.Grp_Internal_id.Gender,'Position':gd.Grp_Internal_id.Position,'Email':gd.Grp_Internal_id.Email,'Mobile':gd.Grp_Internal_id.Mobile}
    return JsonResponse({"status": "ok", 'data':data})



def View_allProjects(request):
    pr=Group.objects.all()
    print(pr)
    ls=[]
    for i in pr:
        ls.append({
            'id':i.id,
            'TopicName':i.TopicName,

            }
        )
    return JsonResponse({"status":"ok",'data':ls})
    print(ls)


def View_AllSchedule(request):
    pr = Schedule.objects.all()
    ls = []
    for i in pr:
        ls.append({
            'id': i.id,
            'Date': i.Date,
            'Subject':i.Subject,

        }
        )
    return JsonResponse({"status": "ok", 'data': ls})


def connect(request):
    return JsonResponse({"status": "ok"})


# def log(request):
#     return JsonResponse({"status": "ok"})




# def check(request):
#     return JsonResponse({"status": "ok"})