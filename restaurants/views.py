from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context ={ 
        "my_list":[


        {
        
            "restaurant_name":"a",
            "food_type":"fast food"

        },
        {
        
            "restaurant_name":"b",
            "food_type":"fast food"

        },
        {
        
            "restaurant_name":"c",
            "food_type":"fast food"

        }
    ]}
    return render(request, 'list.html', context)


def restaurant_detail(request):
    context = {
    "my_object" : {
        "restaurant_name":"a",
        "food_type":"fast food"
    }}
    return render(request, 'detail.html', context)
