from django.db import models
from django.utils import timezone
from smart_selects.db_fields import ChainedForeignKey,  ChainedManyToManyField, GroupedForeignKey

def one_day_hence():
    return timezone.now() + timezone.timedelta(days=1)


class Application(models.Model):
    Application_Name = models.CharField(max_length=500,default="")
    Description = models.CharField(max_length=500,default="")
    Version = models.CharField(max_length=500,default="")
    OS = 'OS'
    App = 'App'
    Antivir = 'Antivir'
    Util = 'Util'
    APPLICATION_TYPE = (
        (OS, 'Operating System'),
        (App, 'Application'),
        (Antivir, 'Anti Virus'),
        (Util, 'Utility'),
    )
    Type = models.CharField(
        max_length=100,
        choices=APPLICATION_TYPE,
        default=App,
    )
    RegisteredDate = models.DateTimeField(default=timezone.now)
    DeclaredUser = models.CharField(max_length=500,default="")
    RevisedDate = models.DateTimeField(null=True,default=one_day_hence)
    Application_Provider = models.CharField(max_length=500,default="")
    Storage_Location = models.URLField(max_length=100,default="")
    License = models.CharField(max_length=50,default="")
    Installed_User = models.CharField(max_length=500,default="")
    Reviewed_User = models.CharField(max_length=500,default="")
    def __str__(self):
        return self.Application_Name

class Zone(models.Model):
    Zone_Name = models.CharField(max_length=500,default="")
    BPCS = 'BCPS'
    SIS = 'SIS'
    PIZ = 'PIZ'
    CN = 'CN'
    OZ = 'OZ'
    DMZ = 'DMZ'
    CCR = 'CCR'
    VPN = 'VPN'
    ZoneType_List = (
        (BPCS, 'Basic Control Process System Zone'),
        (SIS, 'Safety Instrumented Systems Zone'),
        (PIZ, 'Plant Information Zone'),
        (OZ, 'Other Zone'),
        (CN,'Corporate Network'),
        (DMZ,'DMZ Zone'),
        (CCR,'CCR Zone'),
        (VPN,'VPN Zone'),

      )
    Zone_Type = models.CharField(
        max_length=50,
        choices=ZoneType_List,
        default=BPCS,
    )
    RegisteredDate = models.DateTimeField(default=timezone.now)
    ResponsibleUser = models.CharField(max_length=500,default="")
    ReviewedDate = models.DateTimeField(null=True,default=one_day_hence)
    def __str__(self):
                return self.Zone_Name

class Asset(models.Model):
    Asset_Name = models.CharField(max_length=500,default="")
    Zone = models.ForeignKey('Zone',null=True,default="")
    WS = 'WS'
    SV = 'SV'
    RT = 'RT'
    PT = 'PT'
    OT = 'OT'
    Asset_List = (
        (WS, 'Work Station'),
        (SV, 'Server'),
        (RT, 'Router'),
        (PT, 'Printer'),
        (OT,'Other')

       ) 
    Asset_Type = models.CharField(
        max_length=50,
        choices=Asset_List,
        default=WS,
    )

    Operating_Sytem = models.CharField(max_length=200,default="")
    Version = models.CharField(max_length=200)
    Application= models.ManyToManyField(Application,default="")
    Connect_To = models.ForeignKey('Asset',null=True,blank=True)
    RegisteredDate = models.DateTimeField(default=timezone.now)
    ReviewedDate = models.DateTimeField(null=True,default=one_day_hence)
    ResponsibleUser = models.CharField(max_length=500,default="")

    def __str__(self):
                return self.Asset_Name



class Conduit(models.Model):
    Name = models.CharField(max_length=500,default="")
    From_Zone = models.ForeignKey('Zone',null=True,blank=True,related_name='+')
    To_Zone = models.ForeignKey('Zone',null=True,blank=True)
    IC = 'IC'
    EC = 'EC'
    Type_List = (
        (IC,'Internal Conduit'),
        (EC,'External Conduit'),
    ) 
    Type = models.CharField(max_length=10,choices = Type_List,default = IC
    )
    ConnectionType = models.CharField(max_length=500,default="")
    ConnectionPort = models.IntegerField(default=0)
    TCP_IP = 'TCP/IP'
    MB = 'MB'
    Protocol_List=(
           (TCP_IP,'TCP/IP'),
           (MB,'Modbus') 
     )
    Protocol = models.CharField(max_length=10,choices= Protocol_List,default=TCP_IP)
    RegisteredDate = models.DateTimeField(default=timezone.now)
    ReviewedDate = models.DateTimeField(null=True,default=one_day_hence)
    ResponsibleUser = models.CharField(max_length=500,default="")
    def __str__(self):
        return self.Name



class Risk(models.Model):
    Risk_Name = models.CharField(max_length=500,default="",unique=True)
    Description = models.CharField(max_length=2000,default="")
    SE = 'SE'
    PH = 'PH'
    MW = 'MW'
    UACC = 'UACC'
    UA = 'UA'
    UD ='UD'
    Threat_List = (
        (SE,'Social Engineering'),
        (PH,'Phishing'),
        (MW,'Malware'),
        (UACC,'Unauthorised access'),
        (UA,'Unauthorised actions'),
        (UD,'Unauthorised data transfer'),

    )  
    Threat_Name = models.CharField(max_length=100,choices=Threat_List,default=MW)
    Zone = models.ForeignKey(Zone)
    Asset = ChainedForeignKey(
        'Asset',
        chained_field="Zone",
        chained_model_field="Zone",
        show_all=True,
        auto_choose=True)
    FREQ = 'FREQ'
    PRO = 'PRO'
    OCC = 'OCC'
    REM= 'REM'
    IMP = 'IMP'
    INC = 'INC'
    Category_List = (
        (FREQ,'Frequent - Many times in system lifetime (Range > 10^-3)'),
        (PRO,'Probable - Several times in system lifetime (10^-3 < Range <  10^-4)'),
        (OCC,'Occasional - Once in system lifetime (10^-4 < Range < 10^-5)'),
        (REM,'Remote - Unlikely in system lifetime (10^-5 < Range < 10^-6) '),
        (IMP,'Improbable - Very unlikely to occur (10^-6 < Range < 10^-7)'),
        (INC,'Incredible - Cannot believe that it could occur (Range < 10^-7)')
    )

    Likelihood = models.CharField(max_length=50,choices=Category_List,default=FREQ)
    CAT = 'CAT'
    CRI = 'CRI'
    MAR = 'MAR'
    NEG = 'NEG'
    Consequence_List = (
        (CAT,'Catastrophic - Multiple loss of life'),
        (CRI,'Catastrophic - Loss of a single life'),
        (MAR,'Major injuries to one or more persons'),
        (NEG,'Minor injuries at worst')
        )

    Consequence = models.CharField(max_length=50,choices=Consequence_List,default=NEG)
    Responsible_Person = models.CharField(max_length=500,default="")
    Date_of_risk_assessment = models.DateTimeField(default=timezone.now)
    Reviewed_date = models.DateTimeField(null=True,default=one_day_hence)
  

class CounterMeasure(models.Model):
    Name = models.CharField(max_length=500,default="")
    IR = 'IR'
    AU = 'AU'
    AC = 'AC'
    Counter_List = (
        (IR,'Inherent Resilience'),
        (AU,'Authentication and Authorization Technologies'),
        (AC,'Filtering/Blocking/Access Control Technologies'),
        )
    Counter_Type = models.CharField(max_length=10,choices = Counter_List,verbose_name='Counter Measure Category')
    Description = models.CharField(max_length=2000,default="")
    Risk = models.ForeignKey(Risk)
    Responsible_Person =  models.CharField(max_length=200,default="")
    RegisteredDate = models.DateTimeField(default=timezone.now)
    ReviewedDate = models.DateTimeField(null=True,default=one_day_hence)

