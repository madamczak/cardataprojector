from django.shortcuts import render, redirect

from cars.models import Brand, Car
from cars.operations.db_operations import DataBase


def home_page(request):
    brandNames = set([brand.brandName for brand in Brand.objects.all()])

    rows = Car.objects.all()

    if request.method == "POST":
        cbn = request.POST.get('brand_item', "")

        #note the replacement
        cbn = cbn.replace(" ", "_")

        return redirect("/cars/%s" % cbn)
    return render(request, 'home.html', {'brands': brandNames})



def view_brand_data(request, brand_name):
    #refactor this
    if request.method == "POST":
        if request.POST.get('back', "") == 'reset':
            return redirect("/")
        else:
            cmi = request.POST.get('model_item', "")
            if cmi != "--":
                return redirect("/cars/%s/%s" % (brand_name.replace(" ", "_"), cmi))
            else:
                return redirect("/")


    modelNames = set([brand.modelName for brand in Brand.objects.filter(brandName=brand_name)])

    bds = Brand.objects.filter(brandName=brand_name)

    rows = set()
    for brand in bds:
        rows.update(Car.objects.filter(B_Id=brand.B_Id))

    avgMileage = int(sum([car.mileage for car in rows]) / len(rows))
    avgPrice = int(sum([car.price for car in rows]) / len(rows))

    #note the replacement in brand name
    return render(request, 'brand.html', {'items': rows,
                                          'chosen_brand': brand_name.replace("_", " "),
                                          'models': modelNames,
                                          'averageMileage': avgMileage,
                                          'averagePrice': avgPrice})

def view_model_data(request, brand_name, model_name):
    #refactor this
    if request.method == "POST":
        if request.POST.get('back', "") == 'reset':
            return redirect("/")
        elif request.POST.get('back', "") == 'back1':
            return redirect("/cars/%s" % brand_name)
        else:
            cmi = request.POST.get('version_item', "")
            if cmi != "--":
                return redirect("/cars/%s/%s/%s/" % (brand_name, model_name.replace(" ", "_"), cmi.replace(" ", "_")))
            else:
                return redirect("/")

    versionNames = set([brand.version for brand in Brand.objects.filter(modelName=model_name)])

    mds = Brand.objects.filter(modelName=model_name)

    rows = set()

    for model in mds:
        rows.update(Car.objects.filter(B_Id=model.B_Id))

    avgMileage = int(sum([car.mileage for car in rows]) / len(rows))
    avgPrice = int(sum([car.price for car in rows]) / len(rows))

    return render(request, 'model.html', {'items': rows, 'chosen_brand': brand_name,
                                          'chosen_model': model_name.replace(" ", "_"),
                                          'versions': versionNames,
                                          'averageMileage': avgMileage,
                                          'averagePrice': avgPrice})


def view_version_data(request, brand_name, model_name, version_name):

    if request.method == "POST":
        if request.POST.get('back', "") == 'reset':
            return redirect("/")
        elif request.POST.get('back', "") == 'back1':
            return redirect("/cars/%s" % brand_name)
        elif request.POST.get('backmodel', "") == 'back2':
            return redirect("/cars/%s/%s" % (brand_name, model_name))


    version = Brand.objects.get(version=version_name.replace("_", " "), modelName=model_name)

    rows = set()

    cars = Car.objects.filter(B_Id=version.B_Id)

    rows.update(cars)

    avgMileage = int(sum([car.mileage for car in cars])/len(cars))
    avgPrice = int(sum([car.price for car in cars])/len(cars))

    return render(request, 'version.html', {'items': rows, 'chosen_brand': brand_name,
                                            'chosen_model': model_name,
                                            'chosen_version': version_name.replace("_", " "),
                                            'averageMileage': avgMileage,
                                            'averagePrice': avgPrice})
