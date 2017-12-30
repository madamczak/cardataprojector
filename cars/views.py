from django.shortcuts import render, redirect

import sqlite3
from cars.models import Brand
from cars.operations.db_operations import DataBase


def home_page(request):
    database = DataBase("refactor_test6.db")
    brandIds = database.getAllParsedBrandsIds()
    brandNames = set()
    for brandId in brandIds:
        name = database.getBrandInfo(brandId)[0].capitalize()
        if name == "Bmw":
            brandNames.add("BMW")
        elif name == "Pozostae":
            pass
        elif name == "Mercedes-benz":
            brandNames.add("Mercedes-Benz")
        elif name == "Rolls-royce":
            brandNames.add("Mercedes-Benz")
        elif name == "Land rover":
            brandNames.add("Land Rover")
        elif name == "Alfa romeo":
            brandNames.add("Alfa Romeo")
        else:
            brandNames.add(name)
    #[database.getBrandInfo(brandId)[0].capitalize() for brandId in brandIds]

    if request.method == "POST":
        cbn = request.POST.get('brand_item', "")
        return redirect("/cars/%s" % cbn)
    return render(request, 'home.html', {'brands': brandNames})



def view_brand_data(request, brand_name):
    if request.method == "POST":
        if request.POST.get('back', "") == 'reset':
            return redirect("/")
        else:
            cmi = request.POST.get('model_item', "")
            if cmi != "--":
                return redirect("/cars/%s/%s" % (brand_name, cmi))
            else:
                return redirect("/")



    database = DataBase("refactor_test6.db")

    modelIds = database.getAllBrandIdsOfBrand(brand_name)
    modelNames = set()
    for modelid in modelIds:
        name = database.getBrandInfo(modelid)[1].capitalize()
        modelNames.add(name.replace(" ", "_"))

    if brand_name == "Land":
        rows = database.getAllCarsOfBrand("Land Rover")
        brand_name = "Land Rover"
    elif brand_name == "Alfa":
        rows = database.getAllCarsOfBrand("Alfa Romeo")
        brand_name = "Alfa Romeo"
    else:
        rows = database.getAllCarsOfBrand(brand_name)


    #modelids = database.getAllBrandIdsOfBrand(brand_name)


    #rows = database.getAllCarsOfBrand(brand_name)
    return render(request, 'brand.html', {'items': rows, 'chosen_brand': brand_name, 'models': modelNames})

def view_model_data(request, brand_name, model_name):
    if request.method == "POST":
        if request.POST.get('back', "") == 'reset':
            return redirect("/")
        elif request.POST.get('back', "") == 'back1':
            return redirect("/cars/%s" % brand_name)
        else:
            cmi = request.POST.get('version_item', "")
            if cmi != "--":
                return redirect("/cars/%s/%s/%s/" % (brand_name, model_name, cmi))
            else:
                return redirect("/")

    database = DataBase("refactor_test6.db")

    rows = database.getAllCarsOfModel(model_name.replace("_", " "))

    verIds = database.getAllBrandIdsOfModel(model_name.replace("_", " ") )

    versionNames = set()
    for vid in verIds:
        vinfo = database.getBrandInfo(vid)
        if len(vinfo) > 2:
            print vinfo[2]
            versionNames.add(vinfo[2].replace(" ", "_"))

    return render(request, 'model.html', {'items': rows, 'chosen_brand': brand_name, 'chosen_model': model_name, 'versions': versionNames})


def view_version_data(request, brand_name, model_name, version_name):

    if request.method == "POST":
        if request.POST.get('back', "") == 'reset':
            return redirect("/")
        elif request.POST.get('back', "") == 'back1':
            return redirect("/cars/%s" % brand_name)
        elif request.POST.get('backmodel', "") == 'back2':
            return redirect("/cars/%s/%s" % (brand_name, model_name))
        else:
            cmi = request.POST.get('version_item', "")
            if cmi != "--":
                return redirect("/cars/%s/%s/%s/" % (brand_name, model_name.replace(" ", "_"), cmi))
            else:
                return redirect("/")

    database = DataBase("refactor_test6.db")

    rows = database.getAllCarsOfVersion(model_name.replace("_", " "), version_name.replace("_", " ").capitalize())

    print



    return render(request, 'version.html', {'items': rows, 'chosen_brand': brand_name, 'chosen_model': model_name, 'chosen_version': version_name})
