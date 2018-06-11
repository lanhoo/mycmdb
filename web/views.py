from django.shortcuts import render, HttpResponse
from django.http.response import JsonResponse
from django.views.generic.base import View
import json


# Create your views here.
def hello(request):
    return render(request, 'hello.html')


def jsonpost(request):
    data_list = [
        {
            'q': 'id',
            'title': 'ID',
            'display': False,
            'text': {},
            'attrs': {}
        },
        {
            'q': 'device_type_id',
            'title': '资产类型',
            'display': True,
            'text': {'content': "{n}", 'kwargs': {'n': "@@device_type_choices"}},
            'attrs': {}
        },
        {
            'q': 'device_status_id',
            'title': '状态',
            'display': True,
            'text': {'content': "{n}", 'kwargs': {'n': "@@device_status_choices"}},
            'attrs': {'edit-enable': 'true', 'edit-type': 'select'}
        },
        {
            'q': 'idc__name',
            'title': 'IDC',
            'display': True,
            'text': {'content': "{n}", 'kwargs': {'n': "@idc__name"}},
            'attrs': {'edit-enable': 'true', 'edit-type': 'select'}
        },
        {
            'q': 'cabinet_order',
            'title': '机柜位置',
            'display': True,
            'text': {'content': "{n}", 'kwargs': {'n': "@cabinet_order"}},
            'attrs': {'edit-enable': 'true', 'edit-type': 'input'}
        },
        {
            'q': 'cabinet_num',
            'title': '机柜号',
            'display': True,
            'text': {'content': "{n}", 'kwargs': {'n': "@cabinet_num"}},
            'attrs': {},
        },
        {
            'q': None,
            'title': '操作',
            'display': True,
            'text': {'content': "<a href='/assetdetail-{m}.html'>{n}</a>", 'kwargs': {'n': '查看详细', 'm': '@id'}},
            'attrs': {},
        }
    ]

    return HttpResponse(json.dumps(data_list))


class Json_post(View):
    def get(self, request):
        data_list = [
            {
                'q': 'id',
                'title': 'ID',
                'display': False,
                'text':{},
                'attrs': {}
            },
            {
                'q': 'device_type_id',
                'title': '资产类型',
                'display': True,
                'text': {'content': "{n}", 'kwargs': {'n': "@@device_type_choices"}},
                'attrs': {}
            },
            {
                'q': 'device_status_id',
                'title': '状态',
                'display': True,
                'text': {'content': "{n}", 'kwargs': {'n': "@@device_status_choices"}},
                'attrs': {'edit-enable': 'true', 'edit-type': 'select'}
            },
            {
                'q': 'idc__name',
                'title': 'IDC',
                'display': True,
                'text': {'content': "{n}", 'kwargs': {'n': "@idc__name"}},
                'attrs': {'edit-enable': 'true', 'edit-type': 'select'}
            },
            {
                'q': 'cabinet_order',
                'title': '机柜位置',
                'display': True,
                'text': {'content': "{n}",'kwargs': {'n': "@cabinet_order"}},
                'attrs': {'edit-enable': 'true', 'edit-type': 'input'}
            },
            {
                'q': 'cabinet_num',
                'title': '机柜号',
                'display': True,
                'text': {'content': "{n}", 'kwargs': {'n': "@cabinet_num"}},
                'attrs': {},
            },
            {
                'q': None,
                'title': '操作',
                'display': True,
                'text': {'content': "<a href='/assetdetail-{m}.html'>{n}</a>", 'kwargs': {'n': '查看详细','m': '@id'}},
                'attrs': {},
            }
        ]
        q_list = []
        for i in data_list:
            # if not i['q']:
            #     continue
            # q_list.append(i['q'])
            if i['q']:
                q_list.append(i['q'])

        from web import models

        ret_list = list(models.Asset.objects.all().values(*q_list))
        # print(ret_list)
        # return JsonResponse({'ret_list':ret_list, 'conf_list':'data_list'})
        # print('jsre:', JsonResponse({'ret_list': ret_list, 'conf_list': data_list}))
        # print('httpre:', HttpResponse(json.dumps({'ret_list': ret_list, 'conf_list': data_list})))

        # return HttpResponse(json.dumps({'ret_list': ret_list, 'conf_list': data_list}))
        # print(ret_list)
        return JsonResponse({
            'ret_list': ret_list,
            'conf_list': data_list,
            'global_dict': {
                'device_type_choices': models.Asset.device_type_choices,
                'device_status_choices': models.Asset.device_status_choices,
            }
        })
