import re
from django.http import JsonResponse
from django.shortcuts import render , get_object_or_404, redirect
from .models import Product , Category
from .forms import ProductForm , CategoryForm

from django.db.models import Count

import re
from django.http import JsonResponse
from .models import Product
from django.db.models import Sum

def dashboard_view(request):
    # מוצרים במלאי נמוך
    low_stock = Product.objects.filter(quantity__lt=10)

    # מוצרים פופולריים
    top_selling = Product.objects.order_by('-quantity')[:5]

    # מכירות לפי קטגוריה
    sales_by_category = (
        Product.objects.values('category__name')
        .annotate(total_sales=Sum('quantity'))
        .order_by('-total_sales')
    )

    context = {
        'low_stock': low_stock,
        'top_selling': top_selling,
        'sales_by_category': sales_by_category,
    }
    return render(request, 'inventory/dashboard.html', context)
def sales_by_category_api(request):
    sales_by_category = (
        Product.objects.values('category__name')
        .annotate(total_sales=Sum('quantity'))
        .order_by('-total_sales')
    )
    return JsonResponse(list(sales_by_category), safe=False)

def index(request):
    products = Product.objects.all()
    print(products)
    return render(request, 'inventory/index.html', {'products': products})



def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'inventory/add_product.html', {'form': form})
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoryForm()
    return render(request, 'inventory/add_category.html', {'form': form})

# דף למחיקת מוצר
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('index')
    return render(request, 'inventory/delete_product.html', {'product': product})


def product_list(request):
    categories = Product.objects.values('category__name').annotate(total=Count('id')).order_by('category__name')

    category_names = [category['category__name'] for category in categories]
    product_counts = [category['total'] for category in categories]

    return render(request, 'product_list.html', {
        'category_names': category_names,
        'product_counts': product_counts
    })




def chat_api(request):
    message = request.GET.get('message', '').lower()

    # תשובה ברירת מחדל
    response = "מצטער, לא הבנתי את השאלה."

    # חיפוש עבור המוצר המומלץ
    if "מה המוצר המומלץ" in message or "איזה מוצר כדאי" in message:
        # חיפוש המוצר עם הכמות הגבוהה ביותר (לדוגמה)
        recommended_product = Product.objects.order_by('-quantity').first()  # מוצר עם המלאי הגבוה ביותר
        if recommended_product:
            response = f"המוצר המומלץ ביותר הוא {recommended_product.name} עם {recommended_product.quantity} יחידות במלאי."
        else:
            response = "לא נמצאו מוצרים במערכת."

    # חיפוש עבור שאלות על שם מוצר ספציפי
    elif "מוצר" in message:
        # חיפוש שם מוצר מהשאלה
        product_name_match = re.search(r"\bמ(ה)?\s?([א-ת\s]+)\b", message)
        if product_name_match:
            product_name = product_name_match.group(2).strip()
            try:
                product = Product.objects.get(name__icontains=product_name)
                response = f"מלאי המוצר {product.name} הוא {product.quantity} יחידות."
            except Product.DoesNotExist:
                response = f"לא מצאתי מוצר בשם {product_name}."

    # חיפוש עבור כמות של מוצר
    elif "כמה יש" in message or "מה הכמות" in message:
        # חיפוש עבור שם מוצר
        product_name_match = re.search(r"\bמ(ה)?\s?([א-ת\s]+)\b", message)
        if product_name_match:
            product_name = product_name_match.group(2).strip()
            try:
                product = Product.objects.get(name__icontains=product_name)
                response = f"מלאי המוצר {product.name} הוא {product.quantity} יחידות."
            except Product.DoesNotExist:
                response = f"לא מצאתי מוצר בשם {product_name}."

    return JsonResponse({'response': response})
