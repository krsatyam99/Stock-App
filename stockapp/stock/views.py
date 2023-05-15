from django.http import HttpResponse
from django.shortcuts import render
# from yahoo_fin import 
from yahoo_fin.stock_info import get_quote_table
from yahoo_fin.stock_info import *
import pandas as pd
import time
import queue
from threading import Thread


# Create your views here.
def stockspicker(request):
    stock_picker =tickers_nifty50()
    print(stock_picker)
    return render(request,'stock/picker.html',{'stockpicker':stock_picker})


def stockstracker(request):     #change in stock_info.py
    stocks_picker =request.GET.getlist('stockpicker')
    # details=get_quote_table('AAPL')
    # details = pd.concat(details, axis=1)
    print((stocks_picker))
    data = {}
    available_stocks = tickers_nifty50()
    for i in stocks_picker:
        if i in available_stocks:
            details=get_quote_table(i)
            data[i] = details
        else:
            return HttpResponse("Error")
    n_threads =len(stocks_picker)    
    thread_list =[]
    start= time.time()
    print(start)
    # for i in stocks_picker:
    #     details=get_quote_table(i)
    #     data.update({i:details})
    que = queue.Queue()
    start = time.time()
    # for i in stockpicker:
    #     result = get_quote_table(i)
    #     data.update({i: result})
    for i in range(n_threads):
        thread = Thread(target = lambda q, arg1: q.put({stocks_picker[i]: get_quote_table(arg1)}), args = (que, stocks_picker[i]))
        thread_list.append(thread)
        thread_list[i].start()
    for thread in thread_list:
        thread.join()

    while not que.empty():
        result = que.get()
        data.update(result)
    end= time.time()
    time_taken= end-start
    print(time_taken)
    print(end)
    print(data)
    return render(request,'stock/tracker.html',{"data":data,"room_name":"track"})
# def stockstracker(request):
#     stocks_picker = request.GET.getlist('stockpicker')
#     data = {}
#     available_stocks = tickers_nifty50()
#     for i in stocks_picker:
#         if i in available_stocks:
#             details = get_quote_table(i)
#             # Renaming the columns of the DataFrame to make them consistent
#             details = details.rename(columns={'Attribute': 'attribute', 'Value': 'value'})
#             data[i] = details
#         else:
#             return HttpResponse("Error")

#     print(data)
#     return render(request,'stock/tracker.html', {'data': data})

