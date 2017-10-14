# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.http import JsonResponse,HttpResponse
from models import yunwei_table,flag_table
import json
from django.views.decorators.csrf import csrf_exempt
dict3=list(('172.16.0.101','61d'))

teamip = [['172.16.0.1','172.16.0.1','172.16.0.1'],['172.16.0.1','172.16.0.1','172.16.0.1']]
serverip = [['172.16.0.1','172.16.0.1'],['172.16.0.1','172.16.0.1']]

@csrf_exempt
def flag(request):
    if request.method == "POST":
        flag = request.POST['flag']
        if request.META.has_key('HTTP_X_FORWARDED_FOR'):
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        print flag,ip
        return HttpResponse(1)
    else:
        return render_to_response('flag.html',{})

def index(request):
    if request.method=='GET':
        list1={}
        tmp1=[]
        tmp2=[]
        tmp3={}
        for e in range(101,113):
            tmp2.append('172.16.0.'+str(e))
        for i in range(101,113):
            dict2=[]
            ip='172.16.0.'+str(i)
            attackscore=0
            attacktime=0
            defendscore=0
            defendtime=0
            a=yunwei_table.objects.filter(timu_ip=ip).filter(timu_result=1).filter(timu_defensive=1)
            for e in a:
                attackscore+=e.timu_score
                attacktime+=1
            c=yunwei_table.objects.filter(timu_ip=ip).filter(timu_result=1).filter(timu_defensive=0)
            for m in c:
                defendscore+=m.timu_score
                defendtime+=1
            totalscore=0
            b=yunwei_table.objects.filter(timu_ip=ip).filter(timu_result=1)
            for i in b:
                totalscore+=i.timu_score
            name='61d'
            dict2=dict(attack=0,attacktimes=attacktime,attackscores=attackscore,defendtimes=defendtime,defendscores=defendscore,awardsscore=0,design=0,last_data=0,totalscores=totalscore,team_names=name)
            tmp1.append(dict2)
        list1=list(zip(tmp2,tmp1))
        list3=sorted(list1,key=lambda x:x[1]['totalscores'],reverse=True)
        dict_tmp={'result':list3}
        return JsonResponse(dict_tmp,status=200)

def notice(request):
    if request.method=='GET':
        all_ip=[]
        for i in range(101,113):
            all_ip.append('172.16.0.'+str(i))
        tmp=[]
        tmp1=[]
        date=[]
        defensive=[]
        score=[]
        for i in all_ip:
            a=yunwei_table.objects.filter(timu_ip=i).filter(timu_result=1)
            for e in a:
                date.append(e.timu_date)
                defensive.append(e.timu_defensive)
                score.append(e.timu_score)
            name='61d'
            for n in range(len(date)):
                p=dict(name_ip=name,date_answer=date[n],if_defensive=defensive[n],scores=score[n])
                tmp1.append(p)
        tmp=sorted(tmp1,key=lambda x:x['date_answer'])
        return HttpResponse(tmp[:11],status=200)

def teaminfo(request):
    if request.method=='GET':
        a = list(('172.16.0.101:', '61d'))
        return HttpResponse(a,status=200)


