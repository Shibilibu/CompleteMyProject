from django.db import models

class Login(models.Model):
    UserName=models.CharField(max_length=100)
    Password=models.CharField(max_length=60)
    UserType=models.CharField(max_length=100,default=1)

class InternGuide(models.Model):
    Login=models.ForeignKey(Login,default=1,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    Gender=models.CharField(max_length=60)
    Position=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Mobile=models.BigIntegerField(default=1)

class ExternalGuide(models.Model):
    Login = models.ForeignKey(Login, default=1, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=60)
    Position=models.CharField(max_length=100,default=1)
    CompanyName=models.CharField(max_length=60,default=1)
    Place=models.CharField(max_length=120,default=1)
    Post=models.CharField(max_length=100,default=1)
    Pin=models.CharField(max_length=60,default=1)
    Email = models.EmailField(max_length=100)
    Mobile = models.BigIntegerField()


class Batch(models.Model):
    Batch=models.CharField(max_length=100)



class Students(models.Model):
    Login = models.ForeignKey(Login , default=1 , on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    DOB=models.CharField(max_length=100,default=1)
    Gender=models.CharField(max_length=60)
    Education=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Mobile=models.BigIntegerField()
    std_batchid=models.ForeignKey(Batch ,default=1 ,on_delete=models.CASCADE)


class Group(models.Model):
    GroupNumber=models.CharField(max_length=60)
    Email=models.EmailField(max_length=100)
    TopicName=models.CharField(max_length=100)
    Grp_Internal_id=models.ForeignKey(InternGuide,default=1,on_delete=models.CASCADE)
    Grp_External_id=models.ForeignKey(ExternalGuide,default=1,on_delete=models.CASCADE)
    GrpBatchid=models.ForeignKey(Batch,default=1,on_delete=models.CASCADE)
    Login = models.ForeignKey(Login, default=1, on_delete=models.CASCADE)
    Status=models.CharField(max_length=100,default='Pending')


class GroupMember(models.Model):
    Studid=models.ForeignKey(Students,default=1,on_delete=models.CASCADE)
    Groupid=models.ForeignKey(Group,default=1,on_delete=models.CASCADE)


class Attendance(models.Model):
    AGroupid=models.ForeignKey(Group,default=1,on_delete=models.CASCADE)
    Date=models.CharField(max_length=100)
    File=models.FileField(max_length=100)
    Remarks=models.CharField(max_length=400,default=1)


class Schedule(models.Model):
    Date=models.DateField(max_length=100)
    Subject=models.CharField(max_length=100)
    time=models.CharField(max_length=60,default=1)
    Batchid=models.ForeignKey(Batch,default=1,on_delete=models.CASCADE)



class GroupProgress(models.Model):
    PGroupid=models.ForeignKey(Group,default=1,on_delete=models.CASCADE)
    Prgrs=models.FileField(max_length=120,default=1)
    PDate=models.CharField(max_length=100,default=1)
    GrRemarks=models.CharField(max_length=400,default=1)



class Chat(models.Model):
    Fromid=models.ForeignKey(InternGuide,default=1,on_delete=models.CASCADE)
    Toid=models.ForeignKey(ExternalGuide,default=1,on_delete=models.CASCADE)
    Message=models.CharField(max_length=120,default=1)
    Date=models.CharField(max_length=100,default=1)
    SendType=models.CharField(max_length=100,default=1)


