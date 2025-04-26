from django.shortcuts import render
from django.http import HttpResponse
from compar.models import Comparision
import google.generativeai as genai
import PIL.Image
import json
from django.shortcuts import render
import google.generativeai as genai
import json
from PIL import Image
import imagehash
from django.core.files.storage import default_storage
from django.db.models import Q


# from django.shortcuts import render
# from .form import CoinSearchForm
# from compar.models import Coin
 

def home(request):
    if request.method == "POST":
        try:
            image_name = request.POST.get('image_name')
            currency = request.POST.get('currency')
            country = request.POST.get('country')
            coin_rupee_value = request.POST.get('coin_rupee_value')
            coin_year = request.POST.get('coin_year')
            coin_mint_marks = request.POST.get('coin_mint_marks')
            coin_mint_marks_city = request.POST.get('coin_mint_marks_city')
            color = request.POST.get('color')
            shape = request.POST.get('shape')
            which_metal_body = request.POST.get('which_metal_body')
            coin_symbol = request.POST.get('coin_symbol')
            reverse_symbol = request.POST.get('reverse_symbol')
            weight = request.POST.get('weight')
            size = request.POST.get('size')
            image = request.FILES.get('image') 

            savedata = Comparision(
                image_name=image_name,
                currency=currency,
                country=country,
                coin_rupee_value=coin_rupee_value,
                coin_year=coin_year,
                coin_mint_marks=coin_mint_marks,
                coin_mint_marks_city=coin_mint_marks_city,
                color=color,
                shape=shape,
                which_metal_body=which_metal_body,
                coin_symbol=coin_symbol,
                reverse_symbol=reverse_symbol,
                weight=weight,
                size=size,
                image=image
            )
            savedata.save()
            print("DATA INSERTED SUCCESSFULLY")
        except Exception as e:
            print(f"Error while saving data: {e}")
    
    return render(request, "index.html")



def compare_image(request):
    matched_obj = None
    result = None

    if request.method == "POST":
        try:
            uploaded_image = request.FILES['compare_image']
            uploaded_image_obj = Image.open(uploaded_image)
            uploaded_hash = imagehash.average_hash(uploaded_image_obj)

            for obj in Comparision.objects.all():
                stored_image_path = obj.image.path
                stored_image_obj = Image.open(stored_image_path)
                stored_hash = imagehash.average_hash(stored_image_obj)

                if uploaded_hash - stored_hash < 5:
                    matched_obj = obj
                    result = "Match found"
                    break
            else:
                result = "No matching image found."

        except Exception as e:
            result = f"Error: {e}"

    return render(request, "match.html", {"result": result, "matched_obj": matched_obj})




def find(request):
    coin_data = None  
    image_url = None

    if request.method == "POST":
        genai.configure(api_key="AIzaSyCZ6o4aTitS0QPSOi6wgAe5sBIEc7rxc-M")  # Put in env var in prod
        model = genai.GenerativeModel('gemini-2.0-flash')

        uploaded_file = request.FILES.get("image")
        if uploaded_file:
            file_name = default_storage.save(f"coins/{uploaded_file.name}", uploaded_file)
            image_url = default_storage.url(file_name)

            try:
                image = PIL.Image.open(uploaded_file)

                prompt = ("this image to find which currency, Country, Coin Rupee Value (if applicable), "
                          "coin year, coin mint marks, coin mint marks city, color, shape, which metal body, "
                          "coin symbol, reverse symbol,weight,size. Output the information in JSON format.")

                response = model.generate_content([prompt, image])
                response_text = response.text.strip()

                if response_text.startswith("```json"):
                    response_text = response_text[7:-3].strip()
                
                try:
                    coin_data = json.loads(response_text)
                    coin_data["image_name"] = uploaded_file.name

                    # Optional: Save the JSON to a file
                    with open("info.json", "w", encoding="utf-8") as f:
                        json.dump(coin_data, f, indent=4, ensure_ascii=False)
                    print("Coin data saved to info.json")

                except json.JSONDecodeError:
                    print("Model response not valid JSON.")
                    print(response_text)

            except Exception as e:
                print(f"Error processing image: {e}")

    return render(request, "find.html", {"coin_data": coin_data, "image_url": image_url})


# def search_coins(request):
#     form = CoinSearchForm(request.GET or None)
#     coins = None
#     if form.is_valid():
#         filters = {f"{field}__icontains": value for field, value in form.cleaned_data.items() if value}
#         coins = Coin.objects.filter(**filters)
#     return render(request, 'alldata.html', {'form': form, 'coins': coins})

def alldata(request):
    return render(request, 'alldata.html',)


# def search_by_field(request):
#     results = None
#     query = None

#     if request.method == "POST":
#         query = request.POST.get('search_query')
#         search_field = request.POST.get('search_field')

#         if query and search_field:
#             filter_kwargs = {f"{search_field}__icontains": query}
#             results = Comparision.objects.filter(**filter_kwargs)

#     return render(request, "search.html", {"results": results, "query": query})


def search_by_field(request):
    results = None
    query = None
    search_field = None

    if request.method == "POST":
        query = request.POST.get('search_query')
        search_field = request.POST.get('search_field')

        if query and search_field:
            filter_kwargs = {f"{search_field}__icontains": query}
            results = Comparision.objects.filter(**filter_kwargs)
            print(f"Searching for {search_field} = {query}")
            print("Results count:", results.count())

    return render(request, "search_results.html", {
        "results": results,
        "query": query,
        "search_field": search_field
    })


def search_form(request):
    return render(request, "search.html")
